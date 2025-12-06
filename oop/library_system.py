class Book:
    
    def __init__(self, title:str, author:str):
        self.title = title 
        self.author = author

class EBook(Book):
    
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

class Library:


    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for values in self.books:
            print(f"{values.__class__.__name__}: {values.title} by {values.author}", end = "")

            if isinstance(values, EBook):
                print(f", File Size: {values.file_size}KB")

            if isinstance(values, PrintBook):
                print(f", Page Count: {values.page_count}")

            else:
                print("\n")