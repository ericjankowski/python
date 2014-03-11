def max(x,y):
	if x > y:
		return x
	else:
		return y

a = int(raw_input('Enter the first number: '))
b = int(raw_input('Enter the second number: '))

print 'The maximum is', max(a, b)