import cPickle as p
from tile import tile

tl = []
techID = 0

#unsorted tiles
tl.append([])
t=tile(techID,'Low water','light_blue', True, 0, 'Your feet become wet.', None,tile_pos=(0,7))
techID+=1
tl[0].append(t)
t=tile(techID,'Mud','brown', True, 0, 'The ground under your feet feels soft and wet.', None,tile_pos=(6,10))
techID+=1
tl[0].append(t)
t=tile(techID,'Hot caveground','red', True, 0, 'The ground under your feet feels like hot coals.', None,tile_pos=(5,5))
techID+=1
tl[0].append(t)
t=tile(techID,'Water','blue',False,0,'None', None,tile_pos=(1,2))
techID+=1
tl[0].append(t)
t=tile(techID,'Ore','light_red',False, 0,'You brake some ore out of the solid rock here.', None, 2, None,tile_pos=(0,2))
techID+=1
tl[0].append(t)
t=tile(techID,'Gem','light_blue',False, 0,'You brake a gem out of the solid rock here.', None, 4, None,tile_pos=(5,1))
techID+=1
tl[0].append(t)
t=tile(techID,'Blue Mushroom','white', True, 0, 'A blue mushroom grows here.', None, False, None,tile_pos=(1,6))
techID+=1
tl[0].append(t)
t=tile(techID,'Brown Mushroom','white', True, 0, 'A brown mushroom grows here.', None, False, None,tile_pos=(5,8))
techID+=1
tl[0].append(t)
t=tile(techID,'Purple Mushroom','white', True, 0, 'A purple mushroom grows here.', None, False, None,tile_pos=(5,6))
techID+=1
tl[0].append(t)
t=tile(techID,'Lost Gem','red', True, 0, 'Some gem lies on the ground right here.', None, False, None,tile_pos=(1,8))
techID+=1
tl[0].append(t)
t=tile(techID,'Water Lily','white', True, 0, 'A water lily grows here.', None, False, None,tile_pos=(1,1))
techID+=1
tl[0].append(t)
t=tile(techID,'Lost Ore','red', True, 0, 'Some ore lies on the ground right here.', None, False, None,tile_pos=(1,7))
techID+=1
tl[0].append(t)
t=tile(techID,'Present','red', True, 0, 'A present lies on the ground right here.', None, False, None,tile_pos=(6,4))
techID+=1
tl[0].append(t)
t=tile(techID,'Water Lily with Blossom','white', True, 0, 'A water lily with a beautiful blossom grows here.', None, False, None,tile_pos=(1,0))
techID+=1
tl[0].append(t)
t=tile(techID,'Giant Mushroom','white', False, 0, 'There is a giant mushroom here.', None, False, None,tile_pos=(6,0))
techID+=1
tl[0].append(t)

f = file('misc_tiles.data', 'w')
p.dump(tl[0],f)
f.close()

#orcish Tiles
tl.append([])
t=tile(techID,'Orcish Mine Floor','light_red', True, 0, 'You Walk over dry mine ground.', None,tile_pos=(0,5))
techID+=1
tl[1].append(t)
t=tile(techID,'Orcisch Mine Wall','red', False, 0, 'You crack your way trough this wall.', None, 2, tl[1][0],tile_pos=(0,4))
techID+=1
tl[1].append(t)
t=tile(techID,'Blood Moss','red', True, 0, 'Here some blood moss grows on the ground.', None,tile_pos=(8,5))
techID+=1
tl[1].append(t)

f = file('orcish_tiles.data', 'w')
p.dump(tl[1],f)
f.close()

