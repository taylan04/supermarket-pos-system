from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#como é apenas uma tabela intermediária e não tem atributos extras, não é bom colocar como classe (pesquisei)
Produto_fornecedor = Table(
    'produto_fornecedor',
    Base.metadata,
    Column('id_fornecedor', Integer, ForeignKey('fornecedores.id_fornecedor'), primary_key=True),
    Column('id_produto', Integer, ForeignKey('produtos.id_produto'), primary_key=True)
)

class Produto(Base):
    __tablename__ = "produtos"

    id_produto = Column(Integer, primary_key=True)
    nome = Column(String)
    preco = Column(Float)
    quantidade = Column(Integer)

    fornecedores = relationship("Fornecedor", secondary=Produto_fornecedor, back_populates="produtos")
    itens_comprados = relationship("Item", back_populates="produto_referenciado")

    def __init__(self, id_produto, nome, preco, quantidade):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f'{self.id_produto}, {self.nome}, {self.quantidade}, {self.preco}'
    
class Cliente(Base):
    __tablename__ = "clientes"

    id_cliente = Column(Integer, primary_key=True)
    nome = Column(String)

    compras = relationship('Compra', cascade="all, delete-orphan", back_populates='cliente')

    def __init__(self, id_cliente, nome):
        self.id_cliente = id_cliente
        self.nome = nome

    def __str__(self):
        return f'{self.id_cliente}, {self.nome}'
    
class Compra(Base):
    __tablename__ = "compras"

    id_compra = Column(Integer, primary_key=True)
    data_hora = Column(DateTime)
    id_cliente = Column(Integer, ForeignKey('clientes.id_cliente'))

    cliente = relationship('Cliente', back_populates='compras')
    itens = relationship("Item",cascade="all, delete-orphan", back_populates="compra")

    def __init__(self, id_compra, data_hora, id_cliente):
        self.id_compra = id_compra
        self.data_hora = data_hora
        self.id_cliente = id_cliente

    def total(self):
        return sum(item.quantidade * item.produto_referenciado.preco for item in self.itens)

    def __str__(self):
        return f'{self.id_compra}, {self.data_hora}, {self.id_cliente}'

class Fornecedor(Base):
    __tablename__="fornecedores"

    id_fornecedor = Column(Integer, primary_key=True)
    nome = Column(String)

    produtos = relationship("Produto", secondary=Produto_fornecedor, back_populates="fornecedores")

    def __init__(self, id_fornecedor, nome):
        self.id_fornecedor = id_fornecedor
        self.nome = nome

    def __str__(self):
        return f'{self.id_fornecedor}, {self.nome}'

class Item(Base):
    __tablename__="itens"

    id_item = Column(Integer, primary_key=True)
    quantidade = Column(Integer)
    preco = Column(Float)
    id_compra = Column(Integer, ForeignKey("compras.id_compra"))
    id_produto = Column(Integer, ForeignKey("produtos.id_produto"))

    produto_referenciado = relationship("Produto", back_populates="itens_comprados")
    compra = relationship("Compra", back_populates="itens")

    def __init__(self, id_item, quantidade, preco, id_compra, id_produto):
        self.id_item = id_item
        self.quantidade = quantidade
        self.preco = preco
        self.id_compra = id_compra
        self.id_produto = id_produto

    def __str__(self):
        return f'{self.id_item}, {self.quantidade}, {self.preco}, {self.id_compra}, {self.id_produto}'

