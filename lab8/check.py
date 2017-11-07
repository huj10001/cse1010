import checking
class Check:
	def __init__(self, acctNum, to, amount):
		self._from = acctNum 
		self._to = to
		self._amount = amount

	def getAccountNumber(self):
		return self._from	

	def getAmount(self):
		return self._amount

def test():
	ca1 = checking.Checking(123, 'Alice')
	ca1.deposit(1000)
	c1 = Check(ca1, 'Bob', 100)
	print(c1._checkingAccount)
	print(c1._from)
	print(c1._to)
	print(c1._amount)
	
if __name__ == '__main__':
	test()		
