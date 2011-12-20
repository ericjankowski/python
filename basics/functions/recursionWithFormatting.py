"""Line 9 only works with python3"""

def print_complex_list(complex_list, depth):
	for item in complex_list:
		if isinstance(item, list):
			print_complex_list(item, depth+1)
		else:
			for tab in range(depth):
				print("\t", end=' ')
			print(item)
			
crazy_complex_list_of_lists = ["Jazz", ["Cannonball Adderley", ["Somethin' Else",["Autumn Leaves", "Love for Sale", "Somethin' Else"], "Cannonball and Coltrane",["Limehouse Blues", "Stars Fell on Alabama", "Wabash"]], "John Coltrane", ["Blue Train"]],"Classical", "Rock"]

print_complex_list(crazy_complex_list_of_lists,0)