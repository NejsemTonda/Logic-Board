###########################################################################################################################
# Třída Preview slouží pouze k náhledu buňky, kterou se chystéme pokládat, její orientaci nebo k buferu třídy Filehandler #
###########################################################################################################################



import pygame
import classes_models
import classes
from vectors import Vct
import filehandler

class Preview:
	def draw(screen, camera,handler, units):

		if handler.activeunit == classes_models.Transistor:
			classes_models.Transistor.draw(handler.mousexy, screen, camera, orientation = handler.transistorRotation[0][handler.transistorRotation[1]])
		elif handler.activeunit == classes_models.Diode:
			classes_models.Diode.draw(handler.mousexy, screen, camera, orientation = handler.diodeRotation[0][handler.diodeRotation[1]])
		elif handler.activeunit == "insertiontool":
			for info in units:
				if info[1] == classes.Transistor:
					classes_models.Transistor.draw(handler.mousexy+info[0], screen, camera, orientation = info[2])
				elif info[1] == classes.Diode:
					classes_models.Diode.draw(handler.mousexy+info[0], screen, camera, orientation = info[2])
				elif info[1] == classes.Wire:
					classes_models.Wire.draw(handler.mousexy+info[0], screen, camera)
		elif handler.activeunit == "copytool" or handler.activeunit == "croptool":
			pass
		else:
			handler.activeunit.draw(handler.mousexy, screen, camera)
 
	