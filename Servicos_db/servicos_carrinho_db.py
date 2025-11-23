from conexao import *
from models import *

def consultar_carrinho():
    with session:
        items = session.query(Carrinho).all()

    return items

def pesquisar_item_no_carrinho(id):
    with session:
        produto = session.query(Carrinho).filter(Carrinho.id_produto == id).first()

    return produto

def incluir_carrinho(id_produto, nome, quantidade, valor):
    item = Carrinho(None, id_produto, nome, quantidade, valor)
    with session:
        session.add(item)
        session.commit()

def remover_do_carrinho(id):
    with session:
        session.query(Carrinho).filter(Carrinho.id_produto == id).delete() 
        session.commit()

def limpar_carrinho():
    with session:
        session.query(Carrinho).delete()
        session.commit()
