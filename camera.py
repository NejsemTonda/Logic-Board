from vectors import Vct

class Camera():
	def __init__(self, pos, scale):
		self.pos = pos
		self.scale = scale
		self.shiftstart = Vct(0, 0)
		self.shiftapplied = False

	def update(self, m2, mousepos):
		if m2:
			if not self.shiftapplied:
				self.shiftstart = mousepos
				self.shiftapplied = True
			self.pos += self.shiftstart-mousepos
			self.shiftstart = mousepos
		else:
			self.shiftapplied = False
		

	def zoom(self, dir, mousepos):

		if dir == "in":
			self.scale *=1.1

		elif dir == "out":
			self.scale *= 0.9

	def make_copy(self):
		return Camera(self.pos, self.scale)