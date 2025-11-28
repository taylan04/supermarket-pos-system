from SIG.Servicos_db.db_compra import *
from tabulate import tabulate
import pandas as pd

def consultar_compra():
    print("\nDigite o ID da compra que deseja consultar: ")

    compra = consultar_compra(id)

    itens = []
    for item in compra.itens:
        itens.append([item.id_item, item.quantidade, item.preco, item.id_compra, item.id_produto])
    
    df = pd.DataFrame(itens, columns=["Item ID", "Quantidade", "Preço", "Compra ID", "Produto ID"])
    print("\n" + tabulate(df.values, headers=df.columns, tablefmt="grid"))