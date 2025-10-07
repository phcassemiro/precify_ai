import schedule
import time
from scraping.concorrencia import obter_preco_concorrente

def tarefa_scraping():
    url = "https://site.com/produto-x"
    preco = obter_preco_concorrente(url)
    print("Preço concorrente atualizado:", preco)

# Agendar a cada 6 horas
schedule.every(6).hours.do(tarefa_scraping)

# Loop infinito para manter rodando
while True:
    schedule.run_pending()
    time.sleep(1)
