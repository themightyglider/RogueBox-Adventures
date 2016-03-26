import random
from attribute import attribute

class item():
	
	def __init__(self, inv_slot):
		
		self.inv_slot = inv_slot

class item_wear(item):
	
	def __init__(self, classe, material, plus, state=100, cursed = 1, known = False, inv_slot = 'equipment'):
		
		item.__init__(self,inv_slot)
		
		materiales = ('wooden','wooden','wooden','wooden','wooden','wooden', 'tin', 'tin', 'tin', 'tin', 'tin', 'copper', 'copper', 'copper', 'copper', 'steel' ,'steel' ,'steel' ,'titan', 'titan', 'magnicum', '')
		kind = {'spear' : 1 , 'sword' : 2 , 'axe' : 3 , 'hammer' : 4 ,'shoes' : 1 , 'cuisse' : 2, 'helmet' : 3 , 'armor' : 4, 'wand' : 1, 'rune' : 2, 'rune staff' : 3, 'artefact' : 4, 'ring' : 2, 'amulet' : 4, 'necklace' : 2, 'talisman' : 4, 'pickaxe' : 1} 
		material_boni = {'wooden' : 1, 'tin' : 2, 'copper' : 3, 'steel' : 4, 'titan' : 5, 'magnicum' : 6}
		
		self.classe = classe
		self.material = materiales[material]
		try:
			material = material_boni[self.material]
		except:
			material = 0
		
		if self.material == 'wooden':
			self.defensibility_max = 1
		elif self.material == 'tin':
			self.defensibility_max = 2
		elif self.material == 'copper':
			self.defensibility_max = 3
		elif self.material == 'steel':
			self.defensibility_max = 4
		elif self.material == 'titan':
			self.defensibility_max = 5
		elif self.material == 'magnicum':
			self.defensibility_max = 6
		else:
			self.defensibility_max = 1
			
		self.defensibility = self.defensibility_max
		
		self.attribute = attribute(0,0,0,0,0,0,0,0,0,0,0)
		self.cursed = cursed
		self.known = known
		self.plus = plus
		self.state = state
		self.worn_at = 'NA'
		
		if self.classe == 'sword' or self.classe == 'axe' or self.classe == 'hammer' or self.classe == 'spear' or self.classe == 'pickaxe':
			
			plus_final = plus + material + kind[self.classe]
			
			self.attribute.p_strange += plus_final
		
		elif self.classe == 'helmet' or self.classe == 'armor' or self.classe == 'cuisse' or self.classe == 'shoes':
			
			plus_final = plus + material + kind[self.classe]
			
			self.attribute.p_defense += plus_final
			
		elif self.classe == 'wand' or self.classe == 'rune' or self.classe == 'rune staff' or self.classe == 'artefact':
			
			plus_final = plus + material + kind[self.classe]
			
			self.attribute.m_strange += plus_final
			
		elif self.classe == 'amulet' or self.classe == 'ring':
			
			plus_final = plus + material + kind[self.classe]
			
			self.attribute.m_defense += plus_final
			
		elif self.classe == 'talisman' or self.classe == 'necklace':
			
			plus_final = plus + material + kind[self.classe]
			
			self.attribute.luck += plus_final
			
		if self.classe == 'pickaxe':
			
			plus_final = plus + material + kind[self.classe]
			
			self.attribute.pickaxe_power += plus_final
		
		
		self.attribute.p_strange *= cursed
		self.attribute.p_defense *= cursed
		self.attribute.m_strange *= cursed
		self.attribute.m_defense *= cursed
		self.attribute.luck *= cursed
		self.attribute.max_lp *= cursed
		self.attribute.max_mp *= cursed
		
		self.set_name()
		
		if self.classe == 'sword' or self.classe == 'axe' or self.classe == 'spear' or self.classe == 'hammer'or self.classe == 'pickaxe':
			self.worn_at = 'Hold(R)'
		elif self.classe == 'wand' or self.classe == 'rune' or self.classe == 'rune staff' or self.classe == 'artefact':
			self.worn_at = 'Hold(L)'
		elif self.classe == 'helmet':
			self.worn_at = 'Head'
		elif self.classe == 'armor':
			self.worn_at = 'Body'
		elif self.classe == 'cuisse':
			self.worn_at = 'Legs'
		elif self.classe == 'shoes':
			self.worn_at = 'Feet'
		elif self.classe == 'ring':
			self.worn_at = 'Hand'
		elif self.classe == 'necklace' or self.classe == 'amulet' or self.classe == 'talisman':
			self.worn_at = 'Neck'
		
		if self.classe == 'Nothing':
			self.attribute = attribute(0,0,0,0,0,0,0,0,0,0,0)
		
	def set_name(self):
		
		if self.known == True:
			
			if self.cursed < 1:
				curse = 'cursed'
			elif self.cursed == 1:
				curse = 'normal'
			else:
				curse = 'holy'
				
			if self.plus != 0:
				plus = str(self.plus)
				if self.plus > 0:
					plus = '+' + plus
			else:
				plus = ''
			
			
			if self.state > 0:
				self.name = curse + ' ' + self.material + ' ' + self.classe + ' ' + plus + ' (' + str(self.state) + '%)'
			else:
				self.name = curse + ' ' + self.material + ' ' + self.classe + ' ' + plus
			
		else:
			
			if self.state > 0:
				self.name = self.material + ' ' + self.classe + ' (' + str(self.state) + '%)'
			else:
				self.name = self.material + ' ' + self.classe
			
	def identification(self):
		
		self.known = True
		self.set_name()
	
	def take_damage(self):
		
		self.defensibility -= 1
		
		if self.defensibility <= 0:
			self.defensibility = self.defensibility_max
			self.state -= 1
			return True
			
		return False
		
