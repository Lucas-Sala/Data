### Etapa 1 — Fundamentos (2 a 4 semanas)

Objetivo: dominar as ferramentas usadas diariamente.

Aprenda bem:

* Python para análise de dados

  * pandas
  * numpy
  * matplotlib
  * plotly
* SQL

  * SELECT
  * JOIN
  * GROUP BY
  * Window Functions
  * CTEs
* Git
* GitHub

Projeto:

> Faça uma análise exploratória de um conjunto de dados do Kaggle.

Exemplo:

* vendas
* futebol
* filmes
* Spotify
* Airbnb

Esse projeto já pode ir para o GitHub.

---

### Etapa 2 — Estatística

Aprenda:

* média
* mediana
* desvio padrão
* distribuições
* correlação
* testes de hipótese
* regressão linear

Não precisa aprofundar em teoria inicialmente.

Projeto:

> Analise fatores que influenciam preços de imóveis.

---

### Etapa 3 — Banco de Dados

Aprenda:

* PostgreSQL
* modelagem relacional
* normalização
* índices
* views
* procedures

Projeto:

Criar um banco para uma empresa fictícia.

Depois responder perguntas usando SQL.

---

### Etapa 4 — Engenharia de Dados

Aqui você começa a entender como os dados chegam até um analista.

Aprenda:

* ETL
* ELT
* APIs
* JSON
* Parquet
* CSV
* Data Warehouse
* Data Lake

Ferramentas:

* Docker
* Airflow
* dbt
* Spark (mais tarde)

Projeto:

Pipeline:

```
API
   ↓

Python

   ↓

PostgreSQL

   ↓

Dashboard
```

---

### Etapa 5 — Visualização

Aprenda:

* Power BI
* Tableau (opcional)

Projeto:

Criar um dashboard completo.

---

### Etapa 6 — Machine Learning (caso queira Ciência de Dados)

Aprenda:

* scikit-learn
* regressão
* classificação
* clustering

Projeto:

Prever:

* preço de casas
* churn
* fraude
* aprovação de crédito

---

# Como organizar os estudos

Eu faria algo parecido com isto.

```
Data/
│
├── Estudos
│   ├── Python
│   ├── SQL
│   ├── Estatística
│   ├── Machine Learning
│   └── Engenharia de Dados
│
├── Projetos
│   ├── Projeto01
│   ├── Projeto02
│   ├── Projeto03
│   └── ...
│
└── Anotações
```

Cada projeto deve ter:

```
README.md

objetivo

dados

tratamento

análises

conclusões

imagens

código
```

Isso impressiona muito mais do que apenas colocar notebooks.

---

# O GitHub deve contar uma história

Em vez de vinte notebooks pequenos, tenha poucos projetos bem feitos.

Algo como:

```
01 - Análise de vendas

02 - Pipeline ETL com API

03 - Dashboard Power BI

04 - Predição de preços de imóveis

05 - Pipeline usando Airflow

06 - Engenharia de Dados com Spark

07 - Projeto completo de ponta a ponta
```

Quando um recrutador abrir seu perfil, ele deve pensar:

> "Essa pessoa sabe construir soluções completas."

---

# Como estudar cada assunto

Sempre siga este ciclo:

```
Aprender

↓

Fazer exercícios

↓

Construir projeto

↓

Escrever README

↓

Publicar

↓

Aprender próximo assunto
```

Nunca fique meses apenas assistindo cursos.

---

# Tenha um "Diário de Engenharia"

Isso ajuda muito.

Exemplo:

```
docs/

dia01.md

dia02.md

dia03.md
```

Escreva coisas como:

* o que aprendeu
* dificuldades
* decisões tomadas
* referências utilizadas

Além de reforçar o aprendizado, isso mostra organização e capacidade de documentação.

---

# Como escolher entre Analista, Cientista e Engenheiro de Dados

No início, não se preocupe em decidir. À medida que você estuda, vai perceber qual tipo de trabalho mais combina com você.

| Área                | Foco principal                                | Tecnologias comuns                         |
| ------------------- | --------------------------------------------- | ------------------------------------------ |
| Analista de Dados   | Responder perguntas de negócio                | SQL, Power BI, Excel, Python               |
| Cientista de Dados  | Criar modelos preditivos                      | Python, Estatística, Machine Learning      |
| Engenheiro de Dados | Construir pipelines e infraestrutura de dados | Python, SQL, Spark, Airflow, Docker, Cloud |

Pelo seu histórico, vejo um bom alinhamento com **Engenharia de Dados**: sua experiência com arquitetura de computadores, otimização, hardware/software co-design e desenvolvimento em Python indica afinidade com problemas de infraestrutura, desempenho e sistemas. Ao mesmo tempo, começar pela trilha de análise de dados é uma excelente estratégia, porque fortalece SQL, Python e entendimento do ciclo completo dos dados — competências valorizadas em qualquer uma dessas carreiras.

## Um plano de 6 meses

Se eu estivesse começando hoje, seguiria algo próximo disso:

* **Mês 1:** Python para dados, Git e GitHub, primeiro projeto de análise exploratória.
* **Mês 2:** SQL e modelagem de banco de dados, segundo projeto com consultas e banco relacional.
* **Mês 3:** Estatística aplicada e Power BI, terceiro projeto com dashboard.
* **Mês 4:** ETL, APIs, PostgreSQL e Docker, quarto projeto integrando coleta, transformação e armazenamento.
* **Mês 5:** Airflow e fundamentos de engenharia de dados, automatizando um pipeline.
* **Mês 6:** Projeto de ponta a ponta (API → ETL → Banco → Dashboard) e revisão do portfólio e currículo para candidaturas.

