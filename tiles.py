import cPickle as p
from tile import tile

tl = []
techID = 0

#unsorted tiles
tl.append([])
t=tile(techID,'Low water','misc',0, True, 0, 'Your feet become wet.', None)
techID+=1
tl[0].append(t)
t=tile(techID,'Mud','misc',1, True, 0, 'The ground under your feet feels soft and wet.', None)
techID+=1
tl[0].append(t)
t=tile(techID,'Hot caveground','misc',2, True, 0, 'The ground under your feet feels like hot coals.', None)
techID+=1
tl[0].append(t)
t=tile(techID,'Water','misc',3,False,0,'None', None)
techID+=1
tl[0].append(t)
t=tile(techID,'Ore','misc',4,False, 0,'You brake some ore out of the solid rock here.', None, 2, None)
techID+=1
tl[0].append(t)
t=tile(techID,'Gem','misc',5,False, 0,'You brake a gem out of the solid rock here.', None, 4, None)
techID+=1
tl[0].append(t)
t=tile(techID,'Blue Mushroom','misc',6, True, 0, 'A blue mushroom grows here.', None, False, None)
techID+=1
tl[0].append(t)
t=tile(techID,'Brown Mushroom','misc',7, True, 0, 'A brown mushroom grows here.', None, False, None)
techID+=1
tl[0].append(t)
t=tile(techID,'Purple Mushroom','misc',8, True, 0, 'A purple mushroom grows here.', None, False, None)
techID+=1
tl[0].append(t)
t=tile(techID,'Lost Gem','misc',9, True, 0, 'Some gem lies on the ground right here.', None, False, None)
techID+=1
tl[0].append(t)
t=tile(techID,'Water Lily','misc',10, True, 0, 'A water lily grows here.', None, False, None)
techID+=1
tl[0].append(t)
t=tile(techID,'Lost Ore','misc',11, True, 0, 'Some ore lies on the ground right here.', None, False, None)
techID+=1
tl[0].append(t)
t=tile(techID,'Present','misc',12, True, 0, 'A present lies on the ground right here.', None, False, None)
techID+=1
tl[0].append(t)
t=tile(techID,'Water Lily with Blossom','misc',13, True, 0, 'A water lily with a beautiful blossom grows here.', None, False, None)
techID+=1
tl[0].append(t)
t=tile(techID,'Giant Mushroom','misc',14, False, 0, 'There is a giant mushroom here.', None, False, None)
techID+=1
tl[0].append(t)

f = file('misc_tiles.data', 'w')
p.dump(tl[0],f)
f.close()

#orcish Tiles
tl.append([])
t=tile(techID,'Orcish Mine Floor','building',19, True, 0, 'You Walk over dry mine ground.', None)
techID+=1
tl[1].append(t)
t=tile(techID,'Orcisch Mine Wall','building',20, False, 0, 'You crack your way trough this wall.', None, 2, tl[1][0])
techID+=1
tl[1].append(t)
t=tile(techID,'Blood Moss','orcish',0, True, 0, 'Here some blood moss grows on the ground.', None)
techID+=1
tl[1].append(t)

f = file('orcish_tiles.data', 'w')
p.dump(tl[1],f)
f.close()

#cave tiles
tl.append([])
t=tile(techID,'Cave ground','cave',0, True, 0, 'A dark cave surrounds you.', None)
techID+=1
tl[2].append(t)
t=tile(techID,'Worn Rock','cave',1, False, 0, 'You crack your way trough worn rocks.', None, 2, tl[2][0])
techID+=1
tl[2].append(t)
t=tile(techID,'Soft Soil' ,'cave',2, False, 0, 'You dig trough soft soil.', None, 1, tl[2][0])
techID+=1
tl[2].append(t)
t=tile(techID,'Hard Rock','cave',3,False, 0,'You make your way trough the solid rock wall', None, 4, tl[2][0])
techID+=1
tl[2].append(t)
t=tile(techID,'Lava','cave',4, True, 1, 'You stand in a hot stream of lava.', 'The lava burns your flesh.')
techID+=1
tl[2].append(t)

f = file('global_caves_tiles.data', 'w')
p.dump(tl[2],f)
f.close()

