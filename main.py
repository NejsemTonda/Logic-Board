#######################################################################################################################
# Václa Krňák                                                                                                         #
# Zápočtový program: Logic Board                                                                                      #
# programování NPRG030-062                                                                                            #
# Popis:                                                                                                              #
# Celulární automat sloužící k simulaci logiky na elektrických obvodech                                               #
#######################################################################################################################



import pygame
import classes
from vectors import Vct
import inputhandler
import camera
import selection_wheel
import preview
import filehandler 

class Game():
	def __init__(self):
		self.end = False
		self.screen = pygame.display.set_mode((1800, 1000))
		self.clock = pygame.time.Clock()
		self.tick = 0
		self.tickrate = 8
		self.keys = []
		self.mousepos = Vct(0, 0)
		self.m1 = False
		self.m2 = False 
		self.inputhandler = inputhandler.Handler()
		self.camera = camera.Camera(Vct(0, 0), 20)
		self.sWheel = selection_wheel.Wheel(self.screen)
		self.filehandler = filehandler.Filehandler()
	
	def update(self):
		self.keys = pygame.key.get_pressed()
		if self.keys[pygame.K_ESCAPE]:
			self.end = True
		self.mousepos = Vct(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
		self.m1 = pygame.mouse.get_pressed()[0]
		self.m2 = pygame.mouse.get_pressed()[2]
		self.tick = (self.tick+1)%self.tickrate
		if self.tick == 0:
			classes.Unit.make_new_itteration()
		self.inputhandler.update(self.keys, self.m1, self.mousepos, self.camera, self.sWheel, self.filehandler)
		self.camera.update(self.m2, self.mousepos)
		self.sWheel.update(self.mousepos)
		

	def draw(self):
		self.screen.fill((0, 0, 20))
		for u in classes.Unit.units.values():
			u.draw(self.screen, self.camera)
		self.sWheel.draw(self.screen)
		preview.Preview.draw(self.screen, self.camera, self.inputhandler, self.filehandler.buffer)
		self.filehandler.draw(self.screen, self.camera)
		pygame.display.update()
		
	def run(self):
		while not self.end:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.end = True
					break
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 4:
						self.camera.zoom("in", self.mousepos)
					if event.button == 5:
						self.camera.zoom("out", self.mousepos)
			self.update()
			if not self.keys[pygame.K_d]:
				self.draw()

			self.clock.tick(120)
			#print(self.clock.get_fps())

if __name__ == "__main__":
	game = Game()
	print(game)
	game.run()
