#######################################################################################################################
# Modely tříd classes_models slouží k ulehčení funkcí draw() u tříd preview a selection wheel                         #
# Jsou zde přidané nové třídy Remove a BringAlive, jejichž funcke jsou vysvětleny v inputhandler                      #
#######################################################################################################################

import pygame
from vectors import Vct
grey = (127, 127, 127, 255) 
lightgrey = (200, 200, 200, 255)
white = (255, 255, 255, 255)
green = (0, 255, 0, 255)
red = (255, 0, 0, 255)

class Wire:
	def draw(pos,screen, camera, selected = False, orientation = None):
		
		pygame.draw.rect(screen, white, (((pos+Vct(0.05, 0.05))*camera.scale-camera.pos).tuple(), (Vct(0.9, 0.9)*camera.scale).tuple()))
		if selected:
			pygame.draw.rect(screen, green, (((pos+Vct(0.05, 0.05))*camera.scale-camera.pos).tuple(), (Vct(0.9, 0.9)*camera.scale).tuple()), 1)

class Transistor():
	def draw(pos,screen, camera, selected = False, orientation = "upDown"):
		pygame.draw.rect(screen, white, (((pos+Vct(0.05, 0.05))*camera.scale-camera.pos).tuple(), (Vct(0.9, 0.9)*camera.scale).tuple()))
		if orientation == "upDown":
			pygame.draw.rect(screen, white, (((pos-Vct(0.25, 0) )* camera.scale-camera.pos).tuple(), ((Vct(1.5, 1) * camera.scale).tuple())))
			pygame.draw.rect(screen, lightgrey, (((pos-Vct(0.25, 0))* camera.scale-camera.pos).tuple(), ((Vct(1.5, 1)*camera.scale).tuple())),int(0.1 *camera.scale))
		if orientation == "leftRight":
			pygame.draw.rect(screen, white, (((pos-Vct(0, 0.25) )* camera.scale-camera.pos).tuple(), ((Vct(1, 1.5) * camera.scale).tuple())))
			pygame.draw.rect(screen, lightgrey, (((pos-Vct(0, 0.25))* camera.scale-camera.pos).tuple(), ((Vct(1, 1.5) * camera.scale).tuple())),int(0.1 *camera.scale))
		if selected:
			pygame.draw.rect(screen, green, (((pos+Vct(0.05, 0.05))*camera.scale-camera.pos).tuple(), (Vct(0.9, 0.9)*camera.scale).tuple()), 1)

class Diode():
	triangles = {"left":[Vct(0, 0.5), Vct(1, 0), Vct(1, 1)], 
				 "right":[Vct(0, 0), Vct(0, 1), Vct(1, 0.5)],
				 "up":[Vct(0, 1), Vct(1, 1), Vct(0.5, 0)],
				 "down":[Vct(0, 0), Vct(1, 0), Vct(0.5, 1)]}
	def draw(pos,screen, camera, selected = False, orientation = "down"): 
		verts = [((vert+pos)*camera.scale-camera.pos).tuple() for vert in Diode.triangles[orientation]]
		pygame.draw.polygon(screen, grey,verts)
		if selected:
			pygame.draw.rect(screen, green, (((pos+Vct(0.05, 0.05))*camera.scale-camera.pos).tuple(), (Vct(0.9, 0.9)*camera.scale).tuple()), 1)

class Remove():
	def draw(pos,screen, camera, selected = False,orientation = None):
		pygame.draw.line(screen, red, (pos*camera.scale-camera.pos).tuple(), (((pos+Vct(1, 1))*camera.scale-camera.pos).tuple()), int(0.2*camera.scale))
		pygame.draw.line(screen, red, ((pos+Vct(1,0))*camera.scale-camera.pos).tuple(), (((pos+Vct(0, 1))*camera.scale-camera.pos).tuple()), int(0.2*camera.scale))
		if selected:
			pygame.draw.rect(screen, green, (((pos+Vct(0.05, 0.05))*camera.scale-camera.pos).tuple(), (Vct(0.9, 0.9)*camera.scale).tuple()), 1)

class BringAlive():
	def draw(pos,screen, camera, selected = False,orientation = None):
		pygame.draw.rect(screen, red, (((pos+Vct(0.05, 0.05))*camera.scale-camera.pos).tuple(), (Vct(0.9, 0.9)*camera.scale).tuple()))
		if selected:
			pygame.draw.rect(screen, green, (((pos+Vct(0.05, 0.05))*camera.scale-camera.pos).tuple(), (Vct(0.9, 0.9)*camera.scale).tuple()), 1)