import os
import logging
from dotenv import load_dotenv
from operator import itemgetter

# LangChain Core & Community
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.load import dumps, loads
from langchain_community.vectorstores.utils import filter_complex_metadata
from langchain_community.document_loaders import (
    TextLoader,
    CSVLoader,
    UnstructuredExcelLoader
)

load_dotenv()

#### 1. Indexing ####

folder_path = "./LangChain - RH Insights\datas"

LOADER_MAP = {
    ".txt": TextLoader,
    ".csv": CSVLoader,
    ".xlsx": UnstructuredExcelLoader,
}

documents = []
print("--- INICIANDO CARREGAMENTO DE ARQUIVOS ---")

for root, _, files in os.walk(folder_path):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        ext = os.path.splitext(file_name)[1].lower()

        if ext in LOADER_MAP:
            try:
                LoaderClass = LOADER_MAP[ext]
                # Tratamento de encoding
                if ext in [".txt", ".csv"]:
                    loader = LoaderClass(file_path, encoding='utf-8')
                else:
                    loader = LoaderClass(file_path)
                
                docs = loader.load()
                documents.extend(docs)
                print(f"Carregado: {file_name}")
            except Exception as e:
                print(f"Erro ao carregar {file_name}: {e}")

#### VectorStore ####

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
all_splits = text_splitter.split_documents(documents)

cleaned_splits = filter_complex_metadata(all_splits)

vectorstore = Chroma.from_documents(
    documents=cleaned_splits,
    embedding=OpenAIEmbeddings(model="text-embedding-ada-002")
)

base_retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

print("Vector Store pronto.")

#### Prompt and Multi Query

llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")

# Multi Query
template_query_gen = """Você é um assistente de IA útil que gera múltiplas consultas de pesquisa baseadas em uma única consulta de entrada. 
Gere 4 variações da pergunta do usuário focadas em recuperar documentos sobre RH, dados e performance.
Pense em sinônimos (Ex: Turnover = Rotatividade = Saída).
Separe cada consulta por uma nova linha.
Apenas retorne as consultas, sem numeração.

Pergunta original: {question}
"""

prompt_query_gen = ChatPromptTemplate.from_template(template_query_gen)

generate_queries_chain = (
    prompt_query_gen 
    | llm 
    | StrOutputParser() 
    | (lambda x: x.strip().split("\n"))
)


def reciprocal_rank_fusion(results: list[list], k=60):
    """
    Algoritmo RRF: Recebe uma lista de listas de documentos (resultados de cada query).
    Reordena os documentos baseados em 'em quantas queries eles apareceram' e 'qual o rank deles'.
    """
    fused_scores = {}
    doc_map = {}

    
    for docs in results:
        for rank, doc in enumerate(docs):
            
            doc_str = dumps(doc)
            
            
            if doc_str not in doc_map:
                doc_map[doc_str] = doc

            
            if doc_str not in fused_scores:
                fused_scores[doc_str] = 0
            fused_scores[doc_str] += 1 / (rank + k)

    reranked_results = [
        (doc_map[doc_str], score)
        for doc_str, score in sorted(fused_scores.items(), key=lambda x: x[1], reverse=True)
    ]

    return [doc for doc, _ in reranked_results[:5]]

#### Retriever ####

retrieval_chain_rag_fusion = (
    generate_queries_chain 
    | base_retriever.map() 
    | reciprocal_rank_fusion
)

#### Final RAG Chain ####

SYSTEM_TEMPLATE = """
**PAPEL:** Analista Sênior de Personal Analytics (RH Insights).
**REGRA:** Use APENAS o contexto abaixo. Cite métricas. Se não souber, diga que não há dados.

**CONTEXTO (Classificado por Relevância RRF):**
{context}

**PERGUNTA:** {question}
"""

prompt_final = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_TEMPLATE),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}")
])

final_rag_chain = (
    {"context": retrieval_chain_rag_fusion, "question": itemgetter("question"), "history": itemgetter("history")}
    | prompt_final
    | llm
)

#### Memory ####

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

chain_with_history = RunnableWithMessageHistory(
    final_rag_chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history"
)

def iniciar_assistente():
    print("Assistente de RH Insights iniciado. Digite 'sair' para encerrar.")
    while True:
        pergunta_usuario = input("\nVocê: ")
        if pergunta_usuario.lower() in ["sair", "exit"]:
            break
        
        try:
            
            response = chain_with_history.invoke(
                {"question": pergunta_usuario},
                config={"configurable": {"session_id": "fusion_user"}}
            )
            print(f"\nAssistente: {response.content}")
        except Exception as e:
            print(f"Erro na execução: {e}")

if __name__ == "__main__":
    iniciar_assistente()