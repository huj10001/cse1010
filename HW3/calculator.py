#!/usr/bin/python3

accum = 0.0 
contin = True
while contin :
	print("Accumulator = ", accum)
	print("Please choose one of the following options:")
	print("1) Addition")
	print("2) Substration")
	print("3) Multiplication")
	print("4) Division")
	print("5) Square root")
	print("6) Clear")
	print("7) Exit")
	inp = input("What is your option? ")
	opt = int(inp)
	if opt == 0:
		contin = False
	elif opt == 1:
		num = float(input("Enter a number: "))
		accum += num
	else:
		print("Illegal option:", opt)

print("Accumulator = ", accum)
print("Program finished")