class item_food(item):
	
	def __init__(self,techID, name, satisfy_hunger, satisfy_thirst, satisfy_tiredness, heal, rise_hunger_max, rise_thirst_max, rise_tiredness_max, rise_lp_max, life_period, give_seed, eat_mes, eat_name = 'eat', rotten = False, inv_slot = 'food'):
		
		item.__init__(self,inv_slot)
		
		self.techID = techID
		
		if rotten == False:
			self.name = name
		else:
			self.name = 'rotten ' + name
			
		self.satisfy_hunger = satisfy_hunger
		self.satisfy_thirst = satisfy_thirst
		self.satisfy_tiredness = satisfy_tiredness
		self.heal = heal
		self.rise_hunger_max = rise_hunger_max
		self.rise_thirst_max = rise_thirst_max
		self.rise_tiredness_max = rise_tiredness_max
		self.rise_lp_max = rise_lp_max 
		self.life_period = life_period
		self.rotten = rotten

		if self.rotten == False:
			self.protection = True #this is set true for all unrotten foods to protect them of rotting at the day they are gathered
		else:
			self.protection = False
			
		self.give_seed = give_seed
		self.eat_name = eat_name
		self.eat_mes = eat_mes
		
	def rot(self):
		if self.life_period != False:#items with a 'False' life period can't rot
			if self.rotten == False:
				if self.protection == False:
					self.life_period -= 1
				else:
					self.protection = False
			
				if self.life_period <= 0:
					self.rotten = True
					self.satisfy_hunger /= 4
					self.satisfy_thirst /= 4
					self.satisfy_tiredness /= 4
					self.heal /= 4
					self.name = 'rotten ' + self.name
					return True
		 
			return False
		 
class item_misc(item):
	
	def __init__(self, techID, name, use_name, place_cat=None, place_num = None, effect = None):
		
		#place_num and place_cat are for placeable items to define the tile they are producing.
		#effect is for scrolls and spellbooks to define what effect they avtivate
		
		item.__init__(self, 'misc')
		
		self.techID = techID
		self.name = name
		self.use_name = use_name
		self.place_cat = place_cat
		self.place_num = place_num
		self.effect = effect
		
class materials():
	
	def __init__(self):
		
		self.wood = 0
		self.wood_max = 50
		self.stone = 0
		self.stone_max = 40
		self.ore = 0 
		self.ore_max = 15
		self.herb = 0
		self.herb_max = 15
		self.gem = 0
		self.gem_max = 15
		self.seeds = 0
		self.seeds_max = 40
		
	def add(self, name, num):
		
		if name == 'wood':
			gotnum = self.wood + num - self.wood_max # gotnum only becomes positive when there is to many of the material in players inventory
			self.wood += num
			if self.wood > self.wood_max:
				self.wood = self.wood_max
		
		elif name == 'stone':
			gotnum = self.stone + num - self.stone_max
			self.stone += num
			if self.stone > self.stone_max:
				self.stone = self.stone_max
				
		elif name == 'ore':
			gotnum = self.ore + num - self.ore_max
			self.ore += num
			if self.ore > self.ore_max:
				self.ore = self.ore_max
				
		elif name == 'herbs':
			gotnum = self.herb + num - self.herb_max
			self.herb += num
			if self.herb > self.herb_max:
				self.herb = self.herb_max
				
		elif name == 'gem':
			gotnum = self.gem + num - self.gem_max
			self.gem += num
			if self.gem > self.gem_max:
				self.gem = self.gem_max
		
		elif name == 'seeds':
			gotnum = self.seeds + num - self.seeds_max
			self.seeds += num
			if self.seeds > self.seeds_max:
				self.seeds = self.seeds_max
		
		mes = 'err' #to prevent crashes
	
		if gotnum <= 0:
			mes = '+' + str(num) + ' ' + name
		elif gotnum > 0 and gotnum < num:
			mes = '+' + str(num - gotnum) +' ' + name
		
		if mes != 'err':	
			return mes
		else:
			return 'Full!'
		
