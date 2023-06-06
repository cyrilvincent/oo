class User:

    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    def walk(self):
        print("I walk")

class Account:

    def __init__(self, id: str):
        self.id = id
        self._balance = 0

    def credit(self, amount: float):
        if amount >= 0:
            self._balance += amount
        else:
            raise ValueError(f"Amount must be >= 0 {amount}")

    def debit(self, amount: float):
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError('toto')

if __name__ == '__main__':
    cyril = User("Vincent", "Cyril")
    print(cyril)
    cyril.walk()
    print(cyril.first_name)
    a1 = Account("1")
    print(a1._balance)
    a1.credit(100)
    print(a1)
    # a1.debit(200)
    # print(a1)
    a1._balance += 1000000000
