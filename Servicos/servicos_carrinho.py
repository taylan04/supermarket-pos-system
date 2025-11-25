from Servicos_db.servicos_produtos_db import *
from util import *
from tabulate import tabulate

# listar carrinho, excluir produto do carrinho 

def adicionar_produto_carrinho(carrinho, id_produto, quantidade):
    produto = pesquisar_produto(id_produto)
    
    if not produto:
        print("\nProduto não encontrado!")
        return carrinho
    
    quantidade_no_carrinho = 0

    for item in carrinho:
        if item['nome'] == produto.nome:
            quantidade_no_carrinho += item['quantidade']

    if quantidade_no_carrinho + quantidade > produto.quantidade:
        print("\nNão há estoque suficiente desse produto.")
        return carrinho
    
    item_carrinho = {
        "id_produto": produto.id,
        "id": produto.id,
        "nome": produto.nome,
        "quantidade": quantidade,
        "valor": produto.preco * quantidade
    }
    
    carrinho.append(item_carrinho)
    print(f"\nProduto {produto.nome} adicionado ao carrinho!")
    return carrinho

def listar_carrinho(carrinho):
    if not carrinho:
        tabela = [["Carrinho vazio!"]]
        print(f"\n{tabulate(tabela, tablefmt='rounded_outline')}")
        return
    
    tabela = [["Id", "Produto", "Quantidade", "Preço Unitário", "Total"]]
    for item in carrinho:
        preco_unitario = item["valor"] / item["quantidade"]
        tabela.append([item["id"], item["nome"], item["quantidade"], preco_unitario, item["valor"]])
    
    print(f"\n{tabulate(tabela, headers='firstrow', tablefmt='rounded_outline')}")
    
    total = sum(item["valor"] for item in carrinho)
    print(f"\nTotal do carrinho: R${round(total, 2)}")

def remover_produto_carrinho(carrinho, produto_id):
    item_encontrado = None
    
    for item in carrinho:
        if item["id_produto"] == produto_id:
            item_encontrado = item
            break
    
    if item_encontrado:
        carrinho.remove(item_encontrado)
        print(f"\nProduto removido do carrinho!")
        return carrinho
    else:
        print("\nProduto não encontrado no carrinho!")
        return carrinho

def limpar_carrinho(carrinho):
    carrinho.clear()
    return carrinho

def adicionar_carrinho(carrinho):
    id_produto = entrar_inteiro("\nDigite o ID do produto que deseja adicionar: ")
    quantidade = entrar_inteiro("Digite a quantidade: ")
    carrinho = adicionar_produto_carrinho(carrinho, id_produto, quantidade)
    return carrinho

