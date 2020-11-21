import pygame
import logic_board_classes as classes
from logic_board_vectors import Vct

class Game:
	run = True
	window = pygame.display((0, 0), pygame.FULLSCREEN)
	clock = pygame.time.Clock()
	key = []
	mousepos = (0, 0)
	m1 = False
	m2 = False 
	def update():
		classes.Unit.new_itteration()
	def draw():
		pass
	def run():
		while self.run:
			self.keys = pygame.keys.get_pressed()
			if keys[pygame.K_ESCAPE]:
				self.run = False
			self.mousepos = Vct(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
			self.m1 = pygame.mouse.get_pressed()[0]
			self.m2 = pygame.mouse.get_pressed()[2]
			update()
			draw()
			clock.tick(120)