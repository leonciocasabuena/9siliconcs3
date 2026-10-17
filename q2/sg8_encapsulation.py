class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number 
        self.__balance = balance
        self.set_balance(balance)

    def set_account_number(self, account_number):
        self.__account_number = account_number
    
    def set_balance(self, balance):
        if balance<0:
            print("The balance must not be a negative number.")
        else:
            self.__balance = balance
    
    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance


account_1 = BankAccount(2311, 5000)

print("---Account 1---")
print(f"Account Number: {account_1.get_account_number()}")
print(f"Balance: {account_1.get_balance()}")

print(f"\nUpdate balance to -1000")
account_1.set_balance(-1000)

print(f"\nAccount Number: {account_1.get_account_number()}")
print(f"Balance: {account_1.get_balance()}")








