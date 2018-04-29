from antClass import *
from roomClass import *
import fileinput
import math
import visu
import sys

def parse(roomList, AntList, pipeList):
	i = 0
	line = sys.stdin.readlines()
	if line[0] == "ERROR":
		exit()
	AntList = initAnts(int(line[0]))
	while i < len(line):
		if line[i] == "##start":
			addRoom(line[i + 1].split(), "sta", roomList)
			i += 1
		elif line[i] == "##end":
			addRoom(line[i + 1].split(), "end", roomList)
			i += 1
		elif line[i].find("-") == -1:
			addRoom(line[i].split(), "def", roomList)
		elif line[i].find("-") != -1:
			addPipe(line[i].split("-"), pipeList)
		elif line[i] == "\n":
			parseToMove()
			return
		i += 1
		
def parseToMove():
	return 
			
def addRoom(args, type, roomList):
	roomList.append(Room((math.floor((args[1] * visu.windowWidth) / 100), math.floor((args[2] * visu.windowHeight) / 100)), args[0], type, AntList, visu.radius))

def addPipe(args, pipeList):
	pipeList.append(Pipe((args[0], args[1]), roomList))

def initAnts(nbr):
	antList = []
	i = 1
	while i <= nbr:
		antList.append(Ant(i, (0, 0)))
		i += 1
	return antList