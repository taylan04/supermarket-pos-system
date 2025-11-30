from SIG.Servicos_db.db_item import *
from Caixa.Servicos_caixa_db.db_produtos import *
from util import *

def produtos_mais_vendidos_e_menos_vendidos():
    produtos = consultar_produtos()

    if all(not produto.itens_comprados for produto in produtos):
        print("\nNenhum produto foi vendido no momento atual.")
        return

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

    print("\nProdutos com pouco estoque:")
    for produto in produtos:
        print(f"\nID: {produto.id_produto}\n{produto.nome}\nQuantidade: {produto.quantidade}")

def fornecedores_do_produto():
    id_produto = entrar_inteiro("\nDigite o ID do produto: ")
    produto = pesquisar_produto(id_produto)

    if not produto:
        print("\nProduto não encontrado.")
        return
    
    if not produto.fornecedores:
        print("\nEsse produto não tem fornecedores. =(")
        return
    
    print("\nFornecedores\n")
    for fornecedor in produto.fornecedores:
        print(fornecedor.__str__())