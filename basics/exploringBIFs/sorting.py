data_out_of_order = [4,7,1,3,8,9,2,10,4567,1234]

print("Original list: ", end='')
print(data_out_of_order)
print("\n")

print("Sorting in place using sort()")
data_out_of_order.sort()
print(data_out_of_order)
print("\n")

print("Sorting in a copy using sorted()")
data_out_of_order = [4,7,1,3,8,9,2,10,4567,1234]
data_in_order = sorted(data_out_of_order)
print(data_out_of_order)
print(data_in_order)

print("Reverse that mother")
data_in_order = sorted(data_out_of_order, reverse=True)
print(data_out_of_order)
print(data_in_order)

