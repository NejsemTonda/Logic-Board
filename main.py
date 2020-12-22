import pygame
import classes
from vectors import Vct
import inputhandler
import camera
import selection_wheel

class Game():
	def __init__(self):
		self.end = False
		self.screen = pygame.display.set_mode((1400, 800))#,pygame.FULLSCREEN
		self.clock = pygame.time.Clock()
		self.tick = 0
		self.key = []
		self.mousepos = Vct(0, 0)
		self.m1 = False
		self.m2 = False 
		self.inputhandler = inputhandler.Handler()
		self.camera = camera.Camera()
		self.sWheel = selection_wheel.Wheel(self.screen)
	
	def update(self):
		self.tick = (self.tick+1)%8
		if self.tick == 0:
			classes.Unit.make_new_itteration()
		self.draw()
		self.inputhandler.update(self.keys, self.m1, self.mousepos, self.camera, self.sWheel)
		self.camera.update(self.m2, self.mousepos)
		

	def draw(self):
		self.screen.fill((0, 0, 20))
		for u in classes.Unit.units.values():
			u.draw(self.screen, self.camera)
		self.sWheel.draw(self.screen)
		pygame.display.update()
		
	def run(self):
		while not self.end:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.end = True
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 4:
						self.camera.zoom("in", self.mousepos)
					if event.button == 5:
						self.camera.zoom("out", self.mousepos)


			self.keys = pygame.key.get_pressed()
			if self.keys[pygame.K_ESCAPE]:
				self.end = True
			self.mousepos = Vct(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
			self.m1 = pygame.mouse.get_pressed()[0]
			self.m2 = pygame.mouse.get_pressed()[2]
			self.update()
			#print(classes.Unit.living_units)
			self.clock.tick(120)
			#print(self.clock.get_fps())
if __name__ == "__main__":
	game = Game()
	print(game)
	game.run()
