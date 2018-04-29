from antClass import *
from roomClass import *
import fileinput
import math
import visu
import sys

def parse():
	global AntList
	i = 0
	lines = getLines()
	if lines[0] == "ERROR":
		exit()
	AntList = initAnts(int(lines[0]))
	while i < len(lines):
		if lines[i] == "##start":
			addRoom(lines[i + 1].split(), "sta")
			i += 1
		elif lines[i] == "##end":
			addRoom(lines[i + 1].split(), "end")
			i += 1
		elif lines[i].find("-") == -1:
			addRoom(lines[i].split(), "def")
		elif lines[i].find("-") != -1:
			addPipe(lines[i].split("-"))
		elif lines[i] == "\n":
			parseToMove(lines, i + 1)
			return
		i += 1
		
def parseToMove(lines, i):
	global toMove
	while i < len(lines):
		instL = []
		insts = lines[i].split()
		for inst in insts:
			instL.append((inst[1], inst[3:]))
		toMove.append(instL)
		i += 1

def getLines():
	lines = []
	stdin = sys.stdin.readlines()
	for l in stdin:
		lines.append(l.replace('\n', ''))
	return lines
			
def addRoom(args, type):
	global roomList
	roomList.append(Room((math.floor((args[1] * visu.windowWidth) / 100), math.floor((args[2] * visu.windowHeight) / 100)), args[0], type, AntList, visu.radius))

def addPipe(args):
	global pipeList
	pipeList.append(Pipe((args[0], args[1]), roomList))

def initAnts(nbr):
	antList = []
	i = 1
	while i <= nbr:
		antList.append(Ant(i, (0, 0)))
		i += 1
	return antList