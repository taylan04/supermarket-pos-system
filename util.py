import datetime
from Caixa.arquivo import *
from sqlalchemy import func
from conexao import session

def entrar_inteiro(msg):
    opcao = 0
    while True:
        try:
            opcao = int(input(msg))
            if opcao > 0:
                return opcao
            else:
                print("\nDigite um número maior que 0.")
        except Exception as e:
            print(f"\nErro: número inválido. Digite um número inteiro\n{e}")

def entrar_inteiro_zero_permitido(msg):
    opcao = 0
    while True:
        try:
            opcao = int(input(msg))
            if opcao >= 0:
                return opcao
            else:
                print("\nDigite um numero maior ou igual a zero!")
        except Exception as e:
            print(f"\nErro: número inválido. Digite um número inteiro\n{e}")

def entrar_float(msg):
    opcao = 0
    while True:
        try:
            opcao = float(input(msg))
            if opcao > 0:
                return opcao
            else:
                print("\nDigite um numero maior que zero!")
        except Exception as e:
            print(f"\nErro: número inválido. Digite um número válido.\n{e}")

def entrar_string(msg):
    resultado = input(msg)
    return resultado

def hora_e_data_atual():
    data = datetime.datetime.now()
    return f"Data: {data.strftime("%d/%m/%Y")} {data.strftime("%H:%M")}"

def popular_banco():
    abertura_caixa()
    iniciar_clientes()

def gerar_proximo_id(objeto_com_id):
    #func.max pega o ID maximo que tem na tabela compras e o scalar me devolve apenas o numero, sem me retornaria objeto
    ultimo = session.query(func.max(objeto_com_id)).scalar()
    if ultimo is None:
        return 1
    return ultimo + 1

# cliente

def solicitar_nome_do_cliente():
    while True:
        nome = entrar_string("\nDigite o nome do cliente (Cliente #): ").strip()

        if "cliente" not in nome.lower():
            print("\nNome do cliente inválido! Deve conter 'Cliente'.")
            continue

        #ia fazer um for, mas estou tentando codificar melhor e com any talvez fique mais "elegante"
        # any() -> se um elemento da condição for verdadeiro retorna verdadeiro
        if not any(c.isdigit() for c in nome):
            print("\nO nome deve conter um número!")
            continue

        return nome

def retornar_id_do_cliente(nome):
    id_cliente = ""
    for c in nome:
        if c.isdigit():
            id_cliente += c
    return int(id_cliente)

