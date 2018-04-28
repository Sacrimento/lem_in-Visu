class Ant:
	def __init__(self, nbr, coo):
		self.num = nbr
		self.coo = coo

	def display(self, window, AntImg, radius):
		window.blit(AntImg, (self.coo[0] - 2.3 * radius, self.coo[1] - radius))

	def move(self, where, roomList):
		for room in roomList:
			if room.name == where:
				self.coo = room.coo