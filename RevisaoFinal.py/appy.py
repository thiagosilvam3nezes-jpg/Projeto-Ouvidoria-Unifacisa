print("""Grupo composto por:
Thiago Silva Menezes - 2613080042
Danilo Silva Menezes - 2613080091
PEDRO HENRIQUE CABRAL DE ARAUJO - 2613080033
MAYKE WILLYAN SILVA MOURA - 2613080027 - """)

from operacoesbd import criarConexao, encerrarConexao
from FuncoesOuvidoria import *

user = input("Usuário: ")
senha = input("Senha: ")
banco = input("Banco: ")

connection = criarConexao("localhost", user, senha, banco)

if not connection:
    print("[ERRO] Falha na conexão.")
    exit()

while True:
    print("\n" + "="*50)
    print(f"{'SISTEMA DE OUVIDORIA':^50}")
    print("="*50)

    print("""
    1 - Listar Reclamações
    2 - Registrar Reclamação
    3 - Pesquisar Reclamação
    4 - Atualizar Reclamação
    5 - Remover Reclamação
    6 - Quantidade
    7 - Sair
    """)

    entrada = input("Escolha: ")

    if not entrada.isdigit():
        print("[ERRO] Digite apenas números!")
        continue

    opcao = int(entrada)

    if opcao == 1:
        listar_reclamacoes(connection)
    elif opcao == 2:
        inserir_reclamacao(connection)
    elif opcao == 3:
        pesquisar_reclamacao(connection)
    elif opcao == 4:
        atualizar_reclamacao(connection)
    elif opcao == 5:
        remover_reclamacao(connection)
    elif opcao == 6:
        quantidade_reclamacoes(connection)
    elif opcao == 7:
        print("Encerrando sistema...")
        break
    else:
        print("[ERRO] Opção inválida!")

encerrarConexao(connection)
