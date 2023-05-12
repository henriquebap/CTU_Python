from functions import show_options, show_books
from crud import create_author, create_book


authors = {}
books = {}

while True:
    Option = show_options()
    if Option == 0:
        print("Finalizando o programa")
    if Option == 1:
        author = create_author()
        authors[author.id] = author
    elif Option == 2:
        book = create_book(authors)
        books[books.id] = book
    elif Option == 3:
        show_books(books)