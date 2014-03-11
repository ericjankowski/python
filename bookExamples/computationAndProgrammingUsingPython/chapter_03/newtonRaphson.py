epsilon = 0.01
y = int(raw_input('Enter an integer: '))
numGuesses = 0
guess = y/2.0
while abs(guess*guess - y) >= epsilon:
	numGuesses += 1
	guess = guess - (((guess**2) - y)/(2*guess))
print 'Number of Guesses:', numGuesses
print 'Square root of', y, 'is about', guess
