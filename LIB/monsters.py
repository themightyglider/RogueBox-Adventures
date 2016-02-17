from monster import monster
from attribute import attribute
import pickle as p

ml = []
techID = 0

#grassland monster
ml.append([])
m=monster(techID = techID,
		name = 'angry dryade',
		sprite_pos = (2,8),
		move_border = 2,
		attribute_prev = (0,1,2,2,1),
		worn_equipment = (0,1,0,0,0),
		AI_style = 'hostile',
		corps_style = 'dryade',
		corps_lvl = 1,
		ignore_damage = False,
		ignore_water = True, 
		behavior = 'attack_magic', 
		attack_were = ('Head','Body','Legs'),
		possible_effect = None, 
		effect_duration = 0, 
		effect_probability = 0, 
		message = 'None')
techID+=1
ml[0].append(m)

m=monster(techID = techID,
		name = 'grassland snake',
		sprite_pos = (0,9),
		move_border = 1,
		attribute_prev = (2,1,0,0,0),
		worn_equipment = (0,0,0,0,0),
		AI_style = 'hostile',
		corps_style = 'animal',
		corps_lvl = 1,
		ignore_damage = False,
		ignore_water = False, 
		behavior = 'attack_melee', 
		attack_were = ('Legs','Feet'),
		possible_effect = 'poisoned', 
		effect_duration = 20, 
		effect_probability = 20, 
		message = 'Poison runs trough your veins!')
techID+=1
ml[0].append(m)

m=monster(techID = techID,
		name = 'rabbit',
		sprite_pos = (1,4),
		move_border = 0,
		attribute_prev = (0,1,0,1,1),
		worn_equipment = (0,0,0,0,0),
		AI_style = 'flee',
		corps_style = 'animal',
		corps_lvl = 1,
		ignore_damage = False,
		ignore_water = False, 
		behavior = 'attack_melee', 
		attack_were = ('Feet'),
		possible_effect = None, 
		effect_duration = 0, 
		effect_probability = 0, 
		message = 'None')
techID+=1
ml[0].append(m)

m=monster(techID = techID,
		name = 'green blob',
		sprite_pos = (1,8),
		move_border = 4,
		attribute_prev = (2,2,0,1,1),
		worn_equipment = (0,0,0,0,0),
		AI_style = 'hostile',
		corps_style = 'vanish',
		corps_lvl = 5,
		ignore_damage = False,
		ignore_water = False, 
		behavior = 'attack_melee', 
		attack_were = ('Legs','Feet'),
		possible_effect = None, 
		effect_duration = 0, 
		effect_probability = 0, 
		message = 'None')
techID+=1
ml[0].append(m)

m=monster(techID = techID,
		name = 'hill orc',
		sprite_pos = (1,7),
		move_border = 2,
		attribute_prev = (3,1,0,1,1),
		worn_equipment = (1,0,1,0,0),
		AI_style = 'hostile',
		corps_style = 'human',
		corps_lvl = 2,
		ignore_damage = False,
		ignore_water = True, 
		behavior = 'attack_melee', 
		attack_were = ('Head','Body','Legs','Feet'),
		possible_effect = None, 
		effect_duration = 0, 
		effect_probability = 0, 
		message = 'None')
techID+=1
ml[0].append(m)

f = file('overworld_monster.data', 'w')
p.dump(ml[0],f)
f.close()

#civilians
ml.append([])
m=monster(techID = techID,
		name = 'dryade',
		sprite_pos = (2,2),
		move_border = 2,
		attribute_prev = (0,1,2,2,1),
		worn_equipment = (0,1,0,0,0),
		AI_style = 'ignore',
		corps_style = 'dryade',
		corps_lvl = 1,
		ignore_damage = False,
		ignore_water = False, 
		behavior = 'talk', 
		attack_were = ('Feet'),
		possible_effect = None, 
		effect_duration = 0, 
		effect_probability = 0, 
		message = 'The dryade smiles mysterious.')
techID+=1
ml[1].append(m)

m=monster(techID = techID,
		name = 'tame orc',
		sprite_pos = (0,4),
		move_border = 2,
		attribute_prev = (2,1,0,1,1),
		worn_equipment = (1,0,1,0,0),
		AI_style = 'ignore',
		corps_style = 'human',
		corps_lvl = 1,
		ignore_damage = False,
		ignore_water = False, 
		behavior = 'talk', 
		attack_were = ('Feet'),
		possible_effect = None, 
		effect_duration = 0, 
		effect_probability = 0, 
		message = 'The tame orc geets you.')
