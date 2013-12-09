x = 123456
epsilon = 0.01
step = epsilon**3
numGuesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans <= x:
	ans += step
	numGuesses += 1
print 'numGuesses =', numGuesses
if abs(ans**2 - x) >= epsilon:
	print 'Failed to find the square root of', x
else:
	print ans, 'is close to the square root of', x
