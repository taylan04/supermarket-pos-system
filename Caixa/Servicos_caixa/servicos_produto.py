from Caixa.Servicos_caixa_db.db_produtos import *
from SIG.Servicos_db.db_fornecedor import *
from .servicos_carrinho import *
from util import *
from tabulate import tabulate
from conexao import session
from models import *
from sqlalchemy.orm import joinedload

def listar_produtos():
    produtos = consultar_produtos()
    if not produtos:
        tabela = [["Não há produtos disponíveis!"]]
        print(f"\n{tabulate(tabela, tablefmt="rounded_outline")}")
        return
    tabela = [["Id", "Produto", "Estoque", "Preço"]]
    for produto in produtos:
        id, nome, quantidade, preco = produto.id_produto, produto.nome, produto.quantidade, produto.preco
        tabela.append([id, nome, quantidade, preco])
    print(f"\n{tabulate(tabela, headers="firstrow", tablefmt="rounded_outline")}")

def adicionar_produto_novo():
    ultimo_id = gerar_proximo_id(Produto.id_produto)
    nome = entrar_string("\nDigite o nome do produto: ")
    preco = entrar_float("\nDigite o preço unitário desse produto: ")
    quantidade = entrar_inteiro_zero_permitido("\nDigite a quantidade atual em estoque: ")
    produto = Produto(ultimo_id, nome, preco, quantidade)
    adicionar_produto(produto)
    return ultimo_id

def remover_produto_do_banco():
    id_produto = entrar_inteiro("\nDigite o ID do produto que deseja remover: ")
    produto = pesquisar_produto(id_produto)

    if produto.itens_comprados:
        print("\nEsse produto possui registro em compras, portanto não pode ser deletado.")
        return

    if not produto:
        print("\nProduto não encontrado.")
        return
    
    remover_produto(produto)
    print("\nRemovido.")

def atualizar_dados_do_produto():
    id_produto = entrar_inteiro("\ndigite o id do produto que deseja atualizar: ")
    produto = pesquisar_produto(id_produto)

    if not produto:
        print("\nproduto não encontrado.")
        return None

    while True:
        print(f"\nProduto selecionado: {produto.nome}")
        print("o que deseja atualizar?")
        print("1 - nome")
        print("2 - preço")
        print("3 - quantidade em estoque")
        print("4 - adicionar fornecedor")
        print("5 - remover fornecedor")
        print("6 - cancelar")

        opcao = entrar_inteiro("\nescolha uma opção: ")

        if opcao == 1:
            novo_nome = entrar_string("\ndigite o novo nome: ")
            atualizar_produto(id_produto, {"nome": novo_nome})
            print("\nnome atualizado com sucesso.")
            produto = pesquisar_produto(id_produto)

        elif opcao == 2:
            novo_preco = entrar_float("\ndigite o novo preço: ")
            atualizar_produto(id_produto, {"preco": novo_preco})
            print("\npreço atualizado com sucesso.")
            produto = pesquisar_produto(id_produto)

        elif opcao == 3:
            nova_quantidade = entrar_inteiro_zero_permitido("\ndigite a nova quantidade em estoque: ")
            atualizar_produto(id_produto, {"quantidade": nova_quantidade})
            print("\nquantidade atualizada com sucesso.")
            produto = pesquisar_produto(id_produto)

        elif opcao == 4:
            fornecedores = consultar_fornecedores()
            if not fornecedores:
                print("\nNão há fornecedores cadastrados.")
                continue
            
            print("\nFornecedores disponíveis:")
            for f in fornecedores:
                print(f"ID: {f.id_fornecedor}, Nome: {f.nome}")
            
            id_fornecedor = entrar_inteiro("\nDigite o ID do fornecedor: ")
            adicionar_fornecedor(id_produto, id_fornecedor)
            produto = pesquisar_produto(id_produto)

        elif opcao == 5:
            if not produto.fornecedores:
                print("\nEste produto não possui fornecedores associados.")
                continue
            
            print("\nFornecedores do produto:")
            for f in produto.fornecedores:
                print(f"ID: {f.id_fornecedor}, Nome: {f.nome}")
            
            id_fornecedor = entrar_inteiro("\nDigite o ID do fornecedor a remover: ")
            remover_fornecedor(id_produto, id_fornecedor)
            produto = pesquisar_produto(id_produto)

        elif opcao == 6:
            print("\ncancelado.")
            return

        else:
            print("\nopção inválida.")

'''def excluir_produto_carrinho(carrinho):
    if not carrinho:
        print("\nCarrinho vazio!")
        return carrinho
    
    produto_id = entrar_inteiro("\nDigite o ID do produto que deseja excluir do carrinho: ")
    carrinho = remover_produto_carrinho(carrinho, produto_id)
    return carrinho'''

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

def remover_fornecedor(id_produto, id_fornecedor):
    produto = session.query(Produto).options(joinedload(Produto.fornecedores)).get(id_produto)
    fornecedor = session.query(Fornecedor).get(id_fornecedor)

    if not produto or not fornecedor:
        print("\nProduto ou fornecedor não encontrado.")
        return

    if fornecedor not in produto.fornecedores:
        print("\nEste fornecedor não está associado a este produto.")
        return

    produto.fornecedores.remove(fornecedor)
    session.commit()

    print(f"\nFornecedor {fornecedor.nome} removido do produto {produto.nome}.")

def adicionar_fornecedor(id_produto, id_fornecedor):
    produto = session.query(Produto).options(joinedload(Produto.fornecedores)).get(id_produto)
    fornecedor = session.query(Fornecedor).get(id_fornecedor)

    if not produto or not fornecedor:
        print("\nProduto ou fornecedor não encontrado.")
        return

    if fornecedor in produto.fornecedores:
        print("\nEste fornecedor já está associado a este produto.")
        return

    produto.fornecedores.append(fornecedor)
    session.commit()

    print(f"\nFornecedor {fornecedor.nome} adicionado ao produto {produto.nome}.")