from operacoesbd import *
from codigo import *

categorias_validas = {
    
    1: "elogio",
    2: "sugestao", 
    3: "reclamacao"
    
    }

connection = criarConexao("localhost", "root", "Code10091009!", "ouvidoriareclamacao")

def listarReclamacao(connection, ):
    try:
        cursor = connection.cursor()
        
        slq = "select * from reclamacoes"
        cursor.execute(slq)
        
        dados = cursor.fetchall()

        if len(dados) == 0:
            print("Nenhuma reclamação existente!")
        else:
            print("\n --- reclamações ---")
            for codigo, categoria, descricao in dados:
                print(f"Código: {codigo}")
                print(f"Categoria: {categoria}")
                print(f"Descrição: {descricao}")
                print(f"-=" * 30)
                
    except Exception as erro:
        print("Erro! não foi possivel listar as reclamações", erro)
        
    finally:
        cursor.close()        
        
def registrarReclamacao(connection):
    try:
        cursor = connection.cursor()
        
        reclamacao = input("Digite sua reclamação: ")
        print(categorias_validas)              
        categoria_num = int(input("Digite o número da categoria: "))
        
        if categoria_num not in categorias_validas:
            print("categoria inválida")
        
        categoria = categorias_validas[categoria_num]
        
        print("Categoria válida:", categoria)
        
        codigo = CodigoGerado()
        
        sql = "insert into reclamacoes(codigo, categoria, descricao) values(%s, %s, %s)"
        
        dados = (codigo, categoria, reclamacao)
        
        cursor.execute(sql, dados)
        connection.commit()   
        
        print("Reclamação registrada com sucesso!")     
    
    except Exception as erro:
        print("Erro ao tentar registrar", erro)
        
    finally:
        cursor.close()
        
def PesquisarReclamacao(connection):
    try:
    
        cursor = connection.cursor()
        codigo_pes = input("Digite o código da sua reclamação: ")
        
        sql = "select * from reclamacoes where codigo = %s"
        cursor.execute(sql, (codigo_pes,))
        dados = cursor.fetchall()
        
        
        if not dados:
            print("Código não encontrado!")
            return
        else:
            for codigo, categoria, descricao in dados:
                print(f"Código: {codigo}")
                print(f"Categgoria: { categoria}")
                print(f"Descrição: {descricao}")
                
    except Exception as erro:
        print("Não foi possível pesquisar o código", erro)
        
    finally:
        cursor.close()
        
def AtualizarReclamacao(connection):
    try:
        cursor = connection.cursor()
        codigo_pes = input("Digite o código da sua reclamação: ")
        
        sql = "select * from reclamacoes where codigo = %s"
        cursor.execute(sql, (codigo_pes,))
        dados = cursor.fetchall()
        
        
        if not dados:
            print("Código não encontrado!")
            return
        else:
            for codigo, categoria, descricao in dados:
                print(f"Código: {codigo}")
                print(f"Categgoria: { categoria}")
                print(f"Descrição: {descricao}")
                
        print("\n1 - Categoria\n2 - Descrição")
        per = int("O que deseja mudar na sua reclamação? Digite o número:")
        if per == 1:
            for numero, nome in categorias_validas:
                print(f"{numero} - {nome}")
                
            nova_opcao = int(input("Digite o número da categoria que deseja: "))
            
            if nova_opcao not in categorias_validas:
                print("Categoria inválida")
                return
        
            nova_categoria = categorias_validas[nova_opcao]
            
            sql_update = "update reclamacoes set categoria = %s where codigo = %s"
            cursor.execut(sql_update, (nova_categoria, codigo_pes) )
        
        elif per == 2:
            nova_descrição = input("Digite a nova descrição: ")
            sql_update = "update reclamacoes set descricao where codigo = %s"
            cursor.execute(sql_update, (nova_descrição, codigo))
        else:
            print("opção inválida.")
            return
        
    except Exception as erro:
        print("Não foi possível atualizar", erro)
            
    finally:
        cursor.close()
        
def RemoverReclamacao(connection):
    try:
        cursor = connection.cursor()
        
        codigo_pes = input("Digite o código da reclamação que deseja remover: ")
        
        sql = "select * from reclamacoes where codigo = %s"
        cursor.execute(sql, (codigo_pes,))
        dados = cursor.fetchall()
        
        if not dados:
            print("Dados não encontrados.")
            return
        
        sql_remove = "delete from reclamacoes where codigo = %s"
        cursor.execute(sql_remove, (codigo_pes,)) 
        connection.commit()
         
        print("Reclamação removida com sucesso!")
        
    except Exception as erro:
        print("Não foi possivel remover a reclamação", erro)
        
    finally:
        cursor.close()
        
def QuantidadeReclamacoes(connection):
    try:
        cursor = connection.cursor()
        
        sql_print = "select count(*) from reclamacoes"
        cursor.execute(sql_print)
        
        quantidade = cursor.fetchone()[0]
        
        if quantidade == 0:
            print("Você não tem reclamações")
        else:
            print(f"Você tem um total de {quantidade} reclamações")
    
    except Exception as erro:
        print("Não foi possivel ver a quantidade de reclamações")
    finally:
        cursor.close()