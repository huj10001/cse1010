field1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
field2 = [[1,2,3],[4,5,6,7],[8,9,10,11,12]]

def showField(field):
	for row in field:
		print('row =', row)
		for col in row:
			print('square =', col)

showField(field2)

def squareit(x):
	print('x is', x)
	y = x * x
	print('the square of', x, 'is', y)
	return y

squareit(9)

def squareit1(x):
	print('x is', x)
	y = x * x
	print('the square of', x, 'is', y)

y = squareit1(9)
print(y)

def squareit2(x):
	y = x * x
	print(y)
	return y
z = squareit2(9)
print(z)
