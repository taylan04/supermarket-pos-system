from SIG.Consultas.consultas_clientes import *
from SIG.Consultas.consultas_compras import *
from SIG.Consultas.consultas_produtos import *
from SIG.menus.menus import *
from Caixa.Servicos_caixa_db.db_produtos import *
from Caixa.Servicos_caixa_db.db_clientes import *
from Caixa.Servicos_caixa.servicos_produto import *
from SIG.Servicos_db.db_fornecedor import consultar_fornecedores, consultar_fornecedor
from util import *
from models import *

def gerenciar_clientes_com_compras():
    while True:
        menu_clientes_com_compras()
        opcao = entrar_inteiro_zero_permitido("\nOpção: ")
        
        match opcao:
            case 0:
                id_cliente = entrar_inteiro("\nDigite o ID do cliente: ")
                cliente = pesquisar_cliente(id_cliente)
                
                if not cliente:
                    print("\nCliente não encontrado.")
                    continue
                
                if not cliente.compras:
                    print("\nEste cliente não possui compras.")
                    continue
                
                exibir_compras_do_cliente(id_cliente)
                
                id_compra = entrar_inteiro_zero_permitido("\nDigite o ID da compra que deseja consultar (ou 0 para voltar): ")
                if id_compra == 0:
                    continue
                
                exibir_compra(id_compra)
            case 1:
                exibir_clientes_mais_compram()
            case 2:
                exibir_clientes_mais_gastam()  
            case 3:
                return
            case _:
                print("\nOpção inválida.")

def gerenciar_clientes():
    while True:
        menu_clientes()
        opcao = entrar_inteiro_zero_permitido("\nOpção: ")
        
        match opcao:
            case 0:
                exibir_clientes_com_compras()
                gerenciar_clientes_com_compras()        
            case 1:
                exibir_clientes_sem_compras()
            case 2:
                return 
            case _:
                print("\nOpção inválida.")

def gerenciar_fornecedores_produto(id_produto):
    produto = pesquisar_produto(id_produto)
    
    if not produto:
        print("\nProduto não encontrado.")
        return
    
    while True:
        print("\n[0] - Adicionar fornecedor")
        print("[1] - Finalizar")
        
        opcao = entrar_inteiro_zero_permitido("\nOpção: ")
        
        match opcao:
            case 0:
                fornecedores = consultar_fornecedores()
                if not fornecedores:
                    print("\nNão há fornecedores cadastrados.")
                    continue
                
                print("\nFornecedores disponíveis:")
                for f in fornecedores:
                    print(f"ID: {f.id_fornecedor}, Nome: {f.nome}")
                
                id_fornecedor = entrar_inteiro("\nDigite o ID do fornecedor: ")
                fornecedor = consultar_fornecedor(id_fornecedor)
                adicionar_fornecedor_ao_produto(produto, fornecedor)
                print("\nFornecedor adicionado!")
                
            case 1:
                return    
            case _:
                print("\nOpção inválida.")

def gerenciar_consultas_produtos():
    while True:
        menu_consultas_produtos()
        opcao = entrar_inteiro_zero_permitido("\nOpção: ")
        match opcao:
            case 0:
                produtos_mais_vendidos_e_menos_vendidos()
            case 1:
                produtos_com_pouco_estoque()
            case 2:
                fornecedores_do_produto()
            case 3:
                return
            case _:
                print("\nOpção inválida.")

def gerenciar_produtos():
    while True:
        menu_produtos()
        opcao = entrar_inteiro_zero_permitido("\nOpção: ")
        
        match opcao:
            case 0:
                id_produto = adicionar_produto_novo()
                print("\nDeseja associar fornecedores a este produto?")
                print("[0] - Sim")
                print("[1] - Não")
                escolha = entrar_inteiro_zero_permitido("\nOpção: ")
                
                if escolha == 0:
                    gerenciar_fornecedores_produto(id_produto)  
            case 1:
                listar_produtos()
            case 2:
                atualizar_dados_do_produto()
            case 3:
                remover_produto_do_banco()
            case 4:
                gerenciar_consultas_produtos()
            case 5:
                return
                
            case _:
                print("\nOpção inválida.")
