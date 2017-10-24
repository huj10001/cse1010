accounts = {}
def create_acct(number, name, balance):
	global accounts
	if not accounts.get(number):
		acct = {'num':number, 'name':name, 'bal':balance}
		accounts[number] = acct
		result = ('success', acct)
	else:
		result = ('error', 'account exists', number)
	return result

def find_acct(number):
	global accounts
	if accounts.get(number):
		result = ('account', accounts.get(number))
	else:
		result = ('error', 'no such account', number)
	return result

def get_balance(number):
	global accounts
	findRes = find_acct(number)
	if findRes[0] == 'account':
		result = ('balance', number, accounts.get(number).get('bal'))
	else:
		result = ('error', 'no such account', number)
	return result

def deposit(number, amount):
	global accounts
	findRes = find_acct(number)
	if findRes[0] == 'account':
		accounts.get(number)['bal'] += amount
		result = ('deposit', number, amount, accounts.get(number).get('bal'))
	else:
		result = ('error', 'no such account', number)
	return result;

def withdraw(number, amount):
	global accounts
	findRes = find_acct(number)
	if findRes[0] == 'account':
		accounts.get(number)['bal'] -= amount
		result = ('withdraw', number, amount, accounts.get(number).get('bal'))
	else:
		result = ('error', 'no such account', number)
	return result;
	


def main():
	global accounts

	print('creating accounts:')
	print(create_acct(123, 'Jeff', 10))
	print(create_acct(987, 'Donald T.', 1000000))

	print('\nthe account dictionary is:')
	print(accounts)

	print('\ntesting find_account:')
	print(find_acct(123))
	print(find_acct(987))
	print(find_acct(555))
	
	print('\ntesting get_balance:')
	print(get_balance(123))
	print(get_balance(987))
	print(get_balance(555))
	print(get_balance(987))
	
	print('\ntesting deposit:')
	print(deposit(123, 100))
	print(deposit(987, 50))
	print(deposit(555, 10))

	print('\ntesting withdraw:')
	print(withdraw(123, 100))
	print(withdraw(987, 50))
	print(withdraw(555, 10))


if __name__ == '__main__':
	main()


