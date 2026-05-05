# 🏫 EVASÃO ESCOLAR BRASIL 2020-2024
## Ciência de Dados para Políticas Públicas

[![Streamlit](https://img.shields.io/badge/Streamlit-FF6B35)](https://evasao.streamlit.app)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?logo=Jupyter&logoColor=white)](evasao_escolar_completo.ipynb)

### 📊 SOBRE O PROJETO
Este repositório contém a análise completa e os modelos preditivos desenvolvidos para investigar a **Evasão Escolar no Brasil (2020-2024)**, focando em escolas públicas do Ensino Fundamental e Médio.

O principal problema abordado e resolvido foi a **falha nos dados históricos** (que erroneamente indicavam que o Sul possuía maior evasão que o Nordeste). Através do cruzamento com microdados reais do INEP/Censo Escolar, a realidade foi restabelecida.

### 🎯 RESULTADOS PRINCIPAIS E INSIGHTS
- **Nordeste Lidera a Evasão**: A taxa média real no NE é de **10.2%**, contra **4.3%** no Sul.
- **Pico Pandêmico**: 2021 apresentou o maior índice de abandonos.
- **Pobreza**: Existe uma forte correlação negativa (`-0.7`) entre renda per capita e abandono escolar. Famílias com renda < R$ 800 possuem até 4x mais risco.
- **Escolas Críticas**: O Treemap evidencia que o Top 10% de escolas críticas encontram-se predominantemente nas regiões Nordeste e Norte (68%).

### 📂 ESTRUTURA DO PROJETO
- `evasao_escolar.ipynb`: Notebook com 100% da análise (EDA, Inferência Estatística e Modelagem de Regressão/SHAP).
- `dashboard_streamlit.py`: Dashboard interativo e *deploy-ready* com Plotly.
- `dados/`: Todos os Datasets do INEP que utilizamos.
- `graficos/`: Gráficos gerados (Barras, Linhas, Mapa, Heatmap, Boxplot, Treemap).
- `VIDEO.md/`: Vídeo das etapas do projeto acadêmico.
- `PDF das Análises/`: Pdf de todas as análises e insights.
- `insights.md/`: Principais Insights.

### 🚀 COMO EXECUTAR O DASHBOARD
1. Instale as dependências: `pip install -r requirements.txt`
2. Execute o Streamlit: `streamlit run dashboard_streamlit.py`
