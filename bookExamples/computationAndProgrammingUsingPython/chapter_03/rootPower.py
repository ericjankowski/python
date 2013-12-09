target = int(raw_input('Enter an integer: '))
for power in xrange(1, 20):
	temp = 0
	root = 0
	while temp < target:
		root = root + 1
		temp = root**power
	if temp == target:
		print target, '=', root, '^', power