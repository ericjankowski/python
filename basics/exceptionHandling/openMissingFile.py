try:
	kathy_lee_file = open('kathy_lee.txt')
	print(kathy_lee_file.readline(), end='')
except IOError as error:
	print('IOError encountered: ' + str(error))
		
"""Rewritten to use the With statement"""

try:
	with open('kathy_lee.txt') as kathy_lee_file:
		print(kathy_lee_file.readline(), end='')
except IOError as error:
	print('IOError encountered: ' + str(error))
