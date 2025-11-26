from conexao import *
from models import *

def consultar_fornecedor():
    with session:
        fornecedores = session.query(Fornecedor).all()
    
    return fornecedores

def consultar_fornecedores(id):
    with session:
        fornecedor = session.get(Fornecedor, id)
    
    return fornecedor

def adicionar_fornecedor(fornecedor):
    with session:
        session.add(fornecedor)
        session.commit()
    
def remover_fornecedor(id):
    with session:
        fornecedor = session.get(Fornecedor, id)
        session.delete(fornecedor)
        session.commit()