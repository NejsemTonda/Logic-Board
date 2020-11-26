import pygame
import logic_board_classes as classes
from logic_board_vectors import Vct
import logic_board_inputhandler
import logic_board_camera

class Game():
	def __init__(self):
		self.end = False
		self.screen = pygame.display.set_mode((0, 0))#,pygame.FULLSCREEN
		self.clock = pygame.time.Clock()
		self.tick = 0
		self.key = []
		self.mousepos = (0, 0)
		self.m1 = False
		self.m2 = False 
		self.inputhandler = logic_board_inputhandler.Handler()
		self.camera = logic_board_camera.Camera()
	
	def update(self):
		self.tick = (self.tick+1)%4
		if self.tick == 0:
			classes.new_itter()
		self.inputhandler.update(self.keys, self.m1, self.mousepos)
		self.camera.update(self.m2, self.mousepos)

	def draw(self):
		self.screen.fill((0, 0, 0))
		for u in classes.Unit.units.values():
			u.draw(self.screen, self.camera)
		pygame.display.update()
	def run(self):
		while not self.end:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.end = True
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 4:
						self.camera.scale*=1.1
					if event.button == 5:
						self.camera.scale*=0.9


			self.keys = pygame.key.get_pressed()
			if self.keys[pygame.K_ESCAPE]:
				self.end = True
			self.mousepos = Vct(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
			self.m1 = pygame.mouse.get_pressed()[0]
			self.m2 = pygame.mouse.get_pressed()[2]
			self.update()
			if not self.keys[pygame.K_d]:
				self.draw()
			self.clock.tick(120)
			#print(self.clock.get_fps())

game = Game()
print(game)
game.run()