import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Precify.AI", layout="centered")

st.title("📊 Precify.AI — Precificação Inteligente com IA")
st.markdown("Insira os dados do produto para obter o preço ideal sugerido pela IA.")

# Inputs do usuário
preco_concorrente = st.number_input("💰 Preço do concorrente", min_value=0.0, value=100.0)
estoque = st.number_input("📦 Estoque disponível", min_value=0, value=50)
demanda = st.number_input("📈 Demanda estimada", min_value=0, value=200)
custo = st.number_input("🧾 Custo do produto", min_value=0.0, value=70.0)

# Botão para calcular
if st.button("🔍 Calcular preço ideal"):
    entrada = {
        "preco_concorrente": preco_concorrente,
        "estoque": estoque,
        "demanda": demanda,
        "custo": custo
    }

    try:
        resposta = requests.post("http://localhost:8000/prever", json=entrada).json()
        st.success(f"💡 Preço sugerido: R$ {resposta['preco_sugerido']}")
        st.write(f"📐 Margem estimada: R$ {resposta['margem']}")
        st.write(f"💸 Lucro estimado: R$ {resposta['lucro_estimado']}")
    except Exception as e:
        st.error("Erro ao conectar com a API. Verifique se o backend está rodando.")
        st.code(str(e))

# Simulação fictícia de histórico
historico = pd.DataFrame({
    "Data": ["Out 1", "Out 2", "Out 3"],
    "Preço Sugerido": [resposta["preco_sugerido"] - 2, resposta["preco_sugerido"], resposta["preco_sugerido"] + 1]
})

st.line_chart(historico.set_index("Data"))
