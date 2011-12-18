print("Creating a three-element list")
list_of_tempos = ["Andante", "Allegro", "Presto"]
print(list_of_tempos)
print("The length of the list is: " + `len(list_of_tempos)`)
print("\n")

print("Getting the first element of the list with index notation - [0] indexed")
print(list_of_tempos[0])
print("...Last Element...")
print(list_of_tempos[2])
print("\n")

print("Adding to the end of the list with the append() method")
list_of_tempos.append("Prestissimo")
print(list_of_tempos)
print("The length of the list is now: " + `len(list_of_tempos)`)
print("\n")

print("Removing the last element of the list with the pop() method")
popped = list_of_tempos.pop()
print("Removed: " + `popped`)
print(list_of_tempos)
print("\n")

print("Adding more than one element to a list with the extend() method")
list_of_tempos.extend(["Lento","Adagio", "Adagietto"])
print(list_of_tempos)
print("\n")

print("Removing a specific element with the remove() method")
list_of_tempos.remove("Lento")
print(list_of_tempos)
print("\n")

print("Adding an element before a specific index with the insert() method")
list_of_tempos.insert(0,"Lento")
print(list_of_tempos)
print("\n")

