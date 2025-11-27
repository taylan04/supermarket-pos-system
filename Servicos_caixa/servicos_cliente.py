from util import *
from Servicos_caixa_db.db_clientes import *

def cadastrar_cliente():
    nome = solicitar_nome_do_cliente()
    id_cliente = retornar_id_do_cliente(nome)
    cliente = Cliente(id_cliente, nome)
    adicionar_cliente(cliente)
    return cliente

def consultar_ou_cadastrar_cliente():
    id_cliente = entrar_inteiro("\nDigite o ID do cliente: ")
    cliente = session.query(Cliente).get(id_cliente)

    if cliente:
        return cliente

    print("\nCliente não encontrado. Precisaremos cadastrá-lo: ")
    while True:
        nome = solicitar_nome_do_cliente()
        id_cliente = ""
        for char in nome:
            if char.isdigit():
                id_cliente += char

        clientex = pesquisar_cliente(id_cliente)
        if clientex:
            print("\nCliente com ID já cadastrado.")
            continue

        novo_cliente = Cliente(int(id_cliente),nome)
        session.add(novo_cliente)
        session.commit()

        return novo_cliente
