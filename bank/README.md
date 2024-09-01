## Bank Exercise

A bank is responsible for managing customer accounts, allowing customers to perform deposits, withdrawals, and transfers. The bank must also keep a record of all transactions and generate reports summarizing the activities of each account.

### Features

The bank should be able to perform the following operations:

1. **Create Account**: Register a new account with an account number, initial balance, and creation date.
2. **Deposit**: Deposit money into an account, increasing the account balance.
3. **Withdraw**: Withdraw money from an account, decreasing the account balance. Ensure that the withdrawal amount does not exceed the available balance.
4. **Transfer**: Transfer money between two accounts by withdrawing from the source account and depositing into the target account.
5. **Generate Report**: Generate a report for a specific account, showing all transactions (deposits, withdrawals, and transfers) within a given date range.

### Conditions

#### Account:
- Each account must have a unique account number.
- The account number is not a string, and it must be greater than zero.
- The account balance should be updated with every transaction.

#### Transactions:
- Transactions must occur on or before the current day and must not predate the account creation date.
- Deposits and withdrawals should affect the account balance accordingly.
- Withdrawals must not exceed the available balance.
- Transfers involve both a withdrawal from the source account and a deposit into the target account.
- Each transaction must have its type (deposit, withdrawal, or transfer) in the description. For transfers, the description must include the target or source account details.

#### Report Generation:
- The report should list all transactions for a specific account, showing the transaction description, amount, and date.
- For transfers, the report should only show the transaction that directly affects the account's balance.
