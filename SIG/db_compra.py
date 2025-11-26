from conexao import *
from models import *

def consultar_compras():
    with session:
        compras = session.query(Compra).all()
    
    return compras

def consultar_compra(id):
    with session:
        compra = session.get(Compra, id)
    
    return compra

def adicionar_compra(compra):
    with session:
        session.add(compra)
        session.commit()
    
def remover_compra(id):
    with session:
        compra = session.get(Compra, id)
        session.delete(compra)
        session.commit()
        

