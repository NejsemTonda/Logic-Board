class Vct():
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __add__(self, other):
		if other is Vct:
			return Vct(self.x+other.x, self.y+other.y)
		else:
			raise TypeError ("Wrong type input, expect Vct, got {}".format(type(other)))
	def __mul__(self, n):
		return Vct(self.x*n, self.y*n)
	def __rmul__(self, n):
		return self*n

	def tuple(self):
		return (self.x, self.y)

	def __repr__(self):
		return (self.x, self.y)

	def __getitem__(self, key):
		return (self.x, self.y)[key]
	def __eq__(self, other):
		if self.x == other.x and self.y == other.y:
			return True
		else:
			return False
	def __hash__(self):
		return hash((self.x, self.y))
	def __mod__(self, n):
		return Vct(self.x%n, self.y%n)
	def round(self):
		return Vct(round(self.x), round(self.y))
a = Vct(1, 1)
b = Vct(1, 1)

