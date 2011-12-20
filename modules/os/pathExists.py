import os

if os.path.exists('no-exist.txt'):
	should_this_be_here = open('no-exist.txt')
	
	should_this_be_here.close()
	
if os.path.exists('exists.txt'):
	should_this_be_here = open('exists.txt')
	for line in should_this_be_here:
		print(line)
	should_this_be_here.close()