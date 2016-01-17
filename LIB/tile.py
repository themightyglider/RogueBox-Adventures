class tile():
	
	def __init__(self,techID, name, tile_color,  move, damage, move_message = None, damage_message = None, destroy = False, replace = None, transparent = True, civilisation = False, can_grown = False, build_here = True, tile_pos = (0,0)):
		
		self.techID = techID
		self.name = name
		self.tile_color = tile_color
		self.move = move
		self.damage = damage
		self.move_mes = move_message
		self.damage_mes = damage_message
		self.destroy = destroy
		self.replace = replace
		self.transparent = transparent
		self.civilisation = civilisation
		self.can_grown = can_grown
		self.build_here = build_here
		self.tile_pos = tile_pos
		
		print self.name , ':' , str(self.techID)
