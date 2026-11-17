#PARA EXECUTAR UTILIZE O COMANDO A BAIXO:
# python -m streamlit run frontend_02.py

import streamlit as st
from consumidor_api import obter_dados_meteorologicos

st.set_page_config(
    page_title="Estação Meteorológica",
    page_icon="🌡️",
    layout="centered"
)

st.title("🌡️ Estação Meteorológica")
st.write("Monitoramento das condições ambientais")
st.caption("Jaraguá do Sul — Santa Catarina")

st.divider()

try:
    with st.spinner("Obtendo informações meteorológicas..."):
        dados = obter_dados_meteorologicos()

    st.success("Consulta realizada com sucesso!")

    st.subheader("🌡️ Temperatura")

    col1, col2 = st.columns(2)

    col1.metric(
        "Temperatura do ar",
        f"{dados['temperatura']:.1f} °C"
    )

    col2.metric(
        "Sensação térmica",
        f"{dados['sensacao_termica']:.1f} °C"
    )

    st.divider()

    st.subheader("💧 Umidade e precipitação")

    st.metric(
        "Umidade relativa",
        f"{dados['umidade_relativa']:.0f} %"
    )

    st.progress(
        max(0.0, min(1.0, dados['umidade_relativa'] / 100))
    )

    st.metric(
        "Precipitação",
        f"{dados['precipitacao']:.1f} mm"
    )

    st.divider()

    st.subheader("💨 Vento")

    st.metric(
        "Velocidade do vento",
        f"{dados['velocidade_vento']:.1f} km/h"
    )

    st.divider()

    st.info(f"Horário informado pela API: {dados['horario']}")

except Exception as erro:
    st.error(f"Falha ao obter os dados meteorológicos: {erro}")
