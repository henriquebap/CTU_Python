
def show_options():
    print("Selecione uma das opções")
    print("1 - Cadastrar Cliente")
    print("2 - Cadastrar Vendedor")
    print("3 - Ver Clientes")
    print("4 - Ver Vendedores")
    print("5 - Adicionar Salario")
    print("0 - Sair")

    try:
        option = int(input())
        return option
    except ValueError:
        print("Digite um opção válida")

def get_int(message):
    while True:
        try:
            value = input(message)
            value = int(value)
            return value
        except ValueError:
            print("Digite um número inteiro")
