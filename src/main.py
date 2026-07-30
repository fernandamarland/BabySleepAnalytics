from banco import criar_tabelas

from cadastro import cadastrar_bebe, visualizar_bebes
from sono import registrar_sono, visualizar_sono
from mamadas import registrar_mamada, visualizar_mamadas
from alimentacao import registrar_alimentacao, visualizar_alimentacao
from vacinas import registrar_vacina, visualizar_vacinas

criar_tabelas()

criar_tabelas()


def mostrar_titulo():
    print("=" * 50)
    print("      BABY SLEEP ANALYTICS")
    print("=" * 50)


def menu():
    print("\n===== MENU =====")
    print("1 - Cadastrar bebê")
    print("2 - Visualizar bebês")
    print("3 - Registrar sono")
    print("4 - Histórico do sono")
    print("5 - Registrar mamada")
    print("6 - Histórico das mamadas")
    print("7 - Registrar alimentação")
    print("8 - Histórico da alimentação")
    print("9 - Registrar vacina")
    print("10 - Histórico das vacinas")
    print("0 - Sair")


while True:

    mostrar_titulo()

    menu()

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar_bebe()

    elif opcao == "2":
        visualizar_bebes()

    elif opcao == "3":
        registrar_sono()

    elif opcao == "4":
        visualizar_sono()

    elif opcao == "5":
        registrar_mamada()

    elif opcao == "6":
        visualizar_mamadas()

    elif opcao == "7":
        registrar_alimentacao()

    elif opcao == "8":
        visualizar_alimentacao()

    elif opcao == "9":
        registrar_vacina()

    elif opcao == "10":
        visualizar_vacinas()

    elif opcao == "0":
        print("\nObrigado por utilizar o Baby Sleep Analytics!")
        break

    else:
        print("\nOpção inválida.")