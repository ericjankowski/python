try:
	kathy_lee_file = open('kathy_lee.txt')
	print(kathy_lee_file.readline(), end='')
except IOError:
	print('IOError encountered')
finally:
	if 'kathy_lee_file' in locals():
		kathy_lee_file.close()
	else:
		print('Kathy Lee not in locals, so file was not closed')