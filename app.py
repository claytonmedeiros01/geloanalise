import streamlit as st
import pandas as pd
import plotly.express as px

# Carregando o arquivo CSV
df = pd.read_csv("resultados.csv")

# Configuração da página
st.set_page_config(
    page_title="Análise de CO2 e Área de Geleira no Ártico",
    page_icon="❄️",
    layout="wide"
)

# Título da página
st.title('Análise de CO2 Global e Área de Geleira no Ártico')

# Carregar imagem
logo_teste = st.sidebar.image('imggelo.png', use_column_width=True)

# Sidebar para seleção do período
st.sidebar.title("Filtros")
st.sidebar.markdown('Selecione o período de análise:')
min_year = df['Ano'].min()
max_year = df['Ano'].max()
start_year, end_year = st.sidebar.slider(
    "Período",
    min_value=min_year, max_value=max_year,
    value=(min_year, max_year)
)

# Filtrando os dados pelo período selecionado
df_filtered = df[(df['Ano'] >= start_year) & (df['Ano'] <= end_year)]

# Exibindo o dataframe filtrado
st.sidebar.markdown('### Dados Filtrados')
st.sidebar.dataframe(df_filtered)

# Gráfico de Média de CO2 global ao longo do tempo
st.markdown('### Média de CO2 Global ao Longo do Tempo')
fig_co2 = px.line(
    data_frame=df, x='Ano', y='Média CO2 Global',
    title='Média de CO2 Global ao longo dos Anos',
    markers=True  # Adicionando marcadores aos pontos da linha
    )
fig_co2.update_layout(
    plot_bgcolor='#1C1C1C',  # Cor de fundo do gráfico
   )
st.plotly_chart(fig_co2)


# Gráfico de Área de Geleira no Ártico ao longo do tempo
st.markdown('### Área de Geleira no Ártico ao Longo do Tempo')
fig_area = px.line(
    data_frame=df, x='Ano', y='Area',
    title='Área de Geleira no Ártico ao longo dos Anos',
    markers=True  # Adicionando marcadores aos pontos da linha
)
fig_area.update_layout(
    plot_bgcolor='#1C1C1C',  # Cor de fundo do gráfico
   )
st.plotly_chart(fig_area)

# Gerando gráfico de dispersão entre Área e Média de CO2 Global
st.markdown('### Área/CO2 no Ártico ao Longo do Tempo')
fig_dispersion = px.scatter(
    data_frame=df, x='Area', y='Média CO2 Global',
    title='Dispersão entre Área e Média de CO2 Global',
)
fig_dispersion.update_layout(
    plot_bgcolor='#1C1C1C',  # Cor de fundo do gráfico
   )
# Exibindo gráfico de dispersão
st.plotly_chart(fig_dispersion)

# Comentários sobre os gráficos e dados
st.markdown('## Comentários e Observações:')
st.markdown(
    "1. O primeiro gráfico mostra a **média de CO2 global** ao longo dos anos. "
    "Observamos um aumento constante, indicando um possível impacto das atividades humanas nas concentrações de CO2."
)
st.markdown(
    "2. O segundo gráfico exibe a **área de geleira no Ártico** ao longo do tempo. "
    "Podemos notar uma tendência de diminuição da área, indicando mudanças climáticas e o derretimento das geleiras."
)
# Comentário sobre o gráfico de dispersão
st.write("3. O gráfico de dispersão acima mostra a relação entre a Área de Geleira no Ártico e a Média de CO2 Global. Cada ponto representa um ano no dataframe, e a posição do ponto no gráfico indica os valores correspondentes de Área e Média de CO2 Global para aquele ano. Podemos observar se há alguma tendência ou padrão entre essas duas variáveis.")

st.markdown('---')
st.markdown("Dados fornecidos pelo [NOAA](https://example.com)")

##para exibir a base de dados
#st.markdown("# Base de Dados")
#st.dataframe(df)





