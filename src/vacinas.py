from banco import conectar


def registrar_vacina():

    print("\n===== REGISTRO DE VACINA =====")

    bebe = input("Nome do bebê: ")
    nome = input("Nome da vacina: ")
    data = input("Data da aplicação (dd/mm/aaaa): ")
    proxima = input("Próxima dose (dd/mm/aaaa): ")
    observacao = input("Observações: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO vacinas
        (bebe, nome, data, proxima, observacao)
        VALUES (?, ?, ?, ?, ?)
    """, (
        bebe,
        nome,
        data,
        proxima,
        observacao
    ))

    conexao.commit()
    conexao.close()

    print("\n✅ Vacina registrada com sucesso!")


def visualizar_vacinas():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM vacinas")

    registros = cursor.fetchall()

    conexao.close()

    print("\n===== HISTÓRICO DE VACINAS =====")

    if len(registros) == 0:
        print("Nenhuma vacina registrada.")
        return

    for vacina in registros:

        print("\n----------------------------")
        print(f"ID: {vacina[0]}")
        print(f"Bebê: {vacina[1]}")
        print(f"Vacina: {vacina[2]}")
        print(f"Data: {vacina[3]}")
        print(f"Próxima dose: {vacina[4]}")
        print(f"Observações: {vacina[5]}")