from banco import conectar


def registrar_alimentacao():

    print("\n===== REGISTRO DE ALIMENTAÇÃO =====")

    bebe = input("Nome do bebê: ")
    data = input("Data (dd/mm/aaaa): ")
    horario = input("Horário (HH:MM): ")
    refeicao = input("Tipo da refeição: ")
    alimento = input("Alimento: ")
    quantidade = input("Quantidade: ")
    aceitou = input("Aceitou? (Sim/Não): ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO alimentacao
        (bebe, data, horario, refeicao, alimento, quantidade, aceitou)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        bebe,
        data,
        horario,
        refeicao,
        alimento,
        quantidade,
        aceitou
    ))

    conexao.commit()
    conexao.close()

    print("\n✅ Alimentação registrada com sucesso!")


def visualizar_alimentacao():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alimentacao")

    registros = cursor.fetchall()

    conexao.close()

    print("\n===== HISTÓRICO DE ALIMENTAÇÃO =====")

    if len(registros) == 0:
        print("Nenhum registro encontrado.")
        return

    for registro in registros:

        print("\n----------------------------")
        print(f"ID: {registro[0]}")
        print(f"Bebê: {registro[1]}")
        print(f"Data: {registro[2]}")
        print(f"Horário: {registro[3]}")
        print(f"Refeição: {registro[4]}")
        print(f"Alimento: {registro[5]}")
        print(f"Quantidade: {registro[6]}")
        print(f"Aceitou: {registro[7]}")