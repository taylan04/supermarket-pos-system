from SIG.Servicos_db.db_compra import *
from tabulate import tabulate
from util import *
import pandas as pd

def exibir_compra(id_compra):
    compra = consultar_compra(id_compra)
    
    if not compra:
        print("\nCompra não encontrada.")
        return

    print("\n===== NOTA FISCAL =====")
    print(f"Compra ID: {compra.id_compra}")
    print(f"Cliente: {compra.cliente.nome}")
    print(f"Data e Hora: {compra.data_hora.strftime("%d/%m/%Y %H:%M")}")
    print("\nItens:")
    
    itens = []
    for item in compra.itens:
        itens.append([item.produto_referenciado.nome, item.quantidade, item.preco])
    
    df = pd.DataFrame(itens, columns=["Produto", "Quantidade", "Preço"])

    df_agrupado = df.groupby("Produto", as_index=False).agg({"Quantidade": "sum","Preço": "sum"})

    valor_total_compra = sum(item.preco for item in compra.itens)
    
    print("\n" + tabulate(df_agrupado.values, headers=df.columns, tablefmt="grid"))
    print(f"\nValor total da compra: R$ {round(valor_total_compra, 2)}")