sequence = '1.23,2.4,3.123'
numString = ''
total = 0.0
for c in sequence:
	if c != ',':
		numString = numString + c
	else:
		total = total + float(numString)
		numString = ''
print 'The total is:', total