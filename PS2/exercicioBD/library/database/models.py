class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Book:
    def __init__(self, id, isbn, name, author):
        self.id = id
        self.isbn = isbn
        self.name = name
        self.author = author
