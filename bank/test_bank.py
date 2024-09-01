import unittest
from bank import Bank, Account, Transaction
from datetime import date, timedelta


class TestBank(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()

    def test_create_account(self):
        self.bank.create_account(1, 100)
        self.assertIn(1, self       .bank.accounts)

    def test_create_account_invalid_account_number(self):
        with self.assertRaises(ValueError):
            self.bank.create_account(0, 100)

    def test_create_account_invalid_initial_amount(self):
        with self.assertRaises(ValueError):
            self.bank.create_account(1, 0)

    def test_create_account_duplicate_account_number(self):
        self.bank.create_account(1, 100)
        with self.assertRaises(ValueError):
            self.bank.create_account(1, 100)

    def test_deposit(self):
        self.bank.create_account(1, 100)
        self.bank.deposit(1, 50, date.today())
        self.assertEqual(self.bank.accounts[1].balance, 150)

    def test_deposit_invalid_amount(self):
        self.bank.create_account(1, 100)
        with self.assertRaises(ValueError):
            self.bank.deposit(1, 0, date.today())

    def test_withdraw(self):
        self.bank.create_account(1, 100)
        self.bank.withdraw(1, 50, date.today())
        self.assertEqual(self.bank.accounts[1].balance, 50)

    def test_withdraw_invalid_amount(self):
        self.bank.create_account(1, 100)
        with self.assertRaises(ValueError):
            self.bank.withdraw(1, 0, date.today())

    def test_transfer(self):
        self.bank.create_account(1, 100)
        self.bank.create_account(2, 100)
        self.bank.transfer(1, 2, 50, date.today())
        self.assertEqual(self.bank.accounts[1].balance, 50)
        self.assertEqual(self.bank.accounts[2].balance, 150)

    def test_transfer_invalid_amount(self):
        self.bank.create_account(1, 100)
        self.bank.create_account(2, 100)
        with self.assertRaises(ValueError):
            self.bank.transfer(1, 2, 0, date.today())

    def test_generate_report(self):
        self.bank.create_account(1, 100)
        self.bank.deposit(1, 50, date.today())
        report = self.bank.generate_report(1, date.today() - timedelta(days=1), date.today())
        self.assertEqual(len(report), 1)

    def test_generate_report_invalid_date_range(self):
        self.bank.create_account(1, 100)
        with self.assertRaises(ValueError):
            self.bank.generate_report(1, date.today(), date.today() - timedelta(days=1))

    def test_validate_new_account(self):
        with self.assertRaises(ValueError):
            self.bank._validate_new_account(0, 100)

    def test_validate_amount(self):
        with self.assertRaises(ValueError):
            self.bank._validate_amount(0)

    def test_validate_account(self):
        with self.assertRaises(ValueError):
            self.bank._validate_account(1)

    def test_validate_transaction(self):
        account = Account(1, 100)
        transaction = Transaction(1, -150, "Withdraw", date.today())
        with self.assertRaises(ValueError):
            self.bank._validate_transaction(transaction, account)


if __name__ == '__main__':
    unittest.main()
