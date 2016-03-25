import cPickle as p
from tile import tile
from item_list import itemlist

il = itemlist()

class tilelist():
	def __init__(self):
	
		self.tlist = {}
		techID = 0
	
		self.tlist['misc'] = []
		#0
		t=tile(techID = techID,
					name = 'Low water',
					tile_color = 'light_blue',
					use_groupe = 'drink',
					move_groupe = 'low_liquid',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'Your feet become wet.', 
					damage_message = None,
					tile_pos = (0,7))
		self.tlist['misc'].append(t)
		techID+=1
		#1
		t=tile(techID = techID,
					name = 'Mud',
					tile_color = 'brown',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'The ground under your feet feels soft and wet.', 
					damage_message = None,
					tile_pos = (6,10))
		self.tlist['misc'].append(t)
		techID+=1
		#2
		t=tile(techID = techID,
					name = 'Hot caveground',
					tile_color = 'red',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'The ground under your feet feels like hot coals.', 
					damage_message = None,
					tile_pos = (5,5))
		self.tlist['misc'].append(t)
		techID+=1
		#3
		t=tile(techID = techID,
					name = 'Water',
					tile_color = 'blue',
					use_groupe = 'drink',
					move_groupe = 'swim',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'Cool water surrounds you.', 
					damage_message = None,
					tile_pos = (1,2))
		self.tlist['misc'].append(t)
		techID+=1
		#4
		t=tile(techID = techID,
					name = 'Ore',
					tile_color = 'ligh_red',
					use_groupe = 'None',
					move_groupe = 'solide',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You brake some ore out of the solid rock here.', 
					damage_message = None,
					destroy = 2,
					tile_pos = (0,2),
					transparency = False,
					conected_resources = ('ore',1))
		self.tlist['misc'].append(t)
		techID+=1
		#5
		t=tile(techID = techID,
					name = 'Gem',
					tile_color = 'ligh_blue',
					use_groupe = 'None',
					move_groupe = 'solide',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You brake a gem out of the solid rock here.', 
					damage_message = None,
					destroy = 4,
					tile_pos = (5,1),
					transparency = False,
					conected_resources = ('gem',1))
		self.tlist['misc'].append(t)
		techID+=1
		#6
		t=tile(techID = techID,
					name = 'Blue mushroom',
					tile_color = 'white',
					use_groupe = 'gather',
					move_groupe = 'soil',
					grow_groupe = 'mushroom',
					damage = 0, 
					move_message = 'A blue mushroom grows here.', 
					damage_message = None,
					tile_pos = (1,6),
					conected_items = (il.ilist['food'][1]))
		self.tlist['misc'].append(t)
		techID+=1
		#7
		t=tile(techID = techID,
					name = 'Brown mushroom',
					tile_color = 'white',
					use_groupe = 'gather',
					move_groupe = 'soil',
					grow_groupe = 'mushroom',
					damage = 0, 
					move_message = 'A brown mushroom grows here.', 
					damage_message = None,
					tile_pos = (5,8),
					conected_items = (il.ilist['food'][2]))
		self.tlist['misc'].append(t)
		techID+=1
		#8
		t=tile(techID = techID,
					name = 'Purple mushroom',
					tile_color = 'white',
					use_groupe = 'gather',
					move_groupe = 'soil',
					grow_groupe = 'mushroom',
					damage = 0, 
					move_message = 'A purple mushroom grows here.', 
					damage_message = None,
					tile_pos = (5,6),
					conected_items = (il.ilist['food'][3]))
		self.tlist['misc'].append(t)
		techID+=1
		#9
		t=tile(techID = techID,
					name = 'Lost gem',
					tile_color = 'red',
					use_groupe = 'resource',
					move_groupe = 'soil',
					grow_groupe = 'vanish',
					damage = 0, 
					move_message = 'A gem lies on the ground right here.', 
					damage_message = None,
					tile_pos = (1,8),
					conected_resources = ('gem',1))
		self.tlist['misc'].append(t)
		techID+=1
		#10
		t=tile(techID = techID,
					name = 'Water lily',
					tile_color = 'white',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'herblike',
					damage = 0, 
					move_message = 'A water lily grows here.', 
					damage_message = None,
					tile_pos = (1,1),
					conected_tiles = ('misc',14))
		self.tlist['misc'].append(t)
		techID+=1
		#11
		t=tile(techID = techID,
					name = 'Lost ore',
					tile_color = 'red',
					use_groupe = 'resource',
					move_groupe = 'soil',
					grow_groupe = 'vanish',
					damage = 0, 
					move_message = 'Some ore lies on the ground right here.', 
					damage_message = None,
					tile_pos = (1,7),
					conected_resources = ('ore',1))
		self.tlist['misc'].append(t)
		techID+=1
		#12
		t=tile(techID = techID,
					name = 'Lost gem',
					tile_color = 'red',
					use_groupe = 'resource',
					move_groupe = 'soil',
					grow_groupe = 'vanish',
					damage = 0, 
					move_message = 'A gem lies on the ground right here.', 
					damage_message = None,
					tile_pos = (1,8),
					conected_resources = ('gem',1))
		self.tlist['misc'].append(t)
		techID+=1
		#13
		t=tile(techID = techID,
					name = 'Present',
					tile_color = 'red',
					use_groupe = 'container',
					move_groupe = 'soil',
					grow_groupe = 'vanish',
					damage = 0, 
					move_message = 'A present lies on the ground right here.', 
					damage_message = None,
					tile_pos = (6,4))
		self.tlist['misc'].append(t)
		techID+=1
		#14
		t=tile(techID = techID,
					name = 'Water lily with blossom',
					tile_color = 'white',
					use_groupe = 'resource',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'A water lily with a beautiful blossom grows here.', 
					damage_message = None,
					tile_pos = (1,0),
					conected_tiles = (('misc',10)),
					conected_resources = ('herb',1))
		self.tlist['misc'].append(t)
		techID+=1
		#15
		t=tile(techID = techID,
					name = 'Giant mushroom',
					tile_color = 'white',
					use_groupe = 'tree',
					move_groupe = 'tree',
					grow_groupe = 'tree',
					damage = 0, 
					move_message = 'There is a giant mushroom here.', 
					damage_message = None,
					tile_pos = (6,0),
					transparency = False,
					conected_tiles = (('misc',7),('global_caves',0)),
					conected_resources = ('wood',3))
		self.tlist['misc'].append(t)
		techID+=1
	
		self.tlist['mine'] = []
	
		t=tile(techID = techID,
					name = 'Orcish mine floor',
					tile_color = 'light_red',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You walk over dry mine ground.', 
					damage_message = None,
					tile_pos = (0,5))
		self.tlist['mine'].append(t)
		techID+=1
		
		t=tile(techID = techID,
					name = 'Orcish mine wall',
					tile_color = 'red',
					use_groupe = 'None',
					move_groupe = 'solide',
					grow_groupe = 'None',
					damage = 0, 
					replace = self.tlist['mine'][0],
					move_message = 'You crack your way trough this wall.', 
					damage_message = None,
					destroy = 4,
					tile_pos = (0,4),
					transparency = False)
		self.tlist['mine'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Blood moss',
					tile_color = 'red',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'Some blood moss grows on the ground here.', 
					damage_message = None,
					tile_pos = (8,5))
		self.tlist['mine'].append(t)
		techID+=1
	
		self.tlist['global_caves'] = []
	
		t=tile(techID = techID,
					name = 'Cave ground',
					tile_color = 'light_brown',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'A dark cave surrounds you.', 
					damage_message = None,
					tile_pos = (9,0))
		self.tlist['global_caves'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Worn rock',
					tile_color = 'light_grey',
					use_groupe = 'None',
					move_groupe = 'solide',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You crack your way trough worn rocks.', 
					damage_message = None,
					destroy = 2,
					replace = self.tlist['global_caves'][0],
					tile_pos = (0,0),
					transparency = False,
					conected_resources = ('stone',3))
		self.tlist['global_caves'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Soft soil',
					tile_color = 'brown',
					use_groupe = 'None',
					move_groupe = 'solide',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You dig trough soft soil.', 
					damage_message = None,
					destroy = 1,
					replace = self.tlist['global_caves'][0],
					tile_pos = (0,1),
					transparency = False)
		self.tlist['global_caves'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Hard rock',
					tile_color = 'grey',
					use_groupe = 'None',
					move_groupe = 'solide',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You crack your way trough worn rocks.', 
					damage_message = None,
					destroy = 4,
					replace = self.tlist['global_caves'][0],
					tile_pos = (0,10),
					transparency = False,
					conected_resources = ('stone',5))
		self.tlist['global_caves'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Lava',
					tile_color = 'red',
					use_groupe = 'None',
					move_groupe = 'low_liquid',
					grow_groupe = 'None',
					damage = 1, 
					move_message = 'You stand in a hot stream of lava.', 
					damage_message = 'The lava burns your flesh',
					tile_pos = (0,0))
		self.tlist['global_caves'].append(t)
		techID+=1
	
		self.tlist['functional'] = []
	
		t=tile(techID = techID,
					name = 'Border',
					tile_color = 'white',
					use_groupe = 'None',
					move_groupe = 'solide',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'HERE BE DRAGONS', 
					damage_message = None,
					build_here = False,
					tile_pos = (9,1),
					transparency = False)
		self.tlist['functional'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Stair down',
					tile_color = 'white',
					use_groupe = 'stair_down',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'There is a down leading stairway here.', 
					damage_message = None,
					civilisation = True,
					build_here = False,
					tile_pos = (3,4))
		self.tlist['functional'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Stair up',
					tile_color = 'white',
					use_groupe = 'stair_up',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'There is a up leading stairway here.', 
					damage_message = None,
					civilisation = True,
					build_here = False,
					tile_pos = (3,3))
		self.tlist['functional'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Empty chest',
					tile_color = 'white',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'Here is a empty chest.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (5,10))
		self.tlist['functional'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Chest',
					tile_color = 'white',
					use_groupe = 'container',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'Here is a chest.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (6,9))
		self.tlist['functional'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Stack',
					tile_color = 'white',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'Something lies on the ground here.', 
					damage_message = None,
					tile_pos = (3,5))
		self.tlist['functional'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Humanoid remains',
					tile_color = 'white',
					use_groupe = 'loot',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'Here are some humanoid remains.', 
					damage_message = None,
					tile_pos = (3,9))
		self.tlist['functional'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Fontain',
					tile_color = 'blue',
					use_groupe = 'drink',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You stand in front of a fontain.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (6,3))
		self.tlist['functional'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Bed',
					tile_color = 'white',
					use_groupe = 'sleep',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You stand in front of a confortable bed.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (8,6))
		self.tlist['functional'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Carpenter\'s workbench',
					tile_color = 'white',
					use_groupe = 'carpenter',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You stand in front of a carpenter\'s workbench.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (8,2))
		self.tlist['functional'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Carvers\'s workbench',
					tile_color = 'white',
					use_groupe = 'carver',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You stand in front of a carvers\'s workbench.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (8,1))
		self.tlist['functional'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Stonecutter\'s workbench',
					tile_color = 'white',
					use_groupe = 'stonecutter',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You stand in front of a stonecutter\'s workbench.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (3,2))
		self.tlist['functional'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Forger\'s workbench',
					tile_color = 'white',
					use_groupe = 'forger',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You stand in front of a forger\'s workbench.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (8,0))
		self.tlist['functional'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'alchemist\'s workshop',
					tile_color = 'white',
					use_groupe = 'alchemist',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You stand in front of a alchemist\'s workshop.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (8,4))
		self.tlist['functional'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Furnace',
					tile_color = 'white',
					use_groupe = 'furnace',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You stand in front of a furnace.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (5,2))
		self.tlist['functional'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Altar',
					tile_color = 'white',
					use_groupe = 'altar',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You stand in front of a holy altar.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (8,3))
		self.tlist['functional'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Table',
					tile_color = 'white',
					use_groupe = 'None',
					move_groupe = 'solide',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You stand on a table.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (3,1))
		self.tlist['functional'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Wooden seat',
					tile_color = 'white',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'Here is a confortable looking wooden seat.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (3,6))
		self.tlist['functional'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Stone seat',
					tile_color = 'white',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'Here is a confortable looking stone seat.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (3,7))
		self.tlist['functional'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Bookshelf',
					tile_color = 'white',
					use_groupe = 'None',
					move_groupe = 'solide',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'Here is a bookshelf.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (9,2),
					transparency = False)
		self.tlist['functional'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Divine gift',
					tile_color = 'light_purple',
					use_groupe = 'None',
					move_groupe = 'holy',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'The gods blessed this world here.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (6,8))
		self.tlist['functional'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Animal remains',
					tile_color = 'white',
					use_groupe = 'gather',
					move_groupe = 'soil',
					grow_groupe = 'vanish',
					damage = 0, 
					move_message = 'Here lies a piece of raw flesh.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (8,7),
					conected_items = il.ilist['food'][9])
		self.tlist['functional'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Pilar',
					tile_color = 'white',
					use_groupe = 'None',
					move_groupe = 'solide',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You stand in front of a pilar.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (5,9),
					transparency = False)
		self.tlist['functional'].append(t)
		techID+=1
	
		t=tile(techID = techID,
					name = 'Master forge',
					tile_color = 'purple',
					use_groupe = 'masterforge',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You stand in front of a legendary master forge.', 
					damage_message = None,
					tile_pos = (0,6))
		self.tlist['functional'].append(t)
		techID+=1
	
		self.tlist['local'] = []
		#0
		t=tile(techID = techID,
					name = 'Grass',
					tile_color = 'light_green',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You walk over soft grass.', 
					damage_message = None,
					can_grown = True,
					tile_pos = (5,0))
		self.tlist['local'].append(t)
		techID+=1
		#1
		t=tile(techID = techID,
					name = 'Scrub',
					tile_color = 'green',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'scrub',
					damage = 0, 
					move_message = 'There is a scrub here.', 
					damage_message = None,
					tile_pos = (6,1),
					conected_tiles = (('local',4)))
		self.tlist['local'].append(t)
		techID+=1
		#2
		t=tile(techID = techID,
					name = 'Scrub with red berries',
					tile_color = 'red',
					use_groupe = 'gather',
					move_groupe = 'soil',
					grow_groupe = 'scrub_berries',
					damage = 0, 
					move_message = 'There is a scrub with red berries here.', 
					damage_message = None,
					tile_pos = (6,1),
					conected_items = (il.ilist['food'][0]),
					conected_tiles = (('local',5)))
		self.tlist['local'].append(t)
		techID+=1
		#3
		t=tile(techID = techID,
					name = 'Scrub with buds',
					tile_color = 'green',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'scrub_buds',
					damage = 0, 
					move_message = 'There is a scrub with some buds here.', 
					damage_message = None,
					tile_pos = (5,4),
					conected_tiles = (('local',4)))
		self.tlist['local'].append(t)
		techID+=1
		#4
		t=tile(techID = techID,
					name = 'Scrub with blossoms',
					tile_color = 'green',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'scrub_blossom',
					damage = 0, 
					move_message = 'There is a scrub with beautiful blossoms here.', 
					damage_message = None,
					tile_pos = (1,4),
					conected_tiles = (('local',2),('local',18),('local',19)))
		self.tlist['local'].append(t)
		techID+=1
		#5
		t=tile(techID = techID,
					name = 'Scrub with scruffy berries',
					tile_color = 'brown',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'scrub_scruffy',
					damage = 0, 
					move_message = 'There is a scrub with scruffy berries here.', 
					damage_message = None,
					tile_pos = (6,2),
					conected_tiles = (('local',1),('local',9)))
		self.tlist['local'].append(t)
		techID+=1
		#6
		t=tile(techID = techID,
					name = 'Scrub seed',
					tile_color = 'brown',
					use_groupe = 'gather',
					move_groupe = 'soil',
					grow_groupe = 'scrub_seed',
					damage = 0, 
					move_message = 'There are some seeds on the ground here.', 
					damage_message = None,
					tile_pos = (5,3),
					conected_items = (il.ilist['misc'][47]),
					conected_tiles = (('local',7)))
		self.tlist['local'].append(t)
		techID+=1
		#7
		t=tile(techID = techID,
					name = 'Scrub sepling',
					tile_color = 'green',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'scrub_sepling',
					damage = 0, 
					move_message = 'Something starts to grow here.', 
					damage_message = None,
					tile_pos = (5,7),
					conected_tiles = (('local',8)))
		self.tlist['local'].append(t)
		techID+=1
		#8
		t=tile(techID = techID,
					name = 'Small scrub',
					tile_color = 'green',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'small_scrub',
					damage = 0, 
					move_message = 'There is a small scrub at this place.', 
					damage_message = None,
					tile_pos = (1,3),
					conected_tiles = (('local',1)))
		self.tlist['local'].append(t)
		techID+=1
		#9
		t=tile(techID = techID,
					name = 'Dead scrub',
					tile_color = 'brown',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'vanish',
					damage = 0, 
					move_message = 'There is a dead scrub here.', 
					damage_message = None,
					tile_pos = (6,7))
		self.tlist['local'].append(t)
		techID+=1
		#10
		t=tile(techID = techID,
					name = 'Tree sepling',
					tile_color = 'brown',
					use_groupe = 'gather',
					move_groupe = 'soil',
					grow_groupe = 'tree_sepling',
					damage = 0, 
					move_message = 'There is a sepling here.', 
					damage_message = None,
					tile_pos = (4,1),
					conected_items = (il.ilist['misc'][48]),
					conected_tiles = (('local',11)))
		self.tlist['local'].append(t)
		techID+=1
		#11
		t=tile(techID = techID,
					name = 'Tree young',
					tile_color = 'brown',
					use_groupe = 'None',
					move_groupe = 'tree',
					grow_groupe = 'tree_young',
					damage = 0, 
					move_message = 'There is a young tree here.', 
					damage_message = None,
					tile_pos = (4,0),
					conected_tiles = (('local',12)),
					conected_resources = ('wood',1))
		self.tlist['local'].append(t)
		techID+=1
		#12
		t=tile(techID = techID,
					name = 'Tree',
					tile_color = 'brown',
					use_groupe = 'None',
					move_groupe = 'tree',
					grow_groupe = 'tree',
					damage = 0, 
					move_message = 'There is a tree here.', 
					damage_message = None,
					tile_pos = (4,3),
					transparency = False,
					conected_tiles = (('local',10),('local',13)),
					conected_resources = ('wood',5))
		self.tlist['local'].append(t)
		techID+=1
		#13
		t=tile(techID = techID,
					name = 'Tree dead',
					tile_color = 'brown',
					use_groupe = 'None',
					move_groupe = 'tree',
					grow_groupe = 'vanish',
					damage = 0, 
					move_message = 'There is a dead tree here.', 
					damage_message = None,
					tile_pos = (4,2),
					transparency = False,
					conected_resources = ('wood',3))
		self.tlist['local'].append(t)
		techID+=1
		#14
		t=tile(techID = techID,
					name = 'Rock',
					tile_color = 'grey',
					use_groupe = 'None',
					move_groupe = 'solide',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You break a big rock.', 
					damage_message = None,
					destroy = 2,
					tile_pos = (3,8),
					conected_resources = ('stone',1))
		self.tlist['local'].append(t)
		techID+=1
		#15
		t=tile(techID = techID,
					name = 'Herbs',
					tile_color = 'white',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'herblike',
					damage = 0, 
					move_message = 'Herbs grow at the ground.', 
					damage_message = None,
					tile_pos = (1,9),
					conected_tiles = (('local',16)))
		self.tlist['local'].append(t)
		techID+=1
		#16
		t=tile(techID = techID,
					name = 'Flowering herbs',
					tile_color = 'white',
					use_groupe = 'resource',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'Flowering herbs grow at the ground.', 
					damage_message = None,
					tile_pos = (0,9),
					conected_tiles = (('local',15)),
					conected_resources = ('herbs',1))
		self.tlist['local'].append(t)
		techID+=1
		#17
		t=tile(techID = techID,
					name = 'Scrub with blue berries',
					tile_color = 'light_blue',
					use_groupe = 'gather',
					move_groupe = 'soil',
					grow_groupe = 'scrub_berries',
					damage = 0, 
					move_message = 'There is a scrub with blue berries here.', 
					damage_message = None,
					tile_pos = (15),
					conected_items = (il.ilist['food'][27]),
					conected_tiles = (('local',5)))
		self.tlist['local'].append(t)
		techID+=1
		#18
		t=tile(techID = techID,
					name = 'Scrub with yellow berries',
					tile_color = 'yellow',
					use_groupe = 'gather',
					move_groupe = 'soil',
					grow_groupe = 'scrub_berries',
					damage = 0, 
					move_message = 'There is a scrub with yellow berries here.', 
					damage_message = None,
					tile_pos = (4,4),
					conected_items = (il.ilist['food'][28]),
					conected_tiles = (('local',5)))
		self.tlist['local'].append(t)
		techID+=1

		self.tlist['building'] = []
		#0
		t=tile(techID = techID,
					name = 'Floor',
					tile_color = 'light_red',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You walk over a wooden floor.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (7,5))
		self.tlist['building'].append(t)
		techID+=1
		#1
		t=tile(techID = techID,
					name = 'Wall',
					tile_color = 'red',
					use_groupe = 'None',
					move_groupe = 'solide',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'There is a wall here.', 
					damage_message = None,
					civilisation = True,
					transparency = False,
					tile_pos = (2,5))
		self.tlist['building'].append(t)
		techID+=1
		#2
		t=tile(techID = techID,
					name = 'Door open',
					tile_color = 'white',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You walk trough a open door.', 
					damage_message = None,
					civilisation = True,
					build_here = False,
					tile_pos = (7,10))
		self.tlist['building'].append(t)
		techID+=1
		#3
		t=tile(techID = techID,
					name = 'Door closed',
					tile_color = 'white',
					use_groupe = 'None',
					move_groupe = 'solide',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'The door swings open.', 
					damage_message = None,
					destroy = 1,
					replace = self.tlist['building'][2],
					civilisation = True,
					transparency = False,
					tile_pos = (6,6))
		self.tlist['building'].append(t)
		techID+=1
		#4
		t=tile(techID = techID,
					name = 'Agriculture',
					tile_color = 'yellow',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'agri0',
					damage = 0, 
					move_message = 'You are walking on bare fields.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (9,7),
					conected_tiles = (('building',5),('building',6)))
		self.tlist['building'].append(t)
		techID+=1
		#5
		t=tile(techID = techID,
					name = 'Budding agriculture (overworld)',
					tile_color = 'yellow',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'agri1',
					damage = 0, 
					move_message = 'Something starts to grow at this field.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (8,8),
					conected_tiles = (('building',7)))
		self.tlist['building'].append(t)
		techID+=1
		#6
		t=tile(techID = techID,
					name = 'Budding agriculture (caves)',
					tile_color = 'yellow',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'agri1',
					damage = 0, 
					move_message = 'Something starts to grow at this field.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (9,8),
					conected_tiles = (('building',8)))
		self.tlist['building'].append(t)
		techID+=1
		#7
		t=tile(techID = techID,
					name = 'Agriculture crops',
					tile_color = 'yellow',
					use_groupe = 'gather',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'The crops stand high here.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (8,10),
					conected_items = (il.ilist['food'][6]))
		self.tlist['building'].append(t)
		techID+=1
		#8
		t=tile(techID = techID,
					name = 'Agriculture mushroom',
					tile_color = 'yellow',
					use_groupe = 'gather',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'A great mushroom grows at this field.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (8,9),
					conected_items = (il.ilist['food'][11]))
		self.tlist['building'].append(t)
		techID+=1
		#9
		t=tile(techID = techID,
					name = 'Blue floor',
					tile_color = 'light_red',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You walk over a blue floor.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (7,4))
		self.tlist['building'].append(t)
		techID+=1
		#10
		t=tile(techID = techID,
					name = 'Blue wall',
					tile_color = 'red',
					use_groupe = 'None',
					move_groupe = 'solide',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'There is a wall here.', 
					damage_message = None,
					civilisation = True,
					transparency = False,
					tile_pos = (2,4))
		self.tlist['building'].append(t)
		techID+=1
		#11
		t=tile(techID = techID,
					name = 'Green floor',
					tile_color = 'light_red',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You walk over a green floor.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (7,3))
		self.tlist['building'].append(t)
		techID+=1
		#12
		t=tile(techID = techID,
					name = 'Green wall',
					tile_color = 'red',
					use_groupe = 'None',
					move_groupe = 'solide',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'There is a wall here.', 
					damage_message = None,
					civilisation = True,
					transparency = False,
					tile_pos = (2,3))
		self.tlist['building'].append(t)
		techID+=1
		#13
		t=tile(techID = techID,
					name = 'Red floor',
					tile_color = 'light_red',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You walk over a red floor.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (7,0))
		self.tlist['building'].append(t)
		techID+=1
		#14
		t=tile(techID = techID,
					name = 'Red wall',
					tile_color = 'red',
					use_groupe = 'None',
					move_groupe = 'solide',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'There is a wall here.', 
					damage_message = None,
					civilisation = True,
					transparency = False,
					tile_pos = (2,0))
		self.tlist['building'].append(t)
		techID+=1
		#15
		t=tile(techID = techID,
					name = 'Orange floor',
					tile_color = 'light_red',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You walk over a orange floor.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (7,2))
		self.tlist['building'].append(t)
		techID+=1
		#16
		t=tile(techID = techID,
					name = 'Orange wall',
					tile_color = 'red',
					use_groupe = 'None',
					move_groupe = 'solide',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'There is a wall here.', 
					damage_message = None,
					civilisation = True,
					transparency = False,
					tile_pos = (2,2))
		self.tlist['building'].append(t)
		techID+=1
		#17
		t=tile(techID = techID,
					name = 'Purple floor',
					tile_color = 'light_red',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You walk over a purple floor.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (7,1))
		self.tlist['building'].append(t)
		techID+=1
		#18
		t=tile(techID = techID,
					name = 'Purple wall',
					tile_color = 'red',
					use_groupe = 'None',
					move_groupe = 'solide',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'There is a wall here.', 
					damage_message = None,
					civilisation = True,
					transparency = False,
					tile_pos = (2,1))
		self.tlist['building'].append(t)
		techID+=1
		#19
		t=tile(techID = techID,
					name = 'Orcish floor',
					tile_color = 'light_red',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You walk over a hard soil.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (0,5))
		self.tlist['building'].append(t)
		techID+=1
		#20
		t=tile(techID = techID,
					name = 'Orcish wall',
					tile_color = 'red',
					use_groupe = 'None',
					move_groupe = 'solide',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'There is a wall here.', 
					damage_message = None,
					civilisation = True,
					transparency = False,
					tile_pos = (0,4))
		self.tlist['building'].append(t)
		techID+=1
		#21
		t=tile(techID = techID,
					name = 'Noble floor',
					tile_color = 'light_red',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You walk over a floor made of stone.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (0,3))
		self.tlist['building'].append(t)
		techID+=1
		#22
		t=tile(techID = techID,
					name = 'Noble wall',
					tile_color = 'red',
					use_groupe = 'None',
					move_groupe = 'solide',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'There is a wall here.', 
					damage_message = None,
					civilisation = True,
					transparency = False,
					tile_pos = (2,6))
		self.tlist['building'].append(t)
		techID+1
		#23
		t=tile(techID = techID,
					name = 'Elfish floor',
					tile_color = 'light_red',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You walk over cobbled floor.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (7,8))
		self.tlist['building'].append(t)
		techID+=1
		#22
		t=tile(techID = techID,
					name = 'Elfish wall',
					tile_color = 'red',
					use_groupe = 'None',
					move_groupe = 'solide',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'There is a wall here.', 
					damage_message = None,
					civilisation = True,
					transparency = False,
					tile_pos = (7,6))
		self.tlist['building'].append(t)
		techID+1

		self.tlist['help'] = []
		#0
		t=tile(techID = techID,
					name = 'scrub_here',
					tile_color = 'light_red',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You walk over a wooden floor.', 
					damage_message = None,
					civilisation = True,
					tile_pos = (7,5))
		self.tlist['help'].append(t)
		techID+=1
		#1
		t=tile(techID = techID,
					name = 'tree_here',
					tile_color = 'red',
					use_groupe = 'None',
					move_groupe = 'solide',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'There is a wall here.', 
					damage_message = None,
					civilisation = True,
					transparency = False,
					tile_pos = (0,0))
		self.tlist['help'].append(t)
		techID+=1
		#2
		t=tile(techID = techID,
					name = 'water_here',
					tile_color = 'white',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You walk trough a open door.', 
					damage_message = None,
					civilisation = True,
					build_here = False,
					tile_pos = (0,0))
		self.tlist['help'].append(t)
		techID+=1
	
		self.tlist['sanctuary'] = []
		#0
		t=tile(techID = techID,
					name = 'Sanctuary floor',
					tile_color = 'light_purple',
					use_groupe = 'None',
					move_groupe = 'holy',
					grow_groupe = 'None',
					damage = -1, 
					move_message = 'You walk over holy ground.', 
					damage_message = 'Your wounds are cured.',
					build_here = False,
					tile_pos = (4,10))
		self.tlist['sanctuary'].append(t)
		techID+=1
		#1
		t=tile(techID = techID,
					name = 'Wall',
					tile_color = 'purple',
					use_groupe = 'None',
					move_groupe = 'solide',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'There is a pilar here.', 
					damage_message = None,
					build_here = False,
					transparency = False,
					tile_pos = (4,9))
		self.tlist['sanctuary'].append(t)
		techID+=1
		#2
		t=tile(techID = techID,
					name = 'Sanctuary spawnpoint',
					tile_color = 'light_red',
					use_groupe = 'None',
					move_groupe = 'holy',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You walk over holy ground.', 
					damage_message = 'Your wounds are cured.',
					build_here = False,
					tile_pos = (2,10))
		self.tlist['sanctuary'].append(t)
		techID+=1
	
		self.tlist['shop'] = []
		#0
		t=tile(techID = techID,
					name = 'Shop floor',
					tile_color = 'light_purple',
					use_groupe = 'None',
					move_groupe = 'shop',
					grow_groupe = 'None',
					damage = 0,
					move_message = 'You are inside a shop.', 
					damage_message = None,
					build_here = False,
					tile_pos = (0,3))
		self.tlist['shop'].append(t)
		techID+=1
		#1
		t=tile(techID = techID,
					name = 'Shop wall',
					tile_color = 'purple',
					use_groupe = 'None',
					move_groupe = 'solide',
					grow_groupe = 'None',
					damage = 0,
					move_message = 'You are inside a shop.', 
					damage_message = None,
					build_here = False,
					transparency = False,
					tile_pos = (2,6))
		self.tlist['shop'].append(t)
		techID+=1
		#3
		t=tile(techID = techID,
					name = 'Shop door',
					tile_color = 'white',
					use_groupe = 'None',
					move_groupe = 'shop',
					grow_groupe = 'None',
					damage = 0,
					move_message = 'You are entering a shop.', 
					damage_message = None,
					build_here = False,
					tile_pos = (7,10))
		self.tlist['shop'].append(t)
		techID+=1
	
	#effect tiles

		self.tlist['effect'] = []
		#0
		t=tile(techID = techID,
					name = 'Bomb3',
					tile_color = 'red',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'The time is ticking.', 
					damage_message = 'None',
					build_here = False,
					tile_pos = (9,3))
		self.tlist['effect'].append(t)
		techID+=1
		#1
		t=tile(techID = techID,
					name = 'Bomb2',
					tile_color = 'red',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'The time is ticking.', 
					damage_message = 'None',
					build_here = False,
					tile_pos = (9,4))
		self.tlist['effect'].append(t)
		techID+=1
		#2
		t=tile(techID = techID,
					name = 'Bomb1',
					tile_color = 'red',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'The time is ticking.', 
					damage_message = 'None',
					build_here = False,
					tile_pos = (9,5))
		self.tlist['effect'].append(t)
		techID+=1
		#3
		t=tile(techID = techID,
					name = 'Boom',
					tile_color = 'light_red',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 10, 
					move_message = 'BOOM', 
					damage_message = 'BOOM',
					build_here = False,
					tile_pos = (9,6))
		self.tlist['effect'].append(t)
		techID+=1
		#4
		t=tile(techID = techID,
					name = 'Flame',
					tile_color = 'light_red',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 1, 
					move_message = 'The fire burns your flesh.', 
					damage_message = 'The fire burns your flesh.',
					build_here = False,
					tile_pos = (6,5))
		self.tlist['effect'].append(t)
		techID+=1
		#5
		t=tile(techID = techID,
					name = 'Healing Aura',
					tile_color = 'light_blue',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = -1, 
					move_message = 'A healing aura surrounds you.', 
					damage_message = 'Your wounds are cured.',
					build_here = False,
					tile_pos = (1,10))
		self.tlist['effect'].append(t)
		techID+=1

		#elfish tiles
	
		self.tlist['elfish'] = []
		#0
		t=tile(techID = techID,
					name = 'Elfish floor indoor',
					tile_color = 'light_purple',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You walk over a cobbled floor.', 
					damage_message = None,
					tile_pos = (7,8))
		self.tlist['elfish'].append(t)
		techID+=1
		#1
		t=tile(techID = techID,
					name = 'Elfish floor outdoor',
					tile_color = 'light_purple',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'You walk over gritty floor.', 
					damage_message = None,
					tile_pos = (7,7))
		self.tlist['elfish'].append(t)
		techID+=1
		#2
		t=tile(techID = techID,
					name = 'Elfish agriculture',
					tile_color = 'light_green',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'Some strange plants grow at this field.', 
					damage_message = None,
					tile_pos = (7,9),
					conected_tiles = (('elfish',6)),
					conected_resources = ('seeds',1))
		self.tlist['elfish'].append(t)
		techID+=1
		#3
		t=tile(techID = techID,
					name = 'Elfish wall',
					tile_color = 'purple',
					use_groupe = 'None',
					move_groupe = 'solide',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'There is a wall here.', 
					damage_message = None,
					build_here = False,
					transparency = False,
					tile_pos = (7,6))
		self.tlist['elfish'].append(t)
		techID+=1
		#4
		t=tile(techID = techID,
					name = 'help_active',
					tile_color = 'black',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'ACTIVE', 
					damage_message = None,
					build_here = False,
					transparency = False,
					tile_pos = (0,0))
		self.tlist['elfish'].append(t)
		techID+=1
		#5
		t=tile(techID = techID,
					name = 'help_passive',
					tile_color = 'black',
					use_groupe = 'None',
					move_groupe = 'soil',
					grow_groupe = 'None',
					damage = 0, 
					move_message = 'PASSIVE', 
					damage_message = None,
					build_here = False,
					transparency = False,
					tile_pos = (0,0))
		self.tlist['elfish'].append(t)
		techID+=1
		#6
		t=tile(techID = techID,
					name = 'Elfish agriculture',
					tile_color = 'light_green',
					use_groupe = 'resource',
					move_groupe = 'soil',
					grow_groupe = 'herblike',
					damage = 0,
					move_message = 'You are walking on bare fields.', 
					damage_message = None,
					tile_pos = (9,7),
					conected_tiles = (('elfish',2)))
		self.tlist['elfish'].append(t)
		techID+=1
