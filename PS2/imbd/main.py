from database import crud
from functions import show_options

while True:
    option = show_options()
    if option == 1:
        crud.create_cliente()
    elif option == 2:
        crud.create_vendedor()
    elif option == 3:
        crud.get_cliente
    elif option == 4:
        crud.get_vendedor()
    elif option == 5:
        crud.coloca_salario_comissao()
    elif option == 0:
        break
    else:
        print("Opção inválida!")
