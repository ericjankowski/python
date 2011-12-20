text_file = open('ratchet.txt')
print(text_file.readline(), end='')

text_file.seek(0)
for line in text_file:
	print(line, end='')
text_file.close()