#functional tiles
tl.append([])
t=tile(techID,'Border','functional',0, False, 0, 'HERE BE DRAGONS', None,build_here = False)
techID+=1
tl[3].append(t)
t=tile(techID,'Stair down','functional',1, True, 0, 'There is a down leading stairway here.', None, False, None, True, True, False, build_here=False)
techID+=1
tl[3].append(t)
t=tile(techID,'Stair up','functional',2, True, 0, 'There is a up leading stairway here.', None, False, None, True, True, False, build_here=False)
techID+=1
tl[3].append(t)
t=tile(techID,'Empty Chest','functional',3, True, 0, 'Here is a empty chest.', None, False, None, True, True, False)
techID+=1
tl[3].append(t)
t=tile(techID,'Chest','functional',4, True, 0, 'Here is a chest.', None, False, tl[3][3], True, True, False)
techID+=1
tl[3].append(t)
t=tile(techID,'Stack','functional',5, True, 0, 'Something lies around here:', None, False, None)
techID+=1
tl[3].append(t)
t=tile(techID,'Humanoid remains','functional',6, True, 0, 'Here are some humanoid remains.', None, False, None)
techID+=1
tl[3].append(t)
t=tile(techID,'Fontain','functional',7, True, 0, 'You stand in front of a fontain.', None, False, None)
techID+=1
tl[3].append(t)
t=tile(techID,'Bed','functional',8, True, 0, 'You stand in front of a confortable bed.', None, False, None, True, True, False)
techID+=1
tl[3].append(t)
t=tile(techID,'Carpenter\'s Workbench','functional',9, True, 0, 'You stand in front of a carpenter\'s workbench.', None, False, None, True, True, False)
techID+=1
tl[3].append(t)
t=tile(techID,'Carvers\'s Workbench','functional',10, True, 0, 'You stand in front of a carvers\'s workbench.', None, False, None, True, True, False)
techID+=1
tl[3].append(t)
t=tile(techID,'Stonecutter\'s Workbench','functional',11, True, 0, 'You stand in front of a stonecutter\'s workbench.', None, False, None, True, True, False)
techID+=1
tl[3].append(t)
t=tile(techID,'Forger\'s Workbench','functional',12, True, 0, 'You stand in front of a forger\'s workbench.', None, False, None, True, True, False)
techID+=1
tl[3].append(t)
t=tile(techID,'Alchemists\'s Workshop','functional',13, True, 0, 'You stand in front of a alchemists\'s workshop.', None, False, None, True, True, False)
techID+=1
tl[3].append(t)
t=tile(techID,'Furnace','functional',14, True, 0, 'You stand in front of a furnace.', None, False, None, True, True, False)
techID+=1
tl[3].append(t)
t=tile(techID,'Altar','functional',15, True, 0, 'You stand in front of an holy altar.', None, False, None, True, True, False)
techID+=1
tl[3].append(t)
t=tile(techID,'Table','functional',16, False, 0, 'You stand on a table.', None, False, None, True, True, False)
techID+=1
tl[3].append(t)
t=tile(techID,'Wooden seat','functional',17, True, 0, 'Here is a confortable looking wooden seat.', None, False, None, True, True, False)
techID+=1
tl[3].append(t)
t=tile(techID,'Stone seat','functional',18, True, 0, 'Here is a confortable looking stone seat.', None, False, None, True, True, False)
techID+=1
tl[3].append(t)
t=tile(techID,'Bookshelf','functional',19, False, 0, 'Here is a bookshelf', None, False, None, True, True, False)
techID+=1
tl[3].append(t)
t=tile(techID,'Divine gift','functional',20, True, -1, 'The gods blessed this world here.', None, False, None, True, True, False,build_here=False)
techID+=1
tl[3].append(t)
t=tile(techID,'Animal remains','functional',21, True, 0, 'Here are some animal remains.', None, False, None, True, True, False)
techID+=1
tl[3].append(t)
t=tile(techID,'Pilar','functional',22, False, 0, 'You stand in front of a pilar.', None, False, None, True, True, False)
techID+=1
tl[3].append(t)
t=tile(techID,'Master Forge','functional',23, True, 0, 'You stand in front of a legendary master forge.', None, False, None, build_here=False)
techID+=1
tl[3].append(t)

f = file('functional_tiles.data', 'w')
p.dump(tl[3],f)
f.close()

#local