#cave tiles
tl.append([])
t=tile(techID,'Cave ground','light_brown', True, 0, 'A dark cave surrounds you.', None,tile_pos=(9,0))
techID+=1
tl[2].append(t)
t=tile(techID,'Worn Rock','light_grey', False, 0, 'You crack your way trough worn rocks.', None, 2, tl[2][0],tile_pos=(0,0))
techID+=1
tl[2].append(t)
t=tile(techID,'Soft Soil' ,'brown', False, 0, 'You dig trough soft soil.', None, 1, tl[2][0],tile_pos=(0,1))
techID+=1
tl[2].append(t)
t=tile(techID,'Hard Rock','grey',False, 0,'You make your way trough the solid rock wall', None, 4, tl[2][0],tile_pos=(0,10))
techID+=1
tl[2].append(t)
t=tile(techID,'Lava','red',True, 1, 'You stand in a hot stream of lava.', 'The lava burns your flesh.',tile_pos=(0,8))
techID+=1
tl[2].append(t)

f = file('global_caves_tiles.data', 'w')
p.dump(tl[2],f)
f.close()

#functional tiles
tl.append([])
t=tile(techID,'Border','white', False, 0, 'HERE BE DRAGONS', None,build_here = False,tile_pos=(9,1))
techID+=1
tl[3].append(t)
t=tile(techID,'Stair down','white', True, 0, 'There is a down leading stairway here.', None, False, None, True, True, False, build_here=False,tile_pos=(3,4))
techID+=1
tl[3].append(t)
t=tile(techID,'Stair up','white', True, 0, 'There is a up leading stairway here.', None, False, None, True, True, False, build_here=False,tile_pos=(3,3))
techID+=1
tl[3].append(t)
t=tile(techID,'Empty Chest','white', True, 0, 'Here is a empty chest.', None, False, None, True, True, False,tile_pos=(5,10))
techID+=1
tl[3].append(t)
t=tile(techID,'Chest','white', True, 0, 'Here is a chest.', None, False, tl[3][3], True, True, False,tile_pos=(6,9))
techID+=1
tl[3].append(t)
t=tile(techID,'Stack','red', True, 0, 'Something lies around here:', None, False, None,tile_pos=(3,5))
techID+=1
tl[3].append(t)
t=tile(techID,'Humanoid remains','white', True, 0, 'Here are some humanoid remains.', None, False, None,tile_pos=(3,9))
techID+=1
tl[3].append(t)
t=tile(techID,'Fontain','blue', True, 0, 'You stand in front of a fontain.', None, False, None,tile_pos=(6,3))
techID+=1
tl[3].append(t)
t=tile(techID,'Bed','white', True, 0, 'You stand in front of a confortable bed.', None, False, None, True, True, False,tile_pos=(8,6))
techID+=1
tl[3].append(t)
t=tile(techID,'Carpenter\'s Workbench','white', True, 0, 'You stand in front of a carpenter\'s workbench.', None, False, None, True, True, False,tile_pos=(8,2))
techID+=1
tl[3].append(t)
t=tile(techID,'Carvers\'s Workbench','white', True, 0, 'You stand in front of a carvers\'s workbench.', None, False, None, True, True, False,tile_pos=(8,1))
techID+=1
tl[3].append(t)
t=tile(techID,'Stonecutter\'s Workbench','white', True, 0, 'You stand in front of a stonecutter\'s workbench.', None, False, None, True, True, False,tile_pos=(3,2))
techID+=1
tl[3].append(t)
t=tile(techID,'Forger\'s Workbench','white', True, 0, 'You stand in front of a forger\'s workbench.', None, False, None, True, True, False,tile_pos=(8,0))
techID+=1
tl[3].append(t)
t=tile(techID,'Alchemists\'s Workshop','white', True, 0, 'You stand in front of a alchemists\'s workshop.', None, False, None, True, True, False,tile_pos=(8,4))
techID+=1
tl[3].append(t)
t=tile(techID,'Furnace','white', True, 0, 'You stand in front of a furnace.', None, False, None, True, True, False,tile_pos=(5,2))
techID+=1
tl[3].append(t)
t=tile(techID,'Altar','white', True, 0, 'You stand in front of an holy altar.', None, False, None, True, True, False,tile_pos=(8,3))
techID+=1
tl[3].append(t)
t=tile(techID,'Table','white', False, 0, 'You stand on a table.', None, False, None, True, True, False,tile_pos=(3,1))
techID+=1
tl[3].append(t)
t=tile(techID,'Wooden seat','white', True, 0, 'Here is a confortable looking wooden seat.', None, False, None, True, True, False,tile_pos=(3,6))
techID+=1
tl[3].append(t)
t=tile(techID,'Stone seat','white', True, 0, 'Here is a confortable looking stone seat.', None, False, None, True, True, False,tile_pos=(3,7))
techID+=1
tl[3].append(t)
t=tile(techID,'Bookshelf','white', False, 0, 'Here is a bookshelf', None, False, None, True, True, False,tile_pos=(9,2))
techID+=1
tl[3].append(t)
t=tile(techID,'Divine gift','light_purple', True, -1, 'The gods blessed this world here.', None, False, None, True, True, False,build_here=False,tile_pos=(6,8))
techID+=1
tl[3].append(t)
t=tile(techID,'Animal remains','white', True, 0, 'Here are some animal remains.', None, False, None, True, True, False,tile_pos=(8,7))
techID+=1
tl[3].append(t)
t=tile(techID,'Pilar','white', False, 0, 'You stand in front of a pilar.', None, False, None, True, True, False,tile_pos=(5,9))
techID+=1
tl[3].append(t)
t=tile(techID,'Master Forge','purple', True, 0, 'You stand in front of a legendary master forge.', None, False, None, build_here=False,tile_pos=(0,6))
techID+=1
tl[3].append(t)

