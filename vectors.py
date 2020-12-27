import math
class Vct():
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __add__(self, other):
		if type(other) is Vct:
			return Vct(self.x+other.x, self.y+other.y)
		else:
			raise TypeError ("Wrong type input, expect Vct, got {}".format(type(other)))
	def __mul__(self, n):
		return Vct(self.x*n, self.y*n)
	def __rmul__(self, n):
		return self*n
	def __sub__(self, other):
		return Vct(self.x-other.x, self.y-other.y)
	def __truediv__(self, n):
		return Vct(self.x/n, self.y/n)

	def __repr__(self):
		return "({},{})".format(self.x, self.y)

	def __getitem__(self, key):
		return (self.x, self.y)[key]

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __hash__(self):
		return hash((self.x, self.y))

	def __mod__(self, n):
		return Vct(self.x%n, self.y%n)

	def __round__(self):
		return Vct(round(self.x), round(self.y))

	def tuple(self):
		return (self.x, self.y)

	def mag(self):
		return math.sqrt(self.x**2 + self.y**2)
