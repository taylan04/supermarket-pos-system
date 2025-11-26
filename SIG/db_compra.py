from conexao import *
from models import *
from sqlalchemy.orm import joinedload

def consultar_compras():
    with session:
        compras = session.query(Compra).options(joinedload(Compra.cliente), joinedload(Compra.itens)).all()
    
    return compras

def consultar_compra(id):
    with session:
        compra = session.query(Compra).options(joinedload(Compra.cliente), joinedload(Compra.itens)).get(id)
    
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


