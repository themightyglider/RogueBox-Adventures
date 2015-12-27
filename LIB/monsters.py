from monster import monster
from attribute import attribute
import pickle as p

ml = []
techID = 0

#grassland monster
ml.append([])
a = attribute(2,2,2,2,2,2,3,0,0,0,0)
m=monster(techID,'angry dryade','overworld',0,2,a,'hostile','dryade',1,False,True, 'attack_magic', ('Head','Body','Legs'), None, 0, 0, 'None')
techID+=1
ml[0].append(m)
a = attribute(1,1,1,1,10,1,3,0,0,0,0)
m=monster(techID,'grassland snake','overworld',1,1,a,'hostile','animal',1,False,False, 'attack_melee', ('Legs', 'Feet'), 'poisoned', 10, 20, 'Poison runs trough your veins!')
techID+=1
ml[0].append(m)
a = attribute(0,0,0,0,0,1,0,0,0,0,0)
m=monster(techID,'rabbit','overworld',2,0,a,'flee','animal',1,False,False, 'attack_melee', ('Feet'), None, 0, 0, 'None')
techID+=1
ml[0].append(m)
a = attribute(1,2,1,2,2,2,3,0,0,0,0)
m=monster(techID,'green blob','overworld',3,4,a,'hostile','vanish',5,False,False, 'attack_melee', ('Head','Body','Legs','Feet'), None, 0, 0, 'None')
techID+=1
ml[0].append(m)
a = attribute(4,3,1,1,2,2,4,0,0,0,0)
m=monster(techID,'hill orc','overworld',4,2,a,'hostile','human',2,False,True, 'attack_melee', ('Head','Body','Legs','Feet'), None, 0, 0, 'None')
techID+=1
ml[0].append(m)

f = file('overworld_monster.data', 'w')
p.dump(ml[0],f)
f.close()

#civilians
ml.append([])
a = attribute(0,0,0,0,0,1,0,0,0,0,0)
m=monster(techID,'dryade','civilian',0,0,a,'ignore','dryade',1,False,True, 'talk', ('Head','Body','Legs'), None, 0, 0, 'The dryade smiles mysterious.')
techID+=1
ml[1].append(m)
a = attribute(0,0,0,0,0,1,0,0,0,0,0)
m=monster(techID,'tame orc','civilian',1,0,a,'ignore','human',1,False,True, 'talk', ('Head','Body','Legs'), None, 0, 0, 'The tame orc greets you.')
techID+=1
ml[1].append(m)
a = attribute(0,0,0,0,0,1,0,0,0,0,0)
m=monster(techID,'golden naga','civilian',2,0,a,'ignore','human',1,False,True, 'talk', ('Head','Body','Legs'), None, 0, 0, 'The golden naga blinks.')
techID+=1
ml[1].append(m)
a = attribute(0,0,0,0,0,1,0,0,0,0,0)
m=monster(techID,'wood elf','civilian',3,0,a,'ignore','human',1,False,True, 'talk', ('Head','Body','Legs'), None, 0, 0, 'The wood elf waves.')
techID+=1
ml[1].append(m)

f = file('civilian_monster.data', 'w')
p.dump(ml[1],f)
f.close()

#cave
ml.append([])
a = attribute(5,4,1,1,4,5,0,0,0,0,0)
m=monster(techID,'cave orc','cave',0,2,a,'hostile','human',2,False,True, 'attack_melee', ('Head','Body','Legs','Feet'), None, 0, 0, 'None')
techID+=1
ml[2].append(m)
a = attribute(2,3,2,3,3,3,0,0,0,0,0)
m=monster(techID,'blue blob','cave',1,4,a,'hostile','vanish',5,False,True, 'attack_melee', ('Legs','Feet'), None, 0, 0, 'None')
techID+=1
ml[2].append(m)
a = attribute(0,0,0,0,1,1,0,0,0,0,0)
m=monster(techID,'bat','cave',2,0,a,'flee','animal',1,True,True, 'attack_melee', ('Legs','Feet'), None, 0, 0, 'None')
techID+=1
ml[2].append(m)
a = attribute(3,3,3,3,3,3,3,0,0,0,0)
m=monster(techID,'soil spirit','cave',3,2,a,'hostile','troll',1,False,False, 'attack_magic', ('Head','Body','Legs','Feet'), None, 0, 0, 'None')
techID+=1
ml[2].append(m)

