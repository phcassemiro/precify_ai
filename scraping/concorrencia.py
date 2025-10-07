import requests
from bs4 import BeautifulSoup

def obter_preco_concorrente(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    preco = soup.find("span", class_="preco").text
    return float(preco.replace("R$", "").replace(",", "."))