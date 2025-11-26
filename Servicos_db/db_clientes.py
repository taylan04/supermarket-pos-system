from conexao import *
from models import *
from sqlalchemy.orm import joinedload

def adicionar_cliente(cliente):
    with session:
        session.add(cliente)
        session.commit()

def consultar_clientes():
    with session:
        clientes = session.query(Cliente).options(joinedload(Cliente.compras)).all()
        
    return clientes

def pesquisar_cliente(id):
    with session:
        cliente = session.query(Cliente).options(joinedload(Cliente.compras)).get(id)

    return cliente