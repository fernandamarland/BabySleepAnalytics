from banco import conectar


def cadastrar_bebe():

    print("\n===== CADASTRO DO BEBÊ =====")

    nome = input("Nome do bebê: ")
    idade = int(input("Idade (meses): "))
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (cm): "))
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    formula = input("Fórmula utilizada: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO bebes
        (nome, idade, peso, altura, data_nascimento, formula)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        nome,
        idade,
        peso,
        altura,
        data_nascimento,
        formula
    ))

    conexao.commit()
    conexao.close()

    print("\n✅ Cadastro realizado com sucesso!")

    print(f"Nome: {nome}")
    print(f"Idade: {idade} meses")
    print(f"Peso: {peso} kg")
    print(f"Altura: {altura} cm")
    print(f"Data de nascimento: {data_nascimento}")
    print(f"Fórmula: {formula}")

    print("\n===== ANÁLISE =====")

    if idade >= 6:
        print("✔ Bebê apto para introdução alimentar.")
    else:
        print("✔ Manter aleitamento exclusivo.")

    if formula.lower() == "aptamil":
        print("✔ Fórmula Aptamil registrada.")
    else:
        print("✔ Outra fórmula registrada.")


def visualizar_bebes():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM bebes")

    bebes = cursor.fetchall()

    conexao.close()

    print("\n===== BEBÊS CADASTRADOS =====")

    if len(bebes) == 0:
        print("Nenhum bebê cadastrado.")
        return

    for bebe in bebes:

        print("\n------------------------------")
        print(f"ID: {bebe[0]}")
        print(f"Nome: {bebe[1]}")
        print(f"Idade: {bebe[2]} meses")
        print(f"Peso: {bebe[3]} kg")
        print(f"Altura: {bebe[4]} cm")
        print(f"Data de nascimento: {bebe[5]}")
        print(f"Fórmula: {bebe[6]}")


def editar_bebe():

    visualizar_bebes()

    id_bebe = input("\nDigite o ID do bebê: ")

    nome = input("Novo nome: ")
    idade = int(input("Nova idade: "))
    peso = float(input("Novo peso: "))
    altura = float(input("Nova altura: "))
    data_nascimento = input("Nova data de nascimento: ")
    formula = input("Nova fórmula: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE bebes
        SET nome = ?,
            idade = ?,
            peso = ?,
            altura = ?,
            data_nascimento = ?,
            formula = ?
        WHERE id = ?
    """, (
        nome,
        idade,
        peso,
        altura,
        data_nascimento,
        formula,
        id_bebe
    ))

    conexao.commit()
    conexao.close()

    print("\n✅ Cadastro atualizado com sucesso!")


def excluir_bebe():

    visualizar_bebes()

    id_bebe = input("\nDigite o ID do bebê que deseja excluir: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM bebes WHERE id = ?",
        (id_bebe,)
    )

    conexao.commit()
    conexao.close()

    print("\n✅ Cadastro excluído com sucesso!")