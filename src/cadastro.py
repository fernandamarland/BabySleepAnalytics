import csv
import os
bebes = []

def cadastrar_bebe():

    print("\n===== CADASTRO DO BEBÊ =====")

    nome = input("Nome do bebê: ")
    idade = int(input("Idade (meses): "))
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (cm): "))
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    formula = input("Fórmula utilizada: ")

    bebe = {
        "nome": nome,
        "idade": idade,
        "peso": peso,
        "altura": altura,
        "data_nascimento": data_nascimento,
        "formula": formula
    }

    bebes.append(bebe)

    salvar_csv(bebe)

    print("\nCadastro realizado com sucesso!")

    print(f"\nNome: {nome}")
    print(f"Idade: {idade} meses")
    print(f"Peso: {peso} kg")
    print(f"Altura: {altura} cm")
    print(f"Data de nascimento: {data_nascimento}")
    print(f"Fórmula: {formula}")

    print(f"\n{nome} tem {idade} meses e utiliza {formula}.")

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

    print("\n===== BEBÊS CADASTRADOS =====")

    if len(bebes) == 0:
        print("Nenhum bebê cadastrado.")
        return

    for indice, bebe in enumerate(bebes, start=1):

        print(f"\nBebê {indice}")
        print(f"Nome: {bebe['nome']}")
        print(f"Idade: {bebe['idade']} meses")
        print(f"Peso: {bebe['peso']} kg")
        print(f"Altura: {bebe['altura']} cm")
        print(f"Data de nascimento: {bebe['data_nascimento']}")
        print(f"Fórmula: {bebe['formula']}")


def salvar_csv(bebe):

    arquivo = "dados/cadastro.csv"

    arquivo_existe = os.path.isfile(arquivo)

    with open(
        arquivo,
        mode="a",
        newline="",
        encoding="utf-8"
    ) as csvfile:

        campos = [
            "nome",
            "idade",
            "peso",
            "altura",
            "data_nascimento",
            "formula"
        ]

        writer = csv.DictWriter(csvfile, fieldnames=campos)

        if not arquivo_existe:
            writer.writeheader()

        writer.writerow(bebe)