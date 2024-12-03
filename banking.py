# BANK PROGRAM:::
class BankAccount:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: Ksh{amount}")
        else:
            print("Amount must be positive")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew Ksh:{amount}")
            else:
                print("Insufficient funds")
        else:
            print("Withdraw amount must be positive")

    def check_balance(self):
        print(f"Current balance: Ksh:{self.balance}")

def main():
    name = input("Enter your name: ")
    account = BankAccount(name)
    print(f"Hello, {name}! Welcome to the bank.")

    while True:
        print("\nBANK MENU")
        print("1. DEPOSIT")
        print("2. WITHDRAW")
        print("3. CHECK BALANCE")
        print("4. EXIT")

        choice = int(input("Enter your choice(1 - 4)"))
        if choice == "1":
            amount = float(input("Enter the amount to deposit: ksh:"))
            account.deposit(amount)
        elif choice == "2":
            amount =float(input("Enter the amount to withdraw: Ksh:"))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice ")

if __name__== "__main__":
    main()