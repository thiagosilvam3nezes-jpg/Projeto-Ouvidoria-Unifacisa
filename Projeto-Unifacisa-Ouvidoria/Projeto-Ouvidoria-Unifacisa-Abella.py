print("""Grupo composto por:
Thiago Silva Menezes - 2613080042
Danilo Silva Menezes - 2613080091
PEDRO HENRIQUE CABRAL DE ARAUJO - 2613080033
MAYKE WILLYAN SILVA MOURA - 2613080027 - """)

ouvidorias = []
codigos = ["F1","F2","F3","F4"]
motivos = [
    "Atendimento inadequado",
    "Demora no serviço",
    "Problema no sistema",
    "Outro problema"
]
opcao = 0

while opcao != 7:
    print(""" 
1) listar todas as reclamações registradas 
2) Registrar uma nova reclamação
3) Pesquisar reclamação pelo código 
4) Atualizar uma reclamação existente
5) Remover uma reclamação pelo código
6) Exibir a quantidade total de reclamação cadastradas 
7) Sair do sistema """)
    
    opcao = int(input("Digite sua opcão: "))
    
    if opcao == 1:
        
        if len(ouvidorias) == 0:
            print("\nNenhuma reclamação cadastrada no momento")
        else:
            print("\n--- Reclamações Registradas ---")
            for ouvidoria in range(len(ouvidorias)):
                print(str(ouvidoria + 1) + " - " + ouvidorias[ouvidoria])
                
    if opcao == 2:
        
        for i in range(len(motivos)):
            tabela_reclamacao = (f"F{i+1} - {motivos[i]}")
            print(tabela_reclamacao)
            
        escolha = input("Digite o código desejado: ").upper().strip()
        
        if escolha not in codigos:
            print("Alternativa não encontrada, Digite somente as disponíveis.")
            
        else:
            reclamar = input("Digite aqui o ocorrido: ")
            ouvidorias.append(f"{escolha} - {reclamar}")
            print("Sua reclamação foi registrada!")
            per = input("Deseja registrar outra reclamação? [sim/não]").lower().strip()
            while per == "sim":
              
                print("Prosseguindo para o próximo envio...")
                for i in range(len(motivos)):
                    print(f"F{i+1} - {motivos[i]}")
                escolha = input("Digite o código desejado: ").upper().strip()
                if escolha not in codigos:
                    print("Alternativa não encontrada, Digite somente as disponíveis.")
                    
                else:
                    reclamar = input("Digite aqui o ocorrido: ")
                    ouvidorias.append(f"{escolha} - {reclamar}")
                    print("Sua reclamação foi registrada!")
                    per = input("Deseja registrar outra reclamação? [sim/não]").lower().strip()
                
            else:
                print("Registro de reclamação encerrado!")
                print("Voltando ao Painel de ouvidoria")
    if opcao == 3:

        if len(ouvidorias) == 0:
            print("Não há reclamações registradas.")

        else:
            codigo_busca = input("Digite o código de reclamação (Exemplo: F1): ").upper().strip()

            encontrado = False

            for reclamacao in ouvidorias:
                codigo = reclamacao.split(" - ")[0]

                if codigo == codigo_busca:
                    print(reclamacao)
                    encontrado = True

            if not encontrado:
                print("Nenhuma reclamação foi encontrada!")
                
    if opcao == 4:
        
        for ouvidoria in range(len(ouvidorias)):
            print(f"{ouvidoria + 1} - {ouvidorias[ouvidoria]}")
            
        escolha_usuario_substituir = int(input("Escolher uma reclamação pelo código para atualizar (Exemplo: 1, 2, ...): "))
        if escolha_usuario_substituir < 1 or escolha_usuario_substituir > len(ouvidorias):
            print("O código de reclamação escolhido não está dentro dentro")
        
        else:
            nova_razao = input("Escreva a nova razão de reclamação: ")
            ouvidorias[escolha_usuario_substituir - 1] = nova_razao
            
            print("Reclamação atualizada com sucesso!")
    if opcao == 5:
        
        for ouvidoria in range(len(ouvidorias)):
            print(f"{ouvidoria + 1} - {ouvidorias[ouvidoria]}")
            
        escolha_usuario_remove = int(input("Escolha uma reclamação pelo código para remover (Exemplo: 1, 2, ...): "))
        
        if escolha_usuario_remove <= 0 or escolha_usuario_remove > len(ouvidorias):
            print("O código de reclamação escolhido não está dentro dos parâmetros.")
        
        else:
            ouvidorias.pop(escolha_usuario_remove - 1)
            
            print("Reclamação removida com sucesso")
    
    if opcao == 6:
        
        count = 0
        
        for i in range(len(ouvidorias)):
            count += 1 
        print(f"Existem {count} ouvidoras cadastradas")

else:
    print("Sistema encerrado!")
    