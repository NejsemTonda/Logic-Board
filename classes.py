import pygame
from vectors import Vct

class Unit():
	units = {}
	living_units = []
	new_itteration = []
	directions = {"up": Vct(0, -1), 
				  "down":Vct(0, 1), 
				  "left":Vct(-1, 0), 
				  "right":Vct(1, 0)}

	colors = {"grey": (127, 127, 127), 
			  "lightgrey":(180, 180, 180), 
			  "white":(255, 255, 255), 
			  "green":(0, 255, 0)}

	wirecolors = {0:(255,255,255),
				  1:(255, 100, 100), 
				  2:(255,50,50),
				  3:(255, 0, 0), 
				  4:(0, 255, 0)}


	shapes = {}
	def __init__(self, pos):
		self.pos = pos
		self.neighbors = {}
		self.life = 0
		self.selected = False
		self.orientation = None

	def updateneighbors(self):
		self.neighbors = {}
		for d in self.directions.values():
			if d+self.pos in self.units:
				self.neighbors[d+self.pos] = self.units[d+self.pos]

	def draw(self, screen, camera):
		pygame.draw.rect(screen, self.wirecolors[self.life], (((self.pos+Vct(0.05, 0.05))*camera.scale-camera.pos).tuple(), (Vct(0.9, 0.9)*camera.scale).tuple()))
		if self.selected:
			pygame.draw.rect(screen, self.colors["green"], (((self.pos)*camera.scale-camera.pos).tuple(), (Vct(1, 1)*camera.scale).tuple()), 1)
	def make_new_itteration():
		#print(Unit.units)
		Unit.new_itteration = []
		filtred_new_itter = []

		for pos in Unit.living_units:
			if not pos in filtred_new_itter:
				filtred_new_itter.append(pos)
		Unit.living_units = filtred_new_itter

		for pos in Unit.living_units:
			if type(Unit.units[pos]) == Diode:
				Unit.units[pos].update()
		for pos in Unit.living_units:
			if type(Unit.units[pos]) != Diode:
				Unit.units[pos].update()

		Unit.living_units = Unit.new_itteration

class Wire(Unit):
	def update(self):
		if self.life == 3:
			for u in self.neighbors.values():
				if type(u) != Diode:
					if u.life == 0:
						self.new_itteration.append(u.pos)
						u.life = 3

		if self.life != 0:
			self.life -=1
			self.new_itteration.append(self.pos)

	def make_new(pos, orientation = None):
		Unit.units[pos] = Wire(pos)
		Unit.units[pos].updateneighbors()
		for n in Unit.units[pos].neighbors.values():
			n.updateneighbors()

	def __repr__(self):
		return("Wire {} {}".format(self.pos.x, self.pos.y))



class Transistor(Unit):
	def __init__(self,pos, orientation = "upDown"):
		super().__init__(pos)
		self.orientation = orientation
		self.blocked = 0
		self.color = self.colors["white"]

	def update(self):
		if self.orientation == "upDown":
			for d in ["left", "right"]:
				if self.pos + self.directions[d] in self.neighbors and self.neighbors[self.pos + self.directions[d]].life != 0:
					self.blocked = 12

		if self.orientation == "leftRight":
			for d in ["up", "down"]:
				if self.pos + self.directions[d] in self.neighbors and self.neighbors[self.pos + self.directions[d]].life != 0:
					self.blocked = 12

		if self.blocked != 0:
			self.life = 0
			self.color = self.colors["lightgrey"]
			self.blocked -=1
			self.new_itteration.append(self.pos)
		else:
			self.color = self.colors["white"]

		if self.life == 3:
			for u in self.neighbors.values():
				if type(u) != Diode:
					if u.life == 0:
						self.new_itteration.append(u.pos)
						u.life = 3
					
		if self.life != 0:
			self.life -=1
			self.new_itteration.append(self.pos)
			
	def draw(self, screen, camera):
		if self.orientation == "upDown":
			pygame.draw.rect(screen, self.color, (((self.pos-Vct(0.25, 0) )* camera.scale-camera.pos).tuple(), ((Vct(1.5, 1) * camera.scale).tuple())))
			pygame.draw.rect(screen, self.colors["grey"], (((self.pos-Vct(0.25, 0))* camera.scale-camera.pos).tuple(), ((Vct(1.5, 1)*camera.scale).tuple())),int(0.1 *camera.scale))
		elif self.orientation == "leftRight":
			pygame.draw.rect(screen, self.color, (((self.pos-Vct(0, 0.25) )* camera.scale-camera.pos).tuple(), ((Vct(1, 1.5) * camera.scale).tuple())))
			pygame.draw.rect(screen, self.colors["grey"], (((self.pos-Vct(0, 0.25))* camera.scale-camera.pos).tuple(), ((Vct(1, 1.5) * camera.scale).tuple())),int(0.1 *camera.scale))
		if self.selected:
			pygame.draw.rect(screen, self.colors["green"], (((self.pos)*camera.scale-camera.pos).tuple(), (Vct(1, 1)*camera.scale).tuple()), 1)

	def make_new(pos, orientation):
		Unit.units[pos] = Transistor(pos, orientation)
		Unit.units[pos].updateneighbors()
		for n in Unit.units[pos].neighbors.values():
			n.updateneighbors()

	def __repr__(self):
		return("Transistor {} {} {}".format(self.pos.x, self.pos.y, self.orientation))



class Diode(Unit):
	triangles = {"left":[Vct(0, 0.5), Vct(1, 0), Vct(1, 1)], 
				 "right":[Vct(0, 0), Vct(0, 1), Vct(1, 0.5)],
				 "up":[Vct(0, 1), Vct(1, 1), Vct(0.5, 0)],
				 "down":[Vct(0, 0), Vct(1, 0), Vct(0.5, 1)]}

	def __init__(self, pos, orientation = "left"):
		super().__init__(pos)
		self.orientation = orientation
		self.new_itteration.append(self.pos)

	def update(self):
		self.life = 0
		for d in self.directions:
			if self.orientation == d:
				if self.pos-self.directions[d] in self.living_units and self.neighbors[self.pos-self.directions[d]].life == 3:
					if self.pos+self.directions[d] in self.neighbors:
						if type(self.neighbors[self.pos+self.directions[d]]) == Transistor and not d in self.neighbors[self.pos+self.directions[d]].orientation.lower():
							self.neighbors[self.pos+self.directions[d]].blocked = 12
							self.new_itteration.append(self.pos+self.directions[d])
						else:
							self.neighbors[self.pos+self.directions[d]].life = 3
							self.new_itteration.append(self.pos+self.directions[d])
		self.new_itteration.append(self.pos)

	def draw(self,screen, camera): 
		verts = [((vert+self.pos)*camera.scale-camera.pos).tuple() for vert in self.triangles[self.orientation]]
		pygame.draw.polygon(screen, self.colors["grey"],verts)
		if self.selected:
			pygame.draw.rect(screen, self.colors["green"], (((self.pos)*camera.scale-camera.pos).tuple(), (Vct(1, 1)*camera.scale).tuple()), 1)

	def make_new(pos, orientation):
		Unit.units[pos] = Diode(pos, orientation)
		Unit.units[pos].updateneighbors()
		for n in Unit.units[pos].neighbors.values():
			n.updateneighbors()

	def __repr__(self):
		return("Diode {} {} {}".format(self.pos.x, self.pos.y, self.orientation))
