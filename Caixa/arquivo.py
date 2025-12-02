import csv
import pandas as pd
from models import *
from conexao import *
from Caixa.Servicos_caixa_db.db_produtos import *
from Caixa.Servicos_caixa_db.db_clientes import *

def abertura_caixa():
    produtos = consultar_produtos()
    try:
        with open("Dados/produtos.csv", "r", encoding="UTF-8") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                if not linha:
                    continue
                if len(linha) == 3:
                    if not produtos:
                        nome, preco, estoque = linha[0], float(linha[1]), int(linha[2])
                        produto = Produto(None,nome,preco,estoque)
                        adicionar_produto(produto)
                    else:
                        pass
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")

def iniciar_clientes():
    df = pd.read_json("Dados/clientes.json")
    #tentei iterar sobre o df mas ele estava lendo o nome das colunas, então precisei usar o df.itertuples()
    clientes = consultar_clientes()
    if not clientes:
        for row in df.itertuples():
            cliente = Cliente(None, row.nome)
            adicionar_cliente(cliente)
    
def salvar_csv():
    produtos = consultar_produtos()
    try:
        with open("Dados/produtos.csv", "w", newline="", encoding="UTF-8") as arquivo:
            escritor = csv.writer(arquivo)
            for p in produtos:
                escritor.writerow([p.nome, p.preco, p.quantidade])  
    except Exception as ex:
        print(f"\nArquivo não encontrado! {ex}")