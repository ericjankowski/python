import datetime
from Person import Person
from MITPerson import MITPerson

me = Person('Michael Guttag')
him = Person('Barack Hussein Obama')
her = Person('Madonna')
print him.getLastName()
him.setBirthday(datetime.date(1961, 8, 4))
her.setBirthday(datetime.date(1958, 8, 16))

pList = [me, him, her]
for p in pList:
    print p
pList.sort()
for p in pList:
    print p


p1 = MITPerson('Barbara Beaver')
print str(p1) + '\'s id number is ' + str(p1.getIdNum())

p1 = MITPerson('Mark Guttag')
p2 = MITPerson('Billy Bob Beaver')
p3 = MITPerson('Billy Bob Beaver')
p4 = Person('Billy Bob Beaver')

print 'p1 < p2 =', p1 < p2
print 'p3 < p2 =', p3 < p2
print 'p4 < p1 =', p4 < p1
