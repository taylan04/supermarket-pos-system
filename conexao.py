from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os.path
from models import *

banco = "Dados/banco.db"
diretorio = os.path.dirname(os.path.abspath(__file__))
banco = os.path.join(diretorio, banco)

def conectar():
    try:
        engine = create_engine("sqlite:///"+banco)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind = engine)
        session = Session()
        return session
    except Exception as ex:
        print("Erro ao conectar ao banco:", ex)
        return None

session = conectar()
