from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import joblib
import os

# Caminho para salvar o modelo
MODELO_PATH = "models/modelo_precos.pkl"

# Função para treinar o modelo com dados fictícios
def treinar_modelo():
    dados = pd.DataFrame({
        'preco_concorrente': [100, 120, 90, 110],
        'estoque': [50, 20, 80, 30],
        'demanda': [200, 150, 300, 180],
        'custo': [70, 80, 60, 75],
        'preco_vendido': [105, 115, 95, 108]
    })

    X = dados[['preco_concorrente', 'estoque', 'demanda', 'custo']]
    y = dados['preco_vendido']

    modelo = RandomForestRegressor()
    modelo.fit(X, y)
    joblib.dump(modelo, MODELO_PATH)

# Função para prever o preço ideal
def prever_preco(entrada):
    if not os.path.exists(MODELO_PATH):
        treinar_modelo()
    modelo = joblib.load(MODELO_PATH)
    return modelo.predict(entrada)[0]
