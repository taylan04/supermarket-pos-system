from conexao import *
from models import *
from sqlalchemy.orm import joinedload

def consultar_itens():
    with session:
        itens = session.query(Item).options(joinedload(Item.produto_referenciado), joinedload(Item.compra)).all()
    
    return itens

def consultar_item(id):
    with session:
        item = session.query(Item).options(joinedload(Item.produto_referenciado), joinedload(Item.compra)).get(id)
    
    return item

def adicionar_item(item):
    with session:
        session.add(item)
        session.commit()
    
def remover_item(id):
    with session:
        item = session.get(Item, id)
        session.delete(item)
        session.commit()