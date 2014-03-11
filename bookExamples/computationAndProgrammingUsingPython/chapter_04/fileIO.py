nameHandle = open('kids.txt', 'w')
for i in range(2):
    name = raw_input('Enter name: ')
    nameHandle.write(name + '\n')
nameHandle.close()

nameHandle = open('kids.txt', 'r')
for line in nameHandle:
    print line
nameHandle.close()