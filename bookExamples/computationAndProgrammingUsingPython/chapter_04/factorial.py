def factorialIterative(n):
    """Assumes that n is an int > 0
       returns n!"""

    res = 1
    while n > 1:
        res = res * n
        n -= 1
    return res

def factorialRecursive(n):
    """Assumes that n is an int > 0
       returns n!"""

    if n==1:
        return n
    return n*factorialRecursive(n-1)

x = int(raw_input("Enter an integer greater than zero:  "))
print 'Factorial of ' + str(x) + ' is: ' + str(factorialIterative(x))
#print 'Factorial of ' + str(x) + ' is: ' + str(factorialRecursive(x))