f = file('functional_tiles.data', 'w')
p.dump(tl[3],f)
f.close()

#local

tl.append([])
t=tile(techID,'Grass','light_green', True, 0, 'You walk over soft grass.', None, False, None, True, False, True,tile_pos=(5,0))
techID+=1
tl[4].append(t)
t=tile(techID,'Scrub','green', True, 0, 'There is a scrub here.', None, False, None,tile_pos=(6,1))
techID+=1
tl[4].append(t)
t=tile(techID,'Scrub with red berries','red', True, 0, 'There is a scrub with red berries here.', None, False, None,tile_pos=(3,10))
techID+=1
tl[4].append(t)
t=tile(techID,'Scrub with buds','green', True, 0, 'There is a scrub with some buds here.', None, False, None,tile_pos=(5,4))
techID+=1
tl[4].append(t)
t=tile(techID,'Scrub with blossoms','green', True, 0, 'There is a scrub with beautiful blossoms here.', None, False, None,tile_pos=(1,4))
techID+=1
tl[4].append(t)
t=tile(techID,'Scrub with scruffy berries','brown', True, 0, 'There is a scrub with scruffy berries here.', None, False, None,tile_pos=(6,2))
techID+=1
tl[4].append(t)
t=tile(techID,'Scrub seed','brown', True, 0, 'There are some seeds on the ground here.', None, False, None,tile_pos=(5,3))
techID+=1
tl[4].append(t)
t=tile(techID,'Scrub sepling','green', True, 0, 'Something start to grow here.', None, False, None,tile_pos=(5,7))
techID+=1
tl[4].append(t)
t=tile(techID,'Small Scrub','green', True, 0, 'There is a small scrub at this place.', None, False, None,tile_pos=(1,3))
techID+=1
tl[4].append(t)
t=tile(techID,'Dead Scrub','green', True, 0, 'There is a dead scrub here.', None, False, None,tile_pos=(6,7))
techID+=1
tl[4].append(t)
t=tile(techID,'Tree sepling','brown', True, 0, 'There is a sepling here.', None, False, None,tile_pos=(4,1))
techID+=1
tl[4].append(t)
t=tile(techID,'Tree young','brown', False, 0, 'There is a young tree here.', None, False, None,tile_pos=(4,0))
techID+=1
tl[4].append(t)
t=tile(techID,'Tree','brown', False, 0, 'There is a tree here.', None, False, None,tile_pos=(4,3))
techID+=1
tl[4].append(t)
t=tile(techID,'Tree dead','brown', False, 0, 'There is a dead tree here.', None, False, None,tile_pos=(4,2))
techID+=1
tl[4].append(t)
t=tile(techID,'Rock','grey', False, 0, 'You break a big rock.', None, 2, None,tl[4][0],tile_pos=(3,8))
techID+=1
tl[4].append(t)
t=tile(techID,'Herbs','white', True, 0, 'Herbs grow at the ground.', None, False,None,tile_pos=(1,9))
techID+=1
tl[4].append(t)
t=tile(techID,'Flowering herbs','white', True, 0, 'Flowering herbs grow at the ground.', None, False,None,tile_pos=(0,9))
techID+=1
tl[4].append(t)
t=tile(techID,'Scrub with blue berries','blue', True, 0, 'There is a scrub with blue berries here.', None, False, None,tile_pos=(1,5))
techID+=1
tl[4].append(t)
t=tile(techID,'Scrub with yellow berries','yellow', True, 0, 'There is a scrub with yellow berries here.', None, False, None,tile_pos=(4,4))
techID+=1
tl[4].append(t)

