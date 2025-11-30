from Caixa.Servicos_caixa_db.db_clientes import *
from tabulate import tabulate
import pandas as pd

def exibir_compras_do_cliente(id):
    cliente = pesquisar_cliente(id)

    compras_ordenadas = sorted(cliente.compras, key=lambda c: c.data_hora, reverse=True)
    dados = [[c.id_compra, c.data_hora] for c in compras_ordenadas]
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

    gastos.columns = ["Cliente ID", "nome", "Total Gasto"]
    print("\n" + tabulate(gastos.values, headers=gastos.columns, tablefmt="rounded_outline"))
    
def exibir_clientes_mais_compram():
    clientes = [cliente for cliente in consultar_clientes() if cliente.compras]

    lista = []

    for cliente in clientes:
        total_comprado = len(cliente.compras)
        lista.append({'id_cliente': cliente.id_cliente,'nome': cliente.nome,'total_comprado': total_comprado})
    
    df = pd.DataFrame(lista)
    comprados = df.sort_values("total_comprado", ascending=False)

    comprados.columns = ["Cliente ID", "nome", "Qtd. Compras"]
    print("\n" + tabulate(comprados.values, headers=comprados.columns, tablefmt="rounded_outline"))

def exibir_clientes_sem_compras():
    clientes = consultar_clientes()
    
    clientes_sem_compras = [cliente for cliente in clientes if len(cliente.compras) == 0]
    
    if not clientes_sem_compras:
        print("\nNão há clientes sem compras.")
        return
    
    dados = [[c.id_cliente, c.nome] for c in clientes_sem_compras]
    df = pd.DataFrame(dados, columns=["Cliente ID", "Nome"])
    print("\n" + tabulate(df.values, headers=df.columns, tablefmt="rounded_outline"))



