import pygame
import logic_board_classes as classes
from logic_board_vectors import Vct
from logic_board_camera import Camera


class Handler():
	def __init__(self):
		self.mousexy = Vct(0, 0)
		self.activeunit = "wire"
		self.keys = []
	def update(self, keys, m1, mousepos):
		self.mousexy = (((mousepos-Camera.pos) - ((mousepos-Camera.pos)%Camera.scale))*(1/Camera.scale)).round()
		self.keys = keys
		self.m1 = m1
		if self.m1:
			if self.activeunit == "wire":
				classes.Unit.units[self.mousexy] = classes.Wire(self.mousexy)
				classes.Unit.units[self.mousexy].updateneighbors()
				for n in classes.Unit.units[self.mousexy].neighbors.values():
					n.updateneighbors()
			elif self.activeunit == "bringalive":
				if self.mousexy in classes.Unit.units:
					classes.Unit.units[self.mousexy].life = 4
					classes.Unit.living_units.append(classes.Unit.units[self.mousexy].pos)
			elif self.activeunit == "transistor":
				classes.Unit.units[self.mousexy] = classes.Transistor(self.mousexy, "Transistorupdown")
				classes.Unit.units[self.mousexy].updateneighbors()
				for n in classes.Unit.units[self.mousexy].neighbors.values():
					n.updateneighbors()

		if keys[pygame.K_e]:
			self.activeunit = "bringalive"
		if keys[pygame.K_w]:
			self.activeunit = "wire"
		if keys[pygame.K_t]:
			self.activeunit = "transistor"