f = file('local_tiles.data', 'w')
p.dump(tl[4],f)
f.close()

#building

tl.append([])
t=tile(techID,'Floor','light_red', True, 0, 'You walk over a wooden floor.', None, False, None, True, True, False,tile_pos=(7,5))
techID+=1
tl[5].append(t)
t=tile(techID,'Wall','red', False, 0, 'There is a wall here.', None, False, None, True, True, False,tile_pos=(2,5))
techID+=1
tl[5].append(t)
t=tile(techID,'Door open','white', True, 0, 'You walk trough a open door.', None, False, None, True, True, False, build_here=False,tile_pos=(7,10))
techID+=1
tl[5].append(t)
t=tile(techID,'Door closed' ,'white', False, 0, 'The door swings open.', None, 1, tl[5][2], True, True, False,tile_pos=(6,6))
techID+=1
tl[5].append(t)
t=tile(techID,'Agriculture','yellow', True, 0, 'You are walking on bare fields.', None, False, None, True, True, False,tile_pos=(9,7))
techID+=1
tl[5].append(t)
t=tile(techID,'Budding Acriculture (Overworld)','yellow', True, 0, 'Something starts to grow at this field.', None, False, None, True, True, False,tile_pos=(8,8))
techID+=1
tl[5].append(t)
t=tile(techID,'Budding Acriculture (Caves)','yellow', True, 0, 'Something starts to grow at this field.', None, False, None, True, True, False,tile_pos=(9,8))
techID+=1
tl[5].append(t)
t=tile(techID,'Acriculture Crops','yellow', True, 0, 'The crops stand high here.', None, False, None, True, True, False,tile_pos=(8,10))
techID+=1
tl[5].append(t)
t=tile(techID,'Acriculture Mushroom','yellow', True, 0, 'A great mushroom grows at this field.', None, False, None, True, True, False,tile_pos=(8,9))
techID+=1
tl[5].append(t)
t=tile(techID,'Blue Floor','light_red', True, 0, 'You walk over a blue floor.', None, False, None, True, True, False,tile_pos=(7,4))
techID+=1
tl[5].append(t)
t=tile(techID,'Blue Wall','red', False, 0, 'There is a wall here.', None, False, None, True, True, False,tile_pos=(2,4))
techID+=1
tl[5].append(t)
t=tile(techID,'Green Floor','light_red', True, 0, 'You walk over a green floor.', None, False, None, True, True, False,tile_pos=(7,3))
techID+=1
tl[5].append(t)
t=tile(techID,'Green Wall','red', False, 0, 'There is a wall here.', None, False, None, True, True, False,tile_pos=(2,3))
techID+=1
tl[5].append(t)
t=tile(techID,'Red Floor','light_red', True, 0, 'You walk over a red floor.', None, False, None, True, True, False,tile_pos=(7,0))
techID+=1
tl[5].append(t)
t=tile(techID,'Red Wall','red', False, 0, 'There is a wall here.', None, False, None, True, True, False,tile_pos=(2,0))
techID+=1
tl[5].append(t)
t=tile(techID,'Orange Floor','light_red', True, 0, 'You walk over a orange floor.', None, False, None, True, True, False,tile_pos=(7,2))
techID+=1
tl[5].append(t)
t=tile(techID,'Orange Wall','red', False, 0, 'There is a wall here.', None, False, None, True, True, False,tile_pos=(2,2))
techID+=1
tl[5].append(t)
t=tile(techID,'Purple Floor','light_red', True, 0, 'You walk over a purple floor.', None, False, None, True, True, False,tile_pos=(7,1))
techID+=1
tl[5].append(t)
t=tile(techID,'Purple Wall','red', False, 0, 'There is a wall here.', None, False, None, True, True, False,tile_pos=(2,1))
techID+=1
tl[5].append(t)
t=tile(techID,'Orcish Floor','light_red', True, 0, 'You walk over a hard soil.', None, False, None, True, True, False,tile_pos=(0,5))
techID+=1
tl[5].append(t)
t=tile(techID,'Orcish Wall','red', False, 0, 'There is a wall here.', None, False, None, True, True, False,tile_pos=(0,4))
techID+=1
tl[5].append(t)
t=tile(techID,'Nobel Floor','light_red', True, 0, 'You walk over a floor made of stone.', None, False, None, True, True, False,tile_pos=(0,3))
techID+=1
tl[5].append(t)
t=tile(techID,'Nobel Wall','red', False, 0, 'There is a wall here.', None, False, None, True, True, False,tile_pos=(2,6))
techID+=1
tl[5].append(t)
t=tile(techID,'Elfish Floor','light_red', True, 0, 'You walk over cobbled floor.', None, False, None, True, True, False,tile_pos=(7,8))
techID+=1
tl[5].append(t)
t=tile(techID,'Elfish Wall','red', False, 0, 'There is a wall here.', None, False, None, True, True, False,tile_pos=(7,6))
techID+=1
tl[5].append(t)

