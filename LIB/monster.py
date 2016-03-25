from attribute import attribute

# This file contains the monster-class:
# It has: 
# a techID to identify the specific monster
# a name
# a sprite_pos to pick the right image when rendering
# a value of move border between 0 and 9: 0 means the monster can move every turn 9 means the monster can move never
# a integer that represents the monsters lvl
# a attribute_prev object that vontains integers that stand for the importence aspecial attribute has to this monstere when the attribute points are given. order: (p_strange,p_defense,m_strange,m_defense,max_lp)
# a basic attribure object
# a worn_equipment object wich is a list if bools standing for equipment this monster type can wear. Order: (melee weapon,magic_weapon,armor,necklance/amulet/talisman,ring)
# a AI_style that says how the monster acts toward the player. possible styles are: 'hostile', 'flee' and 'ignore'
# a crops stile variable that say what kind of crops they maybe let drop when they die. for posible values look at rl.py
# a crops level variable that says how many items the corps can contain.  possible values are between 1 and 7
# a personal ID
# a list of move groups
# a behavior variable. It says how the monster acts in battle. Possible values are: 'attack_melee', 'attack_magic', 'attack_random' and 'talk'(for peaceful characters)
# a attack_were variable. It says witch bodyparts the monster can hit. it must be given as tulpel with strings, like: ('Head', 'Body', 'Legs', 'Feet')
# a message string that is shown when the monster causes a effect on the player or when the player talks to the monster
# a move done variable that is used to indicate if the monster allready was moved in this turn
# the effect variables are unused right now but will be used to give the player a (negative) buff when he's hit by  some kinds of monsters
# a anger variable that determines what makes the monster angry
# a angry monster variable that determines the angry version of this monster

class monster():
	
	def __init__(self,techID, name, sprite_pos, move_border, attribute_prev,worn_equipment, AI_style, corps_style, corps_lvl, move_groups, personal_id, behavior, attack_were, possible_effect, effect_duration, effect_probability, message, anger = 'None', anger_monster = 'None'):
		
		self.techID = techID
		self.name = name
		self.sprite_pos = sprite_pos
		self.move_border = move_border
		self.lvl = 0
		self.attribute_prev = attribute_prev
		self.basic_attribute = attribute(2,2,2,2,2,1,2)
		self.lp = self.basic_attribute.max_lp
		self.worn_equipment = worn_equipment
		self.AI_style = AI_style
		self.corps_style = corps_style
		self.corps_lvl = corps_lvl
		self.move_groups = move_groups
		self.personal_id = personal_id
		self.behavior = behavior
		self.attack_were = attack_were
		self.possible_effect = possible_effect
		self.effect_duration = effect_duration
		self.effect_probability = effect_probability
		self.message = message
		self.anger = anger
		self.anger_monster = anger_monster
		self.move_done = 0
