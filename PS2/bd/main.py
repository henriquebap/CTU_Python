from menu import Menu


def main():
    try:
        print("*" * 50)
        print("Gerenciamento de Usuários e Items!")
        print("*" * 50)
        menu = Menu()

        while True:
            menu.show_options()
            menu.handle_input()
    except KeyboardInterrupt:
        print("")
        print("Programa encerrado")

if __name__ == '__main__':
    main()