from conexao import *
from models import *

def consultar_registros():
    with session:
        registros = session.query(Registro).all()

    return registros

def limpar_registros():
    with session:
        session.query(Registro).delete()
        session.commit()

def salvar_registro(cliente, total):
    registro = Registro(None, cliente, total)
    with session:
        session.add(registro)
        session.commit()