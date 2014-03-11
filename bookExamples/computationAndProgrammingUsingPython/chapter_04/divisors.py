def findDivisors (n1, n2):
    divisors = ()
    for i in range(1, min(n1, n2)+1):
        if n1%i==0 and n2%i == 0:
            divisors = divisors + (i,)
    return divisors

divisors = findDivisors(20, 100)
print divisors
total = 0
for d in divisors:
    total += d
print total