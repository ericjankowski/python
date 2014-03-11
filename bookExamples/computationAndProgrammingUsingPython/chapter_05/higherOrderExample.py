from math import *

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

L = [1, -2, 3.33]
print 'L =', L

print 'Apply abs to each element of L.' 
applyToEach(L, abs)
print 'L =', L
print 'Apply int to each element of', L
applyToEach(L, int)
print 'L =', L
print 'Apply factorial to each element of', L
applyToEach(L, factorial)
print 'L =', 

