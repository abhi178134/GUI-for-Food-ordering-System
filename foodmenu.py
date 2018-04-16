class Food:

	def __init__(self, name, price, rank=0):
		self.name = name
		self.price = price
		self.rank = rank
	
	def __str__(self):
		return self.name+" "+repr(self.price)+" "+repr(self.rank)
	
class Menu:

	def __init__(self):
		self.menu =  {}
	
	def add(self,food):
		self.menu[food.name] = food
		print("Added "+food.name+" to menu")

	def remove(self,name):
		try:
			del self.menu[name]
			print("Deleted "+name+"from menu")
		except KeyError:
			print("No food with name ",name)
			return KeyError
	
	def clearAll(self):
		self.menu = {}
		print("Deleted all items in menu")
	
	def get(self,name):
		try:
			return self.menu[name]
		except KeyError:
			print("No food with name ",name)
			return KeyError
	
	def changePrice(self,name,newPrice):
		try:
			food = self.menu[name]
			print("changed price of ",name," form ",food.price," to ",newPrice)
			self.menu[name].price = newPrice

		except KeyError:
			print("No food with name ",name)
			return KeyError

	def changeName(self,name,newName):
		try:
			food = self.menu[name]
			del self.menu[name]
			print("changed name of ",name," to ",newName)
			food.name = newName
			self.add(food)

		except KeyError:
			print("No food with name ",name)
			return KeyError

	def reduceRanks(self):
		minRank = min([food.rank for food in self.menu.values()])
		for name in self.menu.keys():
			self.menu[name].rank -= minRank
		print("reduced ranks of all foods by ",minRank)
		
	def __str__(self):
		string = ""
		for key in self.menu.keys():
			food = self.menu[key]
			string = string + food.name + " "
			string = string + repr(food.price) + " "
			string = string + repr(food.rank) + "\n"
		return string
		
	def display(self):
		for food in (sorted(self.menu.values(), key=operator.attrgetter("rank"),reverse=True)):
			print(str(food))
		
