import pandas as pd
from SIG.Servicos_db.db_fornecedor import *
from models import *
from conexao import *

def ler_excel_fornecedores():
    df = pd.read_excel("dados/carga_fornecedores_produtos.xlsx", sheet_name='fornecedores')
    return df

def ler_excel_fornecedores_produtos():
    df = pd.read_excel("dados/carga_fornecedores_produtos.xlsx", sheet_name='produtos-fornecedores')
    return df

def carregar_fornecedores_no_banco(df):
    for row in df.itertuples():
        fornecedor = Fornecedor(row.id_fornecedor, row.nome)
        adicionar_fornecedor(fornecedor)

def carregar_produtos_fornecedores_no_banco(df):
    #pesquisei e tive que fazer dessa forma porque a tabela intermediária não é uma classe do ORM entao nao tem session.add
    for row in df.itertuples():
        session.execute(Produto_fornecedor.insert().values(id_fornecedor=row.id_fornecedor,id_produto=row.id_produto))
    session.commit()