tl.append([])
t=tile(techID,'Grass','local',0, True, 0, 'You walk over soft grass.', None, False, None, True, False, True)
techID+=1
tl[4].append(t)
t=tile(techID,'Scrub','local',1, True, 0, 'There is a scrub here.', None, False, None)
techID+=1
tl[4].append(t)
t=tile(techID,'Scrub with red berries','local',2, True, 0, 'There is a scrub with red berries here.', None, False, None)
techID+=1
tl[4].append(t)
t=tile(techID,'Scrub with buds','local',3, True, 0, 'There is a scrub with some buds here.', None, False, None)
techID+=1
tl[4].append(t)
t=tile(techID,'Scrub with blossoms','local',4, True, 0, 'There is a scrub with beautiful blossoms here.', None, False, None)
techID+=1
tl[4].append(t)
t=tile(techID,'Scrub with scruffy berries','local',5, True, 0, 'There is a scrub with scruffy berries here.', None, False, None)
techID+=1
tl[4].append(t)
t=tile(techID,'Scrub seed','local',6, True, 0, 'There are some seeds on the ground here.', None, False, None)
techID+=1
tl[4].append(t)
t=tile(techID,'Scrub sepling','local',7, True, 0, 'Something start to grow here.', None, False, None)
techID+=1
tl[4].append(t)
t=tile(techID,'Small Scrub','local',8, True, 0, 'There is a small scrub at this place.', None, False, None)
techID+=1
tl[4].append(t)
t=tile(techID,'Dead Scrub','local',9, True, 0, 'There is a dead scrub here.', None, False, None)
techID+=1
tl[4].append(t)
t=tile(techID,'Tree sepling','local',10, True, 0, 'There is a sepling here.', None, False, None)
techID+=1
tl[4].append(t)
t=tile(techID,'Tree young','local',11, False, 0, 'There is a young tree here.', None, False, None)
techID+=1
tl[4].append(t)
t=tile(techID,'Tree','local',12, False, 0, 'There is a tree here.', None, False, None)
techID+=1
tl[4].append(t)
t=tile(techID,'Tree dead','local',13, False, 0, 'There is a dead tree here.', None, False, None)
techID+=1
tl[4].append(t)
t=tile(techID,'Rock','local',14, False, 0, 'You break a big rock.', None, 2, None,tl[4][0])
techID+=1
tl[4].append(t)
t=tile(techID,'Herbs','local',15, True, 0, 'Herbs grow at the ground.', None, False, None)
techID+=1
tl[4].append(t)
t=tile(techID,'Flowering herbs','local',16, True, 0, 'Flowering herbs grow at the ground.', None, False, None)
techID+=1
tl[4].append(t)
t=tile(techID,'Scrub with blue berries','local',17, True, 0, 'There is a scrub with blue berries here.', None, False, None)
techID+=1
tl[4].append(t)
t=tile(techID,'Scrub with yellow berries','local',18, True, 0, 'There is a scrub with yellow berries here.', None, False, None)
techID+=1
tl[4].append(t)

f = file('local_tiles.data', 'w')
p.dump(tl[4],f)
f.close()

#building

