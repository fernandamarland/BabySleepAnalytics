from banco import conectar


def registrar_sono():

    print("\n===== REGISTRO DE SONO =====")

    bebe = input("Nome do bebê: ")
    data = input("Data (dd/mm/aaaa): ")
    hora_inicio = input("Hora que dormiu (HH:MM): ")
    hora_fim = input("Hora que acordou (HH:MM): ")
    tipo = input("Tipo (Soneca / Noturno): ")
    observacao = input("Observações: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO sono
        (bebe, data, hora_inicio, hora_fim, tipo, observacao)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        bebe,
        data,
        hora_inicio,
        hora_fim,
        tipo,
        observacao
    ))

    conexao.commit()
    conexao.close()

    print("\n✅ Sono registrado com sucesso!")


def visualizar_sono():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM sono")

    registros = cursor.fetchall()

    conexao.close()

    print("\n===== HISTÓRICO DE SONO =====")

    if len(registros) == 0:
        print("Nenhum registro encontrado.")
        return

    for sono in registros:

        print("\n---------------------------")
        print(f"ID: {sono[0]}")
        print(f"Bebê: {sono[1]}")
        print(f"Data: {sono[2]}")
        print(f"Dormiu: {sono[3]}")
        print(f"Acordou: {sono[4]}")
        print(f"Tipo: {sono[5]}")
        print(f"Observações: {sono[6]}")