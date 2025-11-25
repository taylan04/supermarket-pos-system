from menu import *
from util import *
from arquivo import *
from Servicos.servicos_atendimento import *
from WebScraping.produtoslp import *
from Servicos.servicos_cliente import *
from Servicos.servicos_carrinho import *
from Servicos.servicos_produto import *

def gerenciar_caixa():
    escolha_inicial()
    opcao_inicial = entrar_inteiro_zero_permitido("\nOpção: ")

    if opcao_inicial == 0:
        print("\nCaixa continua fechado!")
        return

    elif opcao_inicial == 1:
        executar_todos_os_processos()
        popular_banco()
        registros = []

        while True:
            cliente = consultar_ou_cadastrar_cliente()
            carrinho = []

            while True:
                menu(cliente)
                opcao = entrar_inteiro("\nDigite o número de sua opção: ")

                match opcao:
                    case 1:
                        listar_produtos()
                    case 2:
                        listar_carrinho(carrinho)
                    case 3:
                        carrinho = adicionar_carrinho(carrinho)
                    case 4:
                        carrinho = excluir_produto_carrinho(carrinho)
                    case 5:
                        deve_sair, carrinho, registros = processar_fechamento_atendimento(cliente.nome, carrinho, registros)

                        if deve_sair:  
                            print("\nCaixa encerrado.")
                            return
                        else:
                            break
                    case __:
                        print("\nDigite um número válido.")

gerenciar_caixa()