techID+=1
ml[1].append(m)

m=monster(techID = techID,
		name = 'golden naga',
		sprite_pos = (1,9),
		move_border = 2,
		attribute_prev = (0,1,2,2,1),
		worn_equipment = (0,1,0,1,1),
		AI_style = 'ignore',
		corps_style = 'human',
		corps_lvl = 1,
		ignore_damage = False,
		ignore_water = True, 
		behavior = 'talk', 
		attack_were = ('Feet'),
		possible_effect = None, 
		effect_duration = 0, 
		effect_probability = 0, 
		message = 'The golden naga blinks.')
techID+=1
ml[1].append(m)

m=monster(techID = techID,
		name = 'wood elf',
		sprite_pos = (0,0),
		move_border = 2,
		attribute_prev = (0,2,0,2,1),
		worn_equipment = (1,1,1,1,1),
		AI_style = 'ignore',
		corps_style = 'human',
		corps_lvl = 1,
		ignore_damage = False,
		ignore_water = False, 
		behavior = 'talk', 
		attack_were = ('Feet'),
		possible_effect = None, 
		effect_duration = 0, 
		effect_probability = 0, 
		message = 'The wood elf waves.')
techID+=1
ml[1].append(m)

f = file('civilian_monster.data', 'w')
p.dump(ml[1],f)
f.close()

#cave

ml.append([])
m=monster(techID = techID,
		name = 'cave orc',
		sprite_pos = (2,3),
		move_border = 2,
		attribute_prev = (2,2,0,1,2),
		worn_equipment = (1,0,1,0,0),
		AI_style = 'hostile',
		corps_style = 'human',
		corps_lvl = 1,
		ignore_damage = False,
		ignore_water = True, 
		behavior = 'attack_melee', 
		attack_were = ('Head','Body','Legs','Feet'),
		possible_effect = None, 
		effect_duration = 0, 
		effect_probability = 0, 
		message = 'None.')
techID+=1
ml[2].append(m)

m=monster(techID = techID,
		name = 'blue blob',
		sprite_pos = (2,5),
		move_border = 4,
		attribute_prev = (2,1,0,0,1),
		worn_equipment = (0,0,0,0,0),
		AI_style = 'hostile',
		corps_style = 'vanish',
		corps_lvl = 1,
		ignore_damage = False,
		ignore_water = False, 
		behavior = 'attack_melee', 
		attack_were = ('Legs','Feet'),
		possible_effect = None, 
		effect_duration = 0, 
		effect_probability = 0, 
		message = 'None.')
techID+=1
ml[2].append(m)

m=monster(techID = techID,
		name = 'bat',
		sprite_pos = (2,7),
		move_border = 0,
		attribute_prev = (0,2,0,2,2),
		worn_equipment = (0,0,0,0,0),
		AI_style = 'flee',
		corps_style = 'human',
		corps_lvl = 1,
		ignore_damage = False,
		ignore_water = True, 
		behavior = 'attack_melee', 
		attack_were = ('Head','Body','Legs','Feet'),
		possible_effect = None, 
		effect_duration = 0, 
		effect_probability = 0, 
		message = 'None.')
techID+=1
ml[2].append(m)

m=monster(techID = techID,
		name = 'soil spirit',
		sprite_pos = (1,0),
		move_border = 2,
		attribute_prev = (0,1,2,1,1),
		worn_equipment = (0,1,0,0,0),
		AI_style = 'hostile',
		corps_style = 'troll',
		corps_lvl = 1,
		ignore_damage = False,
		ignore_water = False, 
		behavior = 'attack_magic', 
		attack_were = ('Head','Body','Legs','Feet'),
		possible_effect = None, 
		effect_duration = 0, 
		effect_probability = 0, 
		message = 'None.')
techID+=1
ml[2].append(m)

f = file('cave_monster.data', 'w')
p.dump(ml[2],f)
f.close()

#mine

ml.append([])
m=monster(techID = techID,
		name = 'orc warlord',
		sprite_pos = (1,5),
		move_border = 2,
		attribute_prev = (2,2,0,1,2),
		worn_equipment = (1,0,1,0,1),
		AI_style = 'hostile',
		corps_style = 'human',
		corps_lvl = 1,
		ignore_damage = False,
		ignore_water = True, 
		behavior = 'attack_melee', 
		attack_were = ('Head','Body','Legs'),
		possible_effect = 'bleeding', 
		effect_duration = 5, 
		effect_probability = 20, 
		message = 'The orc warlord tears you a bleeding wound.')
techID+=1
ml[3].append(m)

