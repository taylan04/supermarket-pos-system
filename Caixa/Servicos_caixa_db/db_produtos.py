from conexao import *
from models import *
from sqlalchemy.orm import joinedload
from SIG.Servicos_db.db_fornecedor import *

def adicionar_produto(produto):
    with session:
        session.add(produto)
        session.commit()

def consultar_produtos():
    with session:
        produtos = session.query(Produto).options(joinedload(Produto.fornecedores), joinedload(Produto.itens_comprados)).all()
  
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
        produto_atual = session.query(Produto).options(joinedload(Produto.fornecedores)).get(produto.id_produto)
        if produto_atual:
            produto_atual.fornecedores.clear()
            session.delete(produto_atual)
            session.commit()

def remover_fornecedor_do_produto(produto, fornecedor):
    with session:
        produto.fornecedores.remove(fornecedor)
        session.commit()

def adicionar_fornecedor_ao_produto(produto, fornecedor):
    with session:
        produto_atual = session.query(Produto).options(joinedload(Produto.fornecedores)).get(produto.id_produto)
        produto_atual.fornecedores.append(fornecedor)
        session.commit()