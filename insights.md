# 💡 Insights Iniciais e Conclusões por Análise

Este documento resume os principais *insights* (descobertas chave) extraídos de cada etapa da nossa análise de dados sobre a evasão escolar no Brasil. Ele serve como um guia rápido para entender o valor prático de cada gráfico e modelo desenvolvido.

---

### 1. Análise Regional (Gráfico de Barras)
- **O que fizemos:** Calculamos a taxa média de evasão escolar por região.
- **Insight Inicial:** A evasão não afeta o Brasil de forma homogênea. A região Nordeste lidera os índices (10.2%), enquanto o Sul apresenta as menores taxas (4.3%). 
- **Conclusão:** Políticas de combate à evasão não podem ser padronizadas para o país inteiro. Elas precisam ser regionalizadas, com foco de investimento nas regiões mais afetadas.

### 2. Análise Temporal (Gráfico de Linhas)
- **O que fizemos:** Acompanhamos a taxa de evasão ao longo dos anos, de 2020 a 2024.
- **Insight Inicial:** Houve um pico brutal e atípico de abandono no ano de 2021.
- **Conclusão:** O sistema educacional é altamente sensível a crises sanitárias e econômicas. O ano de 2021 reflete o ápice da pandemia da COVID-19, mostrando que quando há crise externa, a escola é a primeira a ser abandonada pelos alunos.

### 3. Análise Geográfica (Mapa Coroplético)
- **O que fizemos:** Mapeamos os índices médios de cada estado do Brasil.
- **Insight Inicial:** 68% das escolas em situação de risco crítico (evasão > 10%) estão concentradas em um eixo específico: Norte e Nordeste.
- **Conclusão:** As desigualdades históricas de desenvolvimento do país se refletem de maneira direta na educação. O mapa serve como guia visual de onde os governos devem atuar imediatamente.

### 4. Análise de Correlação (Heatmap)
- **O que fizemos:** Medimos o quanto as variáveis do dataset interagem entre si, buscando a raiz do problema.
- **Insight Inicial:** Encontramos uma fortíssima correlação negativa (em torno de -0.80) entre a renda per capita familiar e a taxa de evasão.
- **Conclusão:** O problema da evasão escolar não é apenas pedagógico, é fundamentalmente **econômico**. Quanto menos dinheiro a família tem, maior a chance de o aluno abandonar a escola para trabalhar ou por falta de recursos.

### 5. Impacto da Pobreza (Boxplot e Teste ANOVA)
- **O que fizemos:** Dividimos as escolas em grupos com base na renda familiar (Extrema pobreza: < R$ 800) e rodamos testes estatísticos.
- **Insight Inicial:** Escolas em áreas de extrema pobreza apresentam um risco de evasão até **4 vezes maior** do que as escolas em áreas de renda média/alta. O teste ANOVA comprovou que essa diferença não é um mero acaso (p-value válido).
- **Conclusão:** Para manter o aluno na escola, é necessário subsidiar a família. Programas de transferência de renda atrelados à presença escolar são a melhor resposta política para essa métrica.

### 6. Escolas em Risco Crítico (Treemap)
- **O que fizemos:** Isolamos os 10% piores casos (escolas com as maiores taxas do país).
- **Insight Inicial:** Uma parcela relativamente pequena do total de escolas concentra uma parte gigantesca do problema de abandono.
- **Conclusão:** Em um cenário de recursos públicos limitados, o foco não deve ser pulverizar o orçamento, mas sim criar "Forças-Tarefa" focadas nesses 10% do Treemap para gerar impacto rápido.

### 7. Inteligência Artificial e Modelagem (Random Forest + SHAP)
- **O que fizemos:** Treinamos a máquina para prever se uma escola terá alta evasão com base nas suas características locais. E usamos a ferramenta SHAP para perguntar ao algoritmo "por que você tomou essa decisão?".
- **Insight Inicial:** O algoritmo nos revelou que, logo após a renda familiar, a **falta de infraestrutura adequada** da escola é o gatilho matemático principal para prever a evasão.
- **Conclusão:** O aluno não abandona a escola apenas por ser pobre. Ele abandona porque, aliado à falta de dinheiro, a escola que o atende não tem infraestrutura atrativa ou digna.
