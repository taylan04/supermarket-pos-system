from SIG.Servicos_db.db_item import *
from Caixa.Servicos_caixa_db.db_produtos import *
from util import *
from tabulate import tabulate
import pandas as pd

def produtos_mais_vendidos_e_menos_vendidos():
    produtos = consultar_produtos()

    produtos_ordenados = sorted(produtos,key=lambda produto: len(produto.itens_comprados),reverse=True)

    print("\nLista de produtos mais vendidos:\n")

    for p in produtos_ordenados:
        print(f"Produto ID: {p.id_produto}, Nome: {p.nome}, Quantidade vendida: {len(p.itens_comprados)}")

    print("\nLista de produtos menos vendidos:\n")

    for p in produtos_ordenados[::-1]:
        print(f"Produto ID: {p.id_produto}, Nome: {p.nome}, Quantidade vendida: {len(p.itens_comprados)}")

def produtos_com_pouco_estoque():
    parametro = entrar_inteiro_zero_permitido("\nDigite o parâmetro: ")

    produtos = [produto for produto in consultar_produtos() if produto.quantidade <= parametro]

    if not produtos:
        print("\nnenhum produto encontrado com estoque menor ou igual ao parâmetro informado.\n")
        return

    print("\nProdutos com pouco estoque:\n")
    for produto in produtos:
        print(produto.__str__())

def fornecedores_do_produto():
    id_produto = entrar_inteiro("\nDigite o ID do produto: ")
    produto = pesquisar_produto(id_produto)

    if not produto:
        print("\nProduto não encontrado.")
        return
    
    print("\nFornecedores\n")
    for fornecedor in produto.fornecedores:
        print(fornecedor.__str__())