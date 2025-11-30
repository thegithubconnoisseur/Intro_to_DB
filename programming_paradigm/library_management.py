class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        return not self._is_checked_out

        




class Library:

    def __init__(self):
        self._book = []

    
    def add_book(self,book):
        self._book.append(book)

    def check_out_book(self, title):
        for book in self._book:
            if book.title == title:
                book.check_out()

    def return_book(self, title):
        for book in self._book:
            if book.title == title:
                book.return_book()
        


    def list_available_books(self):
        for values in self._book:
            if values.is_available():
                print(f"{values.title} by {values.author}")
