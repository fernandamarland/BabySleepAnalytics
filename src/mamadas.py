from banco import conectar


def registrar_mamada():

    print("\n===== REGISTRO DE MAMADA =====")

    bebe = input("Nome do bebê: ")
    data = input("Data (dd/mm/aaaa): ")
    horario = input("Horário (HH:MM): ")
    quantidade = int(input("Quantidade (ml): "))
    formula = input("Fórmula utilizada: ")
    observacao = input("Observações: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO mamadas
        (bebe, data, horario, quantidade, formula, observacao)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        bebe,
        data,
        horario,
        quantidade,
        formula,
        observacao
    ))

    conexao.commit()
    conexao.close()

    print("\n✅ Mamada registrada com sucesso!")


def visualizar_mamadas():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM mamadas
        ORDER BY id
    """)

    registros = cursor.fetchall()

    conexao.close()

    print("\n===== HISTÓRICO DE MAMADAS =====")

    if len(registros) == 0:
        print("Nenhuma mamada registrada.")
        return

    for mamada in registros:

        print("\n----------------------------")
        print(f"ID: {mamada[0]}")
        print(f"Bebê: {mamada[1]}")
        print(f"Data: {mamada[2]}")
        print(f"Horário: {mamada[3]}")
        print(f"Quantidade: {mamada[4]} ml")
        print(f"Fórmula: {mamada[5]}")
        print(f"Observações: {mamada[6]}")