import pygame
from logic_board_vectors import Vct
wirecolors = {0:(255,255,255),1:(255, 100, 100), 2:(255,50,50),3:(255, 0, 0), 4:(0, 255, 0)}
transcolor = [(255, 255, 255), (127, 127, 127)]
size = 1

class Unit():
	units = {}
	living_units = []
	new_itter = []
	directions = {"up": Vct(0, -1), "down":Vct(0, 1), "left":Vct(-1, 0), "right":(1, 0)}
	colors = {"grey": (127, 127, 127), "darkgray":(200, 200, 200), "white":(255, 255, 255), "green":(0, 255, 0)}
	def __init__(self, pos):
		self.pos = pos
		self.neighbors = {}
		self.life = 0
		self.selected = False
	def updateneighbors(self, units):
		self.neighbors = []
		for d in self.directions:
			if d+self.pos in self.units:
				neighbors[d+self.pos] = units[d+self.pos]
	def draw(self, screen, camera):
		pygame.draw.rect(screen, wirecolors[self.life], (((self.pos-camera.pos+Vct(0.05, 0.05))*camera.scale).tuple(), (Vct(0.9, 0.9)*camera.scale).tuple()))
		if self.selected:
			pygame.draw.rect(screen, colors["green"], (((self.pos-camera.pos+Vct(0.05, 0.05))*camera.scale).tuple(), (Vct(0.9, 0.9)*camera.scale).tuple()), 1)
	def new_itteration(self):
		self.new_itteration = []
		for p in self.living_units:
			units[p].update()
		self.living_units = self.new_itteration

class Wire(Unit):
	def update(self):
		for u in self.neighbors:
			if u.life == 0:
				self.new_itter.append(u.pos)
				u.life = 4
		if self.life != 0:
			self.life -=1
			self.new_itter.appned(self.pos)

	def __repr__(self):
		return("Wire {} {}".format(self.pos.x, self.pos.y))

class Transistor(Unit):
	def __init__(self,pos, orientation):
		super().__init__(pos)
		self.orientation = orientation
		self.blocked = 0
		self.color = colors["white"]
	def update(self):
		if self.orientation == "Transistorupdown":
			if self.pos + directions["up"] in living_units or self.pos + directions["down"] in living_units:
				self.life = 4
				self.new_itter.append(self.pos)
			if self.pos + directions["left"] in living_units or self.pos + directions["right"] in living_units:
				self.blocked = 12 

		if self.orientation == "Transistorleftright":
			if self.pos + directions["up"] in living_units or self.pos + directions["down"] in living_units:
				self.blocked = 12 
			if self.pos + directions["left"] in living_units or self.pos + directions["right"] in living_units:
				self.life = 4
				self.new_itter.append(self.pos)

		if self.life != 0:
				self.life -=1
				self.new_itter.appned(self.pos)
		if self.blocked != 0:
			self.life = 0
			self.color = colors["grey"]
			self.blocked -=1
		else:
			self.color = colors["white"]

		for u in neighbors:
			if u.life == 0:
				self.new_itter.append(u.pos)
				u.life = 4
		

	def draw(self, screen, camera):
		if self.orientation == "Transistorupdown":
			pygame.draw.rect(screen, self.color, ((self.pos-Vct(0.25, 0)-camera.pos * camera.scale).tuple(), ((self.pos+Vct(0.5, 0)-camera.pos * camera.scale).tuple())))
			pygame.draw.rect(screen, colors["darkgray"], ((self.pos-Vct(0.25, 0)-camera.pos * camera.scale).tuple(), ((self.pos-Vct(0.5, 0)-camera.pos * camera.scale).tuple(), int(2*camera.scale))))
		if self.orientation == "Transistorleftright":
			pygame.draw.rect(screen, self.color, ((self.pos-Vct(0, 0.25)-camera.pos * camera.scale).tuple(), ((self.pos+Vct(0, 0.5)-camera.pos * camera.scale).tuple())))
			pygame.draw.rect(screen, colors["darkgray"], ((self.pos-Vct(0, 0.25)-camera.pos * camera.scale).tuple(), ((self.pos+Vct(0, 0.5)-camera.pos * camera.scale).tuple(), int(2*camera.scale))))
		if self.selected:
			pygame.draw.rect(screen, (0, 255, 0), ((self.x)*scale + shift[0], (self.y)*scale + shift[1], (size)*scale, (size)*scale), 1)

	def __repr__(self):
		return("Transistor {} {} {}".format(self.x, self.y, self.orientation))

