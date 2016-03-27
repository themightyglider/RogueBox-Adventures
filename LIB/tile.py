class tile():
	
	def __init__(self,techID, name, tile_color, use_group, move_group, grow_group, damage, move_message, damage_message, destroy = False, replace = None, civilisation = False, can_grown = False, build_here = True, tile_pos = (0,0), transparency = True, conected_items = None, conected_tiles = None, conected_resources = None):
		
		self.techID = techID
		self.name = name
		self.tile_color = tile_color
		self.use_group = use_group
		self.move_group = move_group
		self.grow_group = grow_group
		self.damage = damage
		self.move_mes = move_message
		self.damage_mes = damage_message
		self.destroy = destroy
		self.replace = replace
		self.civilisation = civilisation
		self.can_grown = can_grown
		self.build_here = build_here
		self.tile_pos = tile_pos
		self.transparency = transparency
		self.conected_items = conected_items
		self.conected_tiles = conected_tiles
		self.conected_resources = conected_resources
