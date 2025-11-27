from menu import *
from util import *
from arquivo import *
from Servicos_caixa.servicos_atendimento import *
from WebScraping.produtoslp import *
from Servicos_caixa.servicos_cliente import *
from Servicos_caixa.servicos_carrinho import *

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

        # Esse while é para continuar atendendo vários clientes até fechar o caixa
        while True:
            cliente = consultar_ou_cadastrar_cliente()
            carrinho = []

            # Esse while é para continuar no menu do mesmo cliente até ele finalizar o atendimento
            while True:
                menu(cliente)
                opcao = entrar_inteiro("\nDigite o número de sua opção: ")

                match opcao:
                    case 1:
                        carrinho = adicionar_carrinho(carrinho)
                    case 2:
                        deve_sair, carrinho, registros = processar_fechamento_atendimento(cliente.nome, carrinho, registros)

                        if deve_sair:  
                            print("\nCaixa encerrado.")
                            return
                        else:
                            break
                    case __:
                        print("\nDigite um número válido.")

gerenciar_caixa()

