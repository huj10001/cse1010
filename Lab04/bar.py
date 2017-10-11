def bar(a=10,b=chr(0x2588)):
	llimit = 3
	hlimit = 20
	print('{:>5} '.format(a), end='')
	if a > hlimit:
		b = chr(0x2588)
	elif a < llimit:
		b = chr(0x2591)
	else:
		b = chr(0x2593)	
	for i in range(a):
		print(b, sep='', end='')
	print()


def graph(c):
	for j in range(len(c)):
		bar(c[j])


def seq(start, stop, step=1):
	n = int(round((stop - start)/float(step)))
	if n > 1:
		return([start + step*i for i in range(n)])
	else:
		return([])


def sinwave(mult=15, step=0.25):
	import math
	dom = seq(0, 2*math.pi, step)
	range1 = [math.sin(n) for n in dom]
	range2 = [int(mult*n) + mult for n in range1]
	return range2