tl.append([])
t=tile(techID,'Floor','building',0, True, 0, 'You walk over a wooden floor.', None, False, None, True, True, False)
techID+=1
tl[5].append(t)
t=tile(techID,'Wall','building',1, False, 0, 'There is a wall here.', None, False, None, True, True, False)
techID+=1
tl[5].append(t)
t=tile(techID,'Door open','building',2, True, 0, 'You walk trough a open door.', None, False, None, True, True, False, build_here=False)
techID+=1
tl[5].append(t)
t=tile(techID,'Door closed' ,'building',3, False, 0, 'The door swings open.', None, 1, tl[5][2], True, True, False)
techID+=1
tl[5].append(t)
t=tile(techID,'Agriculture','building',4, True, 0, 'You are walking on bare fields.', None, False, None, True, True, False)
techID+=1
tl[5].append(t)
t=tile(techID,'Budding Acriculture (Overworld)','building',5, True, 0, 'Something starts to grow at this field.', None, False, None, True, True, False)
techID+=1
tl[5].append(t)
t=tile(techID,'Budding Acriculture (Caves)','building',6, True, 0, 'Something starts to grow at this field.', None, False, None, True, True, False)
techID+=1
tl[5].append(t)
t=tile(techID,'Acriculture Crops','building',7, True, 0, 'The crops stand high here.', None, False, None, True, True, False)
techID+=1
tl[5].append(t)
t=tile(techID,'Acriculture Mushroom','building',8, True, 0, 'A great mushroom grows at this field.', None, False, None, True, True, False)
techID+=1
tl[5].append(t)
t=tile(techID,'Blue Floor','building',9, True, 0, 'You walk over a blue floor.', None, False, None, True, True, False)
techID+=1
tl[5].append(t)
t=tile(techID,'Blue Wall','building',10, False, 0, 'There is a wall here.', None, False, None, True, True, False)
techID+=1
tl[5].append(t)
t=tile(techID,'Green Floor','building',11, True, 0, 'You walk over a green floor.', None, False, None, True, True, False)
techID+=1
tl[5].append(t)
t=tile(techID,'Green Wall','building',12, False, 0, 'There is a wall here.', None, False, None, True, True, False)
techID+=1
tl[5].append(t)
t=tile(techID,'Red Floor','building',13, True, 0, 'You walk over a red floor.', None, False, None, True, True, False)
techID+=1
tl[5].append(t)
t=tile(techID,'Red Wall','building',14, False, 0, 'There is a wall here.', None, False, None, True, True, False)
techID+=1
tl[5].append(t)
t=tile(techID,'Orange Floor','building',15, True, 0, 'You walk over a orange floor.', None, False, None, True, True, False)
techID+=1
tl[5].append(t)
t=tile(techID,'Orange Wall','building',16, False, 0, 'There is a wall here.', None, False, None, True, True, False)
techID+=1
tl[5].append(t)
t=tile(techID,'Purple Floor','building',17, True, 0, 'You walk over a purple floor.', None, False, None, True, True, False)
techID+=1
tl[5].append(t)
t=tile(techID,'Purple Wall','building',18, False, 0, 'There is a wall here.', None, False, None, True, True, False)
techID+=1
tl[5].append(t)
t=tile(techID,'Orcish Floor','building',19, True, 0, 'You walk over a hard soil.', None, False, None, True, True, False)
techID+=1
tl[5].append(t)
t=tile(techID,'Orcish Wall','building',20, False, 0, 'There is a wall here.', None, False, None, True, True, False)
techID+=1
tl[5].append(t)
t=tile(techID,'Nobel Floor','building',21, True, 0, 'You walk over a floor made of stone.', None, False, None, True, True, False)
techID+=1
tl[5].append(t)
t=tile(techID,'Nobel Wall','building',22, False, 0, 'There is a wall here.', None, False, None, True, True, False)
techID+=1
tl[5].append(t)
t=tile(techID,'Elfish Floor','elfish',0, True, 0, 'You walk over cobbled floor.', None, False, None, True, True, False)
techID+=1
tl[5].append(t)
t=tile(techID,'Elfish Wall','elfish',3, False, 0, 'There is a wall here.', None, False, None, True, True, False)
techID+=1
tl[5].append(t)

f = file('building_tiles.data', 'w')
p.dump(tl[5],f)
f.close()

#help tiles for overworld

tl.append([])
t=tile(techID,'scrub here','help',0, True, 0, '.help.', None, False, None, True, True, False)
techID+=1
tl[6].append(t)
t=tile(techID,'tree here','help',1, True, 0, '.help.', None, False, None, True, True, False)
techID+=1
tl[6].append(t)
t=tile(techID,'water here','help',2, True, 0, '.help.', None, False, None, True, True, False)
techID+=1
tl[6].append(t)

f = file('help_tiles.data', 'w')
p.dump(tl[6],f)
f.close()

#sanctuary tiles

