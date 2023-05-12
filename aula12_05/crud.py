from models import Author, Book
from functions import get_int

def create_author():
    author_id = get_int("Digite p ID do author: ")
    name = input("Digite o nome do autor: ")
    nickname = input("Digite o apelido: ")
    author = Author(name, nickname, author_id)

    return author


def create_book(authors):
    book_id = get_int('Digite o ID do livro: ')
    isbn = get_int("Digite o ISBN do livro: ")
    name = input("Digite o nome do livro: ")
    for author in authors:
        print(f'ID do author: {author}')
    author_id = input("Digite o ID de um autor: ")
    author = authors[author_id]
    book = Book(book_id, isbn, name, author)
    return book

def show_book(book):
    print(f"ID {book.id}")
    print(f"isbn {book.isbn}")
    print(f"Nome {book.name}")
    print(f"\nID {book.author.id}")
    print(f"Author {book.author.name}")
    
def show_books(books):
    for book_id, books in books.items():
        show_book(books)
        