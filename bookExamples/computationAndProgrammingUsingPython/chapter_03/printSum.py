sequence = raw_input('Enter a csv list of numbers: ')
numString = ''
total = 0.0
for c in sequence:
	if c != ',':
		numString = numString + c
	else:
		total = total + float(numString)
		numString = ''
total = total + float(numString)
print 'The total is:', total