m=monster(techID = techID,
		name = 'orc warlord',
		sprite_pos = (1,5),
		move_border = 2,
		attribute_prev = (2,2,0,1,2),
		worn_equipment = (1,0,1,0,1),
		AI_style = 'hostile',
		corps_style = 'human',
		corps_lvl = 3,
		ignore_damage = False,
		ignore_water = True, 
		behavior = 'attack_melee', 
		attack_were = ('Head','Body','Legs'),
		possible_effect = 'bleeding', 
		effect_duration = 5, 
		effect_probability = 20, 
		message = 'The orc warlord tears you a bleeding wound.')
techID+=1
ml[3].append(m)

m=monster(techID = techID,
		name = 'orcish hag',
		sprite_pos = (0,6),
		move_border = 2,
		attribute_prev = (0,1,2,2,2),
		worn_equipment = (0,1,0,1,1),
		AI_style = 'hostile',
		corps_style = 'scrollkeeper',
		corps_lvl = 2,
		ignore_damage = False,
		ignore_water = True, 
		behavior = 'attack_magic', 
		attack_were = ('Head','Body','Legs','Feet'),
		possible_effect = 'hexed', 
		effect_duration = 40, 
		effect_probability = 20, 
		message = 'The orcish hag puts a hex on you.')
techID+=1
ml[3].append(m)

m=monster(techID = techID,
		name = 'orcish digger',
		sprite_pos = (1,6),
		move_border = 2,
		attribute_prev = (1,2,0,1,1),
		worn_equipment = (0,0,0,0,0),
		AI_style = 'hostile',
		corps_style = 'miner',
		corps_lvl = 2,
		ignore_damage = False,
		ignore_water = True, 
		behavior = 'attack_melee', 
		attack_were = ('Head','Body','Legs','Feet'),
		possible_effect = None, 
		effect_duration = 0, 
		effect_probability = 0, 
		message = 'None')
techID+=1
ml[3].append(m)

m=monster(techID = techID,
		name = 'blood snake',
		sprite_pos = (2,6),
		move_border = 2,
		attribute_prev = (2,2,0,0,1),
		worn_equipment = (0,0,0,0,0),
		AI_style = 'hostile',
		corps_style = 'animal',
		corps_lvl = 2,
		ignore_damage = False,
		ignore_water = True, 
		behavior = 'attack_melee', 
		attack_were = ('Legs','Feet'),
		possible_effect = 'poisoned', 
		effect_duration = 60,
		effect_probability = 45,
		message = 'Poison runs trough your veins!')
techID+=1
ml[3].append(m)

f = file('mine_monster.data', 'w')
p.dump(ml[3],f)
f.close()

#elfish fortress

ml.append([])
m=monster(techID = techID,
		name = 'male elf',
		sprite_pos = (2,0),
		move_border = 0,
		attribute_prev = (2,2,0,0,2),
		worn_equipment = (1,0,1,0,0),
		AI_style = 'ignore',
		corps_style = 'human',
		corps_lvl = 3,
		ignore_damage = False,
		ignore_water = True, 
		behavior = 'talk', 
		attack_were = ('Head','Body','Legs','Feet'),
		possible_effect = None, 
		effect_duration = 0, 
		effect_probability = 0, 
		message = 'The male elf greets you friendly.')
techID+=1
ml[4].append(m)

m=monster(techID = techID,
		name = 'female elf',
		sprite_pos = (2,1),
		move_border = 0,
		attribute_prev = (0,0,2,2,2),
		worn_equipment = (0,1,0,1,1),
		AI_style = 'ignore',
		corps_style = 'human',
		corps_lvl = 3,
		ignore_damage = False,
		ignore_water = True, 
		behavior = 'talk', 
		attack_were = ('Head','Body','Legs','Feet'),
		possible_effect = None, 
		effect_duration = 0, 
		effect_probability = 0, 
		message = 'The female elf greets you friendly.')
techID+=1
ml[4].append(m)

f = file('elfish_monster.data', 'w')
p.dump(ml[4],f)
f.close()

#elfish fortress

ml.append([])
ml.append([])
m=monster(techID = techID,
		name = 'male elf',
		sprite_pos = (2,0),
		move_border = 0,
		attribute_prev = (2,2,0,1,2),
		worn_equipment = (1,0,1,0,0),
		AI_style = 'hostile',
		corps_style = 'human',
		corps_lvl = 3,
		ignore_damage = False,
		ignore_water = True, 
		behavior = 'attack_melee', 
		attack_were = ('Head','Body','Legs','Feet'),
		possible_effect = None, 
		effect_duration = 0, 
		effect_probability = 0, 
		message = 'None')
