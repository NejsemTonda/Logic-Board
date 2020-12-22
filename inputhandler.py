import pygame
import classes
from vectors import Vct
import classes_models


class Handler():
	def __init__(self):
		self.mousexy = Vct(0, 0)
		self.activeunit = classes_models.Wire
		self.keys = []
		self.buttonpressed = False
		self.transistorRotation = [["upDown", "leftRight"], 0]
		self.diodeRotation = [["left", "up", "right", "down"], 0]
	def update(self, keys, m1, mousepos,camera, wheel):
		self.mousexy = round(((mousepos+camera.pos) - (mousepos+camera.pos)%camera.scale)/camera.scale)
		self.keys = keys
		self.m1 = m1
		print(self.activeunit)
		wheel.update(mousepos)
		if self.m1:
			if wheel.timer <= 10:
				if self.activeunit == classes_models.Wire:
					classes.Wire.make_new(self.mousexy)
				if self.activeunit == classes_models.Transistor:
					classes.Transistor.make_new(self.mousexy,self.transistorRotation[0][self.transistorRotation[1]])
				if self.activeunit == classes_models.Diode:
					classes.Diode.make_new(self.mousexy, self.diodeRotation[0][self.diodeRotation[1]]) 
				if self.activeunit == classes_models.BringAlive:
					if self.mousexy in classes.Unit.units:
						classes.Unit.units[self.mousexy].life = 3
						classes.Unit.living_units.append(self.mousexy)
				if self.activeunit == classes_models.Remove:
					if self.mousexy in classes.Unit.units:
						del classes.Unit.units[self.mousexy]
						if self.mousexy in classes.Unit.living_units:
							classes.Unit.living_units.remove(self.mousexy)
			else:
				self.activeunit = wheel.change_active_unit()
				if wheel.timer > 50:
					wheel.timer = 50

		if keys[pygame.K_e] and not self.buttonpressed:
			self.buttonpressed = True
			if wheel.timer == 0:
				wheel.timer = 500
			elif wheel.timer > 50:
				wheel.timer = 50

		if keys[pygame.K_r] and not self.buttonpressed:
			self.buttonpressed = True
			if self.activeunit == classes_models.Transistor:
				self.transistorRotation[1] =  (self.transistorRotation[1] + 1)%2
			if self.activeunit == classes_models.Diode:
				self.diodeRotation[1] = (self.diodeRotation[1] + 1)%4

		if not keys[pygame.K_e] and not keys[pygame.K_r]:
			self.buttonpressed = False
