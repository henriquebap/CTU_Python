def show_options():
    print("-------" * 10)
    print("Selecione uma opcao")
    print("1 - Cadastrar Autor")
    print("2 - Cadastrar livro")
    print("3 - Ver livros cadastrados")
    print("0 - Sair")
    print("-------" * 10)

    try:    
        Option = input()
        Option = int(Option)
        return Option
    except TypeError:
        print("Digite um numero")
    except ValueError:
        print("Digite uma opcao valida")
    except:
        print("Porfavor, tente novamente")

    return Option


def get_int(mesage):
     while True:
        try:
            author_id = input(mesage)
            break
        except:
            print("Digite um numero inteiro ")