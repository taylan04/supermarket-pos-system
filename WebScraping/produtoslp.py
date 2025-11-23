from urllib.request import urlopen
import pandas as pd
import csv
from bs4 import BeautifulSoup

URL = "https://pedrovncs.github.io/lindosprecos/produtos.html#"

def acessar_url(url):
    try:
        html = urlopen(url)
    except Exception as ex:
        print(ex)
        exit()
    return html

def obter_lista(bs):
    tag = bs.find("div", id="produtos-lista")
    if not tag:
        print("\nTag da lista não encontrada.")
        exit()
    return tag

def extrair_dados(tag):
    dados_produtos = []
    produtos = tag.find_all("div", class_="product-item") 
    
    for produto in produtos:
        try:
            nome = produto.find("h5", class_="card-title").text.strip()
            preco = produto.find("p", class_="card-price").text.strip()
            quantidade = produto.find("p", {"data-qtd": True}).text.strip()
            dados_produtos.append({"Nome": nome,"Preco": preco,"Quantidade": quantidade})
        except AttributeError as ex:
            print(ex)
            continue 
            
    return dados_produtos

def limpar_dados(dados):
    for dado in dados:
        dado["Nome"] = dado["Nome"].replace(",", "").strip()
        dado["Preco"] = dado["Preco"].replace("Valor:", "").replace("R$", "").replace(",", ".").strip()
        dado["Quantidade"] = dado["Quantidade"].replace("Disponível:", "").replace("un.", "").strip()
    
    return dados
    
def converter_dados_para_df(dados):
    df = pd.DataFrame(dados)
    return df

def executar_todos_os_processos():
    html = acessar_url(URL)
    bs = BeautifulSoup(html, "html.parser")
    tag = obter_lista(bs)
    dados = extrair_dados(tag)
    dados_limpos = limpar_dados(dados)
    df = converter_dados_para_df(dados_limpos)
    df.to_csv('produtos.csv', header=False, index=False)  



