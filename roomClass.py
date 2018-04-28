import pygame

class Room:
	def __init__(self, coo, name, type):
		self.coo = coo
		self.type = type
		self.name = name
		self.radius = 35
		#self.named = font.render(self.name, 1, (255, 255, 255))

	def display(self, window):
		if (self.type == "def"):
			color = (255, 127, 80)
		elif (self.type == "end"):
			color = (30, 144, 255)
		else:
			color = (106, 90, 205)
		pygame.draw.circle(window, color, self.coo, self.radius)