f = file('cave_monster.data', 'w')
p.dump(ml[2],f)
f.close()

#mine

ml.append([])
a = attribute(10,8,4,4,5,7,0,0,0,0,0)
m=monster(techID,'orc warlord','orcish_mines',0,2,a,'hostile','human',3,False,True, 'attack_melee', ('Head','Body','Legs'), 'bleeding', 5, 20, 'The orc warlord tears you a bleeding wound')
techID+=1
ml[3].append(m)
a = attribute(4,4,10,8,5,7,3,0,0,0,0)
m=monster(techID,'orcish hag','orcish_mines',1,2,a,'hostile','scrollkeeper',2,False,True, 'attack_magic', ('Head','Body','Legs','Feet'), 'hexed', 40, 20, 'The orcish hag puts a hex on you.')
techID+=1
ml[3].append(m)
a = attribute(7,7,3,3,3,3,5,0,0,0,0)
m=monster(techID,'orcish digger','orcish_mines',2,2,a,'hostile','miner',2,False,True, 'attack_melee', ('Head','Body','Legs'), None, 0, 0, 'None')
techID+=1
ml[3].append(m)
a = attribute(5,5,5,5,15,3,5,0,0,0,0)
m=monster(techID,'orcish digger','orcish_mines',3,2,a,'hostile','animal',1,False,True, 'attack_melee', ('Legs','Feet'), 'poisoned' , 60, 45, 'Poison runs trough your veins!')
techID+=1
ml[3].append(m)

f = file('mine_monster.data', 'w')
p.dump(ml[3],f)
f.close()

#elfish fortress

ml.append([])
a = attribute(1,1,1,1,1,1,0,0,0,0,0)
m=monster(techID,'elf male','elfish',0,0,a,'ignore','human',3,False,True, 'talk', ('Head','Body','Legs','Feet'), None, 0, 0, 'The male elf greets you friendly.')
techID+=1
ml[4].append(m)
a = attribute(1,1,1,1,1,1,0,0,0,0,0)
m=monster(techID,'elf female','elfish',1,0,a,'ignore','human',3,False,True, 'talk', ('Head','Body','Legs','Feet'), None, 0, 0, 'The female elf greets you friendly.')
techID+=1
ml[4].append(m)

f = file('elfish_monster.data', 'w')
p.dump(ml[4],f)
f.close()

#elfish fortress

ml.append([])
a = attribute(10,10,10,10,10,10,0,0,0,0,0)
m=monster(techID,'elf male','elfish',0,0,a,'hostile','vanish',3,False,True, 'attack_melee', ('Head','Body','Legs','Feet'), None, 0, 0, 'The male elf greets you friendly.')
techID+=1
ml[5].append(m)
a = attribute(10,10,10,10,10,10,0,0,0,0,0)
m=monster(techID,'elf female','elfish',1,0,a,'hostile','vanish',3,False,True, 'attack_magic', ('Head','Body','Legs','Feet'), 'hexed', 40, 40, 'The female elf puts a hex on you.')
techID+=1
ml[5].append(m)

f = file('angry_elfish_monster.data', 'w')
p.dump(ml[5],f)
f.close()

#grot

