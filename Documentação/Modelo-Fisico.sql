CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INTEGER PRIMARY KEY,
    nome VARCHAR(100)
)

CREATE TABLE IF NOT EXISTS compras (
    id_compra INTEGER PRIMARY KEY,
    data_hora TIMESTAMP,
    id_cliente INTEGER,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
)

CREATE TABLE IF NOT EXISTS itens (
    id_item INTEGER PRIMARY KEY,
    quantidade INTEGER,
    preco FLOAT,
    id_compra INTEGER,
    id_produto INTEGER,
    FOREIGN KEY (id_compra) REFERENCES compras(id_compra),
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
)

CREATE TABLE IF NOT EXISTS produtos (
    id_produto INTEGER PRIMARY KEY,
    nome VARCHAR(100),
    quantidade INTEGER,
    preco FLOAT
)

CREATE TABLE IF NOT EXISTS fornecedor_produtos (
    id_fornecedor INTEGER,
    id_produto INTEGER,
    PRIMARY KEY (id_fornecedor, id_produto),
    FOREIGN KEY (id_fornecedor) REFERENCES fornecedores(id_fornecedor),
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
)

CREATE TABLE IF NOT EXISTS fornecedores (
    id_fornecedor INTEGER PRIMARY KEY,
    nome VARCHAR(100)
)