tl.append([])
t=tile(techID,'Sanctuary Floor','sanctuary',0, True, -1, 'You walk over holy ground.', 'Your wounds are cured.',build_here=False)
techID+=1
tl[7].append(t)
t=tile(techID,'Sanctuary Pilar','sanctuary',1, False, 0, 'There is a pilar here.', None, False, None,build_here=False)
techID+=1
tl[7].append(t)
t=tile(techID,'Sanctuary Spawnpoint','sanctuary',2, True, -1, 'You walk over holy ground.', 'Your wounds are cured.',build_here=False)
techID+=1
tl[7].append(t)
t=tile(techID,'Sanctuary Black Portal Inactive','sanctuary',3, True, -1, 'You stand in front of the black portal. It\'s inactive.', 'Your wounds are cured.',build_here=False)
techID+=1
tl[7].append(t)
t=tile(techID,'Sanctuary Black Portal Active','sanctuary',4, True, -1, 'You stand in front of the black portal. It\'s active.', 'Your wounds are cured.',build_here=False)
techID+=1
tl[7].append(t)
t=tile(techID,'Sanctuary White Portal Inactive','sanctuary',5, True, -1, 'You stand in front of the white portal. It\'s inactive.', 'Your wounds are cured.',build_here=False)
techID+=1
tl[7].append(t)
t=tile(techID,'Sanctuary White Portal Active','sanctuary',6, True, -1, 'You stand in front of the white portal. It\'s active.', 'Your wounds are cured.',build_here=False)
techID+=1
tl[7].append(t)

f = file('sanctuary_tiles.data', 'w')
p.dump(tl[7],f)
f.close()

#shop tiles

tl.append([])
t=tile(techID,'Shop Floor','building',21, True, 0, 'You are inside a shop.', 'Your wounds are cured.',build_here=False)
techID+=1
tl[8].append(t)
t=tile(techID,'Shop Wall','building',22, False, 0, 'There is a wall here.', None, False, None,build_here=False)
techID+=1
tl[8].append(t)
t=tile(techID,'Shop Door','building',2, True, 0, 'You are entering a shop.', 'Your wounds are cured.',build_here=False)
techID+=1
tl[8].append(t)
t=tile(techID,'Elfish Shopkeeper','shop',0, False, 0, 'There is a shopkeeper here.', None, False, None,build_here=False)
techID+=1
tl[8].append(t)
t=tile(techID,'Orcish Shopkeeper','shop',1, False, 0, 'There is a shopkeeper here.', None, False, None,build_here=False)
techID+=1
tl[8].append(t)
t=tile(techID,'Naga Shopkeeper','shop',2, False, 0, 'There is a shopkeeper here.', None, False, None,build_here=False)
techID+=1
tl[8].append(t)


f = file('shop_tiles.data', 'w')
p.dump(tl[8],f)
f.close()

#effect tiles

tl.append([])
t=tile(techID,'Bomb3','effect',0, True, 0, 'The time is ticking', None)
techID+=1
tl[9].append(t)
t=tile(techID,'Bomb2','effect',1, True, 0, 'The time is ticking', None)
techID+=1
tl[9].append(t)
t=tile(techID,'Bomb1','effect',2, True, 0, 'The time is ticking', None)
techID+=1
tl[9].append(t)
t=tile(techID,'Boom','effect',3, True, 10, 'BOOM!', None)
techID+=1
tl[9].append(t)
t=tile(techID,'Flame','effect',4, True, 1, 'The fire burns your flesh.', None)
techID+=1
tl[9].append(t)
t=tile(techID,'Healing Aura','effect',5, True, -1, 'A healing aura surrounds you.', 'Your wounds are cured.')
techID+=1
tl[9].append(t)

f = file('effect_tiles.data', 'w')
p.dump(tl[9],f)
f.close()

#elfish tiles

tl.append([])
t=tile(techID,'Elfish Floor indoor','elfish',0, True, 0, 'You walk over cobbled floor.', None)
techID+=1
tl[10].append(t)
t=tile(techID,'Elfish Floor outdoor','elfish',1, True, 0, 'You walk over gritty floor.', None)
techID+=1
tl[10].append(t)
t=tile(techID,'Elfish Agricultur','elfish',2, True, 0, 'Some strange plants grow at this field.', None)
techID+=1
tl[10].append(t)
t=tile(techID,'Elfish Wall','elfish',3, False, 0, 'There is a wall here.', None, build_here=False)
techID+=1
tl[10].append(t)
t=tile(techID,'help_active','elfish',4, False, 0, 'ACTIVE', None, build_here=False)
techID+=1
tl[10].append(t)
t=tile(techID,'help_passive','elfish',5, False, 0, 'PASSIVE', None, build_here=False)
techID+=1
tl[10].append(t)
t=tile(techID,'Bare Agricultur','building',4, True, 0, 'You are walking on bare fields.', None)
techID+=1
tl[10].append(t)

f = file('elfish_tiles.data', 'w')
p.dump(tl[10],f)
f.close()

print('Done')
