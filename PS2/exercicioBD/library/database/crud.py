from functions import get_int
from PS2.exercicioBD.library.database.models import Author, Book


def create_author():
    author_id = get_int("Digite o ID do autor: ")
    name = input("Digite o nome do autor: ")
    author = Author(author_id, name)
    return author


def create_book(authors):
    book_id = get_int("Digite o ID do livro: ")
    isbn = get_int("Digite o ISBN do livro: ")
    name = input("Digite o nome do livro: ")
    print("Lista de autores")
    while True:
        for author_id, author in authors.items():
            print(f"{author_id} -> {author.name}")
        author_id = get_int("Digite o ID de um autor: ")
        try:
            author = authors[author_id]
            break
        except KeyError:
            print("Selecione um autor que existe")

    book = Book(book_id, isbn, name, author)
    return book


def show_book(book):
    print(f"ID: {book.id}")
    print(f"ISBN: {book.isbn}")
    print(f"Nome: {book.name}")
    print("Dados do autor")
    print(f"\tID: {book.author.id}")
    print(f"\tNome: {book.author.name}")


def show_books(books):
    for book_id, book in books.items():
        show_book(book)
