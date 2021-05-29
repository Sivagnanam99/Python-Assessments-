
class Siva:
	
	def __init__(self, name, age):
			
		self.Name = name
		self.Age = age

	def displayAge(self):
			
		print("Age: ", self.Age)

obj = Siva("Shiva", 22)

print("Name: ", obj.Name)

obj.displayAge()
