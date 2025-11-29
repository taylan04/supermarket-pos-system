from conexao import *
from models import *
from sqlalchemy.orm import joinedload

def adicionar_produto(produto):
    with session:
        session.add(produto)
        session.commit()

def consultar_produtos():
    with session:
        produtos = session.query(Produto).options(joinedload(Produto.fornecedores)).all()
  
    return produtos

def pesquisar_produto(id):
    with session:
        produto = session.query(Produto).options(joinedload(Produto.fornecedores)).get(id)

    return produto

def produtos_sem_estoque():
    with session:
        produtos = session.query(Produto).filter(Produto.quantidade == 0).options(joinedload(Produto.fornecedores)).all()

    return produtos

def atualizar_produto(id_produto, campos):
    with session:
        session.query(Produto).filter(Produto.id_produto == id_produto).update(campos)
        session.commit()

def remover_produto(produto):
    with session:
        session.delete(produto)
        session.commit()

