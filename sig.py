from SIG.Consultas.consultas_clientes import *
from SIG.excel_util import *
from SIG.menu import *
from util import *


def gerenciar_sig():
    menu_inicial()
    opcao_inicial = entrar_inteiro_zero_permitido("\nOpção: ")

    if opcao_inicial == 0:
        print("\nSIG não acessado. Volte sempre!")
        return

    elif opcao_inicial == 1:
        executar_carga_fornecedores_e_produtos()

        while True:
            menu_secundario()
            opcao_inicial = entrar_inteiro_zero_permitido("\nOpção: ")

            if opcao_inicial == 0:
                pass

            elif opcao_inicial == 1:
                pass
            else:
                print("\nDigite uma das opções.")
                continue


gerenciar_sig()