techID+=1
ml[5].append(m)

m=monster(techID = techID,
		name = 'female elf',
		sprite_pos = (2,1),
		move_border = 0,
		attribute_prev = (0,1,2,2,2),
		worn_equipment = (0,1,0,1,1),
		AI_style = 'hostile',
		corps_style = 'human',
		corps_lvl = 3,
		ignore_damage = False,
		ignore_water = True, 
		behavior = 'attack_magic', 
		attack_were = ('Head','Body','Legs','Feet'),
		possible_effect = None, 
		effect_duration = 0, 
		effect_probability = 0, 
		message = 'None')
techID+=1
ml[5].append(m)

f = file('angry_elfish_monster.data', 'w')
p.dump(ml[5],f)
f.close()

#grot

ml.append([])
m=monster(techID = techID,
		name = 'blue naga',
		sprite_pos = (2,4),
		move_border = 3,
		attribute_prev = (0,1,2,2,2),
		worn_equipment = (0,1,0,1,1),
		AI_style = 'hostile',
		corps_style = 'scrollkeeper',
		corps_lvl = 2,
		ignore_damage = False,
		ignore_water = True, 
		behavior = 'attack_magic', 
		attack_were = ('Head'),
		possible_effect = 'hexed', 
		effect_duration = 30,
		effect_probability = 50,
		message = 'The blue naga puts a hex on you.')
techID+=1
ml[6].append(m)

m=monster(techID = techID,
		name = 'red naga',
		sprite_pos = (1,2),
		move_border = 3,
		attribute_prev = (2,2,0,1,2),
		worn_equipment = (1,0,0,1,1),
		AI_style = 'hostile',
		corps_style = 'human',
		corps_lvl = 1,
		ignore_damage = False,
		ignore_water = True, 
		behavior = 'attack_melee', 
		attack_were = ('Head','Body','Legs','Feet'),
		possible_effect = 'poisoned', 
		effect_duration = 50,
		effect_probability = 40,
		message = 'Poison runs trough your veins!')
techID+=1
ml[6].append(m)

m=monster(techID = techID,
		name = 'purple blob',
		sprite_pos = (0,5),
		move_border = 4,
		attribute_prev = (2,2,0,0,1),
		worn_equipment = (0,0,0,0,0),
		AI_style = 'hostile',
		corps_style = 'vanish',
		corps_lvl = 5,
		ignore_damage = False,
		ignore_water = True, 
		behavior = 'attack_melee', 
		attack_were = ('Legs','Feet'),
		possible_effect = None, 
		effect_duration = 0,
		effect_probability = 0,
		message = 'None')
techID+=1
ml[6].append(m)

m=monster(techID = techID,
		name = 'water spirit',
		sprite_pos = (0,1),
		move_border = 2,
		attribute_prev = (2,2,0,1,1),
		worn_equipment = (1,0,0,0,0),
		AI_style = 'hostile',
		corps_style = 'vanish',
		corps_lvl = 3,
		ignore_damage = False,
		ignore_water = True, 
		behavior = 'attack_melee', 
		attack_were = ('Head','Body','Legs','Feet'),
		possible_effect = 'confused', 
		effect_duration = 60,
		effect_probability = 20,
		message = 'The water sprit confuses you.')
techID+=1
ml[6].append(m)

f = file('grot_monster.data', 'w')
p.dump(ml[6],f)
f.close()

#lava cave

ml.append([])
m=monster(techID = techID,
		name = 'lava monster',
		sprite_pos = (0,8),
		move_border = 2,
		attribute_prev = (2,2,0,2,2),
		worn_equipment = (1,0,0,0,0),
		AI_style = 'hostile',
		corps_style = 'vanish',
		corps_lvl = 2,
		ignore_damage = True,
		ignore_water = True, 
		behavior = 'attack_melee', 
		attack_were = ('Body','Legs','Feet'),
		possible_effect = None, 
		effect_duration = 0,
		effect_probability = 0,
		message = 'None')
techID+=1
ml[7].append(m)

m=monster(techID = techID,
		name = 'flame spirit',
		sprite_pos = (0,10),
		move_border = 0,
		attribute_prev = (0,0,2,2,2),
		worn_equipment = (0,0,0,0,0),
		AI_style = 'hostile',
		corps_style = 'vanish',
		corps_lvl = 2,
		ignore_damage = True,
		ignore_water = True, 
		behavior = 'attack_magic', 
		attack_were = ('Body','Legs','Feet'),
		possible_effect = 'immobilized', 
		effect_duration = 4,
		effect_probability = 30,
		message = 'You can\'t move!')
