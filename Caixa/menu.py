from util import *

def fechar_caixa_ou_continuar():
    print("\n[0] - Fechar Caixa")
    print("[1] - Continuar Atendimento")

def escolha_inicial():
    print("\n[0] - Não abrir o caixa")
    print("[1] - Abrir o caixa")
    print("\nVocê deseja abrir o caixa?")

def menu(cliente):
    print("\n===== CAIXA =====")
    print(f"\nVocê está atendendo {cliente.nome}, o que deseja realizar?\n")
    print("[1] - Adicionar produto na compra")
    print("[2] - Finalizar Atendimento")

