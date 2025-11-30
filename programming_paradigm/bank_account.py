class BankAccount:

    def __init__(self, account_balance, initial_balance = 0):
        self.account_balance = account_balance
        self.initial_balance = initial_balance

    
    def deposit(self,amount):
        self.account_balance += amount

    def withdraw(self,amount):
        result = self.account_balance - amount
        if result < 0:
            return False
        self.account_balance = result
        return True
        

    def display_balance(self):
        print(f"Current Balance: ${float(self.account_balance):.2f}")


