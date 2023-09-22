from database.crud import create_author, create_book, show_books
from functions import show_options

while True:
    option = show_options()
    if option == 1:
        create_author()
    elif option == 2:
        create_book()
    elif option == 3:
        show_books()
    elif option == 0:
        break
    else:
        print("Opção inválida!")
