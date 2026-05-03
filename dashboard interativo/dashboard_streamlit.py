import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuração da página
st.set_page_config(
    page_title="Evasão Escolar Brasil | Dashboard",
    page_icon="🏫",
    layout="wide"
)

# Estilização Básica (CSS)
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.title("🏫 Evasão Escolar Brasil 2020-2024")
st.markdown("### Ciência de Dados para Políticas Públicas")
st.markdown("---")

# Carregamento dos dados
@st.cache_data
def load_data():
    df = pd.read_csv("data/dados_corrigidos.csv")
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("Arquivo de dados não encontrado. Verifique a pasta 'data/'.")
    st.stop()

# Sidebar para filtros
st.sidebar.header("🎛️ Filtros")
ano_selecionado = st.sidebar.slider("Selecione o Ano", 2020, 2024, (2020, 2024))
regioes = st.sidebar.multiselect("Selecione a Região", df['regiao'].unique(), default=df['regiao'].unique())

# Filtro de dados
df_filtrado = df[(df['ano'] >= ano_selecionado[0]) & (df['ano'] <= ano_selecionado[1])]
df_filtrado = df_filtrado[df_filtrado['regiao'].isin(regioes)]

if df_filtrado.empty:
    st.warning("⚠️ Nenhum dado disponível para os filtros selecionados. Ajuste os filtros na barra lateral.")
    st.stop()

# KPIs
col1, col2, col3, col4 = st.columns(4)
with col1:
    taxa_media = df_filtrado['taxa_evasao'].mean()
    st.metric("Taxa Média Nacional", f"{taxa_media:.1f}%")
with col2:
    regiao_critica = df_filtrado.groupby('regiao')['taxa_evasao'].mean().idxmax()
    val_critico = df_filtrado.groupby('regiao')['taxa_evasao'].mean().max()
    st.metric("Região Crítica", f"{regiao_critica} ({val_critico:.1f}%)")
with col3:
    total_escolas = df_filtrado['escola_id'].nunique()
    st.metric("Escolas Analisadas", f"{total_escolas}")
with col4:
    renda_media = df_filtrado['renda_per_capita'].mean()
    st.metric("Renda Per Capita Média", f"R$ {renda_media:.2f}")

st.markdown("---")

# Gráficos
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.subheader("📈 Evolução Temporal (2020-2024)")
    evasao_ano = df_filtrado.groupby(['ano', 'regiao'])['taxa_evasao'].mean().reset_index()
    fig1 = px.line(evasao_ano, x='ano', y='taxa_evasao', color='regiao', markers=True,
                   labels={'taxa_evasao': 'Taxa de Evasão (%)', 'ano': 'Ano'},
                   color_discrete_sequence=px.colors.qualitative.Set1)
    fig1.update_layout(xaxis=dict(tickmode='linear', dtick=1))
    st.plotly_chart(fig1, use_container_width=True)

with col_graf2:
    st.subheader("📊 Taxa Média por Região")
    evasao_regiao = df_filtrado.groupby('regiao')['taxa_evasao'].mean().sort_values().reset_index()
    fig2 = px.bar(evasao_regiao, x='taxa_evasao', y='regiao', orientation='h',
                  color='taxa_evasao', color_continuous_scale='RdYlGn_r',
                  labels={'taxa_evasao': 'Taxa de Evasão (%)', 'regiao': 'Região'})
    st.plotly_chart(fig2, use_container_width=True)

# Mapa e Detalhes
import requests  # <-- adicionar

st.subheader("🗺️ Mapa Coroplético: Evasão por Estado")
evasao_estado = df_filtrado.groupby('estado')['taxa_evasao'].mean().reset_index()

# <-- adicionar essas 2 linhas
url = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson"
geojson = requests.get(url).json()

fig3 = px.choropleth(
    evasao_estado,
    geojson=geojson,  # <-- adicionar
    locations='estado',
    featureidkey="properties.sigla",  # <-- adicionar
    color='taxa_evasao',
    color_continuous_scale='RdYlGn_r',
    scope='south america',  # pode manter
    labels={'taxa_evasao': 'Evasão (%)'}
)

fig3.update_layout(
    margin={"r":0,"t":0,"l":0,"b":0},
    geo=dict(showcoastlines=True, fitbounds="locations", visible=False)
)

st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")
st.markdown("### 💡 Principais Insights")
st.info("""
- **O Nordeste apresenta o maior índice de evasão** (~10.2%).
- O ano de **2021 reflete o pico da pandemia**, com altas significativas em todas as regiões.
- Há uma **forte correlação negativa entre renda e evasão**, destacando que a pobreza (renda < R$ 800) aumenta o risco de abandono em até 4 vezes.
""")

