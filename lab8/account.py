class Account:
    def __init__(self, number, name):
        self._number = number
        self._name = name
        self._balance = 0.0

    def deposit(self, amount):
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return self._balance
        else:
            raise Exception('Insufficient funds')

    def getBalance(self):
        return self._balance

    def getName(self):
        return self._name

    def getNumber(self):
        return self._number


def test():
    print('Account.test starting')
    a1 = Account(123, 'Jeff')
    assert a1.getNumber() == 123
    assert a1.getName() == 'Jeff'
    assert a1.getBalance() == 0.0
    assert a1.deposit(100) == 100
    assert a1.getBalance() == 100
    assert a1.withdraw(25) == 75
    assert a1.getBalance() == 75
    print('Account.test finished successfully')


if __name__ == '__main__':
    test()
