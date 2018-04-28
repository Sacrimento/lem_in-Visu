import sys
import math
import pygame
from pygame.locals import *
from roomClass import *
from pipeClass import *
from antClass import *


windowHeight = 768
windowWidth = 1366

fontSize = 20
radius = 50

##########################################################################################################

def initAnts(nbr):
	antList = []
	i = 1
	while i <= nbr:
		antList.append(Ant(i, (0, 0)))
		i += 1
	return antList

##########################################################################################################
AntList = initAnts(2)

roomList = []
roomList.append(Room((math.floor((50 * windowWidth) / 100), math.floor((50 * windowHeight) / 100)), "1", "end", AntList, radius))
roomList.append(Room((450, 25), "La test", "sta", AntList, radius))
roomList.append(Room((25, 450), "La test2", "def", AntList, radius))
roomList.append(Room((220, 100), "La test3", "def", AntList, radius))
pygame.init()

pipeList = []
pipeList.append(Pipe(("1", "La test2"), roomList))
pipeList.append(Pipe(("1", "La test3"), roomList))
pipeList.append(Pipe(("1", "La test"), roomList))
pipeList.append(Pipe(("La test3", "La test2"), roomList))

window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Lem_in')
AntImg = pygame.image.load("img/ant.png").convert_alpha()

done = False

toMove = [(1, "La test3"), (2, "1")]

while not done:
	for event in pygame.event.get():
		if event.type == QUIT:
			done = True
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				done = True
			elif event.key == K_RETURN:
				for ant in AntList:
					for who in toMove:
						if ant.num == who[0]:
							ant.move(who[1], roomList)
	for pipe in pipeList:
		pipe.display(window)
	for room in roomList:
		room.display(window)
		window.blit(pygame.font.SysFont('Arial', fontSize, 1).render(room.name, False, (255, 255, 255)), (room.coo[0] - ((len(room.name) * fontSize) / 4.5), room.coo[1] + radius + 2))
	for ant in AntList:
		ant.display(window, AntImg, radius)
	pygame.display.flip()

pygame.quit()