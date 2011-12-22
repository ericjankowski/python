output_file = open('output.txt', 'w')
print("No, mom. I'm writing this output to a file now.  Get off my back.", file=output_file)
output_file.close()

check = open('output.txt') 
print(check.readline())
check.close()