class countdown():
	
	def __init__(self, kind, x, y, countfrom):
	# countdown objects are used to initialize a event after a  certain number of turns. They are bound to a certain map.
	#kind: is a string and tell the min programm what kind of event should be done
	#x,y: cordinates of the tile that is affected by the event
	#countfrom: number of turns
	
		self.kind = kind
		self.x = x
		self.y = y
		self.count = countfrom
	
	def countdown(self):
	#count down and check if it got 0
		
		self.count -= 1
		
		if self.count <= 0:
			return True
		else:
			return False 
