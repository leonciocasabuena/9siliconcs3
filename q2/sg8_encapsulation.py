class BankAccount: #Creates a class named BankAccount 
    def __init__(self, account_number, balance): #Creates a function which iterates all of the class' private attributes which can then be inherited by objects. 
        self.__account_number = account_number 
        self.__balance = balance
        self.set_balance(balance)

    def set_account_number(self, account_number): #Creates a function which updates the account_number attribute of the class BankAccount.
        self.__account_number = account_number
    
    def set_balance(self, balance): #Creates a function which updates the balance attribute of the BankAccount class while setting a restriction which prevents the user from updating the balance into a negative value. 
        if balance<0:
            print("The balance must not be a negative number.")
        else:
            self.__balance = balance
    
    def get_account_number(self): #Creates a function which acts as a public getter and returns the details of the private attribute account_number.
        return self.__account_number

    def get_balance(self): #Creates a function which acts as a public getter and returns the details of the private attribute balance.
        return self.__balance


account_1 = BankAccount(2311, 5000) #Instantiates an object from the BankAccount class.


print("---Account 1---")
print(f"Account Number: {account_1.get_account_number()}") #Calls the function get_account_number and assigns it into the object "account_1", which displays the current account number of the instantiated object.
print(f"Balance: {account_1.get_balance()}") #also calls the function get_balance and gets the balance of the instantiated too.

print(f"\nUpdate balance to -1000")
account_1.set_balance(-1000) #sets the new balance to a new number, but then -- it's a negative number, therefore the program ignores it and prints the existing values because of the restriction of the set_balance function.

print(f"\nAccount Number: {account_1.get_account_number()}")
print(f"Balance: {account_1.get_balance()}")








