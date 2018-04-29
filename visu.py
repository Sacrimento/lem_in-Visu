import math
import pygame
from pygame.locals import *
from roomClass import *
from pipeClass import *
from antClass import *
from parser import *


windowHeight = 768
windowWidth = 1366

fontSize = 20
radius = 50

##########################################################################################################

global toMove
global roomList
global AntList
global pipeList
roomList = []
pipeList = []
AntList = []
toMove = []

parse(roomList, AntList, pipeList, toMove)

# roomList.append(Room((math.floor((50 * windowWidth) / 100), math.floor((50 * windowHeight) / 100)), "1", "end", AntList, radius))
# roomList.append(Room((450, 25), "La test", "sta", AntList, radius))
# roomList.append(Room((25, 450), "La test2", "def", AntList, radius))
# roomList.append(Room((90, 100), "La test3", "def", AntList, radius))
# roomList.append(Room((220, 56), "La test12", "def", AntList, radius))
# roomList.append(Room((500, 500), "La test15", "def", AntList, radius))
# roomList.append(Room((700, 700), "La test0", "def", AntList, radius))


# pipeList.append(Pipe(("1", "La test2"), roomList))
# pipeList.append(Pipe(("1", "La test3"), roomList))
# pipeList.append(Pipe(("1", "La test"), roomList))
# pipeList.append(Pipe(("La test3", "La test2"), roomList))

##########################################################################################################

window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Lem_in')
AntImg = pygame.image.load("img/ant.png").convert_alpha()

pygame.init()

done = False

def nextMove():
	return [(3, "La test0"), (2, "La test15")]

while not done:
	i = 0
	for event in pygame.event.get():
		if event.type == QUIT:
			done = True
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				done = True
			elif event.key == K_RETURN:
				whos = toMove[i]
				for ant in AntList:
					for who in whos:
						if ant.num == who[0]:
							ant.move(who[1], roomList)
				i += 1
	for pipe in pipeList:
		pipe.display(window)
	for room in roomList:
		room.display(window)
		window.blit(pygame.font.SysFont(None, fontSize, 1).render(room.name, False, (255, 255, 255)), (room.coo[0] - ((len(room.name) * fontSize) / 4.5), room.coo[1] + radius + 2))
	for ant in AntList:
		ant.display(window, AntImg, radius)
	pygame.display.flip()

pygame.quit()