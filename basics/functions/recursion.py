def print_complex_list(complex_list):
	for item in complex_list:
		if isinstance(item, list):
			print_complex_list(item)
		else:
			print(item)
			
crazy_complex_list_of_lists = ["Jazz", ["Cannonball Adderley", ["Somethin' Else",["Autumn Leaves", "Love for Sale", "Somethin' Else"], "Cannonball and Coltrane",["Limehouse Blues", "Stars Fell on Alabama", "Wabash"]], "John Coltrane", ["Blue Train"]],"Classical", "Rock"]

print_complex_list(crazy_complex_list_of_lists)