import collections
from datetime import date


class Transaction:
    def __init__(self, account_number, amount, description, transaction_date):
        if transaction_date < date.today():
            raise ValueError("Invalid date")
        self.account_number = account_number
        self.amount = amount
        self.description = description
        self.transaction_date = transaction_date


class Account:
    def __init__(self, account_number, initial_amount):
        if account_number <= 0:
            raise ValueError("Account number must be greater than zero")
        if initial_amount < 0:
            raise ValueError("Initial amount must not be negative")
        self.account_number = account_number
        self.balance = initial_amount

    def compute_transaction(self, transaction: Transaction):
        self.balance += transaction.amount


class Bank:
    def __init__(self):
        self.transactions = collections.defaultdict(list)
        self.accounts = {}

    def create_account(self, account_number, initial_amount):
        if account_number in self.accounts:
            raise ValueError("Account number already exists")
        self.accounts[account_number] = Account(account_number, initial_amount)

    def deposit(self, account_number, amount, transaction_date):
        if amount <= 0:
            raise ValueError("Amount should be greater than zero")
        self._process_transaction(account_number, amount, "Deposit", transaction_date)

    def withdraw(self, account_number, amount, transaction_date):
        if amount <= 0:
            raise ValueError("Amount should be greater than zero")
        self._process_transaction(account_number, -amount, "Withdraw", transaction_date)

    def transfer(self, payer_account_number, payee_account_number, amount, transaction_date):
        if amount <= 0:
            raise ValueError("Amount should be greater than zero")
        self._process_transaction(
            payer_account_number, -amount, f"Transfer to {payee_account_number}", transaction_date)
        self._process_transaction(
            payee_account_number, amount, f"Transfer from {payer_account_number}", transaction_date)

    def generate_report(self, account_number, report_start_date, report_end_date):
        if account_number not in self.accounts:
            raise ValueError("Account not found")
        if report_start_date > report_end_date:
            raise ValueError("Start date cannot be later than end date")

        return [
            f"{transaction.transaction_date} - {transaction.description}: {transaction.amount}"
            for transaction in self.transactions[account_number]
            if report_start_date <= transaction.transaction_date <= report_end_date
        ]

    def _process_transaction(self, account_number, amount, description, transaction_date):
        if account_number not in self.accounts:
            raise ValueError("Account not found")
        transaction = Transaction(account_number, amount, description, transaction_date)
        account = self.accounts[account_number]
        if (account.balance + transaction.amount) < 0:
            raise ValueError("Balance must not be negative")
        account.compute_transaction(transaction)
        self.transactions[account_number].append(transaction)