f = file('building_tiles.data', 'w')
p.dump(tl[5],f)
f.close()

#help tiles for overworld

tl.append([])
t=tile(techID,'scrub here','white', True, 0, '.help.', None, False, None, True, True, False)
techID+=1
tl[6].append(t)
t=tile(techID,'tree here','white', True, 0, '.help.', None, False, None, True, True, False)
techID+=1
tl[6].append(t)
t=tile(techID,'water here','white', True, 0, '.help.', None, False, None, True, True, False)
techID+=1
tl[6].append(t)

f = file('help_tiles.data', 'w')
p.dump(tl[6],f)
f.close()

#sanctuary tiles

tl.append([])
t=tile(techID,'Sanctuary Floor','light_purple', True, -1, 'You walk over holy ground.', 'Your wounds are cured.',build_here=False,tile_pos=(4,10))
techID+=1
tl[7].append(t)
t=tile(techID,'Sanctuary Pilar','purple', False, 0, 'There is a pilar here.', None, False, None,build_here=False,tile_pos=(4,9))
techID+=1
tl[7].append(t)
t=tile(techID,'Sanctuary Spawnpoint','white', True, -1, 'You walk over holy ground.', 'Your wounds are cured.',build_here=False,tile_pos=(2,10))
techID+=1
tl[7].append(t)
t=tile(techID,'Sanctuary Black Portal Inactive','purple', True, -1, 'You stand in front of the black portal. It\'s inactive.', 'Your wounds are cured.',build_here=False,tile_pos=(4,8))
techID+=1
tl[7].append(t)
t=tile(techID,'Sanctuary Black Portal Active','black', True, -1, 'You stand in front of the black portal. It\'s active.', 'Your wounds are cured.',build_here=False,tile_pos=(4,7))
techID+=1
tl[7].append(t)
t=tile(techID,'Sanctuary White Portal Inactive','purple', True, -1, 'You stand in front of the white portal. It\'s inactive.', 'Your wounds are cured.',build_here=False,tile_pos=(4,6))
techID+=1
tl[7].append(t)
t=tile(techID,'Sanctuary White Portal Active','white', True, -1, 'You stand in front of the white portal. It\'s active.', 'Your wounds are cured.',build_here=False,tile_pos=(4,5))
techID+=1
tl[7].append(t)

