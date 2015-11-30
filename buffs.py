#This file contains the definition of the buffs class
#Buffs are effects that work on the player for some rounds. eg.:bleeding
#every player object contains a buff object

class buffs():
	
	def __init__(self):
		
		self.bleeding = 0
		self.hexed = 0
		self.poisoned = 0
		self.immobilized = 0
		self.confused = 0
		self.light = 0
		
	def set_buff(self,name,duration):
		
		if name == 'bleeding':
			self.bleeding += duration
		elif name == 'hexed':
			self.hexed += duration
		elif name == 'poisoned':
			self.poisoned += duration
		elif name == 'immobilized':
			self.immobilized += duration
		elif name == 'confused':
			self.confused += duration
		elif name == 'light':
			if duration > self.light:
				self.light = duration#light can't be added on		
			
	def buff_tick(self):
		
		if self.bleeding > 0:
			self.bleeding -= 1
		elif self.bleeding < 0:
			self.bleeding = 0	
		
		if self.hexed > 0:
			self.hexed -= 1
		elif self.hexed < 0:
			self.hexed = 0
			
		if self.poisoned > 0:
			self.poisoned -= 1
		elif self.poisoned < 0:
			self.poisoned = 0
			
		if self.immobilized > 0:
			self.immobilized -= 1
		elif self.immobilized < 0:
			self.immobilized = 0
			
		if self.confused > 0:
			self.confused -= 1
		elif self.confused < 0:
			self.confused = 0
		
		if self.light > 0:
			self.light -= 1
		elif self.light < 0:
			self.light = 0
			
	def sget(self):
	
		slist = [' ']
		
		if self.bleeding > 0:
			slist.append('BLEEDING(' + str(self.bleeding) + ')')
			
		if self.hexed > 0:
			slist.append('HEXED(' + str(self.hexed) + ')')
			
		if self.poisoned > 0:
			slist.append('POISONED(' + str(self.poisoned) + ')')
			
		if self.immobilized > 0:
			slist.append('IMMOBILIZED(' + str(self.immobilized) + ')')
		
		if self.confused > 0:
			slist.append('CONFUSED(' + str(self.immobilized) + ')')
			
		if self.light > 0:
			slist.append('LIGHT(' + str(self.light) + ')')
			
		if len(slist) > 1:
			del slist[0]
		
		return slist
