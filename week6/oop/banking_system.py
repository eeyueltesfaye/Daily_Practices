class Account:
    def __init__(self, account_number, account_type, balance=0):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")

    def get_balance(self):
        return self.balance

class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def open_account(self, account_number, account_type, initial_deposit=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = Account(account_number, account_type, initial_deposit)
            print(f"Account {account_number} opened with initial deposit of ${initial_deposit:.2f}.")
        else:
            print("Account number already exists.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = {}

    def add_customer(self, customer):
        if customer.name not in self.customers:
            self.customers[customer.name] = customer
            print(f"Customer {customer.name} added to the bank.")
        else:
            print("Customer already exists.")

    def get_customer(self, customer_name):
        return self.customers.get(customer_name, None)

# Example usage:
# Creating a bank
bank = Bank("Abyssinia Bank")

# Creating customers
alem = Customer("Alem")
beza = Customer("Beza")

# Adding customers to the bank
bank.add_customer(alem)
bank.add_customer(beza)

# Opening accounts for Alem
alem.open_account("123", "Savings", 1000)
alem.open_account("124", "Checking", 500)

# Opening accounts for Beza
beza.open_account("125", "Savings", 1500)

# Alem makes transactions
alem_account = alem.get_account("123")
alem_account.deposit(200)
alem_account.withdraw(100)

# Beza makes transactions
beza_account = beza.get_account("125")
beza_account.deposit(300)
beza_account.withdraw(200)

# Checking balances
print(f"Alem's savings account balance: ${alem_account.get_balance():.2f}")
print(f"Beza's savings account balance: ${beza_account.get_balance():.2f}")
