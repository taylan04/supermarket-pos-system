from Servicos_db.servicos_carrinho_db import *
from util import *
from tabulate import tabulate

def listar_carrinho():
    carrinho_items = consultar_carrinho()
    if not carrinho_items:
        tabela = [["Não há produtos no carrinho!"]]
        print(f"\n{tabulate(tabela, tablefmt="rounded_outline")}")
        return
    tabela = [["Item", "Id_produto", "Produto", "Quantidade", "Valor"]]
    for item in carrinho_items:
        id, id_produto, nome, quantidade, preco = item.id, item.id_produto, item.nome, item.quantidade, item.valor
        tabela.append([id, id_produto, nome, quantidade, preco])
    print(f"\n{tabulate(tabela, headers="firstrow", tablefmt="rounded_outline")}")

def adicionar_carrinho():
    produtos_no_carrinho = consultar_carrinho()
    produto_id = entrar_inteiro("\nDigite o ID do produto que deseja adicionar no carrinho: ")
    produto = pesquisar_produto(produto_id)
    if not produto:
        print("\nProduto não encontrado.")
        return
    
    quantidade_no_carrinho = 0

    for item in produtos_no_carrinho:
        if item.nome == produto.nome:
            quantidade_no_carrinho += item.quantidade

    quantidade = entrar_inteiro("\nDigite a quantidade: ")

    if quantidade_no_carrinho + quantidade > produto.quantidade:
        print("\nNão há estoque suficiente desse produto.")
        return
    
    preco = produto.preco
    incluir_carrinho(produto.id, produto.nome, quantidade, preco * quantidade)
    print("\nProduto adicionado ao carrinho.")
 