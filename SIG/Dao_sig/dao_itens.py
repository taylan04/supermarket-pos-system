from models import *
from SIG.Servicos_db.db_item import *

def salvar_itens_da_compra_db(carrinho, id_compra):
    for item in carrinho:
        quantidade, preco, id_compra, id_produto = item['quantidade'], item['valor'], id_compra, item['id_produto']
        item = Item(None, quantidade, round(preco, 2), id_compra, id_produto)
        adicionar_item(item)