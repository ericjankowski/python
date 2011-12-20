data_file = open('bad.txt')

for line in data_file:
	try:
		(key, value) = line.split(':')
	except:
		key="failure"
		value="unintelligible"
	print(key + " -:- " + value)
	
data_file.close()