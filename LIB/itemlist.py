import pickle as p
from item import item_food, item_misc

class itemlist():
	
	def __init__(self):
		
		self.ilist = {'misc' : [], 'food' : []}
		techID = 0
		
		t=item_misc(techID, 'Fontain', 'place', 'functional', 7)#0
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Chest', 'place', 'functional' ,3)#empty chest
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Bed', 'place', 'functional', 8)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Carpenter\'s workbench', 'place', 'functional', 9)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Carver\'s workbench', 'place', 'functional', 10)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Stonecutter\'s workbench', 'place', 'functional', 11)#5
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Forger\'s workbench', 'place', 'functional', 12)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Alchemist\'s workshop', 'place', 'functional', 13)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Furnace', 'place', 'functional', 14)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Altar', 'place', 'functional', 15)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Table', 'place', 'functional', 16)#10
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Wooden seat', 'place', 'functional', 17)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Stone seat', 'place', 'functional', 18)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Bookshelf', 'place', 'functional', 19)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Fishing rod', 'use', 0, 0)
		self.ilist['misc'].append(t)
		techID += 1
		#For blueprints it is important to use the une_name 'apply'. This one is only allowed for blueprints.
		#place_cat and place _num must show on the coresponding floor. The wall to the floor must be the next item inside the tiles list.
		t=item_misc(techID, 'Ordenary Blueprint', 'apply', 'building', 0)#15
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Blue Blueprint', 'apply', 'building', 9)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Green Blueprint', 'apply', 'building', 11)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Red Blueprint', 'apply', 'building', 13)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Orange Blueprint', 'apply', 'building', 15)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Purple Blueprint', 'apply', 'building', 17)#20
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Pilar', 'place', 'functional', 22)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Orcish Blueprint', 'apply', 'building', 19)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Nobel Blueprint', 'apply', 'building', 21)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Bomb', 'place', 'effect', 0)
		self.ilist['misc'].append(t)
		techID += 1
		#only scrolls and spellbooks can use the use_name 'read'
		t=item_misc(techID, 'Scroll of Identify', 'read', None, None, 0)#25
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Spellbook of Identify', 'read', None, None, 0)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Scroll of Repair', 'read', None, None, 1)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Spellbook of Repair', 'read', None, None, 1)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Scroll of Healing', 'read', None, None, 2)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Spellbook of Healing', 'read', None, None, 2)#30
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Scroll of Teleport', 'read', None, None, 3)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Spellbook of Teleport', 'read', None, None, 3)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Scroll of Return', 'read', None, None, 4)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Spellbook of Return', 'read', None, None, 4)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Scroll of Flames', 'read', None, None, 5)#35
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Spellbook of Flames', 'read', None, None, 5)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Scroll of Healing Aura', 'read', None, None, 6)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Spellbook of Healing Aura', 'read', None, None, 6)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Elfish Blueprint', 'apply', 'building', 23)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Heart-Shaped Crystal', 'break', None, None, None)#40
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Mysterious Blue Crystal', 'break', None, None, None)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Anchanted Enhancemen Powder', 'use', None, None, None)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Heavy Bag', 'open', None, None, None)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Torch', 'light', None, None, None)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Scroll of Light', 'read', None, None, 7)#45
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Spellbook of Light', 'read', None, None, 7)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Scrub seed', 'place', 'local', 6)
		self.ilist['misc'].append(t)
		techID += 1
		t=item_misc(techID, 'Sepling', 'place', 'local', 10)
		self.ilist['misc'].append(t)
		techID += 1

		#food items

		t=item_food(techID, 'Red Berries', 200,600, 0, 0, 0, 0, 0, 0, 1, 1, 'You eat some sweet red berries.')#0
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Blue Mushroom', 200, 1040, 0, 0, 0, 0, 0, 0, 4, 0, 'You eat a jucy blue mushroom.')#1
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Brown Mushroom', 800, 0, 0, 0, 0, 0, 0, 0, 4, 0, 'You eat a tasty brown mushroom.')#2
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Purple Mushroom', 200, -400, 800, 0, 0, 0, 0, 0, 4, 0, 'You eat a refreshing purple mushroom.')#3
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Fish', 600, 0, 0, 0, 0, 0, 0, 0, 1, 0, 'Bah! This is raw!.')#4
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Grilled Fish', 1200, 0, 0, 0, 0, 0, 0, 0, 5, 0, 'Delicious!')#5
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Crops', 100, -400, 0, 0, 0, 0, 0, 0, False, 3, 'Dry and tasteless.')#6
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Bread', 1200, 0, 0, 0, 0, 0, 0, 0, 6, 0, 'You eat a bread.')#7
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Rusk', 1200, -400, 0, 0, 0, 0, 0, 0, False, 0, 'You eat some rusk.')#8
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Raw Meat', 700, 0, 0, 0, 0, 0, 0, 0, 2, 0, 'Bah! This is Raw!')#9
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Grilled Meat', 1400, 0, 0, 0, 0, 0, 0, 0, 6, 0, 'Delicious!')#10
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Cultivated Mushroom', 200, 200, 0, 0, 0, 0, 0, 0, 6, 2, 'Tasteless...')#11
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Grilled Mushroom', 600, 0, 0, 0, 0, 0, 0, 0, 6, 0, 'Delicious!')#12
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Potion of healing', 0, 0, 0, 7, 0, 0, 0, 0, False, 0, 'You drink a potion of healing.', 'drink')#13
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Potion of feeding', 700, 0, 0, 0, 0, 0, 0, 0, False, 0, 'You drink a potion of feeding.', 'drink')#14
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Potion of refreshing', 0, 700, 0, 0, 0, 0, 0, 0, False, 0, 'You drink a potion of refreshing.', 'drink')#15
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Potion of vitalising', 0, 0, 700, 0, 0, 0, 0, 0, False, 0, 'You drink a potion of vitalising.', 'drink')#16
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Strong potion of healing', 0, 0, 0, 15, 0, 0, 0, 0, False, 0, 'You drink a strong potion of healing.', 'drink')#17
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Strong potion of feeding', 1400, 0, 0, 0, 0, 0, 0, 0, False, 0, 'You drink a strong potion of feeding.', 'drink')#18
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Strong potion of refreshing', 0, 1400, 0, 0, 0, 0, 0, 0, False, 0, 'You drink a strong potion of refreshing.', 'drink')#19
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Strong potion of vitalising', 0, 0, 1400, 0, 0, 0, 0, 0, False, 0, 'You drink a strong potion of vitalising.', 'drink')#20
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Potion of hunger', 0, 0, 0, 0, 100, 0, 0, 0, False, 0, 'Your stomach grows.', 'drink')#21
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Potion of thirst', 0, 0, 0, 0, 0, 100, 0, 0, False, 0, 'You feel like a camel.', 'drink')#22
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Potion of tiredness', 0, 0, 0, 0, 0, 0, 100, 0, False, 0, 'You feel like a owl.', 'drink')#23
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Potion of life', 0, 0, 0, 0, 0, 0, 0, 1, False, 0, 'You feel stronger now.', 'drink')#24
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Jellyfish', 0, 0, 0, -2, 0, 0, 0, 0, False, 0, 'Ugh... That must have been poisoness.')#25
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Grilled Jellyfish', 800, 0, 0, 0, 0, 0, 0, 0, False, 0, 'Tastes like chicken...')#26
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Blue Berries', 100,1000, 0, 0, 0, 0, 0, 0, 1, 1, 'You eat some juicy blue berries.')#27
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Yellow Berries', 700,200, 0, 0, 0, 0, 0, 0, 1, 1, 'You eat some tasty yellow berries.')#28
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Red Jelly', 300,200, 0, 0, 0, 0, 0, 0, False, 0, 'You eat some tasty red jelly.')#29
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Blue Jelly', 200,200, 0, 0, 0, 0, 0, 0, False, 0, 'You eat some tasty blue jelly.')#30
		self.ilist['food'].append(t)
		techID += 1
		t=item_food(techID, 'Yellow Jelly', 800,100, 0, 0, 0, 0, 0, 0, False, 0, 'You eat some tasty yellow jelly.')#31
		self.ilist['food'].append(t)
		techID += 1
