from util import *
from Servicos_db.servicos_clientes_db import *

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
    nome = solicitar_nome_do_cliente()
    novo_cliente = Cliente(id_cliente,nome)
    session.add(novo_cliente)
    session.commit()

    return novo_cliente
