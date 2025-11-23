from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Produto(Base):
    __tablename__ = "produto"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    preco = Column(Float)
    quantidade = Column(Integer)

    def __init__(self, id, nome, preco, quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f'{self.id}, {self.nome}, {self.quantidade}, {self.preco}'
    
class Carrinho(Base):
    __tablename__ = "carrinho"

    id = Column(Integer, primary_key=True)
    id_produto = Column(Integer)
    nome = Column(String)
    quantidade = Column(Integer)
    valor = Column(Float)

    def __init__(self, id, id_produto, nome, quantidade, valor):
        self.id = id
        self.id_produto = id_produto
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor

    def retornar_dicionario(self):
        return {
            "id": self.id,
            "id_produto": self.id_produto,
            "nome": self.nome,
            "quantidade": self.quantidade,
            "valor": self.valor
        }

    def __str__(self):
        return f'{self.id}, {self.id_produto}, {self.nome}, {self.quantidade}, {self.valor}'
    
class Registro(Base):
    __tablename__ = "registros"

    id = Column(Integer, primary_key=True)
    cliente = Column(String)
    total = Column(Float)

    def __init__(self, id, cliente, total):
        self.id = id
        self.cliente = cliente
        self.total = total

    def __str__(self):
        return f'{self.id}, {self.cliente}, {self.total}'
    
class Cliente(Base):
    __tablename__ = "clientes"

    id_cliente = Column(Integer, primary_key=True)
    nome = Column(String)

    def __init__(self, id_cliente, nome):
        self.id_cliente = id_cliente
        self.nome = nome

    def __str__(self):
        return f'{self.id_cliente}, {self.nome}'