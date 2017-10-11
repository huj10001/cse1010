import random

def d(n):
	return random.randint(1,n)

sum = 0
count = int(input('Please enter the number of dice: '))
side = int(input('Please enter the number of sides: '))
n = 0

while n < count:
	sum += d(side)
	n += 1
print('The average is', sum/count)
