from array import *
integers = array('i', [0,0,0,0,0,0,0,0,0,0])
integers[0] = int(raw_input('Enter the first integer: '))

for i in xrange(1,10):
	integers[i] = int(raw_input('Enter the next integer: '))

max_odd = 0
for num in integers:
	if num % 2 == 1 and num > max_odd:
		max_odd = num

if max_odd == 0:
	print 'No odd numbers were entered'
else:
	print 'The maximum odd number entered is: '+str(max_odd)


