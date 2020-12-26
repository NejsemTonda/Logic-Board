from vectors import Vct
import pygame
import classes

class Filehandler:
	def __init__(self):
		self.units = []
		self.buffer = []
		self.rect = [Vct(0, 0), Vct(0, 0)]

	def update(self, mousexy):
		self.units = []
		if self.rect[0] == Vct(0, 0):
			self.rect[0] = mousexy
		self.rect[1] = mousexy-self.rect[0]

		for pos in classes.Unit.units:
			if self.is_in_rect(pos):
				self.units.append(pos)
				classes.Unit.units[pos].selected = True
			else:
				classes.Unit.units[pos].selected = False

	def draw(self, screen, camera):
		if self.rect == [Vct(0, 0), Vct(0, 0)]:
			return
		else: 
			pygame.draw.rect(screen, (0, 255, 0),( (self.rect[0]*camera.scale-camera.pos).tuple(),  ((self.rect[1]+Vct(1, 1))*camera.scale).tuple()), 1)


	def save(self):
		self.buffer = []
		for pos in self.units:
			classes.Unit.units[pos].selected = False
			rel_pos = pos - self.rect[0]
			self.buffer.append([rel_pos, type(classes.Unit.units[pos]), classes.Unit.units[pos].orientation])
		self.untis = []
		self.rect = [Vct(0, 0), Vct(0, 0)]
		print(self.buffer)

	def load(file):
		pass
	def blit_copy(self, mousexy):
		for info in self.buffer:
			info[1].make_new(mousexy + info[0] , info[2])


	def is_in_rect(self, pos):
		if pos.x < self.rect[0].x or pos.x > self.rect[0].x+self.rect[1].x:
			return False
		if pos.y < self.rect[0].y or pos.y > self.rect[0].y+self.rect[1].y:
			return False
		return True