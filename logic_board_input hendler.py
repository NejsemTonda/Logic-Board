import pygame
import logic_board_classes as classes
import main
from logic_board_vectors import Vct
import 

class Handler():
	mousexy = (((main.Game.mousepos-camera.pos) - ((main.Game.mousepos-camera.pos)%camera.scale))/camera.scale).round()
	activeunit = "Wire"
	def update(self):
		self.mousexy = (((main.Game.mousepos-camera.pos) - ((main.Game.mousepos-camera.pos)%camera.scale))/camera.scale).round()
		if main.Game.m1:
			if self.activeunit == "Wire":
				classes.Units.units[mousexy] = classes.Wire(mousexy)
			if self.activeunit == "Transistor":
				classes.Units.units[mousexy] = classes.Wire(mousexy)