techID+=1
ml[7].append(m)

m=monster(techID = techID,
		name = 'red blob',
		sprite_pos = (1,3),
		move_border = 4,
		attribute_prev = (2,2,0,0,2),
		worn_equipment = (0,0,0,0,0),
		AI_style = 'hostile',
		corps_style = 'vanish',
		corps_lvl = 5,
		ignore_damage = True,
		ignore_water = True, 
		behavior = 'attack_melee', 
		attack_were = ('Legs','Feet'),
		possible_effect = None, 
		effect_duration = 0,
		effect_probability = 0,
		message = 'None')
techID+=1
ml[7].append(m)

m=monster(techID = techID,
		name = 'fire bat',
		sprite_pos = (1,10),
		move_border = 0,
		attribute_prev = (2,2,0,0,2),
		worn_equipment = (0,0,0,0,0),
		AI_style = 'hostile',
		corps_style = 'vanish',
		corps_lvl = 2,
		ignore_damage = True,
		ignore_water = True, 
		behavior = 'attack_melee', 
		attack_were = ('Head','Body'),
		possible_effect = 'confused', 
		effect_duration = 40,
		effect_probability = 30,
		message = 'The bat\'s screen make you confused!')
techID+=1
ml[7].append(m)

f = file('lava_cave_monster.data', 'w')
p.dump(ml[7],f)
f.close()

#special

ml.append([])
m=monster(techID = techID,
		name = 'vase',
		sprite_pos = (0,3),
		move_border = 10,
		attribute_prev = (2,0,2,0,0),
		worn_equipment = (0,0,0,0,0),
		AI_style = 'flee',
		corps_style = 'miner',
		corps_lvl = 5,
		ignore_damage = True,
		ignore_water = True, 
		behavior = 'attack_melee', 
		attack_were = ('Legs','Feet'),
		possible_effect = None, 
		effect_duration = 0,
		effect_probability = 0,
		message = 'None')
techID+=1
ml[8].append(m)

m=monster(techID = techID,
		name = 'monster vase',
		sprite_pos = (0,3),
		move_border = 10,
		attribute_prev = (2,0,2,0,0),
		worn_equipment = (0,0,0,0,0),
		AI_style = 'flee',
		corps_style = 'vase',
		corps_lvl = 5,
		ignore_damage = True,
		ignore_water = True, 
		behavior = 'attack_melee', 
		attack_were = ('Legs','Feet'),
		possible_effect = None, 
		effect_duration = 0,
		effect_probability = 0,
		message = 'None')
techID+=1
ml[8].append(m)

m=monster(techID = techID,
		name = 'vase monster',
		sprite_pos = (0,2),
		move_border = 1,
		attribute_prev = (2,2,2,2,2),
		worn_equipment = (0,0,0,0,0),
		AI_style = 'hostile',
		corps_style = 'miner',
		corps_lvl = 5,
		ignore_damage = False,
		ignore_water = True, 
		behavior = 'attack_random', 
		attack_were = ('Body','Legs','Feet'),
		possible_effect = None, 
		effect_duration = 0,
		effect_probability = 0,
		message = 'None')
techID+=1
ml[8].append(m)

m=monster(techID = techID,
		name = 'sleeping mimic',
		sprite_pos = (1,1),
		move_border = 10,
		attribute_prev = (2,0,2,0,0),
		worn_equipment = (0,0,0,0,0),
		AI_style = 'flee',
		corps_style = 'mimic',
		corps_lvl = 5,
		ignore_damage = True,
		ignore_water = True, 
		behavior = 'attack_melee', 
		attack_were = ('Legs','Feet'),
		possible_effect = None, 
		effect_duration = 0,
		effect_probability = 0,
		message = 'None')
techID+=1
ml[8].append(m)

m=monster(techID = techID,
		name = 'mimic',
		sprite_pos = (0,7),
		move_border = 4,
		attribute_prev = (2,2,2,2,2),
		worn_equipment = (0,0,0,0,0),
		AI_style = 'hostile',
		corps_style = 'vanish',
		corps_lvl = 99,
		ignore_damage = True,
		ignore_water = True, 
		behavior = 'attack_random', 
		attack_were = ('Head','Body','Legs','Feet'),
		possible_effect = None, 
		effect_duration = 0,
		effect_probability = 0,
		message = 'None')
techID+=1
ml[8].append(m)

f = file('special_monster.data', 'w')
p.dump(ml[8],f)
f.close()
