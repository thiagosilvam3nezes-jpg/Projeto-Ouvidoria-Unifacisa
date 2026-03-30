from funcoesOuvidoria import *

print("""Grupo composto por:
Thiago Silva Menezes - 2613080042
Danilo Silva Menezes - 2613080091
PEDRO HENRIQUE CABRAL DE ARAUJO - 2613080033
MAYKE WILLYAN SILVA MOURA - 2613080027 """)

ouvidorias = []

opcao = 0

while opcao != 7:
    print(""" 
1) listar todas as reclamações registradas 
2) Registrar uma reclamação
3) Pesquisar reclamação pelo código 
4) Atualizar uma reclamação existente
5) Remover uma reclamação pelo código
6) Exibir a quantidade total de reclamação cadastradas 
7) Sair do sistema """)
    
    opcao = int(input("Digite sua opcão: "))
    
    if opcao == 1:
        
        listarReclamacao(connection)
                
    if opcao == 2:
        
        registrarReclamacao(connection)
        
    if opcao == 3:
        
        PesquisarReclamacao(connection)
                
    if opcao == 4:
        
        AtualizarReclamacao(connection)
        
    if opcao == 5:
        
        RemoverReclamacao(connection)
    
    if opcao == 6:
        
        QuantidadeReclamacoes(connection)

else:
    print("Sistema encerrado!")
    