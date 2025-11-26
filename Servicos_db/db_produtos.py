from conexao import *
from models import *
from sqlalchemy.orm import joinedload

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

def atualizar_produto(produto):
    with session:
        session.query(Produto).filter(Produto.id_produto == produto.id_produto).update({"quantidade": produto.quantidade})
        session.commit()