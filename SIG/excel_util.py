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
    fornecedores = consultar_fornecedores()
    if not fornecedores:
        for row in df.itertuples():
            fornecedor = Fornecedor(row.id_fornecedor, row.nome)
            adicionar_fornecedor(fornecedor)

def carregar_produtos_fornecedores_no_banco(df):
    produtos_fornecedores = consultar_produtos_fornecedores()
    if not produtos_fornecedores:
        for row in df.itertuples():
            adicionar_produto_fornecedor(row)

def executar_carga_fornecedores_e_produtos():
    df1 = ler_excel_fornecedores()
    df2 = ler_excel_fornecedores_produtos()
    carregar_fornecedores_no_banco(df1)
    carregar_produtos_fornecedores_no_banco(df2)
