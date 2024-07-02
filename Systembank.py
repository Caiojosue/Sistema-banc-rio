# Banking System Software

class BankAccount:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f} into {self.name}'s account.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from {self.name}'s account.")

    def check_balance(self):
        print(f"{self.name}'s balance: ${self.balance:.2f}")


def create_account():
    name = input("Enter account holder's name: ")
    balance = float(input("Enter initial balance: "))
    return BankAccount(name, balance)


def main():
    accounts = []

    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            account = create_account()
            accounts.append(account)
            print(f"Account created for {account.name}.")
        elif choice == "2":
            if not accounts:
                print("No accounts created.")
            else:
                account_name = input("Enter account holder's name: ")
                amount = float(input("Enter amount to deposit: "))
                for account in accounts:
                    if account.name == account_name:
                        account.deposit(amount)
                        break
                else:
                    print("Account not found.")
        elif choice == "3":
            if not accounts:
                print("No accounts created.")
            else:
                account_name = input("Enter account holder's name: ")
                amount = float(input("Enter amount to withdraw: "))
                for account in accounts:
                    if account.name == account_name:
                        account.withdraw(amount)
                        break
                else:
                    print("Account not found.")
        elif choice == "4":
            if not accounts:
                print("No accounts created.")
            else:
                account_name = input("Enter account holder's name: ")
                for account in accounts:
                    if account.name == account_name:
                        account.check_balance()
                        break
                else:
                    print("Account not found.")
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()