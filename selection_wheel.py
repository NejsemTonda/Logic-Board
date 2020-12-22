import pygame
import classes_models as models
import camera
from vectors import Vct
import math 



def polar_to_cartestian(r, angle):
	x = r * math.cos(angle)
	y = r * math.sin(angle)
	return Vct(x,y)

class Wheel:
	def __init__(self,screen):
		self.r = 0
		self.timer = 0
		self.size = Vct(500,500)
		self.surface = pygame.Surface((self.size).tuple(), pygame.SRCALPHA)
		self.models = [models.Wire, models.Transistor, models.Diode, models.Remove, models.BringAlive]
		#self.models = [models.Wire,models.Wire,models.Wire,models.Wire,models.Wire,models.Wire,models.Wire,models.Wire,models.Wire]
		self.spacing = 2*math.pi/ len(self.models)
		self.camera = camera.Camera()
		self.screensize = Vct(screen.get_size()[0], screen.get_size()[1])
		self.closestToMouse = [models.Wire, float("inf")]

	def draw(self,screen):
		self.surface.fill((255, 255, 255, 0))
		if self.timer == 0:
			return
		
		pygame.draw.circle(self.surface, (255, 255, 255, 50), (self.size/2).tuple(), self.r//2, self.r//4)
		for i, m in enumerate(self.models):
			if m == self.closestToMouse[0]:
				selected = True
			else:
				selected = False
			m.draw(polar_to_cartestian(3*self.r/(8*self.camera.scale), self.spacing*i + math.pi/2)+self.size/42, self.surface, self.camera, selected = selected)

		screen.blit(self.surface, ((self.screensize-self.size)/2).tuple())


	def update(self, mousepos):
		

		if self.timer > 450:
			self.r = (500-self.timer)*10
		elif self.timer < 50:
			self.r = self.timer*10
		else:
			self.r = 500

		if self.timer != 0:
			self.timer -=1
		if self.timer > 100:
			self.closestToMouse = [models.Wire, float("inf")]
			for i, m in enumerate(self.models):
				d = (polar_to_cartestian(3*self.r/(8), self.spacing*i + math.pi/2)-mousepos+self.screensize/2).mag()
				if self.closestToMouse[1] > d:
					self.closestToMouse = [m , d]

		
	def change_active_unit(self):
		return self.closestToMouse[0]