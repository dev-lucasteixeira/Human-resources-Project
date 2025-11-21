📊 Dashboard de RH Insights & 🤖 Assistente de IA (Personal Analytics)

Este projeto foi desenvolvido como um case prático para a empresa fictícia "RH Insights". Ele combina Business Intelligence (Power BI) com Inteligência Artificial Generativa (RAG) para diagnosticar problemas de performance e rotatividade, além de fornecer consultoria automatizada em tempo real.

1. 🏢 Contexto e Objetivo

A RH Insights, uma empresa de médio porte (~200 colaboradores), notou recentemente uma queda no desempenho médio e um aumento na rotatividade (turnover).

O objetivo principal é fornecer ao time de RH:

Visualização: Um dashboard interativo para monitorar KPIs.

Consultoria Inteligente: Uma IA capaz de responder perguntas complexas, cruzar dados de gestores/custos e sugerir planos de ação baseados em dados.

2. 📊 Fonte de Dados (Estrutura)

O projeto utiliza uma base de dados híbrida (Excel/CSV) processada tanto pelo Power BI quanto pela engine da IA.

Tabelas Principais

Colaboradores: Dados individuais (Salário, Performance, Idade, Gênero, Tempo de Casa).

Departamentos: Dados gerenciais (Nome do Gestor, Budget/Custo Mensal, Headcount).

Métricas Calculadas

Taxa de TurnOver: $\approx 21,5\%$ (considerada alta).

Desempenho Médio: 7.47 (Escala 0-10).

Custo por Departamento: Mapeado para análise de eficiência.

3. 💡 Principais Respostas do Dashboard (Power BI)

O painel visual respondeu às perguntas fundamentais do briefing:

Colaboradores Ativos: 169 colaboradores.

Desempenho por Departamento: Tecnologia lidera (7.51), enquanto Marketing tem o pior desempenho (7.37).

Curva de Performance: O pico de produtividade ocorre aos 7 anos de casa.

Paradoxo da Satisfação: No Ano 2, o desempenho é alto, mas a satisfação cai drasticamente (Risco de burnout ou falta de reconhecimento).

Áreas de Risco:

Risco de Fuga: Vendas e Tecnologia (Alto Desempenho + Alto Turnover).

Risco de Eficiência: Marketing (Alto Custo + Baixo Desempenho).

4. 🤖 O Assistente de IA (RAG Fusion & Personal Analytics)

Para ir além dos gráficos estáticos, foi implementado um Agente de IA baseado em RAG (Retrieval-Augmented Generation).

🧠 O Que a IA Faz?

Ela atua como um "Analista Sênior de RH". O usuário pode fazer perguntas em linguagem natural e a IA consulta os dados brutos, cruza informações de diferentes arquivos e gera respostas estratégicas.

🚀 Tecnologias Utilizadas

LangChain: Orquestração do fluxo de pensamento da IA.

RAG Fusion / Multi-Query: A IA gera variações da pergunta do usuário para encontrar dados ocultos (ex: se você pergunta "demissões", ela busca também por "turnover" e "saídas").

ChromaDB: Banco de dados vetorial para armazenar a "memória" da IA.

Watchdog: Sistema de Auto-Treinamento. A IA monitora a pasta de dados; se um arquivo Excel for atualizado, a IA re-treina seu cérebro automaticamente em segundos.

OpenAI GPT-4o-mini: O modelo de linguagem responsável pelo raciocínio final.

🎯 Exemplos de Consultas Suportadas

"Qual gestor tem a equipe mais cara e com menor desempenho?"
"Analise o perfil demográfico de quem pediu demissão nos últimos 12 meses."
"O que explica a correlação baixa entre satisfação e performance?"

5. 📈 Novas Perguntas Respondidas (IA + BI)

Com a união do Dashboard e da IA, conseguimos diagnósticos profundos:

Auditoria de Gestão: Identificamos que a gestão de Rafael Costa (Marketing) necessita de intervenção, pois gerencia o maior orçamento da empresa com o menor retorno em desempenho.

Benchmarking Interno: A IA sugere replicar as práticas de Tiago Ramos (Tecnologia), que mantém a maior equipe com o menor custo total e a maior nota de avaliação.

Retenção de Talentos: O problema de turnover não é "limpeza de base". A empresa está perdendo Analistas Plenos com nota 7.54 (acima da média). É uma sangria de talentos.

6. 🛠️ Como Executar o Projeto (IA)

Para rodar o Assistente de IA na sua máquina:

Pré-requisitos

Python 3.9+

Chave de API da OpenAI

Passo a Passo

Clone o repositório:

git clone [https://github.com/dev-lucasteixeira/Human-resources-Project.git](https://github.com/dev-lucasteixeira/Human-resources-Project.git)


Instale as dependências:

pip install -r requirements.txt


Configure as Credenciais:
Crie um arquivo .env na raiz e adicione sua chave:

OPENAI_API_KEY="sua-chave-aqui"
