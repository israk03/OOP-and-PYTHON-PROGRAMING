# BankAccount class with methods for deposit, withdraw, and checking the balance.

class Bank:
    def __init__(self, name, initial_amount):
        self.name = name
        self.amount = initial_amount
        self.min_withdraw = 100
        self.max_withdraw = 10000

    def deposit(self, amount):
        if amount > 0:
            self.amount += amount
            print(f"Deposited amount {amount}tk. New balance {self.amount}tk.")
        else:
            print(f"Invalid deposite amount.")
    
    def withdraw(self, amount):
        if self.min_withdraw <= amount <= self.max_withdraw:
            self.amount -= amount
         
        else:
            print(f"Invalid withdrawal amount.")

account1 = Bank(name = "Israk", initial_amount = 1)
account1.deposit(5000)
account1.withdraw(1000)        