"""class Diode(Unit):
	def __init__(self, x, y, units, orientation):
		super().__init__(x,y, units)
		self.orientation = orientation

	def update(self):
		if self.orientation == "Diodeleft":
			if (self.x + 1, self.y) in self.plus and (self.x - 1, self.y) in self.plus:
				if self.plus[(self.x + 1, self.y)].life == 2:
					if type(self.plus[(self.x - 1, self.y)]) == Wire:
						self.plus[(self.x - 1, self.y)].life = 4
					elif type(self.plus[(self.x - 1, self.y)]) == Transistor:
						if self.plus[(self.x-1, self.y)].orientation == "Transistorleftright":
							self.plus[(self.x - 1, self.y)].blocked = 12
						else:
							self.plus[(self.x - 1, self.y)].life = 4
							
		if self.orientation == "Dioderight":
			if (self.x - 1, self.y) in self.plus and (self.x + 1, self.y) in self.plus:
				if self.plus[(self.x - 1, self.y)].life == 2:
					if type(self.plus[(self.x + 1, self.y)]) == Wire:
						self.plus[(self.x + 1, self.y)].life = 4
					elif type(self.plus[(self.x + 1, self.y)]) == Transistor:
						if self.plus[(self.x+1, self.y )].orientation == "Transistorleftright":
							self.plus[(self.x + 1, self.y)].blocked = 12
						else:
							self.plus[(self.x + 1, self.y)].life = 4

		if self.orientation == "Diodeup":
			if (self.x , self.y+ 1) in self.plus and (self.x , self.y- 1) in self.plus :
				if self.plus[(self.x , self.y+ 1)].life == 2:
					if type(self.plus[(self.x, self.y - 1)]) == Wire:
						self.plus[(self.x, self.y - 1)].life = 4 
					elif type(self.plus[(self.x, self.y - 1)]) == Transistor:
						if self.plus[(self.x, self.y-1)].orientation == "Transistorupdown":
							self.plus[(self.x, self.y - 1)].blocked = 12
						else:
							self.plus[(self.x, self.y - 1)].life = 4
						
		if self.orientation == "Diodedown":
			if (self.x , self.y- 1) in self.plus and (self.x , self.y+ 1) in self.plus:
				if self.plus[(self.x , self.y- 1)].life == 2:
					if type(self.plus[(self.x, self.y +1)]) == Wire:
						self.plus[(self.x, self.y +1)].life = 4
					elif type(self.plus[(self.x, self.y +1)]) == Transistor:
						if self.plus[(self.x, self.y+1)].orientation == "Transistorupdown":
							self.plus[(self.x, self.y +1)].blocked = 12
						else:
							self.plus[(self.x, self.y +1)].life = 4

	def draw(self, screen,scale, shift):
		if self.orientation == "Diodeleft":
			pygame.draw.polygon(screen, (127, 127,127), (((self.x + 1)* scale+shift[0], self.y*scale+shift[1]), ((self.x + 1)*scale+shift[0], (self.y+1)*scale+shift[1]), (self.x*scale+shift[0], (self.y + 0.5)*scale+shift[1])))
		elif self.orientation == "Dioderight":
			pygame.draw.polygon(screen, (127, 127,127), (((self.x)* scale+shift[0], self.y*scale+shift[1]), (self.x*scale+shift[0], (self.y+1)*scale+shift[1]), ((self.x + 1)*scale+shift[0], (self.y + 0.5)*scale+shift[1])))
		elif self.orientation == "Diodeup":
			pygame.draw.polygon(screen, (127, 127,127),(((self.x + 0.5)* scale+shift[0], self.y*scale+shift[1]), ((self.x + 1)*scale+shift[0], (self.y+1)*scale+shift[1]), (self.x*scale+shift[0], (self.y + 1)*scale+shift[1])))
		elif self.orientation == "Diodedown":
			pygame.draw.polygon(screen, (127, 127,127), (((self.x + 0.5)* scale+shift[0], (self.y +1)*scale+shift[1]), ((self.x + 1)*scale+shift[0], self.y*scale+shift[1]), (self.x*scale+shift[0], self.y*scale+shift[1])))
		if self.selected:
			pygame.draw.rect(screen, (0, 255, 0), ((self.x)*scale + shift[0], (self.y)*scale + shift[1], (size)*scale, (size)*scale), 1)
	def __repr__(self):
		return("Diode {} {} {}".format(self.x, self.y, self.orientation))


def draw_preview(screen, scale,shift, mousexy, activeunit, units):
	if activeunit == "Wire":
		Wire(mousexy[0], mousexy[1], units).draw(screen,scale,shift)

	if activeunit == "Transistorupdown":
		Transistor(mousexy[0], mousexy[1], units,"Transistorupdown").draw(screen,scale,shift)

	elif activeunit == "Transistorleftright":
		Transistor(mousexy[0], mousexy[1], units,"Transistorleftright").draw(screen,scale,shift)

	if activeunit == "Diodeup":
		Diode(mousexy[0], mousexy[1], units,"Diodeup").draw(screen,scale,shift)
		
	elif activeunit == "Dioderight":
		Diode(mousexy[0], mousexy[1], units,"Dioderight").draw(screen,scale,shift)
		
	elif activeunit == "Diodeleft":
		Diode(mousexy[0], mousexy[1], units,"Diodeleft").draw(screen,scale,shift)
		
	elif activeunit == "Diodedown":
		Diode(mousexy[0], mousexy[1], units,"Diodedown").draw(screen,scale,shift)
		
"""