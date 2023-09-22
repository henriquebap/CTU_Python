from PS2.exercicioBD.library.database.crud import create_author, create_book, show_books
from functions import show_options

authors = {}
books = {}

while True:
    option = show_options()
    if option == 1:
        author = create_author()
        authors[author.id] = author
    elif option == 2:
        book = create_book(authors)
        books[book.id] = book
    elif option == 3:
        show_books(books)
    elif option == 0:
        break
    else:
        print("Opção inválida!")
