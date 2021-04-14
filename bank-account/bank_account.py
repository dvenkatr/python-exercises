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
            if(self.status != Status.CLOSED):
                return self.balance
            else:
                raise ValueError("Account is closed")

    def open(self):
        with self.lock:
            if(self.status == Status.OPEN):
                raise ValueError("Account is already open")
            else:
                self.status = Status.OPEN

    def deposit(self, amount):
        with self.lock:
            if(self.status != Status.CLOSED):
                if(amount > 0):
                    self.balance += amount
                else:
                    raise ValueError("Cannot deposit negative amount")
            else:
                raise ValueError("Account is closed")

    def withdraw(self, amount):
        with self.lock:
            if(self.status != Status.CLOSED):
                if(amount > 0):
                    if(self.balance >= amount):
                        self.balance -= amount
                    else:
                        raise ValueError("Insufficient balance")
                else:
                    raise ValueError("Cannot withdraw negative amount")
            else:
                raise ValueError("Account is closed")

    def close(self):
        with self.lock:
            if(self.status == Status.OPEN):
                self.status = Status.CLOSED
                self.balance = 0
            else:
                raise ValueError("Account is already closed")
