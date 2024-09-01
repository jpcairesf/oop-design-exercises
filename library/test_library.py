import unittest

from library import Library


class Tests(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_register_book(self):
        self.library.add_book(0, "John's Adventures", "Johnny")
        self.assertIn(0, self.library.books)
        self.library.add_book(1, "Jane's Chronicles", "Janette")
        self.assertIn(1, self.library.books)

    def test_register_member(self):
        self.library.create_member("John", 0)
        self.assertIn(0, self.library.members)
        self.library.create_member("Jane", 1)
        self.assertIn(1, self.library.members)

    def test_check_availability(self):
        self.library.create_member("John", 0)
        self.library.add_book(0, "John's Adventures", "Johnny")
        self.assertTrue(self.library.check_availability(0))
        self.library.lend_book(0, 0)
        self.assertFalse(self.library.check_availability(0))

    def test_lend_a_book(self):
        self.library.create_member("John", 0)
        self.library.add_book(0, "John's Adventures", "Johnny")
        self.library.lend_book(0, 0)
        self.assertIn(0, [book.isbn for book in self.library.borrowed[0]])

    def test_return_a_book(self):
        self.library.create_member("John", 0)
        self.library.add_book(0, "John's Adventures", "Johnny")
        self.library.lend_book(0, 0)
        self.library.return_book(0, 0)
        self.assertNotIn(0, [book.isbn for book in self.library.borrowed[0]])

    def test_get_borrowed_books(self):
        self.library.create_member("John", 0)
        self.library.add_book(0, "John's Adventures", "Johnny")
        self.library.add_book(1, "Jane's Chronicles", "Janette")
        self.library.lend_book(0, 0)
        self.library.lend_book(0, 1)
        self.assertAlmostEqual(2, len(self.library.get_borrowed_books(0)))
