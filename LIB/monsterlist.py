from monster import monster
from attribute import attribute


class monsterlist():
	
	def __init__(self):
		self.mlist = {}
		techID = 0

		#grassland monster
		self.mlist['overworld'] = []
		
		m=monster(techID = techID,
				name = 'dryade',
				sprite_pos = (2,2),
				move_border = 2,
				attribute_prev = (0,1,2,2,1),
				worn_equipment = (0,1,0,0,0),
				AI_style = 'ignore',
				corps_style = 'dryade',
				corps_lvl = 1,
				personal_id = 'None',
				move_groups = ('soil','soil'), 
				behavior = 'talk', 
				attack_were = ('Feet'),
				possible_effect = None, 
				effect_duration = 0, 
				effect_probability = 0, 
				message = 'The dryade smiles mysterious.',
				anger = 'tree',
				anger_monster = 2)
		techID+=1
		self.mlist['overworld'].append(m)

		m=monster(techID = techID,
				name = 'grassland snake',
				sprite_pos = (0,9),
				move_border = 1,
				attribute_prev = (2,1,0,0,0),
				worn_equipment = (0,0,0,0,0),
				AI_style = 'hostile',
				corps_style = 'animal',
				corps_lvl = 1,
				personal_id = 'None',
				move_groups = ('soil','soil'), 
				behavior = 'attack_melee', 
				attack_were = ('Legs','Feet'),
				possible_effect = 'poisoned', 
				effect_duration = 20, 
				effect_probability = 20, 
				message = 'Poison runs trough your veins!',
				def_flee = 0)
		techID+=1
		self.mlist['overworld'].append(m)

		m=monster(techID = techID,
				name = 'rabbit',
				sprite_pos = (1,4),
				move_border = 0,
				attribute_prev = (0,1,0,1,1),
				worn_equipment = (0,0,0,0,0),
				AI_style = 'flee',
				corps_style = 'animal',
				corps_lvl = 1,
				personal_id = 'None',
				move_groups = ('soil','soil'), 
				behavior = 'attack_melee', 
				attack_were = ('Feet'),
				possible_effect = None, 
				effect_duration = 0, 
				effect_probability = 0, 
				message = 'None')
		techID+=1
		self.mlist['overworld'].append(m)

		m=monster(techID = techID,
				name = 'green blob',
				sprite_pos = (1,8),
				move_border = 4,
				attribute_prev = (2,2,0,1,1),
				worn_equipment = (0,0,0,0,0),
				AI_style = 'hostile',
				corps_style = 'vanish',
				corps_lvl = 5,
				personal_id = 'None',
				move_groups = ('soil','soil'), 
				behavior = 'attack_melee', 
				attack_were = ('Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0, 
				effect_probability = 0, 
				message = 'None')
		techID+=1
		self.mlist['overworld'].append(m)

		m=monster(techID = techID,
				name = 'hill orc',
				sprite_pos = (1,7),
				move_border = 2,
				attribute_prev = (3,0,0,1,1),
				worn_equipment = (1,0,1,0,0),
				AI_style = 'hostile',
				corps_style = 'human',
				corps_lvl = 2,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'attack_melee', 
				attack_were = ('Head','Body','Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0, 
				effect_probability = 0, 
				message = 'None',
				def_potion = 0)#set to 20
		techID+=1
		self.mlist['overworld'].append(m)

		#civilians
		self.mlist['civilian'] = []
		
		m=monster(techID = techID,
				name = 'dryade',
				sprite_pos = (2,2),
				move_border = 2,
				attribute_prev = (0,1,2,2,1),
				worn_equipment = (0,1,0,0,0),
				AI_style = 'ignore',
				corps_style = 'dryade',
				corps_lvl = 1,
				personal_id = 'None',
				move_groups = ('soil','soil'), 
				behavior = 'talk', 
				attack_were = ('Feet'),
				possible_effect = None, 
				effect_duration = 0, 
				effect_probability = 0, 
				message = 'The dryade smiles mysterious.')
		techID+=1
		self.mlist['civilian'].append(m)

		m=monster(techID = techID,
				name = 'tame orc',
				sprite_pos = (0,4),
				move_border = 2,
				attribute_prev = (2,1,0,1,1),
				worn_equipment = (1,0,1,0,0),
				AI_style = 'ignore',
				corps_style = 'human',
				corps_lvl = 1,
				personal_id = 'None',
				move_groups = ('soil','soil'), 
				behavior = 'talk', 
				attack_were = ('Feet'),
				possible_effect = None, 
				effect_duration = 0, 
				effect_probability = 0, 
				message = 'The tame orc geets you.')
		techID+=1
		self.mlist['civilian'].append(m)

		m=monster(techID = techID,
				name = 'golden naga',
				sprite_pos = (1,9),
				move_border = 2,
				attribute_prev = (0,1,2,2,1),
				worn_equipment = (0,1,0,1,1),
				AI_style = 'ignore',
				corps_style = 'human',
				corps_lvl = 1,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'talk', 
				attack_were = ('Feet'),
				possible_effect = None, 
				effect_duration = 0, 
				effect_probability = 0, 
				message = 'The golden naga blinks.')
		techID+=1
		self.mlist['civilian'].append(m)

		m=monster(techID = techID,
				name = 'wood elf',
				sprite_pos = (0,0),
				move_border = 2,
				attribute_prev = (0,2,0,2,1),
				worn_equipment = (1,1,1,1,1),
				AI_style = 'ignore',
				corps_style = 'human',
				corps_lvl = 1,
				personal_id = 'None',
				move_groups = ('soil','soil'), 
				behavior = 'talk', 
				attack_were = ('Feet'),
				possible_effect = None, 
				effect_duration = 0, 
				effect_probability = 0, 
				message = 'The wood elf waves.')
		techID+=1
		self.mlist['civilian'].append(m)

		#cave

		self.mlist['cave'] = []
		
		m=monster(techID = techID,
				name = 'cave orc',
				sprite_pos = (2,3),
				move_border = 2,
				attribute_prev = (2,2,0,1,2),
				worn_equipment = (1,0,1,0,0),
				AI_style = 'hostile',
				corps_style = 'human',
				corps_lvl = 1,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'attack_melee', 
				attack_were = ('Head','Body','Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0, 
				effect_probability = 0, 
				message = 'None.')
		techID+=1
		self.mlist['cave'].append(m)

		m=monster(techID = techID,
				name = 'blue blob',
				sprite_pos = (2,5),
				move_border = 4,
				attribute_prev = (2,1,0,0,1),
				worn_equipment = (0,0,0,0,0),
				AI_style = 'hostile',
				corps_style = 'vanish',
				corps_lvl = 1,
				personal_id = 'None',
				move_groups = ('soil','soil'), 
				behavior = 'attack_melee', 
				attack_were = ('Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0, 
				effect_probability = 0, 
				message = 'None.')
		techID+=1
		self.mlist['cave'].append(m)

		m=monster(techID = techID,
				name = 'bat',
				sprite_pos = (2,7),
				move_border = 0,
				attribute_prev = (0,2,0,2,2),
				worn_equipment = (0,0,0,0,0),
				AI_style = 'flee',
				corps_style = 'animal',
				corps_lvl = 1,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'attack_melee', 
				attack_were = ('Head','Body','Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0, 
				effect_probability = 0, 
				message = 'None.')
		techID+=1
		self.mlist['cave'].append(m)

		m=monster(techID = techID,
				name = 'soil spirit',
				sprite_pos = (1,0),
				move_border = 2,
				attribute_prev = (0,1,2,1,1),
				worn_equipment = (0,1,0,0,0),
				AI_style = 'hostile',
				corps_style = 'troll',
				corps_lvl = 1,
				personal_id = 'None',
				move_groups = ('soil','soil'), 
				behavior = 'attack_magic', 
				attack_were = ('Head','Body','Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0, 
				effect_probability = 0, 
				message = 'None.')
		techID+=1
		self.mlist['cave'].append(m)

		#mine

		self.mlist['orcish_mines'] = []
		
		m=monster(techID = techID,
				name = 'orc warlord',
				sprite_pos = (1,5),
				move_border = 2,
				attribute_prev = (2,2,0,1,2),
				worn_equipment = (1,0,1,0,1),
				AI_style = 'hostile',
				corps_style = 'human',
				corps_lvl = 1,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'attack_melee', 
				attack_were = ('Head','Body','Legs'),
				possible_effect = 'bleeding', 
				effect_duration = 5, 
				effect_probability = 20, 
				message = 'The orc warlord tears you a bleeding wound.')
		techID+=1
		self.mlist['orcish_mines'].append(m)

		m=monster(techID = techID,
				name = 'orc warlord',
				sprite_pos = (1,5),
				move_border = 2,
				attribute_prev = (2,2,0,1,2),
				worn_equipment = (1,0,1,0,1),
				AI_style = 'hostile',
				corps_style = 'human',
				corps_lvl = 3,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'attack_melee', 
				attack_were = ('Head','Body','Legs'),
				possible_effect = 'bleeding', 
				effect_duration = 5, 
				effect_probability = 20, 
				message = 'The orc warlord tears you a bleeding wound.')
		techID+=1
		self.mlist['orcish_mines'].append(m)

		m=monster(techID = techID,
				name = 'orcish hag',
				sprite_pos = (0,6),
				move_border = 2,
				attribute_prev = (0,1,2,2,2),
				worn_equipment = (0,1,0,1,1),
				AI_style = 'hostile',
				corps_style = 'scrollkeeper',
				corps_lvl = 2,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'attack_magic', 
				attack_were = ('Head','Body','Legs','Feet'),
				possible_effect = 'hexed', 
				effect_duration = 40, 
				effect_probability = 20, 
				message = 'The orcish hag puts a hex on you.')
		techID+=1
		self.mlist['orcish_mines'].append(m)

		m=monster(techID = techID,
				name = 'orcish digger',
				sprite_pos = (1,6),
				move_border = 2,
				attribute_prev = (1,2,0,1,1),
				worn_equipment = (0,0,0,0,0),
				AI_style = 'hostile',
				corps_style = 'miner',
				corps_lvl = 2,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'attack_melee', 
				attack_were = ('Head','Body','Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0, 
				effect_probability = 0, 
				message = 'None')
		techID+=1
		self.mlist['orcish_mines'].append(m)

		m=monster(techID = techID,
				name = 'blood snake',
				sprite_pos = (2,6),
				move_border = 2,
				attribute_prev = (2,2,0,0,1),
				worn_equipment = (0,0,0,0,0),
				AI_style = 'hostile',
				corps_style = 'animal',
				corps_lvl = 2,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'attack_melee', 
				attack_were = ('Legs','Feet'),
				possible_effect = 'poisoned', 
				effect_duration = 60,
				effect_probability = 45,
				message = 'Poison runs trough your veins!')
		techID+=1
		self.mlist['orcish_mines'].append(m)
		
		#elfish fortress

		self.mlist['elfish_fortress'] = []
		
		m=monster(techID = techID,
				name = 'male elf',
				sprite_pos = (2,0),
				move_border = 0,
				attribute_prev = (2,2,0,0,2),
				worn_equipment = (1,0,1,0,0),
				AI_style = 'ignore',
				corps_style = 'human',
				corps_lvl = 3,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'talk', 
				attack_were = ('Head','Body','Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0, 
				effect_probability = 0, 
				message = 'The male elf greets you friendly.',
				anger = 'kill',
				anger_monster = 0)
		techID+=1
		self.mlist['elfish_fortress'].append(m)

		m=monster(techID = techID,
				name = 'female elf',
				sprite_pos = (2,1),
				move_border = 0,
				attribute_prev = (0,0,2,2,2),
				worn_equipment = (0,1,0,1,1),
				AI_style = 'ignore',
				corps_style = 'human',
				corps_lvl = 3,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'talk', 
				attack_were = ('Head','Body','Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0, 
				effect_probability = 0, 
				message = 'The female elf greets you friendly.',
				anger = 'kill',
				anger_monster = 1)
		techID+=1
		self.mlist['elfish_fortress'].append(m)
		
		#angry_monsters
		
		self.mlist['angry_monster'] = []
		#0		
		m=monster(techID = techID,
				name = 'male elf',
				sprite_pos = (2,0),
				move_border = 0,
				attribute_prev = (2,2,0,1,2),
				worn_equipment = (1,0,1,0,0),
				AI_style = 'hostile',
				corps_style = 'human',
				corps_lvl = 3,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'attack_melee', 
				attack_were = ('Head','Body','Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0, 
				effect_probability = 0, 
				message = 'None')
		techID+=1
		self.mlist['angry_monster'].append(m)
		#1
		m=monster(techID = techID,
				name = 'female elf',
				sprite_pos = (2,1),
				move_border = 0,
				attribute_prev = (0,1,2,2,2),
				worn_equipment = (0,1,0,1,1),
				AI_style = 'hostile',
				corps_style = 'human',
				corps_lvl = 3,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'attack_magic', 
				attack_were = ('Head','Body','Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0, 
				effect_probability = 0, 
				message = 'None')
		techID+=1
		self.mlist['angry_monster'].append(m)
		#2
		m=monster(techID = techID,
				name = 'angry dryade',
				sprite_pos = (2,8),
				move_border = 2,
				attribute_prev = (0,1,2,2,1),
				worn_equipment = (0,1,0,0,0),
				AI_style = 'hostile',
				corps_style = 'dryade',
				corps_lvl = 1,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'attack_magic', 
				attack_were = ('Head','Body','Legs'),
				possible_effect = None, 
				effect_duration = 0, 
				effect_probability = 0, 
				message = 'None',
				def_teleport = 0)#set to 10
		techID+=1
		self.mlist['angry_monster'].append(m)
		#3
		m=monster(techID = techID,
				name = 'male neko',
				sprite_pos = (2,10),
				move_border = 0,
				attribute_prev = (2,2,0,1,2),
				worn_equipment = (1,0,1,0,0),
				AI_style = 'hostile',
				corps_style = 'human',
				corps_lvl = 3,
				personal_id = 'None',
				move_groups = ('soil','low_liquid','house'), 
				behavior = 'attack_melee', 
				attack_were = ('Head','Body','Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0, 
				effect_probability = 0, 
				message = 'None')
		techID+=1
		self.mlist['angry_monster'].append(m)
		#4
		m=monster(techID = techID,
				name = 'female female',
				sprite_pos = (2,9),
				move_border = 0,
				attribute_prev = (0,1,2,2,2),
				worn_equipment = (0,1,0,1,1),
				AI_style = 'hostile',
				corps_style = 'human',
				corps_lvl = 3,
				personal_id = 'None',
				move_groups = ('soil','low_liquid','house'), 
				behavior = 'attack_magic', 
				attack_were = ('Head','Body','Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0, 
				effect_probability = 0, 
				message = 'None')
		techID+=1
		self.mlist['angry_monster'].append(m)
		
		#grot

		self.mlist['grot'] = []
		
		m=monster(techID = techID,
				name = 'blue naga',
				sprite_pos = (2,4),
				move_border = 3,
				attribute_prev = (0,1,2,2,2),
				worn_equipment = (0,1,0,1,1),
				AI_style = 'hostile',
				corps_style = 'scrollkeeper',
				corps_lvl = 2,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'attack_magic', 
				attack_were = ('Head'),
				possible_effect = 'hexed', 
				effect_duration = 30,
				effect_probability = 50,
				message = 'The blue naga puts a hex on you.')
		techID+=1
		self.mlist['grot'].append(m)

		m=monster(techID = techID,
				name = 'red naga',
				sprite_pos = (1,2),
				move_border = 3,
				attribute_prev = (2,2,0,1,2),
				worn_equipment = (1,0,0,1,1),
				AI_style = 'hostile',
				corps_style = 'human',
				corps_lvl = 1,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'attack_melee', 
				attack_were = ('Head','Body','Legs','Feet'),
				possible_effect = 'poisoned', 
				effect_duration = 50,
				effect_probability = 40,
				message = 'Poison runs trough your veins!')
		techID+=1
		self.mlist['grot'].append(m)

		m=monster(techID = techID,
				name = 'purple blob',
				sprite_pos = (0,5),
				move_border = 4,
				attribute_prev = (2,2,0,0,1),
				worn_equipment = (0,0,0,0,0),
				AI_style = 'hostile',
				corps_style = 'vanish',
				corps_lvl = 5,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'attack_melee', 
				attack_were = ('Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0,
				effect_probability = 0,
				message = 'None')
		techID+=1
		self.mlist['grot'].append(m)

		m=monster(techID = techID,
				name = 'water spirit',
				sprite_pos = (0,1),
				move_border = 2,
				attribute_prev = (2,2,0,1,1),
				worn_equipment = (1,0,0,0,0),
				AI_style = 'hostile',
				corps_style = 'vanish',
				corps_lvl = 3,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'attack_melee', 
				attack_were = ('Head','Body','Legs','Feet'),
				possible_effect = 'confused', 
				effect_duration = 60,
				effect_probability = 20,
				message = 'The water sprit confuses you.')
		techID+=1
		self.mlist['grot'].append(m)
		
		#lava cave

		self.mlist['lava_cave'] = []
				
		m=monster(techID = techID,
				name = 'lava monster',
				sprite_pos = (0,8),
				move_border = 2,
				attribute_prev = (2,2,0,2,2),
				worn_equipment = (1,0,0,0,0),
				AI_style = 'hostile',
				corps_style = 'vanish',
				corps_lvl = 2,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'attack_melee', 
				attack_were = ('Body','Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0,
				effect_probability = 0,
				message = 'None')
		techID+=1
		self.mlist['lava_cave'].append(m)

		m=monster(techID = techID,
				name = 'flame spirit',
				sprite_pos = (0,10),
				move_border = 0,
				attribute_prev = (0,0,2,2,2),
				worn_equipment = (0,0,0,0,0),
				AI_style = 'hostile',
				corps_style = 'vanish',
				corps_lvl = 2,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'attack_magic', 
				attack_were = ('Body','Legs','Feet'),
				possible_effect = 'immobilized', 
				effect_duration = 4,
				effect_probability = 30,
				message = 'You can\'t move!')
		techID+=1
		self.mlist['lava_cave'].append(m)

		m=monster(techID = techID,
				name = 'red blob',
				sprite_pos = (1,3),
				move_border = 4,
				attribute_prev = (2,2,0,0,2),
				worn_equipment = (0,0,0,0,0),
				AI_style = 'hostile',
				corps_style = 'vanish',
				corps_lvl = 5,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'attack_melee', 
				attack_were = ('Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0,
				effect_probability = 0,
				message = 'None')
		techID+=1
		self.mlist['lava_cave'].append(m)

		m=monster(techID = techID,
				name = 'fire bat',
				sprite_pos = (1,10),
				move_border = 0,
				attribute_prev = (2,2,0,0,2),
				worn_equipment = (0,0,0,0,0),
				AI_style = 'hostile',
				corps_style = 'vanish',
				corps_lvl = 2,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'attack_melee', 
				attack_were = ('Head','Body'),
				possible_effect = 'confused', 
				effect_duration = 40,
				effect_probability = 30,
				message = 'The bat\'s screen make you confused!')
		techID+=1
		self.mlist['lava_cave'].append(m)
		
		#special

		self.mlist['special'] = []
		#0
		m=monster(techID = techID,
				name = 'vase',
				sprite_pos = (0,3),
				move_border = 10,
				attribute_prev = (2,0,2,0,0),
				worn_equipment = (0,0,0,0,0),
				AI_style = 'flee',
				corps_style = 'miner',
				corps_lvl = 5,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'attack_melee', 
				attack_were = ('Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0,
				effect_probability = 0,
				message = 'None')
		techID+=1
		self.mlist['special'].append(m)
		#1
		m=monster(techID = techID,
				name = 'monster vase',
				sprite_pos = (0,3),
				move_border = 10,
				attribute_prev = (2,0,2,0,0),
				worn_equipment = (0,0,0,0,0),
				AI_style = 'flee',
				corps_style = 'vase',
				corps_lvl = 5,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'attack_melee', 
				attack_were = ('Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0,
				effect_probability = 0,
				message = 'None')
		techID+=1
		self.mlist['special'].append(m)
		#2
		m=monster(techID = techID,
				name = 'vase monster',
				sprite_pos = (0,2),
				move_border = 1,
				attribute_prev = (2,2,2,2,2),
				worn_equipment = (0,0,0,0,0),
				AI_style = 'hostile',
				corps_style = 'miner',
				corps_lvl = 5,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'attack_random', 
				attack_were = ('Body','Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0,
				effect_probability = 0,
				message = 'None')
		techID+=1
		self.mlist['special'].append(m)
		#3
		m=monster(techID = techID,
				name = 'sleeping mimic',
				sprite_pos = (1,1),
				move_border = 10,
				attribute_prev = (2,0,2,0,0),
				worn_equipment = (0,0,0,0,0),
				AI_style = 'flee',
				corps_style = 'mimic',
				corps_lvl = 5,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'attack_melee', 
				attack_were = ('Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0,
				effect_probability = 0,
				message = 'None')
		techID+=1
		self.mlist['special'].append(m)
		#4
		m=monster(techID = techID,
				name = 'mimic',
				sprite_pos = (0,7),
				move_border = 4,
				attribute_prev = (2,2,2,2,2),
				worn_equipment = (0,0,0,0,0),
				AI_style = 'hostile',
				corps_style = 'vanish',
				corps_lvl = 99,
				personal_id = 'None',
				move_groups = ('soil','low_liquid'), 
				behavior = 'attack_random', 
				attack_were = ('Head','Body','Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0,
				effect_probability = 0,
				message = 'None')
		techID+=1
		self.mlist['special'].append(m)
		#5
		m=monster(techID = techID,
				name = 'female neko',
				sprite_pos = (2,9),
				move_border = 0,
				attribute_prev = (2,2,2,2,2),
				worn_equipment = (1,1,1,1,1),
				AI_style = 'ignore',
				corps_style = 'vanish',
				corps_lvl = 5,
				personal_id = 'None',
				move_groups = ('house','house'), 
				behavior = 'talk', 
				attack_were = ('Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0,
				effect_probability = 0,
				message = 'The female neko blinks feiendly.',
				anger = 'kill_neko',
				anger_monster = 4)
		techID+=1
		self.mlist['special'].append(m)
		#6
		m=monster(techID = techID,
				name = 'male neko',
				sprite_pos = (2,10),
				move_border = 0,
				attribute_prev = (2,2,2,2,2),
				worn_equipment = (1,1,1,1,1),
				AI_style = 'ignore',
				corps_style = 'vanish',
				corps_lvl = 5,
				personal_id = 'None',
				move_groups = ('house','house'), 
				behavior = 'talk', 
				attack_were = ('Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0,
				effect_probability = 0,
				message = 'The male neko blinks friendly.',
				anger = 'kill_neko',
				anger_monster = 3)
		techID+=1
		self.mlist['special'].append(m)
		
		#shop
		
		self.mlist['shop'] = []
		#0
		m=monster(techID = techID,
				name = 'elfish shopkeeper',
				sprite_pos = (3,2),
				move_border = 0,
				attribute_prev = (2,2,2,2,2),
				worn_equipment = (1,1,1,1,1),
				AI_style = 'ignore',
				corps_style = 'vanish',
				corps_lvl = 5,
				personal_id = 'None',
				move_groups = ('shop','shop'), 
				behavior = 'talk', 
				attack_were = ('Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0,
				effect_probability = 0,
				message = 'The shopkeeper greets you.')
		techID+=1
		self.mlist['shop'].append(m)
		#1
		m=monster(techID = techID,
				name = 'orcish shopkeeper',
				sprite_pos = (3,0),
				move_border = 0,
				attribute_prev = (2,2,2,2,2),
				worn_equipment = (1,1,1,1,1),
				AI_style = 'ignore',
				corps_style = 'vanish',
				corps_lvl = 5,
				personal_id = 'None',
				move_groups = ('shop','shop'), 
				behavior = 'talk', 
				attack_were = ('Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0,
				effect_probability = 0,
				message = 'The shopkeeper greets you.')
		techID+=1
		self.mlist['shop'].append(m)
		#2
		m=monster(techID = techID,
				name = 'naga shopkeeper',
				sprite_pos = (3,1),
				move_border = 0,
				attribute_prev = (2,2,2,2,2),
				worn_equipment = (1,1,1,1,1),
				AI_style = 'ignore',
				corps_style = 'vanish',
				corps_lvl = 5,
				personal_id = 'None',
				move_groups = ('shop','shop'), 
				behavior = 'talk', 
				attack_were = ('Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0,
				effect_probability = 0,
				message = 'The shopkeeper greets you.')
		techID+=1
		self.mlist['shop'].append(m)
		
		#desert monster
		self.mlist['desert'] = []
		#0
		m=monster(techID = techID,
				name = 'desert snake',
				sprite_pos = (3,3),
				move_border = 4,
				attribute_prev = (3,1,0,0,2),
				worn_equipment = (0,0,0,0,0),
				AI_style = 'hostile',
				corps_style = 'animal',
				corps_lvl = 1,
				personal_id = 'None',
				move_groups = ('soil','soil'), 
				behavior = 'attack_melee', 
				attack_were = ('Legs','Feet'),
				possible_effect = 'poisoned', 
				effect_duration = 240, 
				effect_probability = 80, 
				message = 'Poison runs trough your veins!')
		techID+=1
		self.mlist['desert'].append(m)
		#1
		m=monster(techID = techID,
				name = 'yellow blob',
				sprite_pos = (3,4),
				move_border = 4,
				attribute_prev = (2,2,0,1,1),
				worn_equipment = (0,0,0,0,0),
				AI_style = 'hostile',
				corps_style = 'vanish',
				corps_lvl = 5,
				personal_id = 'None',
				move_groups = ('soil','soil'), 
				behavior = 'attack_melee', 
				attack_were = ('Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0, 
				effect_probability = 0, 
				message = 'None')
		techID+=1
		self.mlist['desert'].append(m)
		#2
		m=monster(techID = techID,
				name = 'scarab',
				sprite_pos = (3,5),
				move_border = 2,
				attribute_prev = (2,2,0,2,2),
				worn_equipment = (0,0,0,0,0),
				AI_style = 'hostile',
				corps_style = 'vanish',
				corps_lvl = 5,
				personal_id = 'None',
				move_groups = ('soil','soil'), 
				behavior = 'attack_melee', 
				attack_were = ('Legs','Feet'),
				possible_effect = None, 
				effect_duration = 0, 
				effect_probability = 0, 
				message = 'None')
		techID+=1
		self.mlist['desert'].append(m)
		#3
		m=monster(techID = techID,
				name = 'lizard',
				sprite_pos = (3,6),
				move_border = 0,
				attribute_prev = (0,1,0,1,1),
				worn_equipment = (0,0,0,0,0),
				AI_style = 'flee',
				corps_style = 'animal',
				corps_lvl = 1,
				personal_id = 'None',
				move_groups = ('soil','soil'), 
				behavior = 'attack_melee', 
				attack_were = ('Feet'),
				possible_effect = None, 
				effect_duration = 0, 
				effect_probability = 0, 
				message = 'None')
		techID+=1
		self.mlist['desert'].append(m)
