from Servicos_db.servicos_produtos_db import *
from .servicos_carrinho import *
from util import *
from tabulate import tabulate

def listar_produtos():
    produtos = consultar_produtos()
    if not produtos:
        tabela = [["Não há produtos disponíveis!"]]
        print(f"\n{tabulate(tabela, tablefmt="rounded_outline")}")
        return
    tabela = [["Id", "Produto", "Estoque", "Preço"]]
    for produto in produtos:
        id, nome, quantidade, preco = produto.id, produto.nome, produto.quantidade, produto.preco
        tabela.append([id, nome, quantidade, preco])
    print(f"\n{tabulate(tabela, headers="firstrow", tablefmt="rounded_outline")}")

def excluir_produto_carrinho(carrinho):
    if not carrinho:
        print("\nCarrinho vazio!")
        return carrinho
    
    produto_id = entrar_inteiro("\nDigite o ID do produto que deseja excluir do carrinho: ")
    carrinho = remover_produto_carrinho(carrinho, produto_id)
    return carrinho

def produtos_esgotados():
    produtos = produtos_sem_estoque()
    if not produtos:
        tabela = [["Não há produtos sem estoque!"]]
        print(f"\n{tabulate(tabela, tablefmt="rounded_outline")}\n")
        return
    print("\nVeja abaixo a lista de produtos sem estoque!")
    tabela = [["Produto", "Estoque"]]
    for produto in produtos:
        tabela.append([produto.nome, produto.quantidade])
    print(f"\n{tabulate(tabela, headers="firstrow", tablefmt="rounded_outline")}")
