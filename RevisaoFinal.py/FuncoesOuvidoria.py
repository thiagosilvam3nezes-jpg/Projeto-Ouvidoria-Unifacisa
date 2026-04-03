from operacoesbd import *
import random

categorias = {
    1: "Elogio",
    2: "Sugestão",
    3: "Reclamação"
}

def gerar_codigo():
    return random.randint(1000, 9999)


def listar_reclamacoes(connection):
    sql = "SELECT * FROM reclamacoes"
    dados = listarBancoDados(connection, sql)

    if not dados:
        print("\nNenhuma reclamação cadastrada.\n")
        return

    print("\n--- RECLAMAÇÕES ---")
    for codigo, categoria, descricao in dados:
        print(f"\n🔹ID: {codigo}")
        print(f"🔸Categoria: {categoria}")
        print(f"📝Descrição: {descricao}")
        print("-" * 30)


def inserir_reclamacao(connection):
    print("\nCategorias:")
    for chave, valor in categorias.items():
        print(f"{chave} - {valor}")

    entrada = input("Escolha: ")

    if not entrada.isdigit():
        print("[ERRO] Digite um número!")
        return

    opcao = int(entrada)

    if opcao not in categorias:
        print("[ERRO] Categoria inválida!")
        return

    descricao = input("Digite a descrição: ")

    if not descricao.strip():
        print("[ERRO] Descrição vazia!")
        return

    codigo = gerar_codigo()

    sql = "INSERT INTO reclamacoes (codigo, categoria, descricao) VALUES (%s, %s, %s)"
    dados = (codigo, categorias[opcao], descricao)

    insertNoBancoDados(connection, sql, dados)

    print("✅ Reclamação registrada!")


def pesquisar_reclamacao(connection):
    codigo = input("Digite o código: ")

    sql = "SELECT * FROM reclamacoes WHERE codigo = %s"
    dados = listarBancoDados(connection, sql, (codigo,))

    if not dados:
        print("Código não encontrado.")
        return

    for c, cat, desc in dados:
        print(f"\n🔹ID: {c}")
        print(f"🔸Categoria: {cat}")
        print(f"📝Descrição: {desc}")


def atualizar_reclamacao(connection):
    codigo = input("Digite o código: ")

    sql = "SELECT * FROM reclamacoes WHERE codigo = %s"
    dados = listarBancoDados(connection, sql, (codigo,))

    if not dados:
        print("Código não encontrado.")
        return

    print("\n1 - Categoria\n2 - Descrição")
    escolha = input("O que deseja alterar? ")

    if not escolha.isdigit():
        print("Opção inválida.")
        return

    escolha = int(escolha)

    if escolha == 1:
        for chave, valor in categorias.items():
            print(f"{chave} - {valor}")

        nova = input("Escolha: ")

        if not nova.isdigit() or int(nova) not in categorias:
            print("Categoria inválida.")
            return

        sql = "UPDATE reclamacoes SET categoria = %s WHERE codigo = %s"
        atualizarBancoDados(connection, sql, (categorias[int(nova)], codigo))

    elif escolha == 2:
        nova_desc = input("Nova descrição: ")

        if not nova_desc.strip():
            print("Descrição inválida.")
            return

        sql = "UPDATE reclamacoes SET descricao = %s WHERE codigo = %s"
        atualizarBancoDados(connection, sql, (nova_desc, codigo))

    else:
        print("Opção inválida.")
        return

    print("✅ Atualizado com sucesso!")


def remover_reclamacao(connection):
    codigo = input("Digite o código: ")

    sql = "SELECT * FROM reclamacoes WHERE codigo = %s"
    dados = listarBancoDados(connection, sql, (codigo,))

    if not dados:
        print("Código não encontrado.")
        return

    confirmar = input("Tem certeza? (S/N): ").upper()

    if confirmar != "S":
        print("Cancelado.")
        return

    sql = "DELETE FROM reclamacoes WHERE codigo = %s"
    excluirBancoDados(connection, sql, (codigo,))

    print("🗑️ Removido com sucesso!")


def quantidade_reclamacoes(connection):
    sql = "SELECT * FROM reclamacoes"
    dados = listarBancoDados(connection, sql)

    print(f"\nTotal de reclamações: {len(dados)}")
    