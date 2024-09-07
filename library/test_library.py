import unittest
from library import Library


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        self.library.add_book(1, 'Book', 'Author')
        self.assertIn(1, self.library.books)
        self.assertEqual(1, len(self.library.books))

    def test_add_book_duplicate_isbn(self):
        self.library.add_book(1, 'Book', 'Author')
        with self.assertRaises(ValueError):
            self.library.add_book(1, 'Book2', 'Author2')

    def test_create_member(self):
        self.library.create_member('John', 1)
        self.assertIn(1, self.library.members)
        self.assertEqual(1, len(self.library.members))

    def test_create_member_duplicate_member_id(self):
        self.library.create_member('John', 1)
        with self.assertRaises(ValueError):
            self.library.create_member('Jane', 1)

    def test_lend_book(self):
        self.library.add_book(1, 'Book', 'Author')
        self.library.create_member('John', 1)
        self.library.lend_book(1, 1)
        self.assertFalse(self.library.books[1].available)

    def test_lend_book_book_not_available(self):
        self.library.add_book(1, 'Book', 'Author')
        self.library.create_member('John', 1)
        self.library.lend_book(1, 1)
        with self.assertRaises(ValueError):
            self.library.lend_book(1, 1)

    def test_return_book(self):
        self.library.add_book(1, 'Book', 'Author')
        self.library.create_member('John', 1)
        self.library.lend_book(1, 1)
        self.library.return_book(1, 1)
        self.assertTrue(self.library.books[1].available)

    def test_return_book_book_not_borrowed(self):
        self.library.add_book(1, 'Book', 'Author')
        self.library.create_member('John', 1)
        with self.assertRaises(ValueError):
            self.library.return_book(1, 1)

    def test_check_availability(self):
        self.library.add_book(1, 'Book', 'Author')
        self.assertTrue(self.library.check_availability(1))

    def test_check_availability_book_not_found(self):
        with self.assertRaises(ValueError):
            self.library.check_availability(1)

    def test_get_borrowed_books(self):
        self.library.add_book(1, 'Book', 'Author')
        self.library.create_member('John', 1)
        self.library.lend_book(1, 1)
        self.assertEqual(self.library.get_borrowed_books(1), [1])

    def test_get_borrowed_books_member_not_found(self):
        with self.assertRaises(ValueError):
            self.library.get_borrowed_books(1)


if __name__ == '__main__':
    unittest.main()
