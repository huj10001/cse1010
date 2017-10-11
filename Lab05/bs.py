def buildSquares(nums):
	squares = []
	for num in nums:
		squares.append(num*num)
	return squares
s = buildSquares([1,2,3,4])
print(s)

a = [1,3,5,7,9]
b = [2,4,6,8,10]
c = [9,3,1]
d = [4,6,1,2,0]

def zip(x,y):
	count = 0
	z = []
	size = min(len(x), len(y))
	while count < size:
		z.append(x[count])
		z.append(y[count])
		count+=1
	z.extend(y[count:len(y)])
	z.extend(x[count:len(x)])		
	return z
print(zip(a,b))
print(zip(c,d))
print(zip(d,c))
