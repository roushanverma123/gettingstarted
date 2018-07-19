class fighter:
	def __init__(self,name):
		self.name = name
		self.health = 100
		self.damage = 10


	def attack(self,other_guy):
		other_guy.health = other_guy.health - self.damage

rv = fighter("rv")
you = fighter("you")

print(rv.name)
print(you.name)

you.attack(rv)

print(rv.health)
		