ml.append([])
a = attribute(2,2,4,4,3,5,0,0,0,0,0)
m=monster(techID,'blue naga','grot',0,3,a,'hostile','scrollkeeper',2,False,True, 'attack_magic', ('Head'),'hexed' , 30, 50, 'The blue naga puts a hex on you.')
techID+=1
ml[6].append(m)
a = attribute(4,4,2,2,3,5,0,0,0,0,0)
m=monster(techID,'red naga','grot',1,3,a,'hostile','human',1,False,True, 'attack_melee', ('Head','Body','Legs','Feet'), 'poisoned', 50, 40, 'Poison runs trough your veins!')
techID+=1
ml[6].append(m)
a = attribute(3,4,3,4,4,3,0,0,0,0,0)
m=monster(techID,'purple blob','grot',2,4,a,'hostile','vanish',5,False,True, 'attack_melee', ('Legs','Feet'), None, 0, 0, 'None')
techID+=1
ml[6].append(m)
a = attribute(3,3,4,4,4,4,0,0,0,0,0)
m=monster(techID,'water spirit','grot',3,2,a,'hostile','vanish',3,False,True, 'attack_melee', ('Legs','Feet'), 'confused', 60, 20, 'The water spirit confuses you.')
techID+=1
ml[6].append(m)

f = file('grot_monster.data', 'w')
p.dump(ml[6],f)
f.close()

#lava cave

ml.append([])
a = attribute(11,12,8,8,10,5,0,0,0,0,0)
m=monster(techID,'lava monster','lava_cave',0,0,a,'hostile','vanish',2,True,True, 'attack_melee', ('Head','Body','Feet'),None , 0, 0, 'None')
techID+=1
ml[7].append(m)
a = attribute(7,7,10,13,10,6,0,0,0,0,0)
m=monster(techID,'flame spirit','lava_cave',1,0,a,'hostile','vanish',2,True,True, 'attack_magic', ('Head','Body','Feet'),'immobilized' , 4, 30, 'You can\'t move!')
techID+=1
ml[7].append(m)
a = attribute(10,10,7,7,10,5,0,0,0,0,0)
m=monster(techID,'red blob','lava_cave',2,4,a,'hostile','vanish',5,True,True, 'attack_melee', ('Legs','Feet'),None, 0, 0, 'None')
techID+=1
ml[7].append(m)
a = attribute(9,9,5,5,10,5,0,0,0,0,0)
m=monster(techID,'fire bat','lava_cave',3,0,a,'hostile','vanish',2,True,True, 'attack_melee', ('Head','Body'),'confused' , 40, 30, 'The bat\'s screen make you confused!')
techID+=1
ml[7].append(m)

f = file('lava_cave_monster.data', 'w')
p.dump(ml[7],f)
f.close()

#special

ml.append([])
a = attribute(0,0,0,0,0,1,0,0,0,0,0)
m=monster(techID,'vase','special',0,10,a,'flee','miner',5,True,True, 'attack_melee', ('Head','Body','Feet'),None , 0, 0, 'None')
techID+=1
ml[8].append(m)
a = attribute(0,0,0,0,0,1,0,0,0,0,0)
m=monster(techID,'monster vase','special',0,10,a,'flee','vase',1,True,True, 'attack_melee', ('Head','Body','Feet'),None , 0, 0, 'None')
techID+=1
ml[8].append(m)
a = attribute(3,3,3,3,5,3,0,0,0,0,0)
m=monster(techID,'vase monster','special',1,1,a,'hostile','miner',5,True,True, 'attack_random', ('Body','Legs','Feet'),None , 0, 0, 'None')
techID+=1
ml[8].append(m)
a = attribute(0,0,0,0,0,1,0,0,0,0,0)
m=monster(techID,'sleeping mimic','special',2,10,a,'flee','mimic',5,True,True, 'attack_melee', ('Head','Body','Legs','Feet'),None , 0, 0, 'None')
techID+=1
ml[8].append(m)
a = attribute(10,10,10,10,10,5,0,0,0,0,0)
m=monster(techID,'mimic','special',3,4,a,'hostile','vanish',99,True,True, 'attack_random', ('Head','Body','Legs','Feet'),None , 0, 0, 'None')
techID+=1
ml[8].append(m)

f = file('special_monster.data', 'w')
p.dump(ml[8],f)
f.close()
