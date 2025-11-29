from Caixa.Servicos_caixa_db.db_clientes import *
from tabulate import tabulate
import pandas as pd

def exibir_compras_do_cliente(id):
    cliente = pesquisar_cliente(id)

    compras_ordenadas = sorted(cliente.compras, key=lambda c: c.data_hora)
    dados = [[c.id, c.data_hora] for c in compras_ordenadas]
    df = pd.DataFrame(dados, columns=["Compra ID", "Data e Hora"])
    print("\n" + tabulate(df.values, headers=df.columns, tablefmt="rounded_outline"))

def exibir_clientes_mais_gastam():
    clientes = consultar_clientes()

    lista = []

    for cliente in clientes:
        for compra in cliente.compras:
            total_gasto = sum(item.preco for item in compra.itens)
            lista.append({"id_cliente": cliente.id_cliente,"cliente": cliente.nome,"total_gasto": total_gasto})
    
    df = pd.DataFrame(lista)
    gastos = df.groupby(["id_cliente", "cliente"])["total_gasto"].sum().reset_index().sort_values("total_gasto", ascending=False)

    df_exibir = pd.DataFrame(gastos, columns=["Cliente ID", "nome", "Total Gasto"])
    print("\n" + tabulate(df_exibir.values, headers=df_exibir.columns, tablefmt="grid"))
    
def exibir_clientes_mais_compram():
    clientes = consultar_clientes()

    lista = []

    for cliente in clientes:
        total_comprado = len(cliente.compras)
        lista.append({'id_cliente': cliente.id_cliente,'nome': cliente.nome,'total_comprado': total_comprado})
    
    df = pd.DataFrame(lista)
    comprados = df.sort_values("total_comprado", ascending=False)

    df_exibir = pd.DataFrame(comprados, columns=["Cliente ID", "nome", "Qtd. Compras"])
    print("\n" + tabulate(df_exibir.values, headers=df_exibir.columns, tablefmt="grid"))

    




