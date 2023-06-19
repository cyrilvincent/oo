import datetime
from dataclasses import dataclass
from typing import List


@dataclass
class Transaction:

    date : datetime.datetime
    amount: float

class User:

    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name


class BankAccount:

    def __init__(self, id: str):
        self.id = id
        self._balance = 0
        self.transactions: List[Transaction] = []

    def credit(self, amount: float):
        self._balance += amount

    def debit(self, amount: float):
        self._balance -= amount


cyril = User("Vincent", "Cyril")
print(cyril)
print(cyril.last_name)
account = BankAccount("001")
account._balance += 100000

print(account.balance)
account.credit(100)
print(account.balance)
account.debit(30)
print(account.balance)
