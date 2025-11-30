from util import *
from SIG.menus.menus import *
from SIG.menus.gerenciar import *
from SIG.excel_util import *

def gerenciar_sig():
    while True:
        menu_inicial()
        opcao = entrar_inteiro_zero_permitido("\nOpção: ")

        match opcao:
            case 0: 
                executar_carga_fornecedores_e_produtos()
                menu_principal()
                opcao = entrar_inteiro_zero_permitido("\nOpção: ")
                
                match opcao:
                    case 0:
                        gerenciar_clientes()
                    case 1:
                        gerenciar_produtos()     
                    case 2:
                        continue 
                    case _:
                        print("\nOpção inválida.")
            case 1:
                print("\nSaindo do sistema.")
                break

gerenciar_sig()
