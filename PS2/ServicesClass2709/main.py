from services import google
from models import Book

query = input("Digite o termo a ser buscado: ")
result = google.get_books(query)
books = [Book(data) for data in result.get("items")]

for book in books:
    print(f"Titulo: {book.title}")
    print(f"Descricao: {book.description}")
    print(f"Paginas: {book.pageCount}")



books = []

for data in result.get("items"):
    book = Book(data)
    books.append(book)