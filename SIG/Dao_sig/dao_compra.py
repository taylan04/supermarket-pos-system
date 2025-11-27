from models import *
from sqlalchemy import func
from SIG.Servicos_db.db_compra import *
from conexao import session

def gerar_proximo_id_compra():
    #func.max pega o ID maximo que tem na tabela compras e o scalar me devolve apenas o numero, sem me retornaria objeto
    ultimo = session.query(func.max(Compra.id_compra)).scalar()
    if ultimo is None:
        return 1
    return ultimo + 1
