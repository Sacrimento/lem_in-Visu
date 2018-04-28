class Ant:
	def __init__(self, nbr, coo):
		self.num = nbr
		self.coo = coo

	def display(self, window, AntImg, radius):
		window.blit(AntImg, (self.coo[0] - 1.4 * radius, self.coo[1] - radius / 1.8))

	def move(self, where, roomList):
		for room in roomList:
			if room.name == where:
				self.coo = room.coo