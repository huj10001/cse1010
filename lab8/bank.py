import checking
class Bank:
	def __init__(self):
		self._accounts = {}
		self._nextAccountNumber = 101
		
	def addAccount(self, number, acct):
		self._accounts[number] = acct

	def getAccount(self, number):
		return self._accounts[number]
	
	def createCheckingAccount(self, name):
		number = self._nextAccountNumber
		self._nextAccountNumber += 1
		ca = checking.Checking(number, name)
		self.addAccount(number, ca)
		return number
	
	def deposit(self, acctNum, amount):
		account = self.getAccount(acctNum)
		account.deposit(amount)

	def getAccountName(self, acctNum):
		account = self.getAccount(acctNum)
		accountName = account.getName()
		return accountName

	def getAccountBalance(self, acctNum):
		account = self.getAccount(acctNum)
		accountBalance = account.getBalance()
		return accountBalance

	def withdraw(self, acctNum, amount):
		account = self.getAccount(acctNum)
		account.withdraw(amount)				
	def depositCheck(self, acctNum, chk):
		destAccount = self.getAccount(acctNum)
		srcAccountNum = chk.getAccountNumber()
		srcAccount = self.getAccount(srcAccountNum)
		depositAmount = chk.getAmount()
		srcAccount.withdraw(depositAmount)
		destAccount.deposit(depositAmount)		

def test():
	import check
	b1 = Bank()
	ca1num = b1.createCheckingAccount('Alice')
	ca2num = b1.createCheckingAccount('Bob')
	b1.deposit(ca1num, 1000)
	check1 = check.Check(ca1num, 'Bob', 100)
	b1.depositCheck(ca2num, check1)
	print(b1.getAccountName(ca1num), 'balance is', b1.getAccountBalance(ca1num))
	print(b1.getAccountName(ca2num), 'balance is', b1.getAccountBalance(ca2num))

if __name__ == '__main__':
	test()
