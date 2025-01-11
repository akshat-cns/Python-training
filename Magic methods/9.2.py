class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.title < other.title

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return (self.title, self.author, self.year) == (other.title, other.author, other.year)

def sort_by_author(books):
    return sorted(books, key=lambda book: book.author)

def sort_by_year(books):
    return sorted(books, key=lambda book: book.year)