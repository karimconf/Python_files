class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]

    def list_books(self):
        return [(book.title, book.author) for book in self.books]

    def search_books_by_author(self, author):
        return [(book.title, book.author) for book in self.books if book.author == author]

    def generate_statistics(self):
        total_books = len(self.books)
        unique_authors = set(book.author for book in self.books)
        return {
            'total_books': total_books,
            'unique_authors': unique_authors,
        }