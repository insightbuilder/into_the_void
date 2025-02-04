class Book:
    def __init__(self, id, title, author, publication_year):
        self.id = id
        self.title = title
        self.author = author
        self.publication_year = publication_year

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books

    def update_book(self, id, title=None, author=None, publication_year=None):
        for book in self.books:
            if book.id == id:
                if title:
                    book.title = title
                if author:
                    book.author = author
                if publication_year:
                    book.publication_year = publication_year
                return True
        return False

    def delete_book(self, id):
        for book in self.books:
            if book.id == id:
                self.books.remove(book)
                return True
        return False


# NEW FILE