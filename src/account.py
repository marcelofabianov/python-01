from datetime import datetime
from transaction import Transaction

class Account:
    def __init__(self, name, number, customer):
        self.name = name
        self.number = number
        self.customer = customer
        self.balance = 0.0
        self.transactions = []

    def deposit(self, value, description):
        self.balance += value
        self.transactions.append(Transaction(description, datetime.now(), "Deposit", value))

    def withdraw(self, value, description):
        if self.balance >= value:
            self.balance -= value
            self.transactions.append(Transaction(description, datetime.now(), "Withdraw", value))
        else:
            print("Insufficient balance")

    def transfer(self, description, destination, value):
        if self.balance >= value:
            self.balance -= value
            self.transactions.append(Transaction(description, datetime.now(), "Sent transfer", value))
            destination.balance += value
            destination.transactions.append(Transaction(description, datetime.now(), "Received transfer", value))
        else:
            print("Insufficient balance")
