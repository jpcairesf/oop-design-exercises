import collections


class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.available = True


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id


class Library:
    def __init__(self):
        self.borrowed = collections.defaultdict(list)
        self.members = {}
        self.books = {}

    def add_book(self, isbn, title, author):
        if isbn in self.books:
            raise ValueError("ISBN already exists")
        self.books[isbn] = Book(isbn, title, author)

    def create_member(self, name, member_id):
        if member_id in self.members:
            raise ValueError("Member ID already exists")
        self.members[member_id] = Member(name, member_id)

    def lend_book(self, member_id, isbn):
        self._validate_member(member_id)
        book = self._find_book_by_isbn(isbn)
        if not book.available:
            raise ValueError("Book not available")
        book.available = False
        self.borrowed[member_id].append(book)

    def return_book(self, member_id, isbn):
        self._validate_member(member_id)
        book = self._find_book_by_isbn(isbn)
        if book not in self.borrowed[member_id]:
            raise ValueError("The member did not borrow this book")
        book.available = True
        self.borrowed[member_id].remove(book)

    def check_availability(self, isbn):
        if isbn in self.books:
            return self.books[isbn].available
        raise ValueError("Book not found")

    def get_borrowed_books(self, member_id):
        self._validate_member(member_id)
        return [book.isbn for book in self.borrowed[member_id]]

    def _validate_member(self, member_id):
        if member_id not in self.members:
            raise ValueError("Member not found")

    def _find_book_by_isbn(self, isbn):
        if isbn in self.books:
            return self.books[isbn]
        raise ValueError("Book not found")
