from database import SessionLocal
from database.models import Author, Book
from functions import get_int


def create_author():
    name = input("Digite o nome do autor: ")
    db = SessionLocal()
    try:
        author = Author()
        author.name = name
        db.add(author)
        db.commit()
    finally:
        db.close()
    
    print(f'Autor {author.id} criado com sucesso!')


def get_author(author_id):
    db = SessionLocal()
    try:
        author = db.query(Author).filter(Author.id == author_id).first()
        return author
    finally:
        db.close()

def get_authors():
    db = SessionLocal()
    try:
        authors = db.query(Author)
        return authors
    finally:
        db.close()

def get_books():
    db = SessionLocal()
    try:
        books = db.query(Book)
        return books
    finally:
        db.close()

def create_book():
    isbn = get_int("Digite o ISBN do livro: ")
    name = input("Digite o nome do livro: ")
    print("Lista de autores")
    while True:
        authors = get_authors()
        for author in authors:
            print(f"{author.id} -> {author.name}")
        author_id = get_int("Digite o ID de um autor: ")
        author = get_author(author_id)
        if not author:
            print("Autor não encontrado")
            continue
        break

    db = SessionLocal()
    try:
        book = Book()
        book.isbn = isbn
        book.name = name
        book.author = author
        db.add(book)
        db.commit()
    finally:
        db.close()
    print(f'Livro {book.id} criado com sucesso')


def show_book(book):
    print(f"ID: {book.id}")
    print(f"ISBN: {book.isbn}")
    print(f"Nome: {book.name}")
    print("Dados do autor")
    print(f"\tID: {book.author.id}")
    print(f"\tNome: {book.author.name}")


def show_books():
    books = get_books()
    for book in books:
        show_book(book)
