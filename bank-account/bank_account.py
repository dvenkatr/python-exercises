import threading
from enum import Enum

class Status(Enum):
    CREATED = 'created'
    OPEN = 'open'
    CLOSED = 'closed'

class BankAccount:

    def __init__(self):
        self.lock = threading.Lock()
        self.status = Status.CREATED
        self.balance = 0

    def get_balance(self):
        with self.lock:
            if(self.status == Status.CLOSED):
                raise ValueError ("Account is closed")
            return self.balance

    def open(self):
        with self.lock:
            if(self.status == Status.OPEN):
                raise ValueError("Account is already open")
            self.status = Status.OPEN

    def deposit(self, amount):
        with self.lock:
            if(self.status == Status.CLOSED):
                raise ValueError("Account is closed")
            if(amount < 0):
                raise ValueError("Cannot deposit negative amount")
            self.balance += amount

    def withdraw(self, amount):
        with self.lock:
            if(self.status == Status.CLOSED): 
                raise ValueError("Account is closed")
            if(amount < 0):
                raise ValueError("Cannot withdraw negative amount")
            if(self.balance < amount):
                raise ValueError("Insufficient balance")
            self.balance -= amount

    def close(self):
        with self.lock:
            if(self.status != Status.OPEN):
                raise ValueError("Account has been created but not opened or it has already been closed")
            self.status = Status.CLOSED
            self.balance = 0
                
