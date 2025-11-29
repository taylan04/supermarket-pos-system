from SIG.Servicos_db.db_compra import *
from tabulate import tabulate
from util import *
import pandas as pd

def exibir_compra():
    id_compra = entrar_inteiro("\nDigite o ID da compra que deseja consultar: ")

    compra = consultar_compra(id_compra)
    
    if not compra:
        print("\nCompra não encontrada.")
        return

    print("\n===== NOTA FISCAL =====")
    print(f"Compra ID: {compra.id_compra}")
    print(f"Cliente: {compra.cliente.nome}")
    print(f"Data e Hora: {compra.data_hora}")
    print("\nItens:")
    
    itens = []
    for item in compra.itens:
        itens.append([item.id_item, item.quantidade, item.preco, item.id_compra, item.id_produto])
    
    df = pd.DataFrame(itens, columns=["Item ID", "Quantidade", "Preço", "Compra ID", "Produto ID"])

    valor_total_compra = sum(item.preco for item in compra.itens)
    
    print("\n" + tabulate(df.values, headers=df.columns, tablefmt="grid"))
    print(f"\nValor total da compra: {valor_total_compra}")