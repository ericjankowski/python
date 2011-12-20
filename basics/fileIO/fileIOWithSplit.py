text_file = open('jazzArtists.txt')
for line in text_file:
	(artist, instrument) = line.split(',',1)
	print(artist + " played the " + instrument, end='')
	
text_file.close()