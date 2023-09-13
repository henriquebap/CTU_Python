import utils
from menu import Menu


def main():
    try:
        print("Bem vindo! A ideia desse programa é fazer uma análise dos dados para" \
            " saber quem, de fato, é melhor: Marvel ou DC")
        file_path = input("Informe a localização do arquivo: ")
        content = utils.get_file_content(file_path)
        if not content:
            print("Arquivo não localizado") 
            return
        menu = Menu()
        menu.setup_data(content)

        while True:
            menu.show_options()
            menu.handle_input()
    except KeyboardInterrupt:
        print("")
        print("Programa encerrado")

if __name__ == '__main__':
    main()
