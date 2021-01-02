from vectors import Vct
import pygame
import classes
import os

class Filehandler:
	def __init__(self):
		self.units = [] # v tomto listu jsou uložené všechny buňky, jež jsou označeny výběrem
		self.buffer = [] # slouží k ukládání a nahrávání buňek
		self.rect = [Vct(0, 0), Vct(0, 0)] # obdelník ukazující výběr

	def update(self, mousexy):
		self.units = []
		if self.rect[0] == Vct(0, 0):
			self.rect[0] = mousexy
		self.rect[1] = mousexy-self.rect[0]

		for pos in classes.Unit.units:
			if self.is_in_rect(pos):
				self.units.append(pos)
				classes.Unit.units[pos].selected = True
			else:
				classes.Unit.units[pos].selected = False

	def draw(self, screen, camera):
		if self.rect == [Vct(0, 0), Vct(0, 0)]:
			return
		else: 
			pygame.draw.rect(screen, (0, 255, 0),( (self.rect[0]*camera.scale-camera.pos).tuple(),  ((self.rect[1]+Vct(1, 1))*camera.scale).tuple()), 1)


	def save(self): #uloží buňky co jsou ve výběru označeném čtvercem a uloží je do listu self.buffer
		self.buffer = []
		for pos in self.units:
			classes.Unit.units[pos].selected = False
			rel_pos = pos - self.rect[0]-round(self.rect[1]/2)
			self.buffer.append([rel_pos, type(classes.Unit.units[pos]), classes.Unit.units[pos].orientation])
		self.untis = []
		self.rect = [Vct(0, 0), Vct(0, 0)]
		print(self.buffer)

	def load(self): # Z uložených textových souborů vytvoří buffer, který lze poté vložit do simulace
		self.buffer = []
		list = [name for name in os.listdir() if ".txt" in name]

		for i, name in enumerate(list):
			print(str(i+1) + ". " + name) # tímto se usnadní výběr souboru, uživatel nemusí psát celý název, stačí pouze číslo
		try:
			file = open(list[int(input("select number of file:"))-1])
		except IndexError:
			print("There is no file with that number :(")
			return

		for line in file.readlines(): # tímto cyklem se načítá soubor do bufferu
			line = line.strip().split(" ")
			line[0] = [s.strip("()") for s in line[0].split(",")]
			if line[1] == "wire":
				self.buffer.append([Vct(int(line[0][0]), int(line[0][1])), classes.Wire, line[2]])
			if line[1] == "diode":
				self.buffer.append([Vct(int(line[0][0]), int(line[0][1])), classes.Diode, line[2]])
			if line[1] == "transistor":
				self.buffer.append([Vct(int(line[0][0]), int(line[0][1])), classes.Transistor, line[2]])

	def store_buffer(self): # tato funkce slouží k uložení list self.buffer do textovécho souboru
		file = None
		fileName = input("Enter file name: ")
		while fileName+".txt" in os.listdir() and file == None:
			des = input("This file already extis, do you wanna overwrite it ? (y/n)")
			if des == "y":
				file = open(fileName+".txt", "w")
			elif des == "n":
				fileName = input("Enter file name: ")

		if file == None:
			file = open(fileName+".txt", "x")

		for info in self.buffer:
			if info[1] == classes.Wire: 
				info[1] = " wire "
			elif info[1] == classes.Diode: 
				info[1] = " diode "
			elif info[1] == classes.Transistor: 
				info[1] = " transistor "
			else:
				print("wrong info:" + info)

			file.write(str(info[0])+info[1]+str(info[2]) + "\n")
		file.close()

	def blit_copy(self, mousexy): # tato funkce umístí všechny buňky v listu buffer do světa simulace
		for info in self.buffer:
			info[1].make_new(mousexy + info[0] , info[2])


	def is_in_rect(self, pos):
		if pos.x < self.rect[0].x or pos.x > self.rect[0].x+self.rect[1].x:
			return False
		if pos.y < self.rect[0].y or pos.y > self.rect[0].y+self.rect[1].y:
			return False
		return True
