import math
radius = input('Enter radius: ')
try:
	area = math.pi * (int(radius)**2)
except ValueError:
	area = math.pi * (float(radius)**2)
print('The area of a circle with radius', radius, 'is', area)
