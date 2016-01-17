# This file contains the monster-class:
# It has: 
# a techID to identify the specific monster
# a name
# a sprite_pos to pick the right image when rendering
# a value of move border between 0 and 9: 0 means the monster can move every turn 9 means the monster can move never
# a attribute object
# a AI_style that says how the monster acts toward the player. possible styles are: 'hostile', 'flee' and 'ignore'
# a crops stile variable that say what kind of crops they maybe let drop when they die. for posible values look at rl.py
# a crops level variable that says how many items the corps can contain.  possible values are between 1 and 7
# a ignore damage variable. If it is 'True' the monster can move over damaging fields like lava
# a ignore water variable. If it is 'True' the monster can move over low water
# a behavior variable. It says how the monster acts in battle. Possible values are: 'attack_melee', 'attack_magic', 'attack_random' and 'talk'(for peaceful characters)
# a attack_were variable. It says witch bodyparts the monster can hit. it must be given as tulpel with strings, like: ('Head', 'Body', 'Legs', 'Feet')
# a message string that is shown when the monster causes a effect on the player or when the player talks to the monster
# a move done variable that is used to indicate if the monster allready was moved in this turn
# the effect variables are unused right now but will be used to give the player a (negative) buff when he's hit by  some kinds of monsters

class monster():
	
	def __init__(self,techID, name, sprite_pos, move_border, attribute, AI_style, corps_style, corps_lvl, ignore_damage, ignore_water, behavior, attack_were, possible_effect, effect_duration, effect_probability, message):
		
		self.techID = techID
		self.name = name
		self.sprite_pos = sprite_pos
		self.move_border = move_border
		self.attribute = attribute
		self.lp = self.attribute.max_lp
		self.AI_style = AI_style
		self.corps_style = corps_style
		self.corps_lvl = corps_lvl
		self.ignore_damage = ignore_damage
		self.ignore_water = ignore_water
		self.behavior = behavior
		self.attack_were = attack_were
		self.possible_effect = possible_effect
		self.effect_duration = effect_duration
		self.effect_probability = effect_probability
		self.message = message
		self.move_done = 0
		
		print self.name , ':' , str(self.techID)
		
