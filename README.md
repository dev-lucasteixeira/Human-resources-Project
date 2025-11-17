# README: Dashboard de Análise de RH (Performance Insights)

Este projeto foi desenvolvido como um case prático para a empresa fictícia "RH Insights", com o objetivo de analisar indicadores de performance e rotatividade de colaboradores.

## 1. 🏢 Contexto e Objetivo

A RH Insights, uma empresa de médio porte, notou recentemente uma queda no desempenho médio e um aumento na rotatividade (turnover).

O **objetivo principal** deste dashboard é fornecer ao time de RH uma ferramenta visual no Power BI para identificar as causas desses problemas. O painel deve ajudar a responder perguntas sobre desafios de desempenho, o perfil dos colaboradores e a relação entre tempo de casa e produtividade.

## 2. 📊 Fonte de Dados (Tabela Principal)

O dashboard foi construído a partir de uma única tabela de fatos (`Principal`), que contém dados brutos, colunas calculadas e medidas.

### Colunas de Dados Brutos
* `ID_Colaborador`
* `Nome`
* `Departamento`
* `Cargo`
* `Data_Admissao`
* `Data_Saida`
* `Idade`
* `Gênero`
* `Status`
* `Salário`
* `Avaliação_Desempenho`
* `Satisfação`
* `Horas_Treinamento`

### Colunas/Grupos Calculados (Power Query / DAX)
* `Tempo_Casa_Meses`
* `Tempo_Casa_Trimestre`
* `Tempo_Casa_Ano`
* `Faixa de Idade` (Coluna DAX para agrupar idades textualmente)
* `Idade (bins)` (Grupo numérico de idades)

### Medidas Principais (DAX)
* `Contagem Ativos`
* `Contagem_Inativos`
* `Taxa de TurnOver`

## 3. 💡 Principais Respostas e Insights (Análise do Dashboard)

O dashboard criado responde com sucesso à maioria das perguntas orientadoras do briefing.

### Visão Geral

* **Colaboradores Ativos:** A empresa possui **160** colaboradores ativos.
* **Taxa de TurnOver:** A taxa de turnover atual é de **25,00%**.

### Análise de Desempenho

* **Desempenho por Departamento:** O desempenho é muito similar entre as áreas, com **Tecnologia (7.7)** e **Vendas (7.7)** liderando, seguidas por **Operações (7.4)** e **Marketing (7.1)**.
* **Tempo de Casa vs. Desempenho:** O desempenho não aumenta linearmente com o tempo de casa. O gráfico "Desempenho por Tempo de casa" mostra picos e vales, atingindo a máxima performance (7.70) em colaboradores com 7 anos de casa.
* **Satisfação vs. Desempenho:** O gráfico "Correlação Satisfação e Desempenho" mostra que as duas métricas não andam sempre juntas. Há um ponto crítico no **Ano 2**, onde o desempenho atinge um pico (7.8), mas a satisfação cai para seu ponto mais baixo (6.7).

### Perfil dos Colaboradores

* **Distribuição (Gênero, Idade, Dept.):** Todos os perfis estão mapeados.
    * **Gênero:** Há um equilíbrio (53,5% Feminino, 46,5% Masculino).
    * **Departamento:** A distribuição é muito equilibrada (Marketing com 53, os demais com 51, 48 e 48).
    * **Idade:** A faixa etária de "24 - 27" é a mais populosa.

### Áreas de Risco (Turnover)

* **Onde está o risco?** O gráfico "Taxa de TurnOver e Desempenho por Departamento" é o mais estratégico do painel.
    * **Vendas e Tecnologia:** São as áreas mais críticas. Elas têm o **melhor desempenho** (7.66 e 7.73), mas também a **maior taxa de turnover** (ambas acima de 20%). Isso indica que a empresa pode estar perdendo seus melhores talentos.
    * **Marketing e Operações:** Possuem um turnover baixo (abaixo de 15%), mas o Marketing também tem a pior média de desempenho (7.15).

## 4. 📈 Novas Perguntas Respondidas pelo Dashboard

Com base nos visuais criados, o dashboard agora pode responder a perguntas ainda mais profundas que não estavam no briefing original:

### Foco em Retenção e Risco

1.  **Risco de Fuga de Talentos:** Qual departamento apresenta a combinação mais perigosa de **alto desempenho** e **alto turnover**?
    * *Resposta (no gráfico):* Tecnologia e Vendas.

2.  **Risco de Estagnação:** Qual departamento apresenta a combinação de **baixo desempenho** e **baixo turnover** (sugerindo que colaboradores com performance mais baixa não estão saindo)?
    * *Resposta (no gráfico):* Marketing.

### Foco no Ciclo de Vida do Colaborador

3.  **Pico de Performance:** Em qual ano de "tempo de casa" os colaboradores atingem seu pico de performance?
    * *Resposta (no gráfico):* No Ano 2 (média 7.8) e novamente no Ano 7 (média 7.7).

4.  **Vale da Insatisfação:** Em qual ano de "tempo de casa" a satisfação é mais baixa, mesmo com o desempenho em alta?
    * *Resposta (no gráfico):* No Ano 2 (Satisfação 6.7 vs. Desempenho 7.8).

### Foco no Perfil Demográfico

5.  **Perfil Etário:** A empresa tem uma força de trabalho predominantemente jovem ou mais experiente?
    * *Resposta (no gráfico):* Jovem, com a faixa de "24 - 27" sendo a maior.

6.  **Equilíbrio de Gênero:** A distribuição de gênero é equilibrada entre os 160 colaboradores ativos?
    * *Resposta (no gráfico):* Sim (53,5% F vs. 46,5% M).

## 5. 🚀 Próximos Passos (Análise de Cobertura)

O dashboard atual cobriu quase todos os pontos do briefing, com uma exceção notável:

* **Impacto do Treinamento:** O dashboard **não responde** à pergunta: "Onde investir em treinamento poderia gerar mais impacto?". A coluna `Horas_Treinamento` não foi utilizada em nenhum gráfico.
* **Sugestão:** Adicionar um gráfico de correlação (dispersão ou barras) que cruze `Horas_Treinamento` com `Avaliação_Desempenho` por departamento.
