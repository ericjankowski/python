def reverse_list(the_list):
	the_new_list = []
	for item in the_list:
		the_new_list.insert(0, item)
	return the_new_list

list_of_saxophones = ["soprano", "alto", "tenor", "baritone"]	
print(reverse_list(list_of_saxophones))