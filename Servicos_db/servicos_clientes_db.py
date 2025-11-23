from conexao import *
from models import *

def adicionar_cliente(cliente):
    with session:
        session.add(cliente)
        session.commit()

def consultar_clientes():
    with session:
        clientes = session.query(Cliente).all()
  
    return clientes

def pesquisar_cliente(id):
    with session:
        cliente = session.query(Cliente).get(id)
        #eu estava pesquisando sobre sql alchemy e vi que agora tem outra forma mais eficiente de fazer essa mesma query
        #cliente = session.get(Cliente, id) - isso não faz select desnecessário
    return cliente