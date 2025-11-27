# Servicos simples para gerenciar registros de atendimentos
# Usa listas normais ao invés de banco de dados

def adicionar_registro(registros, cliente, total):
    registro = {
        "cliente": cliente,
        "total": total
    }
    registros.append(registro)
    return registros

def consultar_registros(registros):
    return registros

def limpar_registros(registros):
    registros.clear()
    return registros

