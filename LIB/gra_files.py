import os
import pygame

class g_files():
	
	def __init__(self):
		
		self.gdic = { 'tile1' : {} , 'char' : {} , 'display' : [] , 'built' : [], 'monster' : {}}
		
		b_path = os.path.dirname(os.path.realpath('gra_files.py'))
		basic_path = b_path.replace('/LIB','')
		
		t32_path = basic_path + os.sep + 'GRAPHIC' + os.sep + 'TILE32' + os.sep
		t1_path = basic_path + os.sep + 'GRAPHIC' + os.sep + 'TILE1' + os.sep
		char_path = basic_path +os.sep + 'GRAPHIC' + os.sep + 'CHAR' + os.sep
		display_path = basic_path +os.sep + 'GRAPHIC' + os.sep + 'DISPLAY' + os.sep
		built_path = basic_path +os.sep + 'GRAPHIC' + os.sep + 'BUILT' + os.sep
		monster_path = basic_path +os.sep + 'GRAPHIC' + os.sep + 'MONSTER' + os.sep
		
		#chars
		
		gender_list = {'MALE', 'FEMALE'}
		amo_list = ('helmet', 'armor', 'cuisse', 'shoes')
		weapon_list = ('spear' , 'sword' , 'axe', 'hammer', 'rune', 'wand', 'rune staff', 'artefact', 'pickaxe')
		weapon_list2 = ('spear' , 'sword' , 'axe', 'hammer', 'rune', 'wand', 'runestaff', 'artefact', 'pickaxe')
		material_list = ('wooden', 'tin', 'copper', 'steel', 'titan', 'magnicum')
		other_list = ('SKIN', 'HAIR')
		
		for h in gender_list:
			for j in amo_list:
				for k in material_list:
					
					key_string = h + '_' + k + '_'+ j
					load_string =  char_path + h + os.sep + 'ARMOR' + os.sep + k +'_' + j + '.png'
		
					i_name = load_string
					i = pygame.image.load(i_name)
					i.set_colorkey((255,0,255),pygame.RLEACCEL)
					i = i.convert_alpha()
					self.gdic['char'][key_string] = i
					
		for k in other_list:			
			for h in gender_list:
				for j in range (1,5):
				
					key_string = k + '_' + h + '_' + str(j)
					load_string =  char_path + h + os.sep + k + os.sep + str(j) + '.png'
	
					i_name = load_string
					i = pygame.image.load(i_name)
					i.set_colorkey((255,0,255),pygame.RLEACCEL)
					i = i.convert_alpha()
					self.gdic['char'][key_string] = i
					
		for h in range (0, len(weapon_list)):
			for j in material_list:
				 
				key_string = 'WEAPONS_' + j + '_' + weapon_list[h]
				load_string =  char_path + 'WEAPONS' + os.sep + j +'_' + weapon_list2[h] + '.png'
				
				i_name = load_string
				i = pygame.image.load(i_name)
				i.set_colorkey((255,0,255),pygame.RLEACCEL)
				i = i.convert_alpha()
				self.gdic['char'][key_string] = i
				
#############################################################################

		#display stuff
		
		display_names = ('gui','game_menu_bg','tab_unmarked','tab_marked','marker','gui_transparent', 'dark', 'unknown_monster','mouse_pad')
		
		for c in display_names:
			i_name = display_path + c + '.png'
			i = pygame.image.load(i_name)
			i.set_colorkey((255,0,255),pygame.RLEACCEL)
			i = i.convert_alpha()
			self.gdic['display'].append(i)
		
#############################################################################

		#tiles
		
		tile_path = t32_path + 'tiles.png'
		tile_object = pygame.image.load(tile_path)
		
		tilemap = []
		
		for i in range (0,11):
			tilemap.append([])
			for j in range (0,11):
				tilemap[i].append(0)
		
		for x in range (0,11):
			for y in range (0,11):
				
				r = pygame.Rect((0,0),(x*32,y*32))
				i = pygame.transform.chop(tile_object,r)
				j = pygame.Surface((32,32))
				j.blit(i,(0,0))
				j.set_colorkey((255,0,255),pygame.RLEACCEL)
				j = j.convert_alpha()
				tilemap[x][y] = j
		
		self.gdic['tile32'] = tilemap
		
		########
		
		color_list = ('light_brown','brown','light_blue','blue','light_red','red','light_purple','purple','light_green','green','light_yellow','yellow','light_grey','grey','black','white')
		
		for c in color_list:
			
			i_name = t1_path + c + '.png'
			i = pygame.image.load(i_name)
			self.gdic['tile1'][c] = i
		
		###############################################################
		
		#built
		
		built_names = ('wall_false','wall_true','door_false','door_true','floor_false','floor_true','wall_over','floor_over','door_over','remove','stairup_true','stairup_false','stairdown_true','stairdown_false','agriculture_false','agriculture_true','agriculture_over')
		
		for c in built_names:
			i_name = built_path + c + '.png'
			i = pygame.image.load(i_name)
			i.set_colorkey((255,0,255),pygame.RLEACCEL)
			i = i.convert_alpha()
			self.gdic['built'].append(i)

		#######################################################
		
		#monsters
		
		m_path = monster_path + 'monsters.png'
		m_object = pygame.image.load(m_path)
		
		tilemap = []
		
		for i in range (0,11):
			tilemap.append([])
			for j in range (0,11):
				tilemap[i].append(0)
		
		for x in range (0,11):
			for y in range (0,11):
				
				r = pygame.Rect((0,0),(x*32,y*32))
				i = pygame.transform.chop(m_object,r)
				j = pygame.Surface((32,32))
				j.blit(i,(0,0))
				j.set_colorkey((255,0,255),pygame.RLEACCEL)
				j = j.convert_alpha()
				tilemap[x][y] = j
		
		self.gdic['monster'] = tilemap
