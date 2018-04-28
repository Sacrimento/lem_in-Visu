import sys
import math
import pygame
from pygame.locals import *
from roomClass import *
from pipeClass import *

windowHeight = 768
windowWidth = 1366

fontSize = 20

roomList = []
roomList.append(Room((math.floor((50 * windowWidth) / 100), math.floor((50 * windowHeight) / 100)), "1", "end"))
roomList.append(Room((450, 25), "La test", "sta"))
roomList.append(Room((25, 450), "La test2", "def"))
roomList.append(Room((220, 100), "La test3", "def"))
pygame.init()

pipeList = []
pipeList.append(Pipe(("1", "La test2"), roomList))
pipeList.append(Pipe(("1", "La test3"), roomList))
pipeList.append(Pipe(("1", "La test"), roomList))
pipeList.append(Pipe(("La test3", "La test2"), roomList))
AntList = []

window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Lem_in')

done = False

while not done:
	for event in pygame.event.get():
		if event.type == QUIT:
			done = True
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				done = True
	for pipe in pipeList:
		pipe.display(window)
	for room in roomList:
		room.display(window)
		window.blit(pygame.font.SysFont('Arial', fontSize, 1).render(room.name, False, (255, 255, 255)), (room.coo[0] - ((len(room.name) * fontSize) / 4.5), room.coo[1] + 37))
	# for ant in AntList:
		# ant.display()
	pygame.display.flip()

pygame.quit()