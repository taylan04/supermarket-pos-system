from conexao import *
from models import *
from sqlalchemy.orm import joinedload

def consultar_fornecedores():
    with session:
        fornecedores = session.query(Fornecedor).options(joinedload(Fornecedor.produtos)).all()
    
    return fornecedores

def consultar_fornecedor(id):
    with session:
        fornecedor = session.query(Fornecedor).options(joinedload(Fornecedor.produtos)).get(id)
    
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

def adicionar_produto_fornecedor(obj):
    with session:
        session.execute(Produto_fornecedor.insert().values(id_fornecedor=obj.id_fornecedor,id_produto=obj.id_produto))
        session.commit()

def consultar_produtos_fornecedores():
    with session:
        produtos_fornecedores = session.query(Produto_fornecedor).all()
    return produtos_fornecedores