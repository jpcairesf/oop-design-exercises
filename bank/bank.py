import collections

from datetime import date


class Transaction:
    def __init__(self, account_number, amount, description, transaction_date):
        self.account_number = account_number
        self.amount = amount
        self.description = description
        self.transaction_date = transaction_date


class Account:
    def __init__(self, account_number, initial_amount):
        self.account_number = account_number
        self.balance = initial_amount

    def compute_transaction(self, transaction: Transaction):
        self.balance += transaction.amount


class Bank:
    def __init__(self):
        self.transactions = collections.defaultdict(list)
        self.accounts = {}

    def create_account(self, account_number, initial_amount):
        self._validate_new_account(account_number, initial_amount)
        account = Account(account_number, initial_amount)
        self.accounts[account_number] = account

    def deposit(self, account_number, amount, transaction_date):
        self._validate_amount(amount)
        self._process_transaction(account_number, amount, "Deposit", transaction_date)

    def withdraw(self, account_number, amount, transaction_date):
        self._validate_amount(amount)
        self._process_transaction(account_number, -amount, "Withdraw", transaction_date)

    def transfer(self, payer_account_number, payee_account_number, amount, transaction_date):
        self._validate_amount(amount)
        self._process_transaction(
            payer_account_number, -amount, f"Transfer to {payee_account_number}", transaction_date)
        self._process_transaction(
            payee_account_number, amount, f"Transfer from {payer_account_number}", transaction_date)

    def generate_report(self, account_number, report_start_date, report_end_date):
        self._validate_account(account_number)
        if report_start_date > report_end_date:
            raise ValueError("Start date cannot be later than end date")

        return [
            f"{transaction.transaction_date} - {transaction.description}: {transaction.amount}"
            for transaction in self.transactions[account_number]
            if report_start_date <= transaction.transaction_date <= report_end_date
        ]

    def _process_transaction(self, account_number, amount, description, transaction_date):
        self._validate_account(account_number)
        self._validate_date(transaction_date, account_number)

        transaction = Transaction(account_number, amount, description, transaction_date)
        account = self.accounts[account_number]
        self._validate_transaction(transaction, account)
        account.compute_transaction(transaction)
        self.transactions[account_number].append(transaction)

    def _validate_new_account(self, account_number, initial_amount):
        if account_number <= 0:
            raise ValueError("Account number must be greater than zero")
        if initial_amount < 0:
            raise ValueError("Initial amount must not be negative")
        if account_number in self.accounts:
            raise ValueError("Account number already exists")
    
    def _validate_amount(self, amount):
        if amount <= 0:
            raise ValueError("Amount should be greater than zero")

    def _validate_account(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Account not found")

    def _validate_transaction(self, transaction: Transaction, account: Account):
        if (account.balance + transaction.amount) < 0:
            raise ValueError("Balance must not be negative")

    def _validate_date(self, transaction_date, account_number):
        if transaction_date < date.today():
            raise ValueError("Invalid date")
