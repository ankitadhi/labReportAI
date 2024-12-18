
class BankAccount:

    def __init__(self, account_number,  initial_balance = 0):
        self.account = account_number
        self.initial_balance = initial_balance
    
    def deposit(self, amount):
        self.initial_balance += amount
    
    def withdraw(self, amount):
        if self.initial_balance >= amount:
            self.initial_balance -= amount
        else:
            print("Insufficient funds")


    def get_balance(self):
        return self.initial_balance
    


namme = BankAccount(1212134, 0)

namme.deposit(500)
amount = namme.get_balance()


print(amount)