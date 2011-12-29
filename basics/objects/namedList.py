class NamedList(list):
	def __init__(self, name):
		list.__init__([])
		self.name = name
		

bono = NamedList("Paul Hewson")
print(type(bono))
print("\n")

print(dir(bono))
print("\n")

bono.append("Singer for U2")
bono.extend(["Guitar Player", "Harmonica Player", "Humanitarian", "Giant Turd"])

print(bono)
print("\n")

print(bono.name)
print("\n")

for attr in bono:
	print(bono.name + " is a " + attr + ".")

