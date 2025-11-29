from Caixa.Servicos_caixa_db.db_produtos import *
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
        id, nome, quantidade, preco = produto.id_produto, produto.nome, produto.quantidade, produto.preco
        tabela.append([id, nome, quantidade, preco])
    print(f"\n{tabulate(tabela, headers="firstrow", tablefmt="rounded_outline")}")

def adicionar_produto_novo():
    #ultimo_id = gerar_proximo_id(Produto.id_produto)
    nome = entrar_string("\nDigite o nome do produto: ")
    preco = entrar_float("\nDigite o preço unitário desse produto: ")
    quantidade = entrar_inteiro_zero_permitido("\nDigite a quantidade atual em estoque: ")
    produto = Produto(None, nome, preco, quantidade)
    adicionar_produto(produto)

def remover_produto_do_banco():
    id_produto = entrar_inteiro("\nDigite o ID do produto que deseja remover: ")
    produto = pesquisar_produto(id_produto)

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
        return

    print(f"\nProduto selecionado: {produto.nome}")
    print("o que deseja atualizar?")
    print("1 - nome")
    print("2 - preço")
    print("3 - quantidade em estoque")
    print("4 - cancelar")

    opcao = entrar_inteiro("\nescolha uma opção: ")

    if opcao == 1:
        novo_nome = entrar_string("\ndigite o novo nome: ")
        atualizar_produto(id_produto, {"nome": novo_nome})
        print("\nnome atualizado com sucesso.")

    elif opcao == 2:
        novo_preco = entrar_float("\ndigite o novo preço: ")
        atualizar_produto(id_produto, {"preco": novo_preco})
        print("\npreço atualizado com sucesso.")

    elif opcao == 3:
        nova_quantidade = entrar_inteiro_zero_permitido("\ndigite a nova quantidade em estoque: ")
        atualizar_produto(id_produto, {"quantidade": nova_quantidade})
        print("\nquantidade atualizada com sucesso.")

    elif opcao == 4:
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
    produto = pesquisar_produto(id_produto)
    fornecedor = consultar_fornecedor(id_fornecedor)

    if not produto or not fornecedor:
        print("\nProduto ou fornecedor não encontrado.")
        return

    if fornecedor not in produto.fornecedores:
        print("\nEste fornecedor não está associado a este produto.")
        return

    remover_fornecedor_do_produto(produto, fornecedor)

    print(f"\nFornecedor {fornecedor.nome} removido do produto {produto.nome}.")

def adicionar_fornecedor(id_produto, id_fornecedor):
    produto = pesquisar_produto(id_produto)
    fornecedor = consultar_fornecedor(id_fornecedor)

    if not produto or not fornecedor:
        print("\nProduto ou fornecedor não encontrado.")
        return

    if fornecedor in produto.fornecedores:
        print("\nEste fornecedor já está associado a este produto.")
        return

    adicionar_fornecedor_ao_produto(produto, fornecedor)

    print(f"\nFornecedor {fornecedor.nome} adicionado ao produto {produto.nome}.")