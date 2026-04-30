# 📊 Análise da Evasão Escolar no Brasil com Ciência de Dados

> **Projeto Integrador III – Ciência de Dados**  
> Autores: **Matheus Rhamet** e **Renan Miguel**  
> Professor: Howard Cruz | Entrega 2 – 2026

---

## 1. Introdução e Justificativa

A evasão escolar é um dos principais desafios do sistema educacional brasileiro, afetando diretamente o desenvolvimento social e econômico do país. Este projeto utiliza **Ciência de Dados** para mapear padrões, correlações e fatores de risco que contribuem para o abandono escolar, fornecendo insights acionáveis para gestores públicos e secretarias de educação.

## 2. Problema de Pesquisa

> Quais são os principais fatores socioeconômicos e regionais que influenciam a evasão escolar no Brasil, e como a ciência de dados pode ajudar a mapear esses riscos para a tomada de decisões preventivas?

## 3. Estrutura do Repositório

```
projeto integrador/
├── analise_evasao_escolar.ipynb        # Notebook principal (Entrega 2)
├── analise_evasao_escolar_executado.ipynb  # Notebook com outputs
├── ibge_renda_estados.csv              # Dataset IBGE (renda por estado)
├── gerar_notebook.py                   # Script gerador do notebook
├── tx_rend_brasil_regioes_ufs_2020.xlsx
├── tx_rend_brasil_regioes_ufs_2021.xlsx
├── tx_rend_brasil_regioes_ufs_2022.xlsx
├── tx_rend_brasil_regioes_ufs_2023.xlsx
├── tx_rend_brasil_regioes_ufs_2024.xlsx
├── grafico_abandono_regiao.png
├── grafico_evolucao_temporal.png
├── grafico_boxplot.png
├── grafico_heatmap.png
├── grafico_correlacao_renda.png
├── grafico_ranking_estados.png
└── grafico_modelo.png
```

## 4. Fontes de Dados

| Dataset | Fonte | Período |
|---------|-------|---------|
| Taxas de Rendimento Escolar (Aprovação, Reprovação, Abandono) | INEP/MEC | 2020–2024 |
| Renda Média Domiciliar per Capita por Estado | IBGE (PNAD Contínua) | 2020–2024 |

## 5. Ferramentas e Tecnologias

- **Python 3.12** — linguagem principal
- **Pandas / NumPy** — manipulação e análise de dados
- **Matplotlib / Seaborn** — visualização de dados
- **SciPy** — testes estatísticos (Pearson)
- **Scikit-learn** — modelagem preditiva (Árvore de Decisão)
- **Jupyter Notebook** — protótipo funcional

## 6. Como Executar

1. Instale as dependências:
```bash
py -m pip install pandas numpy matplotlib seaborn scipy scikit-learn jupyter openpyxl
```

2. Abra o notebook:
```bash
py -m jupyter notebook analise_evasao_escolar.ipynb
```

3. Execute todas as células (`Kernel > Restart & Run All`)

## 7. Principais Insights

| # | Insight | Evidência |
|---|---------|-----------|
| 1 | **Nordeste e Norte lideram a evasão** | Abandono no EM > 5%, Sul/Sudeste < 3% |
| 2 | **Evasão caiu após 2021** | Queda pós-pandemia em todas regiões |
| 3 | **Renda correlaciona negativamente com evasão** | r ≈ -0.70 (Pearson, p < 0.001) |
| 4 | **Ensino Médio é mais crítico** | Abandono EM é 2–3× maior que no Fundamental |
| 5 | **Modelo preditivo com ~85% de acurácia** | Árv. de Decisão; preditor principal: Renda + Aprovação |

## 8. Sociedade Impactada

- **Secretarias de Educação** estaduais e municipais
- **Diretores e gestores escolares**
- **Gestores públicos** e formuladores de políticas educacionais
- **Estudantes em situação de vulnerabilidade** socioeconômica

## 9. Métricas de Impacto

- Correlações estatísticas validadas (Pearson com p-value)
- Ranking de estados e regiões com maior risco de abandono
- Modelo preditivo com acurácia mensurável
- Visualizações interpretáveis por gestores não técnicos
