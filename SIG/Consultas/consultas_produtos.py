from SIG.Servicos_db.db_item import *
from Caixa.Servicos_caixa_db.db_produtos import *
from util import *
from tabulate import tabulate

def produtos_mais_vendidos_e_menos_vendidos():
    produtos = [produto for produto in consultar_produtos() if produto.itens_comprados]

    if all(not produto.itens_comprados for produto in produtos):
        print("\nNenhum produto foi vendido no momento atual.")
        return

    produtos_ordenados = sorted(produtos,key=lambda produto: len(produto.itens_comprados),reverse=True)
    tabela = [[p.id_produto, p.nome, len(p.itens_comprados)]for p in produtos_ordenados]

    print("\nLista de produtos mais vendidos:\n")
    print(tabulate(tabela, tablefmt="rounded_outline"))

    print("\nLista de produtos menos vendidos:\n")
    print(tabulate(tabela[::-1], tablefmt="rounded_outline"))

def produtos_com_pouco_estoque():
    parametro = entrar_inteiro_zero_permitido("\nDigite o parâmetro: ")

    produtos = [[p.id_produto, p.nome, p.quantidade] for p in consultar_produtos() if p.quantidade <= parametro]
    produtos_ordenados = sorted(produtos,key=lambda produto: produto[2],reverse=True)
    
    if not produtos:
        print("\nnenhum produto encontrado com estoque menor ou igual ao parâmetro informado.\n")
        return

    print("\nProdutos com pouco estoque:")
    print(tabulate(produtos_ordenados, headers=["ID", "Produto", "Quantidade em estoque"], tablefmt="rounded_outline"))

def fornecedores_do_produto():
    id_produto = entrar_inteiro("\nDigite o ID do produto: ")
    produto = pesquisar_produto(id_produto)

    if not produto:
        print("\nProduto não encontrado.")
        return
    
    if not produto.fornecedores:
        print("\nEsse produto não tem fornecedores. =(")
        return
    
    print(f"\nProduto: {produto.nome}")
    fornecedores = [[fornecedor.id_fornecedor, fornecedor.nome] for fornecedor in produto.fornecedores]
    print(tabulate(fornecedores, headers=["ID", "Fornecedor"], tablefmt="rounded_outline"))