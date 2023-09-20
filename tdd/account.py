class Account:

    def __init__(self):
        self._balance = 0

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        return self._balance


def deposit(self, amount):
    if amount > 0:
        self._balance += amount
