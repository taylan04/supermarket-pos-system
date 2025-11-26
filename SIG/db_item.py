from conexao import *
from models import *


def consultar_itens():
    with session:
        itens = session.query(Item).all()
        #funcionarios = session.query(Funcionario).options(joinedload(Funcionario.departamento),joinedload(Funcionario.projetos)).all()
        
    return itens

def consultar_item(id):
    with session:
        item = session.get(Item, id)
    
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