f = file('sanctuary_tiles.data', 'w')
p.dump(tl[7],f)
f.close()

#shop tiles

tl.append([])
t=tile(techID,'Shop Floor','light_purple', True, 0, 'You are inside a shop.', 'None',build_here=False,tile_pos=(0,3))
techID+=1
tl[8].append(t)
t=tile(techID,'Shop Wall','purple', False, 0, 'There is a wall here.', None, False, None,build_here=False,tile_pos=(2,6))
techID+=1
tl[8].append(t)
t=tile(techID,'Shop Door','white', True, 0, 'You are entering a shop.', 'Your wounds are cured.',build_here=False,tile_pos=(7,10))
techID+=1
tl[8].append(t)
t=tile(techID,'Elfish Shopkeeper','white', False, 0, 'There is a shopkeeper here.', None, False, None,build_here=False,tile_pos=(2,9))
techID+=1
tl[8].append(t)
t=tile(techID,'Orcish Shopkeeper','white', False, 0, 'There is a shopkeeper here.', None, False, None,build_here=False,tile_pos=(2,7))
techID+=1
tl[8].append(t)
t=tile(techID,'Naga Shopkeeper','white', False, 0, 'There is a shopkeeper here.', None, False, None,build_here=False,tile_pos=(2,8))
techID+=1
tl[8].append(t)


f = file('shop_tiles.data', 'w')
p.dump(tl[8],f)
f.close()

#effect tiles

tl.append([])
t=tile(techID,'Bomb3','red', True, 0, 'The time is ticking', None,tile_pos=(9,3))
techID+=1
tl[9].append(t)
t=tile(techID,'Bomb2','red', True, 0, 'The time is ticking', None,tile_pos=(9,4))
techID+=1
tl[9].append(t)
t=tile(techID,'Bomb1','red', True, 0, 'The time is ticking', None,tile_pos=(9,5))
techID+=1
tl[9].append(t)
t=tile(techID,'Boom','light_red', True, 10, 'BOOM!', None,tile_pos=(9,6))
techID+=1
tl[9].append(t)
t=tile(techID,'Flame','light_red', True, 1, 'The fire burns your flesh.', None,tile_pos=(6,5))
techID+=1
tl[9].append(t)
t=tile(techID,'Healing Aura','light_blue', True, -1, 'A healing aura surrounds you.', 'Your wounds are cured.',tile_pos=(1,10))
techID+=1
tl[9].append(t)

f = file('effect_tiles.data', 'w')
p.dump(tl[9],f)
f.close()

#elfish tiles

tl.append([])
t=tile(techID,'Elfish Floor indoor','light_purple', True, 0, 'You walk over cobbled floor.', None,tile_pos=(7,8))
techID+=1
tl[10].append(t)
t=tile(techID,'Elfish Floor outdoor','light_purple', True, 0, 'You walk over gritty floor.', None,tile_pos=(7,7))
techID+=1
tl[10].append(t)
t=tile(techID,'Elfish Agricultur','light_green', True, 0, 'Some strange plants grow at this field.', None,tile_pos=(7,9))
techID+=1
tl[10].append(t)
t=tile(techID,'Elfish Wall','purple', False, 0, 'There is a wall here.', None, build_here=False,tile_pos=(7,6))
techID+=1
tl[10].append(t)
t=tile(techID,'help_active','black', False, 0, 'ACTIVE', None, build_here=False)
techID+=1
tl[10].append(t)
t=tile(techID,'help_passive','black', False, 0, 'PASSIVE', None, build_here=False)
techID+=1
tl[10].append(t)
t=tile(techID,'Bare Agricultur','light_brown', True, 0, 'You are walking on bare fields.', None,tile_pos=(9,7))
techID+=1
tl[10].append(t)

f = file('elfish_tiles.data', 'w')
p.dump(tl[10],f)
f.close()

print('Done')
