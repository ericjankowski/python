class Person:
	def __init__(self, name=''):
		self.name = name
		
	def get_name(self):
		return self.name
		
user = Person('George Costanza')
print('Printing name using a getter method')
print(user.get_name())
print('\n')

print('Printing using the name field directly')
print(user.name)
print('\n')

		