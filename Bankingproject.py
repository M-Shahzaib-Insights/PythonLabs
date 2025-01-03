import os
import time

# making a data structure for accounts
accounts = {}

class Account:
    def __init__(self,account_number, name, initial_balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = initial_balance
        self.transaction_history = [] # for storing history of transactions

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")
        print(f"Deposited {amount}. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance")
            return
        self.balance -= amount
        self.transaction_history.append(f"Withdraw: {amount}")
        print(f"Withdraw: {amount}. Current Balance: {self.balance}")

    def transfer(self, target_account, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance")
            return
        self.withdraw(amount) #for transfer
        target_account.deposit(amount) #for Receiving
        self.transaction_history.append(f"Transferred: {amount} to {target_account.account_number}")
        target_account.transaction_history.append("Received: {amount} from {self.account_number}")
        print(f"Transferred {amount} to account {target_account.account_number}")

    def view_balance(self):
        print(f"Current balance for account {self.account_number}: {self.balance}")

    def view_transaction_history(self):
        if not self.transaction_history:
            print("No transactions available.")
        else:
            print(f"Transaction history for account {self.account_number}:")
            for transaction in self.transaction_history:
                print(transaction)

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_balance=0):
        account_number = str(len(self.accounts)+1).zfill(3) #generating account number
        new_account = Account(account_number, name, initial_balance)
        self.accounts[account_number] = new_account
        print(f"Account created successfully! Account number: {account_number}")
        return new_account
    def authenticate(self, account_number):
        if account_number in self.accounts:
            print(f"Account {account_number} authenticated.")
            return self.accounts[account_number]
        else:
            print("Account number not found.")
            return None
        
def main():
    bank = Bank()
    logged_in_account = None

    while True:
        if not logged_in_account:
            print("\nWelcome to the MSR Banking Corp.")
            print("\nWelcome to the Python Bank System!")
            print("1. Create a new account")
            print("2. Log in to an existing account")
            print("3. Exit")
            choice = input('PLease select an option: ')

            if choice == "1":
                name = input("Enter your name: ")
                initial_balance = float(input("Enter the initial deposit amount: "))
                logged_in_account = bank.create_account(name, initial_balance)
            
            elif choice == "2":
                account_number = input("Enter your account number: ")
                logged_in_account = bank.authenticate(account_number)

            elif choice == "3":
                print("Thank you for using MSR Banking Corp.")
                break

            else:
                print("Invalid choice. Please try again.")

        else:
            print("\nWelcome, " + logged_in_account.name)
            print("1. View balance")
            print("2. Deposit money")
            print("3. Withdraw money")
            print("4. Transfer money")
            print("5. View transaction history")
            print("6. Log out")
            choice = input("Please select an option: ")

            if choice == "1":
                logged_in_account.view_balance()

            elif choice == "2":
                amount = float(input("Enter deposit amount: "))
                logged_in_account.deposit(amount)

            elif choice == "3":
                amount = float(input("Enter withdrawal amount: "))
                logged_in_account.withdraw(amount)

            elif choice == "4":
                target_account_number = input("Enter target account number: ")
                if target_account_number in bank.accounts:
                    target_account = bank.accounts[target_account_number]
                    amount = float(input("Enter transfer amount: "))
                    logged_in_account.transfer(target_account,amount)
                else:
                    print("Target account not found.")
            
            elif choice == "5":
                logged_in_account.view_transaction_history()

            elif choice == "6":
                print("Logging out...")
                logged_in_account = None
                time.sleep(1)

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()