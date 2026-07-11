from cadastro import cadastrar_bebe, visualizar_bebes


def mostrar_titulo():
    print("=" * 45)
    print("         BABY SLEEP ANALYTICS")
    print("=" * 45)


def menu():
    print("\nMENU")
    print("1 - Cadastrar bebê")
    print("2 - Visualizar bebês cadastrados")
    print("3 - Registrar mamada")
    print("4 - Registrar sono")
    print("5 - Registrar alimentação")
    print("6 - Registrar vacina")
    print("0 - Sair")


mostrar_titulo()

while True:

    menu()

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar_bebe()

    elif opcao == "2":
        visualizar_bebes()

    elif opcao == "3":
        print("\n🚧 Em desenvolvimento.")

    elif opcao == "4":
        print("\n🚧 Em desenvolvimento.")

    elif opcao == "5":
        print("\n🚧 Em desenvolvimento.")

    elif opcao == "6":
        print("\n🚧 Em desenvolvimento.")

    elif opcao == "0":
        print("\nObrigado por utilizar o Baby Sleep Analytics!")
        break

    else:
        print("\nOpção inválida.")