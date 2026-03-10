ouvidorias = [ ]

motivos = [ 
            "Atraso do produto",
            "Produto danificado",
            "Atendimento inadequado",
            "Produto não entregue"
        ]

print("Painel de ouvidoria \
    \n1 - Listar reclamações registradas \
    \n2 - Registrar uma nova reclamação \
    \n3 - Atualizar uma reclamação existente \
    \n4 - Remover uma reclamação pelo código \
    \n5 - Mostrar a quantidade total de reclamações pelo código \
    \n6 - Pesquisar a uma reclamação pelo código \
    \n7 - Sair" )
opcao = int(input("Digite o número da opção desejada: "))
while True:
    if opcao == 1:
        print(ouvidorias)
    elif opcao == 2:
        
        codigos = [ ]
        for i in range(len(motivos)):
            tabela_reclamacao = (f"F{i+1} - {motivos[i]}")
            codigo = (f"F{i+1}")
            codigos.append(codigo)
            print(tabela_reclamacao)
            
        escolha = input("Digite o código desejado: ").upper().strip()
        
        if escolha not in codigos:
            print("Alternativa não encontrada, Digite somente as disponíveis.")
        else:
            reclamar = input("Digite aqui o ocorrido: ")
            ouvidorias.append(f"{escolha} - {reclamar}")
            print("Sua reclamação foi registrada!")
            per = input("Deseja registrar outra reclamação? [sim/não]").lower().strip()
            if per == "sim":
                print("Prosseguindo para o próximo envio...")
                
            else:
                print("Registro de reclamação encerrado!")
                
            
        
    elif opcao == 3:
        print()
    elif opcao == 4:
        print()
    elif opcao == 5:
        print()
    elif opcao == 6:
        print()
    elif opcao == 7:
        print()