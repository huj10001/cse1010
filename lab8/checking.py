import check
class Checking:
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

	def writeCheck(self, to, amount):
		sourceAccount = self
		chk = check.Check(self, to, amount)
		return chk

	def depositCheck(self, check):
		source = check.getSourceAccount()
		amount = check.getAmount()
		try:
			bal = source.withdraw(amount)
			self.deposit(amount)
		except:
			print('Insufficient funds from source account')

def test():
	ca1 = Checking(100, 'Alice')
	ca1.deposit(1000)
	ca2 = Checking(101, 'Bob')
	c1 = check.Check(ca1, ca2, 100)
	ca2.depositCheck(c1)
	print('Alice balance is', ca1.getBalance())
	print('Bob balance is', ca2.getBalance())

if __name__ == '__main__':
	test()	
