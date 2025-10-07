# Precify.AI

Precify.AI é um app de precificação inteligente com IA que sugere preços ideais com base em concorrência, demanda, estoque e margem. Ele inclui backend com FastAPI, frontend com Streamlit, scraping de concorrência, simulação de impacto e banco de dados com SQLite.

## Funcionalidades
- Sugestão de preço com IA
- Simulação de margem e lucro
- Scraping de concorrência
- Relatórios por produto
- Autenticação de usuários
- Sistema de planos pagos

## Como rodar localmente

```bash
# Criar banco
python app/init_db.py

# Rodar com Docker
docker-compose up --build