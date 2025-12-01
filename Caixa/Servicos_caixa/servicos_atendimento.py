from Caixa.menu import *
from util import *
from Caixa.arquivo import *
import pandas as pd
from tabulate import tabulate
from .servicos_produto import *
from .servicos_registros import *
from .servicos_carrinho import *
from Caixa.Servicos_caixa_db.db_produtos import *
from models import *
from SIG.Servicos_db.db_compra import *
from Caixa.Servicos_caixa.servicos_item import *

# sem o . não funcionou, porque eu criei uma pasta para o serviços e sem o ponto ele procura
# no diretório principal, com o ponto ele procura "aqui mesmo". ( pesquisei )
        
# atendimento

def dar_baixa_no_estoque(carrinho):
    produtos = consultar_produtos()
    
    for item in carrinho:
        for produto in produtos:
            if item["id_produto"] == produto.id_produto:
                quantidade_retirada = item["quantidade"]
                nova_qtd = produto.quantidade - quantidade_retirada
                atualizar_produto(produto.id_produto, {"quantidade": nova_qtd})

def finalizar_atendimento(cliente, carrinho, registros):
    data = datetime.datetime.now()
    print(f"\nAtendimento do {cliente.nome} finalizado!")
    print(f"Data: {data.strftime("%d/%m/%Y %H:%M")}")

    if not carrinho:
        print("\nCarrinho Vazio.")
    else:
        tabela = []
        for item in carrinho:
            tabela.append([item["id"], item["nome"], item["quantidade"], item["preco uni"], item["valor"]])

        df = pd.DataFrame(tabela, columns=["Item", "Produto", "Quantidade", "Preço Uni.", "Total"])
        df = df.groupby("Produto").agg({"Quantidade":"sum", "Preço Uni.": "first", "Total":"sum"}).reset_index()
        df.insert(0, "Item", range(1, len(df) + 1))
        total_itens = len(df)
        total_valor = df["Total"].sum()

        print("\n" + tabulate(df.values, headers=df.columns, tablefmt="rounded_outline"))
        print(f"\nTotal de itens distintos comprados: {total_itens}")
        print(f"Total gasto: R$ {round(total_valor, 2)}")

        adicionar_registro(registros, cliente.nome, total_valor)
        
        #adicionar na tabela compras
        id_compra = gerar_proximo_id(Compra.id_compra)
        compra = Compra(id_compra, data, cliente.id_cliente)
        adicionar_compra(compra)
        salvar_itens_da_compra_db(carrinho, id_compra)

        #dar baixa no estoque quando finaliza o atendimento
        dar_baixa_no_estoque(carrinho)
        limpar_carrinho(carrinho)

def encerrar_atendimento(registros):
    data = datetime.datetime.now()
    print("\nFechamento do caixa!")
    print(f"Data: {data.strftime("%d/%m/%Y %H:%M")}")

    if not registros:
        tabela = [["Sem registro de clientes"]]
        print(f"\n{tabulate(tabela, tablefmt='rounded_outline')}")
        return

    tabela = []
    for registro in registros:
        tabela.append([registro["cliente"], registro["total"]])
    
    df = pd.DataFrame(tabela, columns=["Cliente", "Total"])
    df = df.groupby("Cliente")['Total'].sum().reset_index()
    total_vendas = df['Total'].sum()
    print("\n" + tabulate(df.values, headers=df.columns, tablefmt="rounded_outline"))
    print(f"Total de vendas: R$ {round(total_vendas, 2)}")

def processar_fechamento_atendimento(cliente, carrinho, registros):
    finalizar_atendimento(cliente, carrinho, registros)
    fechar_caixa_ou_continuar()
    opcao_fechar = entrar_inteiro_zero_permitido("\nDigite o número de sua opção: ")
    
    if opcao_fechar == 0:
        encerrar_atendimento(registros)
        produtos_esgotados()
        limpar_registros(registros)
        salvar_csv()
        return True, carrinho, registros
    elif opcao_fechar == 1:
        limpar_carrinho(carrinho)
        return False, carrinho, registros
    
    return False, carrinho, registros       