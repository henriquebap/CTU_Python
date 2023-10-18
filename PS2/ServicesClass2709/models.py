class Book:
    def __init__(self, data):
        data = data.get("volumeInfo")
        self.title = data.get("title")
        self.pageCount = data.get("pageCount")
        self.description = data.get("description")
