#! /usr/bin/python
# -*- coding: utf-8 -*-

import time
import sys
import os
basic_path = os.path.dirname(os.path.realpath('main.py')) #just get the execution path for resources
lib_path = basic_path + os.sep + 'LIB'
data_path = basic_path + os.sep + 'DATA'
save_path = basic_path + os.sep + 'SAVE' + os.sep + 'World0'
playing = False
sys.path.append(lib_path)
max_map_size = 202
monitor = [0,0]
import pickle as p
import random
from getch import *
from tile import tile
from attribute import attribute
from item import *
from countdown import *
import pygame
from gra_files import *
from save import save_everything as save
from monster import monster
from copy import deepcopy
from buffs import buffs
from itemlist import *
from tilelist import *
from monsterlist import *
from version import *

class game_options():
	
	def __init__(self):
		
		name = basic_path + os.sep + 'SAVE' + os.sep + 'options.data'
		
		try:
			
			f = file(name, 'r')
			temp = p.load(f)
			self.screenmode = temp.screenmode
			self.bgmmode = temp.bgmmode
			self.sfxmode = temp.sfxmode
			self.turnmode = temp.turnmode
			self.mousepad = temp.mousepad
		
		except:
			self.screenmode = 1 #0:windowed,1:fullscreen
			self.bgmmode = 1 #0:bgm off, 1:bgm on
			self.sfxmode = 1 #0:sfx off, 1:sfx on
			self.turnmode = 1 #0:classic, 1:Semi-Real-Time
			self.mousepad = 0 #0:mouse off, 1:mouse on
			self.save()
			
	def save(self):
		
		name = basic_path + os.sep + 'SAVE' + os.sep + 'options.data'
	
		f = file(name, 'w')
		p.dump(self,f)
		f.close()
		

game_options = game_options()
		
class g_screen():
	
	def __init__(self, mode = game_options.screenmode, show_logo = True):
		
		global monitor
		
		self.fire_mode = 0 #0: normal, 1: fire
		self.win_mode = mode
		self.hit_matrix = []
		
		for y in range(0,12):
			self.hit_matrix.append([])
			for  x in range(0,15):
				self.hit_matrix[y].append(0)
		
		pygame.init()
		
		display_info = pygame.display.Info()
		
		if monitor == [0,0]:
			monitor[0] = display_info.current_w
			monitor[1] = display_info.current_h
		
		self.displayx = monitor[0]
		self.displayy = monitor[1]
		
		#check if the screenmode is 16:9
		
		if float(self.displayx/self.displayy) < float(16/9):
			self.displayx = (self.displayx*9)/16
		elif float(self.displayx/self.displayy) > float(16/9):
			self.displayy = (self.displayy*16)/9
		
		winstyle = pygame.FULLSCREEN
		
		if self.win_mode == 1:  
			self.screen = pygame.display.set_mode((self.displayx,self.displayy),winstyle)
		else:
			self.screen = pygame.display.set_mode((640,360))
			self.displayx = 640
			self.displayy = 360
		
		if low_res == True:
			self.screen = pygame.display.set_mode((320,240))
			self.displayx = 320
			self.displayy = 240
		
		pygame.display.set_caption('RogueBox Adventures')
		
		font_path = basic_path + os.sep + 'FONT' + os.sep + 'PressStart2P.ttf'
		self.font = pygame.font.Font(font_path,8)
		if low_res == False:
			self.menu_font = self.font
		else:
			menu_font_path = basic_path + os.sep + 'FONT' + os.sep + 'DejaVuSansMono-Bold.ttf'
			self.menu_font = pygame.font.Font(menu_font_path,16)
		
		if show_logo == True:
			display_path = basic_path +os.sep + 'GRAPHIC' + os.sep + 'DISPLAY' + os.sep
			ran = random.randint(0,4)
			i_name = display_path + 'logo' + str(ran) + '.png'
			i = pygame.image.load(i_name)
			i = pygame.transform.scale(i,(self.displayx,self.displayy))
			self.screen.blit(i,(0,0))
			pygame.display.flip()
			getch(640,360,mode=1)
			
			display_path = basic_path +os.sep + 'GRAPHIC' + os.sep + 'DISPLAY' + os.sep
			i_name = display_path + 'lrsf' + '.png'
			i = pygame.image.load(i_name)
			i = pygame.transform.scale(i,(self.displayx,self.displayy))
			self.screen.blit(i,(0,0))
			pygame.display.flip()
			getch(640,360,mode=1)
	
	def reset_hit_matrix(self):
		
		self.hit_matrix = []
		
		for y in range(0,12):
			self.hit_matrix.append([])
			for  x in range(0,15):
				self.hit_matrix[y].append(0)
				
	def write_hit_matrix(self,x,y,style):
		
		#style: 0:nothing
		#		1:fire_path
		#		2:fire_path_monster
		#		3:miss
		#		4:hit
		#		5:critical
				
		xx = x - player.pos[0] + 7
		yy = y - player.pos[1] + 6
		
		try:
			self.hit_matrix[yy][xx] = style
		except:
			None
	
	def render_hits(self):
		
		s = pygame.Surface((480,360))
			
		s.fill((255,0,255))
		if low_res == False:
			start = 0
			plus = 20
		else:
			start = 2
			plus = -6
		
		for y in range(start,len(self.hit_matrix)):
			for x in range(start,len(self.hit_matrix[0])):
					
				if self.hit_matrix[y][x] == 1:
					s.blit(gra_files.gdic['display'][11],(((x-start)*32)+plus,(y-start)*32))
				elif self.hit_matrix[y][x] == 2:
					s.blit(gra_files.gdic['display'][12],(((x-start)*32)+plus,(y-start)*32))
				elif self.hit_matrix[y][x] == 3:
					s.blit(gra_files.gdic['display'][13],(((x-start)*32)+plus,(y-start)*32))
				elif self.hit_matrix[y][x] == 4:
					s.blit(gra_files.gdic['display'][14],(((x-start)*32)+plus,(y-start)*32))
				elif self.hit_matrix[y][x] == 5:
					s.blit(gra_files.gdic['display'][15],(((x-start)*32)+plus,(y-start)*32))

		s.set_colorkey((255,0,255),pygame.RLEACCEL)	
		s = s.convert_alpha()
		return s
		
	def render_main_menu(self):
		
		display_path = basic_path +os.sep + 'GRAPHIC' + os.sep + 'DISPLAY' + os.sep
		
		num = 0
		
		run = True
		
		while run:
			s = pygame.Surface((640,360))
			s.fill((48,48,48))
			try:
				i_name = display_path + 'tmp.png'
				i = pygame.image.load(i_name)
				i.set_colorkey((255,0,255),pygame.RLEACCEL)
				i = i.convert_alpha()
				s.blit(i,(0,0))
			except:
				i_name = display_path + 'alt.png'
				i = pygame.image.load(i_name)
				i.set_colorkey((255,0,255),pygame.RLEACCEL)
				i = i.convert_alpha()
				s.blit(i,(0,0))
				
			s.blit(gra_files.gdic['display'][16],(0,0))
			
			menu_list = ('PLAY','OPTIONS','CREDITS','QUIT')
			
			for c in range(0,len(menu_list)):
				name_image = self.menu_font.render(menu_list[c],1,(0,0,0))
				s.blit(name_image,(210,145+(c*45)))
				
			s.blit(gra_files.gdic['display'][4],(185,138+(num*45)))
			
			if game_options.mousepad == 0:
				s_h = pygame.Surface((160,360))
				s_h.fill((48,48,48))
				s.blit(s_h,(480,0))
				s_help = pygame.Surface((640,360))
				s_help.fill((48,48,48))
				s_help.blit(s,(80,0))
				s = s_help
			else:
				s.blit(gra_files.gdic['display'][8],(480,0)) #render mouse pad
			
			s = pygame.transform.scale(s,(self.displayx,self.displayy))
			
			self.screen.blit(s,(0,0))
			
			pygame.display.flip()
			
			ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
			
			if ui == 'w':
				num -= 1
				if num < 0:
					num = 0
					
			elif ui == 's':
				num += 1
				if num > 3:
					num = 3
			
			elif ui == 'e':
				if num == 0:
					screen.choose_save_path()
					run = False
				elif num == 1:
					screen.render_options()
				elif num == 2:
					screen.render_credits()
				elif num == 3:
					exit(0)
	
	def choose_save_path(self):
		
		global save_path
		global playing
		
		run = True
		while run:
			
			menu_items = []
		
			for c in range(0,5):
				save_path = basic_path + os.sep + 'SAVE' + os.sep + 'World' + str(c)
				p_attribute = attribute(2,2,2,2,2,10,10)
				p_inventory = inventory()
				player_help = player_class ('-EMPTY SLOT-', 'local_0_0', p_attribute,p_inventory, build= 'Auto')
				
				if player_help.name != '-EMPTY SLOT-':
					item_string = player_help.name + ' LVL:' + str(player_help.lvl)
				else:
					item_string = '-EMPTY SLOT-'
					
				menu_items.append(item_string)
				
			menu_items.append('~~ERASE~~')
			menu_items.append('~~BACK~~')
				
			choice = screen.get_choice('Choose a saved game',menu_items,False)
				
			if choice < 5:
				save_path = basic_path + os.sep + 'SAVE' + os.sep + 'World' + str(choice)
				playing = True
				run = False
				
			elif choice == 5:
				menu_items_erase = []
				
				for d in range(0,5):
					menu_items_erase.append(menu_items[d])
				
				menu_items_erase.append('~~BACK~~')
					
				choice2 = screen.get_choice('Choose a game to erase',menu_items_erase,False,'Warning')
				
				if choice2 < 5:
						
					save_path = basic_path + os.sep + 'SAVE' + os.sep + 'World' + str(choice2)
						
					try:	
						
						choice3 = screen.get_choice('Are you sure?',('No','Yes'),False,'Warning')
						
						if choice3 == 1:
							h = ('world.data','time.data','player.data','gods.data')
							
							for i in h:	
								path = save_path + os.sep + i
								os.remove(path)
					except:
						None
						
			elif choice == 6:
				run = False
	
	def save_tmp_png(self):
		
		x = player.pos[0]
		if x-10 < 0:
			x += -1*(x-11)
		elif x+10 > max_map_size-2:
			x -= 10
			
		y = player.pos[1]
		if y-10 < 0:
			y += -1*(y-11)
		elif y+10 > max_map_size-2:
			y -= 10
			
		z =  player.pos[2]
		
		s = pygame.Surface((480,360))
		
		for yy in range(-5,10):
			for xx in range(-7,8):
				
				  
				t_pos = world.maplist[z][player.on_map].tilemap[y+yy][x+xx].tile_pos
				t_replace = world.maplist[z][player.on_map].tilemap[y+yy][x+xx].replace
					
				if t_replace == None:
					s.blit(gra_files.gdic['tile32'][t_pos[1]][t_pos[0]],((xx+7)*32,(yy+5)*32))
				else:
					try:
						#render the replaced tile under the replacing one. eg.: for stacks
						s.blit(gra_files.gdic['tile32'][t_replace.tile_pos[1]][t_replace.tile_pos[0]],((xx+7)*32,(yy+5)*32))
						s.blit(gra_files.gdic['tile32'][t_pos[1]][t_pos[0]],((xx+7)*32,(yy+5)*32))
					except:
						None
		
		tmp_save_path = basic_path + os.sep + 'GRAPHIC' + os.sep + 'DISPLAY' + os.sep + 'tmp.png'
					
		pygame.image.save(s,tmp_save_path)
							
	
	def re_init(self): # For changing screenmode
		
		if self.win_mode == 0:
			mode = 1
		else:
			mode = 0
		game_options.screenmode = mode
		game_options.save()
		
		self.__init__(game_options.screenmode,False)
		
	def render(self,mes_num, simulate = False):
		
		radius = 6
		
		if player.pos[2] > 0:
			radius = 2
		elif player.pos[2] == 0:
			if time.hour > 19 or time.hour < 6:
				radius = 2 
			
		if player.buffs.light > 0:
			radius = 6
			
		if player.buffs.blind > 0:
			radius = 0 
		
		s = pygame.Surface((640,360))
		
		test = message.sget(mes_num)
		
		s.fill((48,48,48)) #paint it grey(to clear the screen)
		
		if low_res == False:
			start_pos_x = 240 #the center of the main map view
			start_pos_y = 180
		else:
			start_pos_x = 152 #the center of the main map view
			start_pos_y = 122
		
		ymin = player.pos[1]-6
		if ymin < 0:
			ymin = 0		
		ymax = player.pos[1]+7
		xmin = player.pos[0]-8
		if xmin < 0: 
			xmin = 0
		xmax = player.pos[0]+8
		
		for y in range(ymin,ymax):
			for x in range(xmin,xmax):
								
				rx = x-player.pos[0]
				ry = y-player.pos[1]
				
				distance = ((rx)**2+(ry)**2)**0.5
				
				try:
					t_pos = world.maplist[player.pos[2]][player.on_map].tilemap[y][x].tile_pos
					t_known = world.maplist[player.pos[2]][player.on_map].known[y][x]
					t_replace = world.maplist[player.pos[2]][player.on_map].tilemap[y][x].replace
						
					if t_known == 1:
						if t_replace == None:
							s.blit(gra_files.gdic['tile32'][t_pos[1]][t_pos[0]],(start_pos_x+((x-player.pos[0])*32),start_pos_y+((y-player.pos[1])*32)))
						else:
							#render the replaced tile under the replacing one. eg.: for stacks
							s.blit(gra_files.gdic['tile32'][t_replace.tile_pos[1]][t_replace.tile_pos[0]],(start_pos_x+((x-player.pos[0])*32),start_pos_y+((y-player.pos[1])*32)))
							s.blit(gra_files.gdic['tile32'][t_pos[1]][t_pos[0]],(start_pos_x+((x-player.pos[0])*32),start_pos_y+((y-player.pos[1])*32)))
							
						
						s.blit(gra_files.gdic['display'][6],(start_pos_x+((x-player.pos[0])*32),start_pos_y+((y-player.pos[1])*32)))
					
						if world.maplist[player.pos[2]][player.on_map].npcs[y][x] != 0:	
							ran = random.randint(0,1)
							if world.maplist[player.pos[2]][player.on_map].npcs[y][x].techID == ml.mlist['special'][0].techID or world.maplist[player.pos[2]][player.on_map].npcs[y][x].techID == ml.mlist['special'][1].techID or world.maplist[player.pos[2]][player.on_map].npcs[y][x].techID == ml.mlist['special'][3].techID:
								#if this is a vase, a monster vase or a sleepng mimic show them like they would be tile ojects
								s.blit(gra_files.gdic['monster'][pos[1]][pos[0]],(start_pos_x+((x-player.pos[0])*32),start_pos_y+((y-player.pos[1])*32)))
								ran = 0
						
							if ran == 1:
								s.blit(gra_files.gdic['display'][7],(start_pos_x+((x-player.pos[0])*32),start_pos_y+((y-player.pos[1])*32)))
							else:
								s.blit(gra_files.gdic['display'][6],(start_pos_x+((x-player.pos[0])*32),start_pos_y+((y-player.pos[1])*32)))
						
						if round(distance) <= radius+1 or round(distance) >= radius-1:
							
							run = True
							c = 0
							
							while run:
								
								try:
									yy = ((ry*c)/distance)
								except:
									yy = 1
						
								try:
									xx = ((rx*c)/distance)
								except:
									xx = 1
								
								view_x = int(xx) + player.pos[0]
								view_y = int(yy) + player.pos[1]
								
								t_pos = world.maplist[player.pos[2]][player.on_map].tilemap[view_y][view_x].tile_pos
								t_known = world.maplist[player.pos[2]][player.on_map].known[view_y][view_x]
								t_replace = world.maplist[player.pos[2]][player.on_map].tilemap[view_y][view_x].replace	
								
								if t_known == 1:
									if t_replace == None:
										s.blit(gra_files.gdic['tile32'][t_pos[1]][t_pos[0]],(start_pos_x+((view_x-player.pos[0])*32),start_pos_y+((view_y-player.pos[1])*32)))
									else:
										#render the replaced tile under the replacing one. eg.: for stacks
										s.blit(gra_files.gdic['tile32'][t_replace.tile_pos[1]][t_replace.tile_pos[0]],(start_pos_x+((view_x-player.pos[0])*32),start_pos_y+((view_y-player.pos[1])*32)))
										s.blit(gra_files.gdic['tile32'][t_pos[1]][t_pos[0]],(start_pos_x+((view_x-player.pos[0])*32),start_pos_y+((view_y-player.pos[1])*32)))
							
									if world.maplist[player.pos[2]][player.on_map].npcs[view_y][view_x] != 0:#render monsters
										pos = world.maplist[player.pos[2]][player.on_map].npcs[view_y][view_x].sprite_pos
										s.blit(gra_files.gdic['monster'][pos[1]][pos[0]],(start_pos_x+((view_x-player.pos[0])*32),start_pos_y+((view_y-player.pos[1])*32)))
								
									if view_x == player.pos[0] and view_y == player.pos[1]:
						
										skinstring = 'SKIN_' + player.gender + '_' + str(player.style +1)
										s.blit(gra_files.gdic['char'][skinstring],(start_pos_x+((view_x-player.pos[0])*32),start_pos_y+((view_y-player.pos[1])*32)))
						
										if player.inventory.wearing['Head'] == player.inventory.nothing:
											hairstring = 'HAIR_' + player.gender + '_' + str(player.style +1)
											s.blit(gra_files.gdic['char'][hairstring],(start_pos_x+((view_x-player.pos[0])*32),start_pos_y+((view_y-player.pos[1])*32)))
										else:
											helmetstring = player.gender + '_' + player.inventory.wearing['Head'].material + '_' + player.inventory.wearing['Head'].classe
											s.blit(gra_files.gdic['char'][helmetstring],(start_pos_x+((view_x-player.pos[0])*32),start_pos_y+((view_y-player.pos[1])*32)))
							
										if player.inventory.wearing['Body'] != player.inventory.nothing:
											armorstring = player.gender + '_' + player.inventory.wearing['Body'].material + '_' + player.inventory.wearing['Body'].classe
											s.blit(gra_files.gdic['char'][armorstring],(start_pos_x+((view_x-player.pos[0])*32),start_pos_y+((view_y-player.pos[1])*32)))
									
										if player.inventory.wearing['Legs'] != player.inventory.nothing:
											cuissestring = player.gender + '_' + player.inventory.wearing['Legs'].material + '_' + player.inventory.wearing['Legs'].classe
											s.blit(gra_files.gdic['char'][cuissestring],(start_pos_x+((view_x-player.pos[0])*32),start_pos_y+((view_y-player.pos[1])*32)))
								
										if player.inventory.wearing['Feet'] != player.inventory.nothing:
											shoestring = player.gender + '_' + player.inventory.wearing['Feet'].material + '_' + player.inventory.wearing['Feet'].classe
											s.blit(gra_files.gdic['char'][shoestring],(start_pos_x+((view_x-player.pos[0])*32),start_pos_y+((view_y-player.pos[1])*32)))
						
										if player.inventory.wearing['Hold(R)'] != player.inventory.nothing:
											weaponstring = 'WEAPONS_' + player.inventory.wearing['Hold(R)'].material + '_' + player.inventory.wearing['Hold(R)'].classe
											s.blit(gra_files.gdic['char'][weaponstring],(start_pos_x+((view_x-player.pos[0])*32),start_pos_y+((view_y-player.pos[1])*32)))
										
										if player.inventory.wearing['Hold(L)'] != player.inventory.nothing:
											weaponstring = 'WEAPONS_' + player.inventory.wearing['Hold(L)'].material + '_' + player.inventory.wearing['Hold(L)'].classe
											s.blit(gra_files.gdic['char'][weaponstring],(start_pos_x+((view_x-player.pos[0])*32),start_pos_y+((view_y-player.pos[1])*32)))					
										
								if c >= radius or world.maplist[player.pos[2]][player.on_map].tilemap[view_y][view_x].transparency == False:
									run = False
								else:
									c+=1
						
					elif t_known == 0:
						s.blit(gra_files.gdic['tile32'][0][3],(start_pos_x+((x-player.pos[0])*32),start_pos_y+((y-player.pos[1])*32)))
					else:
						s.blit(gra_files.gdic['tile32'][0][3],(start_pos_x+((x-player.pos[0])*32),start_pos_y+((y-player.pos[1])*32)))
					
				except:
					None	
		
		s.blit(self.render_hits(),(0,0))
		
		if self.fire_mode == 0:			 
			s.blit(gra_files.gdic['display'][0],(0,0)) #render gui
		else:
			s.blit(gra_files.gdic['display'][10],(0,0))
		
		#render lvl info
		
		lvl_string = str(player.lvl)
		if len(lvl_string) == 1:
			lvl_string = '0'+lvl_string
		lvl_image = self.font.render(lvl_string,1,(255,255,255))
		s.blit(lvl_image,(153,48))
		
		bar_length = 1 + ((319/100)*player.xp)
		xp_surface = pygame.Surface((bar_length,64))
		xp_surface.fill((255,0,255))
		xp_surface.blit(gra_files.gdic['display'][19],(0,0))
		xp_surface.set_colorkey((255,0,255),pygame.RLEACCEL)	
		xp_surface = xp_surface.convert_alpha()
		s.blit(xp_surface,(0,0))
		
		if game_options.mousepad == 1:
			if self.fire_mode == 0:
				s.blit(gra_files.gdic['display'][8],(480,0)) #render mouse pad
			else:
				s.blit(gra_files.gdic['display'][9],(480,0))
		else:
			s_help = pygame.Surface((160,360))
			s_help.fill((48,48,48))
			s.blit(s_help,(480,0))
		
		#render buffs
		
		buffs = player.buffs.sget()
		if low_res == False:
			posx = 388 
			posy = 10
		else:
			posx = 228
			posy = 65
		
		for i in buffs:
			if i != ' ':
				buff_shadow = self.font.render(i,1,(0,0,0))
				s.blit(buff_shadow,(posx+2,posy))
				buff_image = self.font.render(i,1,(200,200,200))
				s.blit(buff_image,(posx,posy))
			else:
				None
				
			posy += 20
		
		
		#render date
		
		date_string = time.sget()
		posx = 235
		posy = 10
		
		date_image = self.font.render(date_string[0],1,(0,0,0))
		s.blit(date_image,(posx,posy))
		posy = 20
		time_image = self.font.render(date_string[1],1,(0,0,0))
		s.blit(time_image,(posx,posy))
		
		#render player info
			#lp
		lp_string = str(player.lp) + '/' + str(player.attribute.max_lp)
			
		posx = 13
		posy = 12
		
		if player.lp < 4: 
			lp_image = self.font.render(lp_string,1,(200,0,0))
		else:
			lp_image = self.font.render(lp_string,1,(0,0,0))
		s.blit(lp_image,(posx,posy))
			
			#hunger
		
		hunger_percent = int((100 * player.attribute.hunger) / player.attribute.hunger_max)
		
		hunger_string = str(hunger_percent) + '%'
		
		posx = 75
		posy = 12
		
		hunger_image = self.font.render(hunger_string,1,(0,0,0))
		s.blit(hunger_image,(posx,posy))
		
			#trirst
			
		thirst_percent = int((100 * player.attribute.thirst) / player.attribute.thirst_max)
		
		thirst_string = str(thirst_percent) + '%'
		
		posx = 125
		posy = 12
		
		thirst_image = self.font.render(thirst_string,1,(0,0,0))
		s.blit(thirst_image,(posx,posy))
		
			#tiredness
			
		tiredness_percent = int((100 * player.attribute.tiredness) / player.attribute.tiredness_max)
		
		tiredness_string = str(tiredness_percent) + '%'
		
		posx = 180
		posy = 12
		
		tiredness_image = self.font.render(tiredness_string,1,(0,0,0))
		s.blit(tiredness_image,(posx,posy))
		
		# render messages
		
		if low_res == False:
			mes_pos_y_0 = 305
			mes_pos_y_1 = 335
		else:
			mes_pos_y_0 = 210
			mes_pos_y_1 = 225
		
		text_string1 = test[0]
		text_string2 = test[1]
		shadow_image1 = self.font.render(text_string1,1,(0,0,0))
		shadow_image2 = self.font.render(text_string2,1,(0,0,0))
		s.blit(shadow_image1,(2,mes_pos_y_0))
		s.blit(shadow_image2,(2,mes_pos_y_1))
		text_image1 = self.font.render(text_string1,1,(255,255,255))
		text_image2 = self.font.render(text_string2,1,(255,255,255))
		s.blit(text_image1,(0,mes_pos_y_0))
		s.blit(text_image2,(0,mes_pos_y_1))
		
		if game_options.mousepad == 0 and low_res == False:
			s_help = pygame.Surface((640,360))
			s_help.fill((48,48,48))
			s_help.blit(s,(80,0))
			s = s_help		
		if low_res == False:
			s = pygame.transform.scale(s,(self.displayx,self.displayy))
		
		self.screen.blit(s,(0,0))
		
		if simulate == False:	
			pygame.display.flip()
		
		if test[1] == '~*~':
			return True
		else:
			return False
	
	def render_load(self,num):
		
		s = pygame.Surface((640,360))
		
		s.fill((48,48,48)) #paint it grey(to clear the screen)
		
		if num == 0:
			string = 'Looking for saved data... '
		elif num == 1:
			string = 'Loading world data...'
		elif num == 2:
			string = 'Nothing found...'
		elif num == 3:
			string = 'Generate overworld...'
		elif num == 4:
			string = 'Generate caves...'
		elif num == 5:
			string = 'Saving...'
		elif num == 6:
			string = 'Loading time data...'
		elif num == 7:
			string = 'Loading player data...'
		elif num == 8:
			string = 'Set time...'
		elif num == 9:
			string = 'Generate player...'
		elif num == 10:
			string = 'Making time related changes...'
		elif num == 11:
			string = 'Something has gone wrong...'	
		elif num == 12:
			string = 'Zzzzzzzzzz'
		elif num == 13:
			string = 'Generate deus ex machina...'
		elif num == 14:
			string = 'Loading deus ex machina...'
		elif num == 15:
			string = 'Generate grot...'
		elif num == 16:
			string = 'Generate elfish fortress...'
		elif num == 17:
			string = 'Generate orcish mines...'
		elif num == 18:
			string = 'Generate desert...'
		
		######add more here
		
		posx = 150
		posy = 200
		
		image = self.menu_font.render(string,1,(255,255,255))
		s.blit(image,(posx,posy))
		
		s = pygame.transform.scale(s,(self.displayx,self.displayy))
		
		self.screen.blit(s,(0,0))
			
		pygame.display.flip()
			
	def render_built(self,xmin,xmax,ymin,ymax,style):
		
		if low_res == False:
			start_pos_x = 240 #the center of the main map view
			start_pos_y = 180
		else:
			start_pos_x = 152 #the center of the main map view
			start_pos_y = 122
		
		price = 0
		
		self.render(0, True)
		
		s = pygame.Surface((640,360))
		s.fill((255,0,255))
		
		if style == 'wall':
			
			for y in range (-ymin,ymax+1):
				for x in range (-xmin,xmax+1):
				
					if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].move_group == 'soil' and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].damage == False and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].civilisation == False and world.maplist[player.pos[2]][player.on_map].npcs[player.pos[1]+y][player.pos[0]+x] == 0:
						built_here = 1
						price += 2
					elif world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].civilisation == True:
						built_here = 2
						price += 1
					else: 
						built_here = 0
						
					if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].build_here == False:
						if built_here == 1:
							price -= 2 
						elif built_here == 2:
							price -= 1
						built_here = 0
							
					if built_here != 0:
					
						if x == xmax or x == -xmin or y == ymax or y == -ymin:
							if x == xmax or x == -xmin:
								if built_here == 1:
									s.blit(gra_files.gdic['built'][1],(start_pos_x+(x*32),start_pos_y+(y*32))) #wall_true here
								elif built_here == 2:
									s.blit(gra_files.gdic['built'][6],(start_pos_x+(x*32),start_pos_y+(y*32))) #wall_over here
							if y == ymax or y == -ymin:
								if built_here == 1:
									s.blit(gra_files.gdic['built'][1],(start_pos_x+(x*32),start_pos_y+(y*32))) #wall_true here
								elif built_here == 2:
									s.blit(gra_files.gdic['built'][6],(start_pos_x+(x*32),start_pos_y+(y*32))) #wall_over here
						else:
							
							None
									
					else:
					
						if x == xmax or x == -xmin or y == ymax or y == -ymin:
							if x == xmax or x == -xmin:
								s.blit(gra_files.gdic['built'][0],(start_pos_x+(x*32),start_pos_y+(y*32))) #wall_false here
					
							if y == ymax or y == -ymin:
								s.blit(gra_files.gdic['built'][0],(start_pos_x+(x*32),start_pos_y+(y*32))) #wall_false here
						else:
								None
		
			s.blit(gra_files.gdic['display'][5],(0,0)) #render gui_transparent over gui
		
			# render mode name
			
			name = '~Build Walls~'
			name_image = self.font.render(name,1,(255,255,255))
			
			posx = 0
			posy = 0
			
			s.blit(name_image,(posx,posy))
		
			# render wood needed
		
			wood_need = price/3 
			if wood_need == 0:
				wood_need = 1
			wood_string = 'Wood: ' + str(wood_need) + '(' + str(player.inventory.materials.wood) + ')' 
		
			posx = 0
			posy = 15
		
			if wood_need <= player.inventory.materials.wood:
				wood_image = self.font.render(wood_string,1,(255,255,255))
			else:
				wood_image = self.font.render(wood_string,1,(200,0,0))
			
			s.blit(wood_image,(posx,posy))
		
			# render stone needed
		
			stone_need = price/2
			if stone_need == 0:
				stone_need = 1
			stone_string = 'Stone: ' + str(stone_need) + '(' + str(player.inventory.materials.stone) + ')' 
		
			posx = 160
			posy = 15
		
			if stone_need <= player.inventory.materials.stone:
				stone_image = self.font.render(stone_string,1,(255,255,255))
			else:
				stone_image = self.font.render(stone_string,1,(200,0,0))
			
			s.blit(stone_image,(posx,posy))
			
			# render info line
			
			info_string_0 = '[w,a,s,d]ch. Size [b]ch. Mode' 
			info_string_1 = '[x]Leave [e]BUILT!' 
		
			posx = 0
			posy = 30
		
			info_image = self.font.render(info_string_0,1,(255,255,255))
			s.blit(info_image,(posx,posy))
			
			posx = 0
			posy = 40
		
			info_image = self.font.render(info_string_1,1,(255,255,255))
			s.blit(info_image,(posx,posy))
			
		elif style == 'floor':
			
			for y in range (-ymin,ymax+1):
				for x in range (-xmin,xmax+1):
				
					if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].move_group == 'soil' and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].damage == False and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].civilisation == False and world.maplist[player.pos[2]][player.on_map].npcs[player.pos[1]+y][player.pos[0]+x] == 0:
						built_here = 1
						price += 2
					elif world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].civilisation == True:
						built_here = 2
						price += 1
					else: 
						built_here = 0
						
					if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].build_here == False:
						if built_here == 1:
							price -= 2 
						elif built_here == 2:
							price -= 1
						built_here = 0
							
					if built_here != 0:
					
						
						if built_here == 1:
							s.blit(gra_files.gdic['built'][5],(start_pos_x+(x*32),start_pos_y+(y*32))) #floor_true here
						elif built_here == 2:
							s.blit(gra_files.gdic['built'][7],(start_pos_x+(x*32),start_pos_y+(y*32))) #floor_over
									
					else:
					
						s.blit(gra_files.gdic['built'][4],(start_pos_x+(x*32),start_pos_y+(y*32))) #floor_false here
		
			s.blit(gra_files.gdic['display'][5],(0,0)) #render gui_transparent over gui
			
			# render mode name
			
			name = '~Build Floor~'
			name_image = self.font.render(name,1,(255,255,255))
			
			posx = 0
			posy = 0
			
			s.blit(name_image,(posx,posy))
			
			# render wood needed
		
			wood_need = price/2 
			if wood_need == 0:
				wood_need = 1
			wood_string = 'Wood: ' + str(wood_need) + '(' + str(player.inventory.materials.wood) + ')' 
		
			posx = 0
			posy = 15
		
			if wood_need <= player.inventory.materials.wood:
				wood_image = self.font.render(wood_string,1,(255,255,255))
			else:
				wood_image = self.font.render(wood_string,1,(200,0,0))
			
			s.blit(wood_image,(posx,posy))
		
			# render stone needed
		
			stone_need = price/3
		
			stone_string = 'Stone: ' + str(stone_need) + '(' + str(player.inventory.materials.stone) + ')' 
		
			posx = 160
			posy = 15
		
			if stone_need <= player.inventory.materials.stone:
				stone_image = self.font.render(stone_string,1,(255,255,255))
			else:
				stone_image = self.font.render(stone_string,1,(200,0,0))
			
			s.blit(stone_image,(posx,posy))
			
			# render info line
			
			info_string_0 = '[w,a,s,d]ch. Size [b]ch. Mode'
			info_string_1 = '[x]Leave [e]BUILT!' 
		
			posx = 0
			posy = 30
		
			info_image = self.font.render(info_string_0,1,(255,255,255))
			s.blit(info_image,(posx,posy))
			
			posx = 0
			posy = 40
		
			info_image = self.font.render(info_string_1,1,(255,255,255))
			s.blit(info_image,(posx,posy))
		
		elif style == 'Door':
			
			if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].move_group == 'soil' and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].damage == False and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].civilisation == False and world.maplist[player.pos[2]][player.on_map].npcs[player.pos[1]+ymin][player.pos[0]+xmin] == 0:
				built_here = 1
				price += 2
			elif world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].civilisation == True:
				built_here = 2
				price += 1
			else: 
				built_here = 0
						
			if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].build_here == False:
				if built_here == 1:
					price -= 2 
				elif built_here == 2:
					price -= 1
				built_here = 0
			
			if built_here != 0:
				if built_here == 1:
					s.blit(gra_files.gdic['built'][3],(start_pos_x+(xmin*32),start_pos_y+(ymin*32))) #door_true here
				elif built_here == 2:
					s.blit(gra_files.gdic['built'][8],(start_pos_x+(xmin*32),start_pos_y+(ymin*32))) #door_over
				
			else:
				s.blit(gra_files.gdic['built'][2],(start_pos_x+(xmin*32),start_pos_y+(ymin*32))) #door_false here		
		
			s.blit(gra_files.gdic['display'][5],(0,0)) #render gui_transparent over gui
		
			# render mode name
			
			name = '~Built Door~'
			name_image = self.font.render(name,1,(255,255,255))
			
			posx = 0
			posy = 0
			
			s.blit(name_image,(posx,posy))
			
			# render wood needed
				
			wood_need = price
		
			wood_string = 'Wood: ' + str(wood_need) + '(' + str(player.inventory.materials.wood) + ')' 
		
			posx = 0
			posy = 15
		
			if wood_need <= player.inventory.materials.wood:
				wood_image = self.font.render(wood_string,1,(255,255,255))
			else:
				wood_image = self.font.render(wood_string,1,(200,0,0))
			
			s.blit(wood_image,(posx,posy))
		
			# render stone needed
		
			stone_need = 0
		
			stone_string = 'Stone: ' + str(stone_need) + '(' + str(player.inventory.materials.stone) + ')' 
		
			posx = 160
			posy = 15
		
			if stone_need <= player.inventory.materials.stone:
				stone_image = self.font.render(stone_string,1,(255,255,255))
			else:
				stone_image = self.font.render(stone_string,1,(200,0,0))
			
			s.blit(stone_image,(posx,posy))
			
			# render info line
			
			info_string_0 = '[w,a,s,d]ch. Pos. [b]ch. Mode'
			info_string_1 = '[x]Leave [e]BUILT!' 
		
			posx = 0
			posy = 30
		
			info_image = self.font.render(info_string_0,1,(255,255,255))
			s.blit(info_image,(posx,posy))
			
			posx = 0
			posy = 40
		
			info_image = self.font.render(info_string_1,1,(255,255,255))
			s.blit(info_image,(posx,posy))
			
			pygame.display.flip()
		
		elif style == 'Stair up':

			if player.pos[2] > 0:
					
				if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].replace == None and world.maplist[player.pos[2]-1][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].build_here == True and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].build_here == True and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].move_group == 'soil' and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].damage == False:
					build_here = 0
				else: 
					build_here = 1
							
				if build_here == 0:
					s.blit(gra_files.gdic['built'][10],(start_pos_x+(xmin*32),start_pos_y+(ymin*32))) #stair up true icon here
				else:
					s.blit(gra_files.gdic['built'][11],(start_pos_x+(xmin*32),start_pos_y+(ymin*32))) #stair up false icon here
			else:
				s.blit(gra_files.gdic['built'][11],(start_pos_x+(xmin*32),start_pos_y+(ymin*32))) #stair up false icon here
			
			s.blit(gra_files.gdic['display'][5],(0,0)) #render gui_transparent over gui
		
			# render mode name
			
			name = '~Built stair up~'
			name_image = self.font.render(name,1,(255,255,255))
			
			posx = 0
			posy = 0
			
			s.blit(name_image,(posx,posy))
			
			# render wood needed
				
			wood_need = 10 
		
			wood_string = 'Wood: ' + str(wood_need) + '(' + str(player.inventory.materials.wood) + ')' 
		
			posx = 0
			posy = 15
		
			if wood_need <= player.inventory.materials.wood:
				wood_image = self.font.render(wood_string,1,(255,255,255))
			else:
				wood_image = self.font.render(wood_string,1,(200,0,0))
			
			s.blit(wood_image,(posx,posy))
		
			# render stone needed
		
			stone_need = 40
		
			stone_string = 'Stone: ' + str(stone_need) + '(' + str(player.inventory.materials.stone) + ')' 
		
			posx = 160
			posy = 15
		
			if stone_need <= player.inventory.materials.stone:
				stone_image = self.font.render(stone_string,1,(255,255,255))
			else:
				stone_image = self.font.render(stone_string,1,(200,0,0))
			
			s.blit(stone_image,(posx,posy))
			
			# render info line
			
			info_string_0 = '[w,a,s,d]ch. Pos. [b]ch. Mode'
			info_string_1 = '[x]Leave [e]BUILT!' 
		
			posx = 0
			posy = 30
		
			info_image = self.font.render(info_string_0,1,(255,255,255))
			s.blit(info_image,(posx,posy))
			
			posx = 0
			posy = 40
		
			info_image = self.font.render(info_string_1,1,(255,255,255))
			s.blit(info_image,(posx,posy))
			
			pygame.display.flip()
			
		elif style == 'Stair down':
			
			if player.pos[2] < 15:
				
				if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].replace == None and world.maplist[player.pos[2]+1][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].build_here == True and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].build_here == True and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].move_group == 'soil' and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].damage == False:
					build_here = 0
				else: 
					build_here = 1
							
				if build_here == 0:
					s.blit(gra_files.gdic['built'][12],(start_pos_x+(xmin*32),start_pos_y+(ymin*32))) #stair up true icon here
				else:
					s.blit(gra_files.gdic['built'][13],(start_pos_x+(xmin*32),start_pos_y+(ymin*32))) #stair up false icon here
			else:
				s.blit(gra_files.gdic['built'][12],(start_pos_x+(xmin*32),start_pos_y+(ymin*32))) #stair up false icon here
			
			s.blit(gra_files.gdic['display'][5],(0,0)) #render gui_transparent over gui
		
			# render mode name
			
			name = '~Built stair down~'
			name_image = self.font.render(name,1,(255,255,255))
			
			posx = 0
			posy = 0
			
			s.blit(name_image,(posx,posy))
			
			# render wood needed
				
			wood_need = 10 
		
			wood_string = 'Wood: ' + str(wood_need) + '(' + str(player.inventory.materials.wood) + ')' 
		
			posx = 0
			posy = 15
		
			if wood_need <= player.inventory.materials.wood:
				wood_image = self.font.render(wood_string,1,(255,255,255))
			else:
				wood_image = self.font.render(wood_string,1,(200,0,0))
			
			s.blit(wood_image,(posx,posy))
		
			# render stone needed
			if player.pos[2] > 0:
				stone_need = 40
			else:
				stone_need = 15
		
			stone_string = 'Stone: ' + str(stone_need) + '(' + str(player.inventory.materials.stone) + ')' 
		
			posx = 160
			posy = 15
		
			if stone_need <= player.inventory.materials.stone:
				stone_image = self.font.render(stone_string,1,(255,255,255))
			else:
				stone_image = self.font.render(stone_string,1,(200,0,0))
			
			s.blit(stone_image,(posx,posy))
			
			# render info line
			
			info_string_0 = '[w,a,s,d]ch. Pos. [b]ch. Mode'
			info_string_1 = '[x]Leave [e]BUILT!' 
		
			posx = 0
			posy = 30
		
			info_image = self.font.render(info_string_0,1,(255,255,255))
			s.blit(info_image,(posx,posy))
			
			posx = 0
			posy = 40
		
			info_image = self.font.render(info_string_1,1,(255,255,255))
			s.blit(info_image,(posx,posy))
			
			pygame.display.flip()
		
		elif style == 'Agriculture':
			
			for y in range (-ymin,ymax+1):
				for x in range (-xmin,xmax+1):
				
					if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].move_group == 'soil' and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].damage == False and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].civilisation == False and world.maplist[player.pos[2]][player.on_map].npcs[player.pos[1]+y][player.pos[0]+x] == 0:
						built_here = 1
						price += 1
					elif world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].civilisation == True:
						built_here = 2
						price += 1
					else: 
						built_here = 0
						
					if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].build_here == False:
						if built_here == 1:
							price -= 2 
						elif built_here == 2:
							price -= 1
						built_here = 0
							
					if built_here != 0:
					
						
						if built_here == 1:
							s.blit(gra_files.gdic['built'][15],(start_pos_x+(x*32),start_pos_y+(y*32))) #floor_true here
						elif built_here == 2:
							s.blit(gra_files.gdic['built'][16],(start_pos_x+(x*32),start_pos_y+(y*32))) #floor_over
									
					else:
					
						s.blit(gra_files.gdic['built'][14],(start_pos_x+(x*32),start_pos_y+(y*32))) #floor_false here
		
			s.blit(gra_files.gdic['display'][5],(0,0)) #render gui_transparent over gui
			
			# render mode name
			
			name = '~Build Agriculture~'
			name_image = self.font.render(name,1,(255,255,255))
			
			posx = 0
			posy = 0
			
			s.blit(name_image,(posx,posy))
			
			# render seeds needed
		
			seed_need = price 
			if seed_need == 0:
				seed_need = 1
			wood_need = seed_need
			stone_need = 0
			wood_string = 'Seeds: ' + str(seed_need) + '(' + str(player.inventory.materials.seeds) + ')' 
		
			posx = 120
			posy = 15
		
			if wood_need <= player.inventory.materials.wood:
				wood_image = self.font.render(wood_string,1,(255,255,255))
			else:
				wood_image = self.font.render(wood_string,1,(200,0,0))
			
			s.blit(wood_image,(posx,posy))
			
			# render info line
			
			info_string_0 = '[w,a,s,d]ch. Size [b]ch. Mode'
			info_string_1 = '[x]Leave [e]BUILT!' 
		
			posx = 0
			posy = 30
		
			info_image = self.font.render(info_string_0,1,(255,255,255))
			s.blit(info_image,(posx,posy))
			
			posx = 0
			posy = 40
		
			info_image = self.font.render(info_string_1,1,(255,255,255))
			s.blit(info_image,(posx,posy))
					
		elif style == 'remove':
			
			for y in range (-ymin,ymax+1):
				for x in range (-xmin,xmax+1):
				
					if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].civilisation == True and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].build_here == True:
						remove_here = 0
					else: 
						remove_here = 1
							
					if remove_here == 0:
						s.blit(gra_files.gdic['built'][9],(start_pos_x+(x*32),start_pos_y+(y*32))) #remove icon here
					else:
						None
			
			s.blit(gra_files.gdic['display'][5],(0,0)) #render gui_transparent over gui
		
			# render mode name
			
			name = '~Remove~'
			name_image = self.font.render(name,1,(255,255,255))
			
			posx = 0
			posy = 0
			
			s.blit(name_image,(posx,posy))
			
			# render ---
				
			wood_string = '---' 
		
			posx = 120
			posy = 15
		
			wood_image = self.font.render(wood_string,1,(255,255,255))
			
			s.blit(wood_image,(posx,posy))
			
			# render info line
			
			info_string_0 = '[w,a,s,d]ch. Size [b]ch. Mode'
			info_string_1 = '[x]Leave [e]BUILT!' 
		
			posx = 0
			posy = 30
		
			info_image = self.font.render(info_string_0,1,(255,255,255))
			s.blit(info_image,(posx,posy))
			
			posx = 0
			posy = 40
		
			info_image = self.font.render(info_string_1,1,(255,255,255))
			s.blit(info_image,(posx,posy))
			
			wood_need = 0
			stone_need = 0
		
		if game_options.mousepad == 0 and low_res == False:
			s_help = pygame.Surface((640,360))
			s_help.fill((255,0,255))
			s_help.blit(s,(80,0))
			s = s_help
			
		s.set_colorkey((255,0,255),pygame.RLEACCEL)	
		s = s.convert_alpha()
		if low_res == False:
			s = pygame.transform.scale(s,(self.displayx,self.displayy))
		
		self.screen.blit(s,(0,0))
		
		pygame.display.flip()
		
		
		return (wood_need,stone_need)
		
	def render_request(self,line1,line2,line3):
		#this function just renders 3 lines of text in the textbox
		
		self.render(0, True)
		
		s = pygame.Surface((640,360))
		s.fill((255,0,255))
		
		s.blit(gra_files.gdic['display'][5],(0,0)) #render gui_transparent over gui
		
		# render lines
			
		line1_image = self.font.render(line1,1,(255,255,255))
			
		posx = 0
		posy = 0
			
		s.blit(line1_image,(posx,posy))
			
		line2_image = self.font.render(line2,1,(255,255,255))
		
		posx = 0
		posy = 20
		
		s.blit(line2_image,(posx,posy))
			
			
		line3_image = self.font.render(line3,1,(255,255,255)) 
		
		posx = 0
		posy = 40
		
		s.blit(line3_image,(posx,posy))
		
		if game_options.mousepad == 0:
			s_help = pygame.Surface((640,360))
			s_help.fill((255,0,255))
			s_help.blit(s,(80,0))
			s = s_help
		
		s.set_colorkey((255,0,255),pygame.RLEACCEL)	
		s = s.convert_alpha()
		s = pygame.transform.scale(s,(self.displayx,self.displayy))
		self.screen.blit(s,(0,0))
			
		pygame.display.flip()

	def render_map(self,level=0):
		
		run = True
		
		while run:
			
			m = pygame.Surface((max_map_size,max_map_size))
		
			for y in range(0,max_map_size):
				for x in range(0,max_map_size):
					
					t_col = world.maplist[level][player.on_map].tilemap[y][x].tile_color
					
					if x > player.pos[0]-2 and x < player.pos[0]+2 and y > player.pos[1]-2 and y < player.pos[1]+2 and level == player.pos[2]: #mark players pos
						m.blit(gra_files.gdic['tile1']['white'],(x,y))
					else:
						if world.maplist[level][player.on_map].known[y][x] == 1:
							m.blit(gra_files.gdic['tile1'][t_col],(x,y))
						elif world.maplist[level][player.on_map].known[y][x] == 0:
							m.blit(gra_files.gdic['tile1']['black'],(x,y))
						else:
							m.blit(gra_files.gdic['tile1']['black'],(x,y))
						
			m = pygame.transform.scale(m,(270,270))
			
			s = pygame.Surface((640,360))
			s.blit(gra_files.gdic['display'][1],(0,0)) #render background
			if game_options.mousepad == 1:
				s.blit(gra_files.gdic['display'][8],(480,0)) #render mouse pad
			else:
				s_help = pygame.Surface((160,360))
				s_help.fill((48,48,48))
				s.blit(s_help,(480,0))
			
			text_image = screen.menu_font.render('~*~ Map ~*~        [Press [x] to leave]',1,(255,255,255))
			s.blit(text_image,(5,2))#menue title
			
			lvl_string = 'Level ' + str(level)
			text_image = screen.menu_font.render(lvl_string,1,(0,0,0))
			s.blit(text_image,(300,70))
			
			text_image = screen.menu_font.render('[w] - lvl. up [s] - lvl. down',1,(255,255,255))
			s.blit(text_image,(5,335))
			
			s.blit(m,(25,55))
			
			if game_options.mousepad == 0:
				s_help = pygame.Surface((640,360))
				s_help.fill((48,48,48))
				s_help.blit(s,(80,0))
				s = s_help
			
			s = pygame.transform.scale(s,(self.displayx,self.displayy))
			self.screen.blit(s,(0,0))
			
			pygame.display.flip()
			
			ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
			
			if ui == 's':
				if level < len(world.maplist)-1:
					level += 1
			elif ui == 'w':
				if level > 0:
					level -=1		
			elif ui == 'x':
				run = False
	
	def render_credits(self):
		
		run = True
		
		while run:
			
			s = pygame.Surface((640,360))
			s.blit(gra_files.gdic['display'][1],(0,0)) #render background
			if game_options.mousepad == 1:
				s.blit(gra_files.gdic['display'][8],(480,0)) #render mouse pad
			else:
				s_help = pygame.Surface((160,360))
				s_help.fill((48,48,48))
				s.blit(s_help,(480,0))
			
			text_image = screen.menu_font.render('~*~ Credits ~*~        [Press [x] to leave]',1,(255,255,255))
			s.blit(text_image,(5,2))#menue title
			
			credit_items = ('Idea & Code: Marian Luck aka Nothing', 'BGM: Yubatake & Avgvsta [opengameart.org]' , 'SFX: Little Robot Sound Factory', 'Font: Cody Boisclair' )
		
			for i in range (0,len(credit_items)):
			
				text_image = screen.menu_font.render(credit_items[i],1,(0,0,0))
				s.blit(text_image,(21,120+i*25))#blit credit_items
			
			if game_options.mousepad == 0:
				s_help = pygame.Surface((640,360))
				s_help.fill((48,48,48))
				s_help.blit(s,(80,0))
				s = s_help
				
			s = pygame.transform.scale(s,(self.displayx,self.displayy))
			self.screen.blit(s,(0,0))
			
			pygame.display.flip()
			
			ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
			
			if ui == 'x':
				run = False
			
					  
	def render_options(self):
		
		run = True
		num = 0
		
		while run:
			
			s = pygame.Surface((640,360))
			if low_res == False:
				if game_options.screenmode == 1:
					winm = 'Screenmode: Fullscreen'
				else:
					winm = 'Screenmode: Windowed'
			else:
				winm = '----------'
				
			
			if game_options.bgmmode == 1:
				audiom = 'BGM: ON'
			else:
				audiom = 'BGM: OFF'
				
			if game_options.sfxmode == 1:
				sfxm = 'SFX: ON'
			else:
				sfxm = 'SFX: OFF'
			
			if game_options.turnmode == 1:
				turnm = 'Gamemode: Semi-Realtime'
			else:
				turnm = 'Gamemode: Turnbased'
			
			if low_res == False:	
				if game_options.mousepad == 1:
					mousem = 'Use Mouse: yes'
				else:
					mousem = 'Use Mouse: no'
			else:
				mousem = '----------'
			
			s.blit(gra_files.gdic['display'][1],(0,0)) #render background
		
			text_image = screen.font.render('~*~ Options ~*~        [Press [e] to choose]',1,(255,255,255))
			s.blit(text_image,(5,2))#menue title
		
			menu_items = (winm,audiom,sfxm,turnm,mousem,'Done')
		
			for i in range (0,len(menu_items)):
			
				text_image = screen.menu_font.render(menu_items[i],1,(0,0,0))
				s.blit(text_image,(21,120+i*25))#blit menu_items
			
			s.blit(gra_files.gdic['display'][4],(0,112+num*25))#blit marker
		
			if game_options.mousepad == 1:
				s.blit(gra_files.gdic['display'][8],(480,0)) #render mouse pad
			else:
				s_help = pygame.Surface((160,360))
				s_help.fill((48,48,48))
				s.blit(s_help,(480,0))
			
			if game_options.mousepad == 0:
				s_help = pygame.Surface((640,360))
				s_help.fill((48,48,48))
				s_help.blit(s,(80,0))
				s = s_help
			
			s = pygame.transform.scale(s,(self.displayx,self.displayy))
			self.screen.blit(s,(0,0))
			
			pygame.display.flip()
			
			ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
		
			if ui == 'w':
				num -= 1
				if num < 0:
					num = len(menu_items)-1
				
			if ui == 's':
				num += 1
				if num >= len(menu_items):
					num = 0
			
			if ui == 'x':
				run = False
			
			if ui == 'e':
				
				if num == 0 and low_res == False:
					screen.re_init()
					pygame.display.flip()
					game_options.save()
					
				if num == 1:
					if game_options.bgmmode == 1:
						game_options.bgmmode = 0
						pygame.mixer.music.pause()
					else:
						game_options.bgmmode = 1
						pygame.mixer.music.unpause()
						bgm.check_for_song()
						
					game_options.save()
						
				if num == 2:
					if game_options.sfxmode == 1:
						game_options.sfxmode = 0
					else:
						game_options.sfxmode = 1
						
					game_options.save()
				
				if num == 3:
					if game_options.turnmode == 1:
						game_options.turnmode = 0
					else:
						game_options.turnmode = 1
						
					game_options.save()
				
				if num == 4 and low_res == False:
					if game_options.mousepad == 1:
						game_options.mousepad = 0
					else:
						game_options.mousepad = 1
						
					game_options.save()
					
				if num == 5:
					run = False
					
			
	def render_brake(self):
		
		run = True
		num = 0
		global exitgame
		global playing
		
		while run:
			
			s = pygame.Surface((640,360))
			
			s.blit(gra_files.gdic['display'][1],(0,0)) #render background
		
			text_image = screen.menu_font.render('~*~ Game Paused ~*~        [Press [e] to choose]',1,(255,255,255))
			s.blit(text_image,(5,2))#menue title
		
			menu_items = ('Resume','Map','Message History','Save and Exit', 'Options',)
		
			for i in range (0,len(menu_items)):
			
				text_image = screen.menu_font.render(menu_items[i],1,(0,0,0))
				s.blit(text_image,(21,120+i*25))#blit menu_items
			
			s.blit(gra_files.gdic['display'][4],(0,112+num*25))#blit marker
			
			if game_options.mousepad == 1:
				s.blit(gra_files.gdic['display'][8],(480,0)) #render mouse pad
			else:
				s_help = pygame.Surface((160,360))
				s_help.fill((48,48,48))
				s.blit(s_help,(480,0))
				
			if game_options.mousepad == 0:
				s_help = pygame.Surface((640,360))
				s_help.fill((48,48,48))
				s_help.blit(s,(80,0))
				s = s_help
			
			s = pygame.transform.scale(s,(self.displayx,self.displayy))
			self.screen.blit(s,(0,0))
			
			pygame.display.flip()
		
			ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
		
			if ui == 'w':
				num -= 1
				if num < 0:
					num = len(menu_items)-1
				
			if ui == 's':
				num += 1
				if num >= len(menu_items):
					num = 0
			
			if ui == 'x':
				run = False
			
			if ui == 'e':
				
				if num == 0:
					run = False
					
				if num == 1:
					screen.render_map(player.pos[2])
					
				if num == 2:
					message.render_history()
					
				if num == 3:
					exitgame = True
					screen.render_load(5)
					save(world,player,time,gods,save_path,os.sep)
					screen.save_tmp_png()
					playing = False
					run = False
					
				if num == 4:
					screen.render_options()
											
		return exitgame
	
	def get_choice(self,headline,choices,allow_chancel,style='Default'): 
		
		#this function allows the player to make a coice. The choices-variable is a tulpel with strings. The function returns the number of the choosen string inside the tulpel
		
		run = True
		num = 0
		
		while run:
			
			s = pygame.Surface((640,360))
			
			if style == 'Default':
				s.blit(gra_files.gdic['display'][1],(0,0)) #render background
			elif style == 'Warning':
				s.blit(gra_files.gdic['display'][17],(0,0))
		
			text_image = screen.menu_font.render(headline,1,(255,255,255))
			s.blit(text_image,(5,2))#menue title
		
			menu_items = choices
		
			for i in range (0,len(menu_items)):
			
				text_image = screen.menu_font.render(menu_items[i],1,(0,0,0))
				s.blit(text_image,(21,120+i*25))#blit menu_items
			
			if allow_chancel == True:
				text_image = screen.menu_font.render('[e] - choose [x] - leave',1,(255,255,255))
				s.blit(text_image,(5,335))
			else:
				text_image = screen.menu_font.render('[e] - choose',1,(255,255,255))
				s.blit(text_image,(5,335))
			
			if style == 'Default':
				s.blit(gra_files.gdic['display'][4],(0,112+num*25))#blit marker
			elif style == 'Warning':
				s.blit(gra_files.gdic['display'][18],(0,112+num*25))#blit marker
			
			if game_options.mousepad == 1:
				s.blit(gra_files.gdic['display'][8],(480,0)) #render mouse pad
			else:
				s_help = pygame.Surface((160,360))
				s_help.fill((48,48,48))
				s.blit(s_help,(480,0))
			
			if game_options.mousepad == 0:
				s_help = pygame.Surface((640,360))
				s_help.fill((48,48,48))
				s_help.blit(s,(80,0))
				s = s_help
			
			s = pygame.transform.scale(s,(screen.displayx,screen.displayy))
			screen.screen.blit(s,(0,0))
			
			pygame.display.flip()
		
			ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
		
			if ui == 'w':
				num -= 1
				if num < 0:
					num = len(menu_items)-1
				
			if ui == 's':
				num += 1
				if num >= len(menu_items):
					num = 0
				
			if ui == 'e':
				run = False
				return num
				
			if ui == 'x' and allow_chancel == True:
				run = False
				return 'Break' 
		
	def string_input(self, input_message, length):			
			
		run = True
		string = ''
		pos = 0
		x = 0
		y = 0
			
		char_field = (('A','B','C','D','E','F','G','H','a','b','c','d','e','f','g','h'),('I','J','K','L','M','N','O','P','i','j','k','l','m','n','o','p'),('Q','R','S','T','U','V','W','X','q','r','s','t','u','v','w','x'),('Y','Z','y','z','0','1','2','3','4','5','6','7','8','9', '.',','),('(','[','<','{',')',']','>','}','#','+','-','_','*','/','&','%'))
			
		while run:
			
			s = pygame.Surface((640,360))
			
			s.blit(gra_files.gdic['display'][1],(0,0)) #render background
	
			text_image = screen.font.render(input_message,1,(255,255,255))
			s.blit(text_image,(5,2))#menue title
			
			num_stars = length - len(string)
			
			star_string = ''
			
			if num_stars > 0:
				
				for i in range (0,num_stars):
					star_string += '*'
			
			shown_string = string + '_' + star_string 
			
			string_image = screen.font.render(shown_string,1,(255,255,255))
			s.blit(string_image,(5,35))#string so far
				
			for i in range (0,5):#blit chars
				for j in range (0,16):
						
					if i == y and j == x: 
						char_image = screen.font.render(char_field[i][j],1,(255,255,255))
					else:
						char_image = screen.font.render(char_field[i][j],1,(0,0,0))
							
					s.blit(char_image,(55+(j*20),150+(i*20)))
			
			if game_options.mousepad == 1:			
				s.blit(gra_files.gdic['display'][8],(480,0)) #render mouse pad
			else:
				s_help = pygame.Surface((160,360))
				s_help.fill((48,48,48))
				s.blit(s_help,(480,0))
			
			text_image = screen.font.render('[e] - Add Char [b] - Done [x] - Reset',1,(255,255,255))
			s.blit(text_image,(5,335))
			
			if game_options.mousepad == 0:
				s_help = pygame.Surface((640,360))
				s_help.fill((48,48,48))
				s_help.blit(s,(80,0))
				s = s_help
			
			s = pygame.transform.scale(s,(screen.displayx,screen.displayy))
			screen.screen.blit(s,(0,0))
				
			pygame.display.flip()
						
			ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
		
			if ui == 'w':
				y -= 1
				if y < 0:
					y = 4
				
			if ui == 's':
				y += 1
				if y > 4:
					y = 0
				
			if ui == 'a':
				x -= 1
				if x < 0:
					x = 15
				
			if ui == 'd':
				x += 1
				if x > 15:
					x = 0
				
			if ui == 'e':
					
				if pos <= length:
					string += char_field[y][x]
					pos += 1
						
			if ui == 'b':
				run = False
				
			if ui == 'x':
				pos = 0
				string = ''
					
		return string
		
	def render_dead(self):
		
		global exitgame
		run = True
		
		while run:
			s = pygame.Surface((640,360))
			
			s.fill((48,48,48)) #paint it grey(to clear the screen)
		
			text_image = screen.menu_font.render('YOU ARE DEAD!',1,(255,255,255))
			s.blit(text_image,(175,60))
		
			if player.difficulty == 3: #you play on roguelike mode
				choose_string = '------------- [x] - END GAME'
			else:#you play on a other mode
				choose_string = '[e] - RESPAWN [x] - END GAME'  
		
			choose_image = screen.menu_font.render(choose_string,1,(255,255,255))
			s.blit(choose_image,(125,200))
			
			if game_options.mousepad == 1:
				s.blit(gra_files.gdic['display'][8],(480,0)) #render mouse pad
			else:
				s_help = pygame.Surface((160,360))
				s_help.fill((48,48,48))
				s.blit(s_help,(480,0))
			
			if game_options.mousepad == 0:
				s_help = pygame.Surface((640,360))
				s_help.fill((48,48,48))
				s_help.blit(s,(80,0))
				s = s_help
			
			s = pygame.transform.scale(s,(screen.displayx,screen.displayy))
			screen.screen.blit(s,(0,0))
			
			pygame.display.flip()
		
			ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
		
			if ui == 'e' and player.difficulty != 3:
				player.respawn()
				save(world,player,time,gods,save_path,os.sep)
				run = False
			elif ui == 'x':
				player.respawn()
				if player.difficulty != 3:
					save(world,player,time,gods,save_path,os.sep)
				run = False
				exitgame = True
					
class map():
	
	def __init__(self, name, tilemap, visit=False, map_type='overworld'):
		
		self.name = name
		self.known = []
		self.containers = []
		self.tilemap = tilemap
		self.visit = visit
		self.last_visit = 0 #-------test only
		self.map_type = map_type
		self.build_type = 'Full' #Full: build everything you want, Part: no stairs, None: Buildmode is not callable
		self.countdowns = []
		self.npcs = []
		
		for y in range (0,max_map_size):
			self.known.append([])
			for x in range (0,max_map_size):
				self.known[y].append(0) 
				
		for y in range (0,max_map_size):
			self.containers.append([])
			for x in range (0,max_map_size):
				self.containers[y].append(0)
				
		for y in range (0,max_map_size):
			self.npcs.append([])
			for x in range (0,max_map_size):
				self.npcs[y].append(0) 
	
	def fill(self, tile):
		
		for y in range (0,max_map_size):
			for x in range(0,max_map_size):
				self.tilemap[y][x] = deepcopy(tile)
	
	def floating(self,startx,starty,tile_fill,tile_border):
		#its important to use a tile_fill that isn't on the map and a tile_border that is on the map 
		
		run = True
		
		self.tilemap[starty][startx] = deepcopy(tile_fill)
		
		while run:
			
			count = 0
			
			for y in range(0,max_map_size):
				for x in range(0,max_map_size):
					
					if self.tilemap[y][x].techID == tile_fill.techID:
						
						for yy in range(y-1,y+2):
							for xx in range(x-1,x+2):
								
								try:
									if self.tilemap[yy][xx].techID != tile_border.techID and self.tilemap[yy][xx].techID != tile_fill.techID:
										self.tilemap[yy][xx] = deepcopy(tile_fill)
										count += 1
								except:
									None
									
			if count == 0:
				run = False
	
	def get_quarter_size(self,startx,starty):
		
		#this funktion gives back a tulpel with the width and height of a quarter made out of the same tile like the start position
		
		techID = self.tilemap[starty][startx].techID
		
		q_width = 0
		q_height = 0
		
		run_w = True
		run_h = True
		
		while run_w:
			
			if self.tilemap[starty][startx+q_width].techID == techID:
				q_width += 1
			else:
				run_w = False
				
		while run_h:
			
			if self.tilemap[starty+q_height][startx].techID == techID:
				q_height += 1
			else:
				run_h = False
				
		return (q_width,q_height)
			
	def set_frame(self,tile):
		
		for y in range (0,max_map_size):
			for x in range (0,max_map_size):
				
				if x == 0 or x == max_map_size-1 or y == 0 or y == max_map_size-1:
					self.tilemap[y][x] = tile

			
	def cut(self, minx, maxx, miny, maxy, replace):
		#everything that is not between min and mx is replaced abainst a tile
		
		for y in range (0,max_map_size):
			for x in range (0,max_map_size):
				
				if x < minx or x > maxx or y < miny or y > maxy:
					self.tilemap[y][x] = replace 
		
	def imp(self, start_x, start_y, replace_inner, replace_outer, step_min, step_max, circles, replace_except=None): #dig random caves
		
		#was made to generate random caves but dosn't pleased me. maybe this can be used for mazes.(unused atm)
		
		x = start_x
		y = start_y
		
		for l in range (0,circles):
			
			run = True
			
			while run:
				
				direction = random.randint(0,3)
				
				move_x = 0
				move_y = 0
				
				if direction == 0:
					move_y = -1
				elif direction == 1:
					move_x = 1 
				elif direction == 2:
					move_y = 1
				else:
					move_x= -1
					
				length = random.randint(step_min, step_max)
				
				for m in range (0,length):
					
					x = x + move_x
					y = y + move_y
					
					if x <= 1 or x >= 78 or y <= 1 or y >= 78:
						break
						run = False
					
					self.tilemap[y][x] = replace_inner
					
					for b in range (-1,2):
						for a in range (-1,2):
					
							if self.tilemap[y+a][x+b] != replace_outer and self.tilemap[y+a][x+b] != replace_inner and self.tilemap[y+a][x+b] != replace_except:
								self.tilemap[y+a][x+b] = replace_outer
					
				run = False

	def imp_connect(self,xpos,ypos,replace_inner,replace_except=None,except_replacer=None,style='straight'): #conects two or more points
						
		for a in range (0,len(ypos)):
			for b in range(0,len(xpos)):
				
				y = ypos[a]
				x = xpos[b]
				
				go = True
				direction = 0 #needed for natural ways. jumps between 0 and 1
				
				while go:
					
					try:
						y_goal = ypos[a+1]
						x_goal = xpos[b+1]
				  
					except:
						y_goal = y
						x_goal = x
						
					if x == x_goal and y == y_goal:
						go = False
						
					if x_goal - x < 0: #find out if you need to go right or left
						x_direction = -1
					else:
						x_direction = 1
						
					if y_goal - y < 0: #find out if you need to go up or down
						y_direction = -1
					else:
						y_direction = 1
					
					if style == 'straight':	
						if x != x_goal:
						
							x = x + x_direction
					
							if self.tilemap[y][x] != replace_except:
								self.tilemap[y][x] = replace_inner
							elif self.tilemap[y][x] == replace_except:
								self.tilemap[y][x] = except_replacer
									
						elif y != y_goal:
						
							y = y + y_direction
						
							if self.tilemap[y][x] != replace_except:
								self.tilemap[y][x] = replace_inner
							elif self.tilemap[y][x] == replace_except:
								self.tilemap[y][x] = except_replacer
								
					elif style == 'natural':
						
						if x != x_goal and direction == 0:
						
							x = x + x_direction
					
							if self.tilemap[y][x] != replace_except:
								self.tilemap[y][x] = replace_inner
							elif self.tilemap[y][x] == replace_except:
								self.tilemap[y][x] = except_replacer
									
						elif y != y_goal and direction == 1:
						
							y = y + y_direction
						
							if self.tilemap[y][x] != replace_except:
								self.tilemap[y][x] = replace_inner
							elif self.tilemap[y][x] == replace_except:
								self.tilemap[y][x] = except_replacer
						
						if direction == 0:
							direction = 1
						elif direction == 1:
							direction = 0
	
	def spawn_monsters(self,depth):
		#This function spawns monsters on the map
		
		if self.map_type == 'elfish_fortress':
			monster_max = 0
			for y in range(0,max_map_size):
				for x in range(0,max_map_size):
					if self.tilemap[y][x].techID == tl.tlist['functional'][8].techID:#this is a bed
						monster_max += 1
		else:
			monster_max = (max_map_size*max_map_size)/30
		
		if self.map_type == 'grot':
			spawnpoints = self.find_all_moveable(False)
		else:
			spawnpoints = self.find_all_moveable()
		
		del_list = []
		monster_count = 0
		
		for i in range (0,len(spawnpoints)):
			
			if self.npcs[spawnpoints[i][1]][spawnpoints[i][0]] != 0: #there is a monster here
				spawnpoints[i] = 'del'
				monster_count += 1#count the monsters that are allready on the map
			
		newlist = []
		
		for k in spawnpoints:
			if k != 'del':
				newlist.append(k)
				
		spawnpoints = newlist
			
		monster_max -= monster_count
		
		if monster_max > len(spawnpoints):
			monster_max = len(spawnpoints)
			
		for k in range(0,monster_max):
			
			ran = random.randint(0,len(ml.mlist[self.map_type])-1)
			ran2 = random.randint(0,len(spawnpoints)-1)
			ran3 = random.randint(0,len(ml.mlist['civilian'])-1)
				
			if self.tilemap[spawnpoints[ran2][1]][spawnpoints[ran2][0]].civilisation == False:#spawn a wild monster
				self.npcs[spawnpoints[ran2][1]][spawnpoints[ran2][0]] = deepcopy(ml.mlist[self.map_type][ran])#deepcopy is used that every monster on the map is saved seperate
				self.set_monster_strange(spawnpoints[ran2][0],spawnpoints[ran2][1],depth)
				try:
					if player.difficulty == 4:
						self.npcs[spawnpoints[ran2][1]][spawnpoints[ran2][0]].AI_style = 'ignore'
				except:
					None
						
			else:#spawn a civilian
				self.npcs[spawnpoints[ran2][1]][spawnpoints[ran2][0]] = deepcopy(ml.mlist['civilian'][ran3])
				self.set_monster_strange(spawnpoints[ran2][1],spawnpoints[ran2][1],depth)
	
	def set_monster_strange(self,x,y,z):
		
		if self.npcs[y][x] != 0:
			
			ran = random.randint(1,3)
		
			monster_lvl = z + ran
			self.npcs[y][x].lvl = monster_lvl
			
			attribute_list =[] 
		
			al = ('p_strange','p_defense','m_strange','m_defense','health')
			a_nr = 0
		
			for c in self.npcs[y][x].attribute_prev:
				for h in range(0,c):
					attribute_list.append(al[a_nr])
				a_nr+=1
		
			for i in range(0,monster_lvl):
				choice = al[random.randint(0,len(al)-1)]
				
				if choice == 'p_strange':
					self.npcs[y][x].basic_attribute.p_strange +=3
				elif choice == 'p_defense':
					self.npcs[y][x].basic_attribute.p_defense +=3
				elif choice == 'm_strange':
					self.npcs[y][x].basic_attribute.m_strange +=3
				elif choice == 'm_defense':
					self.npcs[y][x].basic_attribute.m_defense +=3
				elif choice == 'health':
					self.npcs[y][x].basic_attribute.max_lp +=1
					self.npcs[y][x].lp = self.npcs[y][x].basic_attribute.max_lp	
			
			el = [['spear','sword','axe','hammer'],['rune','wand','rune staff','artefact'],['armor','armor'],['necklace','amulet','talisman'],['ring','ring']]
			e_nr = 0
			
			for q in range(0,len(el)-1):
				ran = random.randint(0,len(el[q])-1)
				
				if self.npcs[y][x].worn_equipment[q] == 1:
					help_equipment = item_wear(el[q][ran],random.randint(0,z),random.randint(-2,2))
					
					self.npcs[y][x].basic_attribute.p_strange += help_equipment.attribute.p_strange
					self.npcs[y][x].basic_attribute.p_defense += help_equipment.attribute.p_defense
					self.npcs[y][x].basic_attribute.m_strange += help_equipment.attribute.m_strange
					self.npcs[y][x].basic_attribute.m_defense += help_equipment.attribute.m_defense
					self.npcs[y][x].basic_attribute.luck += help_equipment.attribute.luck
				
	def AI_move(self):
		#This function moves all monsters that are 7 or less fields away from the player.
		#It dosn't move all monsters to save performance
		
		ymin = player.pos[1]-7
		if ymin < 0:
			ymin = 0
		xmin = player.pos[0]-7
		if xmin < 0:
			xmin = 0
		ymax = player.pos[1]+8
		if ymax > max_map_size:
			ymax = max_map_size
		xmax = player.pos[0]+8
		if xmax > max_map_size:
			xmax = max_map_size
			
		for y in range (ymin,ymax):#reset the move_done switches
			for x in range (xmin,xmax):
				
				if self.npcs[y][x] != 0:
					if self.npcs[y][x].lp > 0:
						self.npcs[y][x].move_done = 0
					else:
						test = False
						while test == False:
							test = self.monster_die(x,y)	
		
		for y in range (ymin,ymax):
			for x in range (xmin,xmax):
				
				
				if self.npcs[y][x] != 0 and self.npcs[y][x].move_done == 0:#if there is a monster at this place
						
						#I. Get possible fields for a move
						
					moves = [(x,y)]
						
					yy = (-1,0,0,1)
					xx = (0,-1,1,0)
						
					for i in range (0,4):
							
						try:
								
							monster_move_groups = self.npcs[y][x].move_groups
							tile_move_group = self.tilemap[y+yy[i]][x+xx[i]].move_group
							
							move_group_check = False
							
							for j in range(0,len(monster_move_groups)):
								if monster_move_groups[j] == tile_move_group:
									move_group_check = True
									
							if self.npcs[y+yy[i]][x+xx[i]] == 0:
								npc = False
							else:
								npc = True
									
							if self.tilemap[y+yy[i]][x+xx[i]].techID == tl.tlist['functional'][1].techID or self.tilemap[y+yy[i]][x+xx[i]].techID == tl.tlist['functional'][2].techID: #this is a stair up/down
								stair = True
							else:
								stair = False
									
							if x + xx[i] == player.pos[0] and y + yy[i] == player.pos[1]:
								playerpos = True
							else:
								playerpos = False
							
							if move_group_check == True and npc == False and stair == False and playerpos == False:
									
								moves.append((x+xx[i],y+yy[i]))
									
									
						except:
							print('Debug:Error')
					
						#II. Find out wich possible move leads to wich distance between monster and player
					distances = []
					
					for j in range (0,len(moves)):
						
						a = player.pos[0] - moves[j][0]
						b = player.pos[1] - moves[j][1]
						
						c = (a**2 + b**2)**0.5 # this is just the good old pythagoras (c² = a² + b²)
						
						distances.append(c)
						
						#III. Choose the right move
					
					do_move = 'foo'
					
					if self.npcs[y][x].AI_style == 'hostile':
						
						if distances[0] > 1: #moves[0] is always the position of the monster right now, so distances 0 is always it's distance towards the player
							
							if len(moves) > 0:#if no move is possible at least the 'move' of stay still must remain
								good_moves = []
								for k in range (0, len(moves)):
									if distances[k] < distances[0]:#if the possible move makes the distance between player and monster smaller
										good_moves.append(moves[k])
							else:
								good_moves = moves
								
							if len(good_moves) == 0:
								good_moves = moves
								
							if len(good_moves) > 1:
								ran = random.randint(0,len(good_moves)-1)
							else:
								ran = 0
								
							do_move = good_moves[ran]
						
						else:
							player.monster_attacks(x,y)
							self.npcs[y][x].move_done = 1#set the move_done switch on
					
					elif self.npcs[y][x].AI_style == 'flee':
						
						if distances[0] < 2: #moves[0] is always the position of the monster right now, so distances 0 is always it's distance towards the player
								
							if len(moves) > 1:
								ran = random.randint(0,len(moves)-1)
							else:
								ran = 0
								
							do_move = moves[ran]
						
						else:
							
							if len(moves) > 0:#if no move is possible at least the 'move' of stay still must remain
								
								good_moves = []
								
								for k in range (0, len(moves)):
									if distances[k] > distances[0] or distances[k] == distances[0]:#if the possible move makes the distance between player and monster bigger or at least the same
										good_moves.append(moves[k])
							else:
								good_moves = moves
									
							if len(good_moves) == 0:
								good_moves = moves
								
							if len(good_moves) > 1:
								ran = random.randint(0,len(good_moves)-1)
							else:
								ran = 0
								
							do_move = good_moves[ran]
							
					
					elif self.npcs[y][x].AI_style == 'ignore':
						
						if len(moves) > 1:
							ran = random.randint(0,len(moves)-1)
						else:
							ran = 0
								
						do_move = moves[ran]
							
					#IV. Move the monster
					if do_move != 'foo':
						
						border = random.randint(1,9)
						
						if border > self.npcs[y][x].move_border:
							
							self.npcs[y][x].move_done = 1#set the move_done switch on
							helper = self.npcs[y][x]#copy the monster
							self.npcs[y][x] = 0 #del the monster at the old position
							self.npcs[do_move[1]][do_move[0]] = helper# set monster to the new position
	
	def monster_die(self,x,y):
		#this function is called when the player kills a monster. the x and the y variables are to define the location of the monster
		
		die_mess = 'The ' + self.npcs[y][x].name + ' vanishes!'
		
		if self.tilemap[y][x].replace == None: #only on empty fields corps can be spawned
			
			if self.npcs[y][x].corps_style == 'dryade' and self.tilemap[y][x].techID != tl.tlist['misc'][0].techID: #dryades can leave behind a seppling when they are killed(corpse_lvl dosn't matter)/low water isn't allowed
				
				coin = random.randint(0,99)
				
				if coin < 50:#there is a chance of 50%
					replace = self.tilemap[y][x]
					self.tilemap[y][x] = tl.tlist['local'][10]#<---sepling
					self.tilemap[y][x].replace = replace
					
					die_mess = 'The ' + self.npcs[y][x].name + ' turns into a new tree!'
					 
			elif self.npcs[y][x].corps_style == 'troll' and self.tilemap[y][x].techID != tl.tlist['misc'][0]: #trolls can leave behind a rock when they are killed(corpse_lvl dosn't matter)/low water isn't allowed
				
				coin = random.randint(0,99)
				
				if coin < 50:#there is a chance of 50%
					replace = self.tilemap[y][x]
					self.tilemap[y][x] = deepcopy(tl.tlist['local'][14])#<---rock
					self.tilemap[y][x].replace = replace
					
					die_mess = 'The ' + self.npcs[y][x].name + ' turns to stone!'
					
			elif self.npcs[y][x].corps_style == 'human': #humanoid monsters can leave behind humanoid remains when they die. the corps_lvl says how much items are stored inside them
				
				coin = random.randint(0,99)
				
				if coin < 15:#there is a chance of 15%
					die_mess = 'The ' + self.npcs[y][x].name + ' dies!'
					replace = self.tilemap[y][x]
					self.tilemap[y][x] = deepcopy(tl.tlist['functional'][6])#<--humanoid remains
					self.tilemap[y][x].replace = replace
					
					items = []
					
					max_items = max(1,self.npcs[y][x].corps_lvl)
					
					for i in range (0, max_items):
						#possible drops of a humanoid monster are equipment items and food items
						
						coin = random.randint(0,99)
						
						if coin < 65: #there is a chance of 65% that a item becomes a eqipment item
							
							material = random.randint(0,20) #all materials are allowed
							classes = ('spear','sword','axe','hammer','shoes','cuisse','helmet','armor','wand','rune','rune staff','artefact','ring','amulet','necklace','talisman','pickaxe')
							kind = classes[random.randint(0,len(classes)-1)]#all classes of objects are allowed
							plus = random.randint(-2,+2)# a plus between -2 and +2 is possible
							state = random.randint(10,85)#the state of this used objects will allways be between 10% and 80%
							curse = random.randint(0,2)#all curse-states are allowed from cursed to blessed
 							
							item = item_wear(kind,material,plus,state,curse)
							
						elif coin < 68: #there is a chance of 3% to drop a simple blueprint
							
							blueprint = random.randint(15,20)
							item = deepcopy(il.ilist['misc'][blueprint])
						
						elif coin < 80: #there is a	chance of 12% to drop a torch:
							
							item = deepcoppy(il.ilist['misc'][44])
							
						else:
							
							item = deepcopy(il.ilist['food'][random.randint(0,len(il.ilist['food'])-1)])
							
						items.append(item)
					
					self.containers[y][x] = container(items)
			
			elif self.npcs[y][x].corps_style == 'animal': #humanoid monsters can leave behind humanoid remains when they die. the corps_lvl says how much items are stored inside them
				
				coin = random.randint(0,99)
				
				if coin < 15:#there is a chance of 15%
					replace = self.tilemap[y][x]
					self.tilemap[y][x] = deepcopy(tl.tlist['functional'][21])#<--animal remains
					self.tilemap[y][x].replace = replace
					
					items = []
					
					max_items = max(1,self.npcs[y][x].corps_lvl)
					
					for i in range (0, max_items):
						#animals drop flesh. the corpslvl says how much
							
						items.append(deepcopy(il.ilist['food'][9]))#<---raw meat
						
					self.containers[y][x] = container(items)
					
					die_mess = 'The ' + self.npcs[y][x].name + ' dies!'
			
			elif self.npcs[y][x].corps_style == 'scrollkeeper': #scrollkeepers can leave behind humanoid remains with scrolls and spellbooks when they die. the corps_lvl says how much items are stored inside them
				
				coin = random.randint(0,99)
				
				if coin < 10:#there is a chance of 10%
					die_mess = 'The ' + self.npcs[y][x].name + ' dies!'
					replace = self.tilemap[y][x]
					self.tilemap[y][x] = deepcopy(tl.tlist['functional'][6])#<--humanoid remains
					self.tilemap[y][x].replace = replace
					
					items = []
					
					max_items = max(1,self.npcs[y][x].corps_lvl)
					
					for i in range (0, max_items):
						#possible drops of a scrollkeeper are scrolls and spellbooks
						
						coin = random.randint(0,99)
						
						if coin < 75: #there is a chance of 75% that a item becomes a scroll
							
							scrolls = (il.ilist['misc'][25],il.ilist['misc'][27],il.ilist['misc'][29],il.ilist['misc'][31],il.ilist['misc'][33],il.ilist['misc'][35],il.ilist['misc'][37],il.ilist['misc'][45])
							
							ran = random.randint(0,len(scrolls)-1)
							
							item = deepcopy(scrolls[ran])
								
						else:
							
							books = (il.ilist['misc'][26],il.ilist['misc'][28],il.ilist['misc'][30],il.ilist['misc'][32],il.ilist['misc'][34],il.ilist['misc'][36],il.ilist['misc'][38],il.ilist['misc'][46])
							
							ran = random.randint(0,len(books)-1)
							
							item = deepcopy(books[ran])
							
						items.append(item)
						
					self.containers[y][x] = container(items)
			
			elif self.npcs[y][x].corps_style == 'miner':
				
				if self.npcs[y][x].techID == ml.mlist['special'][0].techID:#this is a vase
					die_mess = 'The vase shatters.'  
				
				if self.tilemap[y][x].replace == None:
					
					ran = random.randint(0,99)
					
					if ran <= self.npcs[y][x].corps_lvl: #for miners the corps_lvl determinates the chance of getting a gem
						
						replace = self.tilemap[y][x]
						self.tilemap[y][x] = deepcopy(tl.tlist['misc'][9])#set a lost gem
						self.tilemap[y][x].replace = replace
					
					elif ran <= self.npcs[y][x].corps_lvl*4:#for miners the corps_lvl determinates the chance of getting some ore. Its the chance to get a gem * 3 
						
						replace = self.tilemap[y][x]
						self.tilemap[y][x] = deepcopy(tl.tlist['misc'][11])#set a lost ore
						self.tilemap[y][x].replace = replace
						
			elif self.npcs[y][x].corps_style == 'vase':
				
				die_mess = 'The vase shatters and monsters jump out.'
				
				for yy in range(y-1,y+2):
					for xx in range(x-1,x+2):
						
						if yy != player.pos[1] or xx!= player.pos[0]:
							if self.npcs[yy][xx] == 0 and self.tilemap[yy][xx].move_group == 'soil' and self.tilemap[yy][xx].damage == 0:
								self.npcs[yy][xx] = deepcopy(ml.mlist['special'][2])#set vase monsters
								self.set_monster_strange(xx,yy,player.pos[2])
								if player.difficulty == 4:
									self.npcs[yy][xx].AI_style = 'ignore'
								
			elif self.npcs[y][x].corps_style == 'mimic':
				
				die_mess = 'The mimic wakes up.'
						
			elif self.npcs[y][x].corps_style == 'vanish':
				
				ran = random.randint(0,99)
					
				if ran <= self.npcs[y][x].corps_lvl: #the corps_lvl determinates the chance of getting a present
					
					replace = self.tilemap[y][x]
					self.tilemap[y][x] = deepcopy(tl.tlist['misc'][13])#set a present
					self.tilemap[y][x].replace = replace
						
					item_ran = random.randint(0,99)
						
					if item_ran < 50:
							
						self.containers[y][x] = container([il.ilist['misc'][43]])#set a heavy bag
							
					elif item_ran < 95:
							
						r = random.randint(3,7)
							
						self.containers[y][x] = container([il.ilist['misc'][r]])#set a workbench
							
					else:
							
						self.containers[y][x] = container([il.ilist['misc'][40]])#set a heart-shaped crystal
						
						
				
			############ADD MORE HERE###############
		
		if self.npcs[y][x].corps_style == 'mimic':
			self.npcs[y][x] = deepcopy(ml.mlist['special'][4])#set a mimic
			self.set_monster_strange(x,y,player.pos[2])
			if player.difficulty == 4:
				self.npcs[y][x].AI_style = 'ignore'
		else:
			self.npcs[y][x] = 0 #allways del the monster if it is no mimic
		self.make_monsters_angry(x,y,'kill')
		message.add(die_mess)
		return True
	
	def make_shops(self):
		
		num = (max_map_size*max_map_size) / (50*50)
		
		for i in range (0,num):
			
			x = random.randint(5,max_map_size-5)
			y = random.randint(5,max_map_size-5)
			
			for yy in range(y-2,y+3):
				for xx in range(x-2,x+3):
					
					self.npcs[yy][xx] = 0 #allways del the monsters
					
					if xx == x-2 or xx == x+2 or yy == y-2 or yy == y+2:
						self.tilemap[yy][xx] = deepcopy(tl.tlist['shop'][1])
					else:
						self.tilemap[yy][xx] = deepcopy(tl.tlist['shop'][0])
						
			self.tilemap[y][x-2] = deepcopy(tl.tlist['shop'][2])
			self.tilemap[y][x+2] = deepcopy(tl.tlist['shop'][2])
			self.tilemap[y-2][x] = deepcopy(tl.tlist['shop'][2])
			self.tilemap[y+2][x] = deepcopy(tl.tlist['shop'][2])   
			
			if self.map_type == 'orcish_mines':			
				self.npcs[y][x] = deepcopy(ml.mlist['shop'][1])
			elif self.map_type == 'grot':			
				self.npcs[y][x] = deepcopy(ml.mlist['shop'][2])
			else:
				self.npcs[y][x] = deepcopy(ml.mlist['shop'][0])#the elfish shopkeeper is only for fallback...In the elfish fortress the shops are spawned on a other way
	
	def make_monsters_angry(self,x,y,style):
		
		for yy in range(y-3,y+4):
			for xx in range(x-3,x+4):
				
				try:
					if self.npcs[yy][xx] != 0:
						if self.npcs[yy][xx].anger == style:
							self.npcs[yy][xx] = deepcopy(ml.mlist['angry_monster'][self.npcs[yy][xx].anger_monster])
							self.set_monster_strange(xx,yy,player.pos[2])
							if player.difficulty == 4:
								self.npcs[yy][xx].AI_style = 'ignore'		
				except:
					None
	
	def time_pass(self):
		#This function refresches the map for every day that past since players last visit... make plants growing ect.
		
		if self.last_visit != time.day_total:
			
			screen.render_load(10)
			
			past_time = time.day_total - self.last_visit
			
			if past_time < 0:
				past_time = 364 - past_time
				
			for c in range (0,past_time):
				
				for y in range (0,max_map_size):
					for x in range(0,max_map_size):
						
						tile = self.tilemap[y][x]
						
						#######Life of plants######
						
						#1. Scrub
						if tile.grow_group == 'scrub':
							rand = random.randint(0,99)
							if rand < 50:
								replace = self.tilemap[y][x].replace
								self.tilemap[y][x] = deepcopy(tl.tlist[tile.conected_tiles[0]][tile.conected_tiles[1]])
								self.tilemap[y][x].replace = replace
							
						if tile.grow_group == 'scrub_buds':
							rand = random.randint(0,99)
							if rand < 90:
								replace = self.tilemap[y][x].replace
								self.tilemap[y][x] = deepcopy(tl.tlist[tile.conected_tiles[0]][tile.conected_tiles[1]])
								self.tilemap[y][x].replace = replace
						
						if tile.grow_group == 'scrub_blossom':
							rand = random.randint(0,99)
							if rand < 80:
								scrubs = random.randint(0,2)
								replace = self.tilemap[y][x].replace
								self.tilemap[y][x] = deepcopy(tl.tlist[tile.conected_tiles[scrubs][0]][tile.conected_tiles[scrubs][1]])
								self.tilemap[y][x].replace = replace
							
						if tile.grow_group == 'scrub_berries':
							rand = random.randint(0,99)
							if rand < 50:
								replace = self.tilemap[y][x].replace
								self.tilemap[y][x] = deepcopy(tl.tlist[tile.conected_tiles[0][0]][tile.conected_tiles[0][1]])
								self.tilemap[y][x].replace = replace
							elif rand > 49 and rand < 75:
								numbers =(-1,1)
								
								for yy in numbers:
									for xx in numbers:
										try:
											
											if self.tilemap[y+yy][x+xx].can_grown == True:
											
												coin = random.randint(0,99)
												
												if coin < 25: #25%
													replace = self.tilemap[y+yy][x+xx]
													self.tilemap[y+yy][x+xx] = deepcopy([tile.conected_tiles[1][0]][tile.conected_tiles[1][1]])
													self.tilemap[y+yy][x+xx].replace = replace
										except:
											None
											
						if tile.grow_group == 'scrub_scruffy':
							rand = random.randint(0,99)
							if rand < 90:
								replace = self.tilemap[y][x].replace
								self.tilemap[y][x] = deepcopy(tl.tlist[tile.conected_tiles[0][0]][tile.conected_tiles[0][1]])
								self.tilemap[y][x].replace = replace
							else:
								replace = self.tilemap[y][x].replace
								self.tilemap[y][x] = deepcopy(tl.tlist[tile.conected_tiles[1][0]][tile.conected_tiles[1][1]])
								self.tilemap[y][x].replace = replace
								
						
						if tile.grow_group == 'scrub_grow':
							rand = random.randint(0,99)
							if rand < 90:
								replace = self.tilemap[y][x].replace
								self.tilemap[y][x] = deepcopy(tl.tlist[tile.conected_tiles[0]][tile.conected_tiles[1]])
								self.tilemap[y][x].replace = replace
								
						#2.Tree
						
						if tile.grow_group == 'tree_grow':
							rand = random.randint(0,99)
							if rand < 80:
								replace = self.tilemap[y][x].replace
								self.tilemap[y][x] = deepcopy(tl.tlist[tile.conected_tiles[0]][tile.conected_tiles[1]])
								self.tilemap[y][x].replace = replace
						
						if tile.grow_group == 'tree':
							rand = random.randint(0,99)
							if rand < 5:
								replace = self.tilemap[y][x].replace
								self.tilemap[y][x] = deepcopy(tl.tlist[tile.conected_tiles[1][0]][tile.conected_tiles[1][1]])
								self.tilemap[y][x].replace = replace

							elif rand > 49:
								numbers =(-2,2)
								
								for yy in numbers:
									for xx in numbers:
										try:
											
											if self.tilemap[y+yy][x+xx].can_grown == True:
											
												coin = random.randint(0,1)
												
												if coin == 1:
													replace = self.tilemap[y+yy][x+xx]
													self.tilemap[y+yy][x+xx] = deepcopy(tl.tlist[tile.conected_tiles[0][0]][tile.conected_tiles[0][1]])
													self.tilemap[y+yy][x+xx].replace = replace
										except:
											None
						
						#3.Herb
						
						if tile.grow_group == 'herblike':
							rand = random.randint(0,99)
							if rand < 20:
								replace = self.tilemap[y][x].replace
								self.tilemap[y][x] = deepcopy(tl.tlist[tile.conected_tiles[0]][tile.conected_tiles[1]])
								self.tilemap[y][x].replace = replace
								
						
						#4. Blue Mushrooms
						
						if tile.grow_group == 'mushroom_mud':
							
							rand = random.randint(0,99)
							
							if rand < 5:
								
								for yy in range(-1,1):
									for xx in range(-1,1):
										try:
											
											if self.tilemap[y+yy][x+xx].techID == tl.tlist['misc'][1].techID:#here is mud 
											
												cent = random.randint(0,99)
												
												if cent < 25 :
													replace = self.tilemap[y+yy][x+xx]
													self.tilemap[y+yy][x+xx] = deepcopy(tl.tlist[tile.conected_tiles[0]][tile.conected_tiles[1]])
													self.tilemap[y+yy][x+xx].replace = replace
										except:
											None
						
						#5. Brown Mushrooms
						
						if tile.grow_group == 'mushroom_treelike':
							rand = random.randint(0,99)
							if rand < 5:
								
								for yy in range(-1,1):
									for xx in range(-1,1):
										try:
											
											if self.tilemap[y+yy][x+xx].techID == tl.tlist['global_caves'][0].techID:#here is cave ground
											
												cent = random.randint(0,99)
												
												if cent < 25 :
													replace = self.tilemap[y+yy][x+xx]
													self.tilemap[y+yy][x+xx] = deepcopy(tl.tlist[tile.conected_tiles[0][0]][tile.conected_tiles[0][1]])
													self.tilemap[y+yy][x+xx].replace = replace
													
										except:
											None
							
							elif rand < 30:#make a giant mushroom
								
								replace = self.tilemap[y][x].replace
								self.tilemap[y][x] = deepcopy(tl.tlist[tile.conected_tiles[1][0]][tile.conected_tiles[1][1]])
								self.tilemap[y][x].replace = replace
									
						#6. Purple Mushrooms
						
						if tile.grow_group == 'mushroom': #let grow new mushrooms and let the old ones die(5%)
							rand = random.randint(0,99)
							if rand < 5:
								
								for yy in range(-1,1):
									for xx in range(-1,1):
										try:
											
											if self.tilemap[y+yy][x+xx].techID == tl.tlist['global_caves'][0].techID:#here is cave ground
											
												cent = random.randint(0,99)
												
												if cent < 25 :
													replace = self.tilemap[y+yy][x+xx]
													self.tilemap[y+yy][x+xx] = deepcopy(tl.tlist[tile.conected_tiles[0]][tile.conected_tiles[1]])
													self.tilemap[y+yy][x+xx].replace = replace
												
										except:
											None
											
						#7. Agriculture
						
						if tile.grow_group == 'agri0':
							rand = random.randint(0,99)
							if rand < 50:
								if self.map_type == 'overworld': 
									self.tilemap[y][x] = tl.tlist[tile.conected_tiles[0][0]][tile.conected_tiles[0][1]]
								elif self.map_type == 'cave':
									self.tilemap[y][x] = tl.tlist[tile.conected_tiles[1][0]][tile.conected_tiles[1][1]]
									
						if tile.grow_group == 'agri1': #let something grow on a acriculture (final, at the overworld) (50%)
							rand = random.randint(0,99)
							if rand < 50:
									self.tilemap[y][x] = tl.tlist[tile.conected_tiles[0]][tile.conected_tiles[1]]
						
						#8. Vanish
						if tile.grow_group == 'vanish':
							rand = random.randint(0,99)
							if rand < 50:
								self.tilemap[y][x] = self.tilemap[y][x].replace
								self.containers[y][x] = 0
							
						#########add other events for growing plants ect here########
			
				self.last_visit = time.day_total #change the day of last visit to today to prevent the map of changed a second time for this day
			
				self.spawn_monsters(player.pos[2])#spawn new monsters 
			
			for i in range(0,len(player.inventory.food)):#let the food rot in the players inventory
			
				if player.inventory.food[i] != player.inventory.nothing:
					player.inventory.food[i].rot()
			
	def exchange(self,old_tile,new_tile,use_deepcopy=False):
		
		for y in range (0,max_map_size):
			for x in range (0,max_map_size):
				
				if self.tilemap[y][x].techID == old_tile.techID:
					if use_deepcopy == False:
						self.tilemap[y][x] = new_tile
					else:
						self.tilemap[y][x] = deepcopy(new_tile)
					
	def find_first(self,tile):
		
		for y in range (0,max_map_size):
			for x in range (0,max_map_size):
				
				if self.tilemap[y][x].techID == tile.techID:
					return [x,y]
		
		return False
					
	def find_any(self,tile):
		
		found = []
		
		for y in range(0,max_map_size):
			for x in range(0,max_map_size):
				
				if self.tilemap[y][x].techID == tile.techID:
					found.append((x,y))
					
		if found == []:
			return False
		elif len(found) == 1:
			return found[0]
		else:
			ran = random.randint(0,len(found)-1)
			return found[ran]
	
	def find_all_moveable(self,ignore_water = True):

		cordinates_list = []
		for y in range (0, max_map_size):
			for x in range (0,max_map_size):
				
				moveable = False
				
				if ignore_water == True:
					if self.tilemap[y][x].move_group == 'soil':
						moveable = True
				else:
					if self.tilemap[y][x].move_group == 'soil' or self.tilemap[y][x].move_group == 'low_liquid':
						moveable = True
				
				if moveable == True and self.tilemap[y][x].damage == False and self.tilemap[y][x].techID != tl.tlist['misc'][0].techID:
					cordinates_list.append((x,y))
						
		if len(cordinates_list) > 0:
			return cordinates_list
				
		else:
					
			return False
	
	def add_container(self, inventory, x, y):
		
		self.containers[y][x] = container(inventory)
	
	def make_special_monsters(self, min_no, max_no, on_tile, depth, monster_type='vase'):
		
		size = (max_map_size*max_map_size)/(50*50)
		
		for i in range(0,size):
			
			num_monster = random.randint(min_no,max_no)
			
			if num_monster > 0:
				
				for z in range (0,num_monster):
					
					pos = self.find_any(on_tile)
					
					if monster_type == 'vase':
						
						ran = random.randint(0,99)
						
						if ran < 10:
							self.npcs[pos[1]][pos[0]] = deepcopy(ml.mlist['special'][1]) #spawn a monster vase
						else:
							self.npcs[pos[1]][pos[0]] = deepcopy(ml.mlist['special'][0]) #spawn a vase
							
					elif monster_type == 'mimic':
						
						pos = self.find_any(on_tile)
						self.npcs[pos[1]][pos[0]] = deepcopy(ml.mlist['special'][3]) #spawn a sleeping mimic
			
	def make_containers(self, min_no, max_no, on_tile, item_min, item_max, container_type='remains'):
		
		size = (max_map_size*max_map_size)/(50*50)
		
		for i in range(0,size):
		
			num_container = random.randint(min_no,max_no)
			
			if num_container > 0:
				
				for z in range (0,num_container):
					
					place = self.find_any(on_tile)
					
					inventory = []
					
					num_items = random.randint(item_min,item_max)##############item_min,item_max
					
					for t in range (0,num_items):
					
						if container_type == 'chest':
					
							classes = ['sword', 'axe', 'hammer', 'spear', 'helmet', 'armor', 'cuisse', 'shoes', 'wand', 'rune', 'rune staff', 'artefact', 'amulet', 'ring', 'talisman', 'necklace', 'pickaxe']
					
							class_num = random.randint(0,len(classes)-1)
							material = random.randint(0,20)
							plus = random.randint(-3,3)
							state = random.randint(80,100)
					
							curses = (0,1,2)
							curse_num = random.randint(0,2) 
					
							item = item_wear(classes[class_num], material, plus, state, curses[curse_num], False)
							inventory.append(item)
					
						elif container_type == 'remains':
						
							classes = ['sword', 'axe', 'hammer', 'spear', 'helmet', 'armor', 'cuisse', 'shoes', 'wand', 'rune', 'rune staff', 'artefact', 'amulet', 'ring', 'talisman', 'necklace', 'pickaxe']
						
							class_num = random.randint(0,len(classes)-1)
							material = random.randint(0,20)
							plus = random.randint(-3,3)
							state = random.randint(20,60)
					
							curses = (0,1,2)
							curse_num = random.randint(0,2) 
					
							item = item_wear(classes[class_num], material, plus, state, curses[curse_num], False)
							inventory.append(item)
					
					if container_type == 'chest':
					
						self.add_container(inventory, place[0], place[1])
						replace = self.tilemap[place[1]][place[0]]
						self.tilemap[place[1]][place[0]] = deepcopy(tl.tlist['functional'][4])#chest
						self.tilemap[place[1]][place[0]].replace = replace
					
					elif container_type == 'remains':
						replace_tile = self.tilemap[place[1]][place[0]]
						self.add_container(inventory, place[0], place[1])
						self.tilemap[place[1]][place[0]] = deepcopy(tl.tlist['functional'][6])#remains
						self.tilemap[place[1]][place[0]].replace = replace_tile

	def exchange_when_surrounded(self, tile_check, tile_replace, number_neighbors):
		
		#check all cordinates for their neighbors(including them self) and exchange th tile when the number of neighbors with the same techID => number_neighbors
		
		for y in range (0,max_map_size):
			for x in range (0,max_map_size):
				
				count = 0
				
				for yy in range (-1,2):
					for xx in range (-1,2):
						
						try:
							if self.tilemap[y+yy][x+xx].techID == tile_check.techID or self.tilemap[y+yy][x+xx].techID == tile_replace.techID:
								count += 1
						except:
							None
							
				if count >= number_neighbors:
					self.tilemap[y][x] = tile_replace
									
	def sget(self):
		
		string = ''
		
		for c in range (0,max_map_size):
			for d in range (0,max_map_size):
				
				
				if d != player.pos[0] or c != player.pos[1]:
					
					if self.known[c][d] != 0:
						string = string + self.tilemap[c][d].char
					else:
						string += '\033[0;30;40m '
				else:
					string = string + player.char
				
			string = string + '\n'
		
		return string
		
	def set_sanctuary(self,startx,starty):
		
		for y in range (starty-2, starty+3):
			for x in range (startx-2, startx+3):
				
				self.tilemap[y][x] = deepcopy(tl.tlist['sanctuary'][0])#sanctuary floor
				
				if x == startx-2 or x == startx or x == startx+2: 
					if y == starty-2 or y == starty or y == starty+2:
						
						self.tilemap[y][x] = deepcopy(tl.tlist['sanctuary'][1])#sanctuary pilar
						
		self.tilemap[starty][startx] = deepcopy(tl.tlist['sanctuary'][2])#sanctuary spawn point
		
		self.tilemap[starty-1][startx] = deepcopy(tl.tlist['functional'][20])#divine gift
		self.tilemap[starty-1][startx].replace = tl.tlist['sanctuary'][0]
		
		material_pick = random.randint(0,10)
		material_axe = random.randint(0,10)
		material_amo = random.randint(0,10)
		amo_classes = ('shoes','cuisse','armor','helmet')
		ran = random.randint(0,3)
		amo_class = amo_classes[ran]
		
		pick = item_wear('pickaxe', material_pick,0)
		axe = item_wear('axe',material_axe,0)
		amo = item_wear(amo_class,material_amo,0)
		
		self.add_container([pick,axe,amo,il.ilist['misc'][3],il.ilist['misc'][2],il.ilist['misc'][44]],startx,starty-1)
		
		self.tilemap[starty+1][startx] = deepcopy(tl.tlist['functional'][1])#stair down
		self.tilemap[starty+1][startx].damage = -1
		self.tilemap[starty+1][startx].damage_mes = 'Your wounds are cured.'
		self.tilemap[starty+1][startx].build_here = False
		

		
class world_class():
	
	def __init__(self,tilelist):
		
		global max_map_size
		
		screen.render_load(0)
		
		name = save_path + os.sep + 'world.data'
		
		self.map_size = 52
		
		self.startx = 0
		self.starty = 0
		
		try:
			
			f = file(name, 'r')
			temp = p.load(f)
			screen.render_load(1)
			self.maplist = temp.maplist
			self.map_size = temp.map_size
			max_map_size = self.map_size
			self.startx = temp.startx
			self.starty = temp.starty
			
		except:
			screen.render_load(2)
			self.choose_size()
			self.maplist = []
		
			for x in range (0,16):
				self.maplist.append({})
				
			screen.render_load(3)
		
			pos = self.grassland_generator(0,0,30,80,5,(max_map_size*max_map_size)/20)
			
			self.startx = pos[0]
			self.starty = pos[1]
			
			screen.render_load(4)
			self.cave_generator(13)
			
			screen.render_load(15)
			self.grot_generator(3)
			
			screen.render_load(16)
			test = False
			while test==False:
				test = self.elfish_generator(6)
			
			screen.render_load(17)
			self.mine_generator(9)
			
			self.border_generator(15)
			
			screen.render_load(18)
			self.desert_generator(20)
			
			screen.render_load(5)
			
	def default_map_generator(self, name, tiles, tilelist):	#check if tilelist can be deleted
		
		tilemap = []
		
		for i in range (0,max_map_size):
			tilemap.append([])
		
		a = 0
		
		for b in range (0,max_map_size):
			
			ran_num = random.randint(0,len(tl.tlist[tiles])-1)
			tilemap[a].append(tl.tlist[tiles][ran_num])
			
		b = 0
		
		for a in range (1,max_map_size):
		
			ran_num = random.randint(0,len(tl.tlist[tiles])-1)
			tilemap[a].append(tl.tlist[tiles][ran_num])
			
		for a in range (1,max_map_size):
			for b in range (1,max_map_size):
				
				ran_same = random.randint(0,9)
				
				if ran_same < 5 :
					tilemap[a].append(tilemap[a-1][b])
				elif ran_same < 8:
					tilemap[a].append(tilemap[a][b-1])
				else:
					ran_num = random.randint(0,len(tl.tlist[tiles])-1)
					tilemap[a].append(tl.tlist[tiles][ran_num])
					
		m = map(name ,tilemap)
		
		return m
	def border_generator(self,layer):
		
		cave_name = 'local_0_0'
		m = self.default_map_generator(cave_name,'global_caves', tilelist)
		m.map_type = 'border'
		
		m.fill(tl.tlist['functional'][0])#fill with border
		
		self.maplist[layer][cave_name] = m
		
	def grot_generator(self,layer):
		
		cave_name = 'local_0_0'
		m = self.default_map_generator(cave_name,'global_caves', tilelist)
		m.map_type = 'grot'
		
		m.exchange(tl.tlist['global_caves'][4],tl.tlist['misc'][0])#exchange lava against low water
		m.exchange(tl.tlist['global_caves'][0],tl.tlist['misc'][1])#exchange caveground against mud
		m.exchange(tl.tlist['global_caves'][2],tl.tlist['misc'][0])#exchange soft soil against low water
		
		m.set_frame(tl.tlist['functional'][0])
		
		chance_ore = layer
		chance_gem = layer/2
			
		for y in range (0,max_map_size):
			for x in range (0,max_map_size):
					
				if m.tilemap[y][x].techID == tl.tlist['global_caves'][3].techID:#this is hard rock
						
					replace = m.tilemap[y][x].replace
						
					coin = random.randint(0,1)
					percent = random.randint(1,100) 
						
					if coin == 0 and percent <= chance_ore:
						m.tilemap[y][x] = tl.tlist['misc'][4]#set ore here
						m.tilemap[y][x].replace = replace
					elif coin == 1 and percent <= chance_gem:
						m.tilemap[y][x] = tl.tlist['misc'][5]#set gem here
						m.tilemap[y][x].replace = replace
		
		for y in range (0,max_map_size):
				for x in range (0,max_map_size):
					
					if m.tilemap[y][x].techID == tl.tlist['misc'][1].techID:#this is mud
						
						cent = random.randint(0,99)
						
						if cent < 10: #its a chance of 10% that a blue mushroom spawns here
							
							replace = m.tilemap[y][x]
							m.tilemap[y][x] = tl.tlist['misc'][6]
							m.tilemap[y][x].replace = replace
							
							m.containers[y][x] = container([deepcopy(il.ilist['food'][1])])
		
		num_lilys = ((max_map_size*max_map_size)/100)*3
		
		for i in range (0,num_lilys):
			pos = m.find_any(tl.tlist['misc'][0])#find low wather
			try:
				coin = random.randint(0,1)
				if coin == 0:
					m.tilemap[pos[1]][pos[0]] = tl.tlist['misc'][10]#set a water lily
				else:
					m.tilemap[pos[1]][pos[0]] = tl.tlist['misc'][14]#set a water lily with blossom
					
			except:
				None
		
		m.make_shops()
		
		m.spawn_monsters(3)
							
		self.maplist[layer][cave_name] = m
		
	def elfish_generator(self,layer):
		
		map_name = 'local_0_0'
		m = self.default_map_generator(map_name,'global_caves', tilelist)
		m.map_type = 'elfish_fortress'
		
		m.fill(tl.tlist['elfish'][0])
		
		for y in range (10, max_map_size-10,10):
				
			ran = random.randint(0,3)
			for yy in range (y-1,y+2):
				if ran < 3:
					m.imp_connect((0,max_map_size-1),(yy,yy),tl.tlist['elfish'][1],tl.tlist['elfish'][1],tl.tlist['elfish'][1])
					
			if ran < 3:
				m.imp_connect((0,max_map_size-1),(y-2,y-2),tl.tlist['elfish'][3],tl.tlist['elfish'][1],tl.tlist['elfish'][1])
				m.imp_connect((0,max_map_size-1),(y+2,y+2),tl.tlist['elfish'][3],tl.tlist['elfish'][1],tl.tlist['elfish'][1])
				
		for x in range (10, max_map_size-10,10):
			
			ran = random.randint(0,3)
			for xx in range (x-1,x+2):
				if ran < 3:
					m.imp_connect((xx,xx),(0,max_map_size-1),tl.tlist['elfish'][1],tl.tlist['elfish'][1],tl.tlist['elfish'][1])
		
			if ran < 3:
				m.imp_connect((x-2,x-2),(0,max_map_size-1),tl.tlist['elfish'][3],tl.tlist['elfish'][1],tl.tlist['elfish'][1])
				m.imp_connect((x+2,x+2),(0,max_map_size-1),tl.tlist['elfish'][3],tl.tlist['elfish'][1],tl.tlist['elfish'][1])
		
		m.cut(5,max_map_size-6,5,max_map_size-6,tl.tlist['elfish'][3])
		
		building_count = 0
		run = True
		
		while run:
			
			pos=m.find_first(tl.tlist['elfish'][0])
			
			if pos != False:
				m.floating(pos[0],pos[1],tl.tlist['elfish'][5],tl.tlist['elfish'][3])#fill with help passive
				building_count += 1
			else:
				run = False
				
		m.exchange(tl.tlist['elfish'][5],tl.tlist['elfish'][0])
				
		if building_count < 6:
			return False #return false to make a loop if there are to less buildings inside the map
		
		num_temples = int((float(building_count)/100)*10)
		
		if num_temples == 0:
			num_temples = 1
			
		num_agriculture = int((float(building_count)/100)*10)
		
		if num_agriculture == 0:
			num_agriculture=1
		
		num_meetingarea = int((float(building_count)/100)*10)
		
		if num_meetingarea == 0:
			num_meetingarea = 1
			
		num_marketplace = int((float(building_count)/100)*10)
		
		if num_marketplace == 0:
			num_marketplace = 1
		
		num_libaries = int((float(building_count)/100)*10)
		
		if num_libaries == 0:
			num_libaries = 1
			
		num_dwellings = building_count-num_temples-num_agriculture-num_meetingarea-num_marketplace-num_libaries
			
		m.cut(5,max_map_size-6,5,max_map_size-6,tl.tlist['elfish'][1])
		
		for i in range(0,num_agriculture):
			pos = m.find_any(tl.tlist['elfish'][0])#find any elfish_floor_indoor
			m.floating(pos[0],pos[1],tl.tlist['elfish'][2],tl.tlist['elfish'][1])#replace this building with elfish_agriculture
		
		for y in range(0,max_map_size,2):
			for x in range(0,max_map_size):
				
				if m.tilemap[y][x].techID == tl.tlist['elfish'][2].techID:#this is elfish agriculture
					m.tilemap[y][x] = tl.tlist['misc'][0]#set low water
		
		m.cut(5,max_map_size-6,5,max_map_size-6,tl.tlist['elfish'][3])	
		
		for i in range(0,num_marketplace):#set marketplaces
			pos = m.find_any(tl.tlist['elfish'][0])#find any elfish_floor_indoor
			m.floating(pos[0],pos[1],tl.tlist['elfish'][4],tl.tlist['elfish'][3])#fill this building with elfish_active
			pos = m.find_first(tl.tlist['elfish'][4])
			size = m.get_quarter_size(pos[0],pos[1])
			
			for y in range(pos[1]+1,pos[1]+size[1]-1,2):
				for x in range(pos[0]+1,pos[0]+size[0]-1,3):
					m.npcs[y][x] = ml.mlist['shop'][0]
			
			m.exchange(tl.tlist['elfish'][4],tl.tlist['shop'][0])
			
		for i in range(0,num_temples):
			
			pos = m.find_any(tl.tlist['elfish'][0])#find any elfish_floor_indoor
			m.floating(pos[0],pos[1],tl.tlist['elfish'][4],tl.tlist['elfish'][3])#fill this building with elfish_active
			pos = m.find_first(tl.tlist['elfish'][4])
			size = m.get_quarter_size(pos[0],pos[1])
			
			for y in range(pos[1],pos[1]+size[1],2):
				for x in range(pos[0],pos[0]+size[0],2):
					m.tilemap[y][x] = deepcopy(tl.tlist['functional'][22])
					m.tilemap[y][x].replace = tl.tlist['elfish'][0]
					m.tilemap[y][x].civilisation = False
			
			m.tilemap[pos[1]+(size[1]/2)][pos[0]+(size[0]/2)] = deepcopy(tl.tlist['functional'][15])#set a altar
			m.tilemap[pos[1]+(size[1]/2)][pos[0]+(size[0]/2)].replace = tl.tlist['elfish'][0]
			m.tilemap[pos[1]+(size[1]/2)][pos[0]+(size[0]/2)].civilisation = False
			
			m.exchange(tl.tlist['elfish'][4],tl.tlist['elfish'][5])
		
		for i in range(0,num_meetingarea):
			
			pos = m.find_any(tl.tlist['elfish'][0])
			m.floating(pos[0],pos[1],tl.tlist['elfish'][4],tl.tlist['elfish'][3])#fill this building with elfish_active
			pos = m.find_first(tl.tlist['elfish'][4])
			size = m.get_quarter_size(pos[0],pos[1])
			
			for y in range(pos[1]+2,pos[1]+size[1]-2):
				for x in range(pos[0]+2,pos[0]+size[0]-1,4):
					m.tilemap[y][x] = deepcopy(tl.tlist['functional'][16]) #set table
					m.tilemap[y][x].replace = tl.tlist['elfish'][0]
					m.tilemap[y][x].civilisation = False
					
					for xx in range(x-1,x+2):
						if m.tilemap[y][xx].techID == tl.tlist['elfish'][4].techID:
							m.tilemap[y][xx] = deepcopy(tl.tlist['functional'][18])
							m.tilemap[y][xx].replace = tl.tlist['elfish'][0]
							m.tilemap[y][xx].civilisation = False
			
					for yy in range(y-1,y+2):
						if m.tilemap[yy][x].techID == tl.tlist['elfish'][4].techID:
							m.tilemap[yy][x] = deepcopy(tl.tlist['functional'][18])
							m.tilemap[yy][x].replace = tl.tlist['elfish'][0]
							m.tilemap[yy][x].civilisation = False
			
			m.exchange(tl.tlist['elfish'][4],tl.tlist['elfish'][5])
			
		for i in range(0,num_libaries):
			
			pos = m.find_any(tl.tlist['elfish'][0])
			m.floating(pos[0],pos[1],tl.tlist['elfish'][4],tl.tlist['elfish'][3])#fill this building with elfish_active
			pos = m.find_first(tl.tlist['elfish'][4])
			size = m.get_quarter_size(pos[0],pos[1])
			
			for y in range(pos[1]+1,pos[1]+size[1]-1,2):
				for x in range(pos[0]+1,pos[0]+size[0]-1,2):
					
					m.tilemap[y][x] = deepcopy(tl.tlist['functional'][19])
					m.tilemap[y][x].civilisation = False
			
			m.exchange(tl.tlist['elfish'][4],tl.tlist['elfish'][5])
					
		for i in range(0,num_dwellings):
			
			pos = m.find_any(tl.tlist['elfish'][0])
			m.floating(pos[0],pos[1],tl.tlist['elfish'][4],tl.tlist['elfish'][3])#fill this building with elfish_active
			pos = m.find_first(tl.tlist['elfish'][4])
			pos_original = pos
			size = m.get_quarter_size(pos[0],pos[1])
			
			num_beds = (size[0]*size[1])/9
			num_furniture = (size[0]*size[1])/25
			
			for y in range(pos[1],pos[1]+size[1]):
				for x in range(pos[0],pos[0]+size[0]):
					m.tilemap[y][x] = tl.tlist['elfish'][5]
			
			for y in range(pos[1]+1,pos[1]+size[1]-1):
				for x in range(pos[0]+1,pos[0]+size[0]-1):
					m.tilemap[y][x] = tl.tlist['elfish'][4]
					
			for i in range(0,num_beds):#set beds
				pos = m.find_any(tl.tlist['elfish'][4])
				m.tilemap[pos[1]][pos[0]] = deepcopy(tl.tlist['functional'][8])
				m.tilemap[pos[1]][pos[0]].replace = deepcopy(tl.tlist['building'][9])
				m.tilemap[pos[1]][pos[0]].civilisation = False
				m.tilemap[pos[1]][pos[0]].replace.civilisation = False
			
			for i in range(0,num_furniture):#set furnaces
				pos = m.find_any(tl.tlist['elfish'][4])
				m.tilemap[pos[1]][pos[0]] = deepcopy(tl.tlist['functional'][14])
				m.tilemap[pos[1]][pos[0]].replace = deepcopy(tl.tlist['building'][9])
				m.tilemap[pos[1]][pos[0]].civilisation = False
				m.tilemap[pos[1]][pos[0]].replace.civilisation = False
				
			for i in range(0,num_furniture):#set wb's
				pos = m.find_any(tl.tlist['elfish'][4])
				ran = random.randint(9,13)
				m.tilemap[pos[1]][pos[0]] = deepcopy(tl.tlist['functional'][ran])
				m.tilemap[pos[1]][pos[0]].replace = deepcopy(tl.tlist['building'][9])
				m.tilemap[pos[1]][pos[0]].civilisation = False
				m.tilemap[pos[1]][pos[0]].replace.civilisation = False
				
			for y in range(pos_original[1]+1,pos_original[1]+size[1]-1):#set blue floor
				for x in range(pos_original[0]+1,pos_original[0]+size[0]-1):
					if m.tilemap[y][x].techID == tl.tlist['elfish'][4].techID:
						 m.tilemap[y][x] = deepcopy(tl.tlist['building'][9])
						 m.tilemap[y][x].civilisation = False
						
		for yy in range(0,max_map_size,5):
			for xx in range(0,max_map_size):
				if m.tilemap[yy][xx].techID == tl.tlist['elfish'][3].techID:#this is elfish wall
					m.tilemap[yy][xx] = deepcopy(tl.tlist['building'][2]) #set a open door here
					m.tilemap[yy][xx].civilisation = False
					
					for yyy in range(yy-1,yy+2):
						for xxx in range(xx-1,xx+2):
							if yyy >= 0 and xxx >= 0 and xxx < max_map_size and yyy < max_map_size:
								if m.tilemap[yyy][xxx].techID != tl.tlist['elfish'][0].techID and m.tilemap[yyy][xxx].techID != tl.tlist['elfish'][1].techID and m.tilemap[yyy][xxx].techID != tl.tlist['shop'][0].techID and m.tilemap[yyy][xxx].techID != tl.tlist['building'][2].techID and m.tilemap[yyy][xxx].techID != tl.tlist['elfish'][3].techID and m.tilemap[yyy][xxx].techID != tl.tlist['elfish'][2].techID and m.tilemap[yyy][xxx].techID != tl.tlist['misc'][0].techID:
									#if a field next to a door isn't elfish_indoor, elfish_wall or shop_floor set it to elfish_indoor
									m.tilemap[yyy][xxx] = tl.tlist['elfish'][0]
					
		for yy in range(0,max_map_size):
			for xx in range(0,max_map_size,5):
				if m.tilemap[yy][xx].techID == tl.tlist['elfish'][3].techID:#this is elfish wall
					m.tilemap[yy][xx] = deepcopy(tl.tlist['building'][2]) #set a open door here
					m.tilemap[yy][xx].civilisation = False
					
					for yyy in range(yy-1,yy+2):
						for xxx in range(xx-1,xx+2):
							if yyy >= 0 and xxx >= 0 and xxx < max_map_size and yyy < max_map_size:
								if m.tilemap[yyy][xxx].techID != tl.tlist['elfish'][0].techID and m.tilemap[yyy][xxx].techID != tl.tlist['elfish'][1].techID and m.tilemap[yyy][xxx].techID != tl.tlist['shop'][0].techID and m.tilemap[yyy][xxx].techID != tl.tlist['building'][2].techID and m.tilemap[yyy][xxx].techID != tl.tlist['elfish'][3].techID and m.tilemap[yyy][xxx].techID != tl.tlist['elfish'][2].techID and m.tilemap[yyy][xxx].techID != tl.tlist['misc'][0].techID:
									#if a field next to a door isn't elfish_indoor, elfish_wall or shop_floor set it to elfish_indoor
									m.tilemap[yyy][xxx] = tl.tlist['elfish'][0]
					
		m.cut(5,max_map_size-6,5,max_map_size-6,tl.tlist['elfish'][3])
		m.set_frame(tl.tlist['functional'][0])
		
		#set fontains
		
		for y in range(10,max_map_size-10,10):
			for x in range(10,max_map_size-10,10):
				
				if m.tilemap[y][x].techID == tl.tlist['elfish'][1].techID:
					
					coin = random.randint(0,1)
					
					if coin == 0:
						m.tilemap[y][x] = deepcopy(tl.tlist['functional'][7])#set a fontain
						m.tilemap[y][x].replace = tl.tlist['elfish'][1]
						m.tilemap[y][x].civilisation = False #this is no players fontain 
		
		m.exchange(tl.tlist['elfish'][5],tl.tlist['elfish'][0])
		m.spawn_monsters(6)
		
		self.maplist[layer][map_name] = m
		
	def mine_generator(self,layer):
		
		cave_name = 'local_0_0'
		m = self.default_map_generator(cave_name,'global_caves', tilelist)
		m.map_type = 'orcish_mines'
		
		m.exchange(tl.tlist['global_caves'][4],tl.tlist['mine'][0])#exchange lava against mine floor
		m.exchange(tl.tlist['global_caves'][0],tl.tlist['mine'][0])#exchange cave ground against mine floor
		m.exchange(tl.tlist['global_caves'][2],tl.tlist['mine'][0])#exchange soft soil against mine floor
		m.exchange(tl.tlist['global_caves'][1],tl.tlist['mine'][1])#exchange worn rock against mine wall
		m.exchange(tl.tlist['global_caves'][3],tl.tlist['mine'][1])#exchange hard rock against mine wall
		
		m.exchange_when_surrounded(tl.tlist['mine'][1],tl.tlist['global_caves'][3],8) #only the outer tiles become mine wall
		
		for y in range (0, max_map_size):
			for x in range(0,max_map_size):
				 
				if m.tilemap[y][x].techID == tl.tlist['global_caves'][3].techID:#this is hard rock
				 
					ran = random.randint(0,99)
					 
					if ran > 69:
						 
						 m.tilemap[y][x] = tl.tlist['misc'][4]#set ore
					
					elif ran < 10:
						m.tilemap[y][x] = tl.tlist['misc'][5]#set gem
		
		m.set_frame(tl.tlist['functional'][0])
		
		m.make_shops()
		
		m.make_containers(15,30,tl.tlist['mine'][0],1,4,'remains')
		
		num_moss = ((max_map_size*max_map_size)/100)*3
		
		for i in range (0,num_moss):
			pos = m.find_any(tl.tlist['mine'][0])#find mine floor
			try:
				m.tilemap[pos[1]][pos[0]] = tl.tlist['mine'][2]#set blood moss
			except:
				None
		
		m.spawn_monsters(9)
							
		self.maplist[layer][cave_name] = m		
		
	def cave_generator(self, deep):
			
		cave_name = 'local_0_0'
					
		for d in range(1,deep+2):
			
			m = self.default_map_generator(cave_name,'global_caves', tilelist)
			if d < 10:
				m.map_type = 'cave'
			else:
				m.map_type = 'lava_cave'
			
			if d > 9:
				m.exchange(tl.tlist['global_caves'][4],tl.tlist['misc'][2])#exchange lava against hot cave ground
				if d > 10:
					m.exchange_when_surrounded(tl.tlist['misc'][2],tl.tlist['global_caves'][4],8)#make lava spots between hot cave ground
					num = (max_map_size*max_map_size)/(50*50)
					for i in range(0,num):
						ran = random.randint(0,1)
						if ran > 0:
							pos = m.find_any(tl.tlist['global_caves'][0]) #cave ground
							m.tilemap[pos[1]][pos[0]] = deepcopy(tl.tlist['functional'][23])# make master forges
			else:
				m.exchange(tl.tlist['global_caves'][4],tl.tlist['misc'][1])#exchange lava against mud
				m.exchange_when_surrounded(tl.tlist['misc'][1],tl.tlist['misc'][0],8)#make low water spots between mud
				
			#######set mushrooms, ore and gems
		
			chance_ore = d
			chance_gem = d/2
			
			for y in range (0,max_map_size):
				for x in range (0,max_map_size):
					
					if m.tilemap[y][x].techID == tl.tlist['global_caves'][3].techID:#this is hard rock
						
						replace = m.tilemap[y][x].replace
						
						coin = random.randint(0,1)
						percent = random.randint(1,100) 
						
						if coin == 0 and percent <= chance_ore:
							m.tilemap[y][x] = tl.tlist['misc'][4]#set ore here
							m.tilemap[y][x].replace = replace
						elif coin == 1 and percent <= chance_gem:
							m.tilemap[y][x] = tl.tlist['misc'][5]#set gem here
							m.tilemap[y][x].replace = replace
							
					if m.tilemap[y][x].techID == tl.tlist['misc'][1].techID:#this is mud
						
						cent = random.randint(0,99)
						
						if cent < 10: #its a chance of 10% that a blue mushroom spawns here
							
							replace = m.tilemap[y][x]
							m.tilemap[y][x] = tl.tlist['misc'][6]
							m.tilemap[y][x].replace = replace
							
							m.containers[y][x] = container([deepcopy(il.ilist['food'][1])])
					
					if m.tilemap[y][x].techID == tl.tlist['global_caves'][0].techID:#this is cave ground
						
						cent = random.randint(0,99)
						
						if cent < 10: #its a chance of 10% that a brown mushroom spawns here
							
							replace = m.tilemap[y][x]
							m.tilemap[y][x] = tl.tlist['misc'][7]
							m.tilemap[y][x].replace = replace
							
							m.containers[y][x] = container([deepcopy(il.ilist['food'][2])])
							
						elif cent < 15: #its a chance of 5% that a purple mushroom spawns here
							
							replace = m.tilemap[y][x]
							m.tilemap[y][x] = tl.tlist['misc'][8]
							m.tilemap[y][x].replace = replace
							
							m.containers[y][x] = container([deepcopy(il.ilist['food'][3])])
			
			m.set_frame(tl.tlist['functional'][0])
			
			if d == 1:#set stair up on lvl 1
				pos = (max_map_size/2,max_map_size/2)
				m.tilemap[pos[1]+1][pos[0]] = deepcopy(tl.tlist['functional'][2])#stair down
				m.tilemap[pos[1]+1][pos[0]].damage = -1
				m.tilemap[pos[1]+1][pos[0]].damage_mes = 'Your wounds are cured.'
				m.tilemap[pos[1]+1][pos[0]].build_here = False
				
				for x in range(0,max_map_size):
					if m.tilemap[x][pos[0]].techID == tl.tlist['global_caves'][3].techID:#this is hard rock
						ran = random.randint(1,2)
						m.tilemap[x][pos[0]] = deepcopy(tl.tlist['global_caves'][ran])
						
				for y in range(0,max_map_size):
					if m.tilemap[pos[1]+1][y].techID == tl.tlist['global_caves'][3].techID:#this is hard rock
						ran = random.randint(1,2)
						m.tilemap[pos[1]+1][y] = deepcopy(tl.tlist['global_caves'][ran])
			
			m.make_containers(1,2,tl.tlist['global_caves'][0],2,5,'chest')#set some chests
			m.make_special_monsters(0,1,tl.tlist['global_caves'][0],d,'mimic')#maybe set some mimics
			m.make_special_monsters(15,25,tl.tlist['global_caves'][0],d,'vase')#set some vases
			
			m.spawn_monsters(d)
							
			self.maplist[d][cave_name] = m
							
	def grassland_generator(self,x,y,chance_scrubs, chance_trees, chance_herbs, number_rocks):
		# chance_scrubs and chance_trees must be between 0 and 99
		name = 'local_0_0'
		
		helpmap = self.default_map_generator('1','help',tilelist)
		
		tilemap = []
		for a in range (0,max_map_size):
			tilemap.append([])
			for b in range (0,max_map_size):
				tilemap[a].append(0)
	
		m = map(name,tilemap)
		m.map_type = 'overworld'
		
		
		m.fill(tl.tlist['local'][0])#fill the map with grass
				
		# set scrubs
		
		for y in range (0,max_map_size):
			for x in range (0,max_map_size):
				if helpmap.tilemap[y][x].techID == tl.tlist['help'][0].techID: #<---scrub here
					chance = random.randint(0,99)
					if chance < chance_scrubs:
						scrubs = (1,3,4,6,7,8,9)
						coin = random.randint(0,len(scrubs)-1)
						m.tilemap[y][x] = deepcopy(tl.tlist['local'][scrubs[coin]])
						m.tilemap[y][x].replace = tl.tlist['local'][0]
						
							
		#set trees
		
		for y in range (0,max_map_size):
			for x in range (0,max_map_size):
				if helpmap.tilemap[y][x].techID == tl.tlist['help'][1].techID: #<---tree here
					chance = random.randint(0,99)
					if chance < chance_trees:
						coin = random.randint(10,13)
						m.tilemap[y][x] = tl.tlist['local'][coin]
						m.tilemap[y][x].replace = tl.tlist['local'][0]#grass
		
		#set herbs
		
		for y in range (0,max_map_size):
			for x in range (0,max_map_size):
				if helpmap.tilemap[y][x].techID == tl.tlist['help'][0].techID: #<---scrub here
					chance = random.randint(0,99)
					if chance < chance_herbs:
						coin = random.randint(15,16)
						m.tilemap[y][x] = tl.tlist['local'][coin]
						m.tilemap[y][x].replace = tl.tlist['local'][0]#grass
			
		# set rocks
		
		for n in range (0,number_rocks):
			x = random.randint(0,max_map_size-1)
			y = random.randint(0,max_map_size-1)
			m.tilemap[y][x] = tl.tlist['local'][14]
			m.tilemap[y][x].replace = tl.tlist['local'][0]#grass
		
		#set water
			
		for y in range (0,max_map_size):
			for x in range (0,max_map_size):
				if helpmap.tilemap[y][x].techID == tl.tlist['help'][2].techID: #<---water here
					m.tilemap[y][x] = tl.tlist['misc'][0] # set low water here
					
		m.exchange_when_surrounded(tl.tlist['misc'][0],tl.tlist['misc'][3],8) # exchange low wather against deep water
		
		pos = (max_map_size/2,max_map_size/2)
		
		m.set_sanctuary(pos[0],pos[1])
		
		m.set_frame(tl.tlist['functional'][0])
		
		#set guidepost
		y = max_map_size -2
		x = random.randint(2,max_map_size-2)
		m.tilemap[y][x] = tl.tlist['extra'][6]
		m.tilemap[y][x].replace = tl.tlist['local'][0]#grass
		m.tilemap[y-1][x] = tl.tlist['local'][0]#grass
		
		m.spawn_monsters(0)
					
		self.maplist[0][name] = m
		
		return pos
		
	def desert_generator(self,chance_cactus):
		# chance_scrubs and chance_trees must be between 0 and 99
		name = 'desert_0_0'
		
		tilemap = []
		for a in range (0,max_map_size):
			tilemap.append([])
			for b in range (0,max_map_size):
				tilemap[a].append(0)
	
		m = map(name,tilemap)
		m.map_type = 'desert'
		m.build_type = 'Part'
		
		m.fill(tl.tlist['extra'][0])
		
		y_river = random.randint((17),(max_map_size-17))
		river_offset = random.randint(-3,3)
		plus = 0
		minus = 0
		
		for c in range (0,max_map_size):
			
			for g in range (-2,7):
				m.tilemap[y_river+river_offset+g][c] = tl.tlist['local'][0]#set grass
				
			for w in range (0,5):
				m.tilemap[y_river+river_offset+w][c] = tl.tlist['misc'][0]#set low water
				
			if river_offset < 5:
				plus = 1
			else:
				plus = 0
				
			if river_offset > -5:
				minus = -1
			else:
				minus = 0
				
			offset_change = random.randint(minus,plus)
			river_offset += offset_change
			
		m.exchange_when_surrounded(tl.tlist['misc'][0],tl.tlist['misc'][3],7)
		
		for b in range(2,max_map_size-2,10):
			#north side of the river
			building_offset =random.randint(0,4)
			
			for y in range(y_river-12,y_river-7):
				for x in range(b+building_offset,b+building_offset+5):
					
					if x == b+building_offset or x == b+building_offset+4:
						if y == y_river-10:
							m.tilemap[y][x] = deepcopy(tl.tlist['extra'][9])
						else:
							m.tilemap[y][x] = deepcopy(tl.tlist['extra'][2])
					elif y == y_river-12 or y == y_river-8:
						if x == b+building_offset+2:
							m.tilemap[y][x] = deepcopy(tl.tlist['extra'][9])
						else:
							m.tilemap[y][x] = deepcopy(tl.tlist['extra'][2])
					else:
						m.tilemap[y][x] = deepcopy(tl.tlist['extra'][1])
						
					if x == b+building_offset+1 or x == b+building_offset+3:
						if y == y_river-10:
							ran = random.randint(5,6)
							m.npcs[y][x] = deepcopy(ml.mlist['special'][ran])
							
			#south side of the river			
			building_offset =random.randint(0,4)
			
			for y in range(y_river+8,y_river+13):
				for x in range(b+building_offset,b+building_offset+5):
					
					if x == b+building_offset or x == b+building_offset+4:
						if y == y_river+10:
							m.tilemap[y][x] = deepcopy(tl.tlist['extra'][9])
						else:
							m.tilemap[y][x] = deepcopy(tl.tlist['extra'][2])
					elif y == y_river+12 or y == y_river+8:
						if x == b+building_offset+2:
							m.tilemap[y][x] = deepcopy(tl.tlist['extra'][9])
						else:
							m.tilemap[y][x] = deepcopy(tl.tlist['extra'][2])
					else:
						m.tilemap[y][x] = deepcopy(tl.tlist['extra'][1])
		
					if x == b+building_offset+1 or x == b+building_offset+3:
						if y == y_river+10:
							ran = random.randint(5,6)
							m.npcs[y][x] = deepcopy(ml.mlist['special'][ran])
		
		x_pos = random.randint(3,10)
		make_bridges = True
		
		while make_bridges:
			x_pos_plus = random.randint(5,15)
			x_pos += x_pos_plus
			
			if x_pos >= max_map_size:
				make_bridges = False
			if make_bridges == True:
				for y in range(0,max_map_size):
					if m.tilemap[y][x_pos].techID == tl.tlist['misc'][0].techID or m.tilemap[y][x_pos].techID == tl.tlist['misc'][3].techID: #this is low wather or deep water
						replace = deepcopy(m.tilemap[y][x_pos])
						m.tilemap[y][x_pos] = deepcopy(tl.tlist['extra'][8])
						m.tilemap[y][x_pos].replace = replace
				
		for y in range (0,max_map_size):
			for x in range (0,max_map_size): 
				if m.tilemap[y][x].techID == tl.tlist['extra'][0].techID:
					chance = random.randint(0,99)
					if chance < chance_cactus:
						coin = random.randint(3,5)
						m.tilemap[y][x] = tl.tlist['extra'][coin]
						m.tilemap[y][x].replace = tl.tlist['extra'][0]#sand
		
		m.set_frame(tl.tlist['functional'][0])
		
		#set guidepost
		y = 2
		x = random.randint(2,max_map_size-2)
		m.tilemap[y][x] = tl.tlist['extra'][7]
		m.tilemap[y][x].replace = tl.tlist['extra'][0]#sand
		m.tilemap[y+1][x] = tl.tlist['extra'][0]#sand
		
		m.spawn_monsters(0)
					
		self.maplist[0][name] = m
		
	def choose_size(self):
		#this is a all in one function with render, choose and set
		global max_map_size # I know its no good style
		run = True
		mms = 52 #this is a temp variable that is used to store the worth for the max_map_size till this function is called 
		num = 0
		
		while run:
		#Part 1: Render
			s = pygame.Surface((640,360))
			s.blit(gra_files.gdic['display'][1],(0,0)) #render background


			text_image = screen.menu_font.render('~*~ Choose Map-Size ~*~            [e]',1,(255,255,255))
			s.blit(text_image,(5,2))#menue title
			
			entries = ('Small (50x50)', 'Medium (100x100)', 'Big (150x150)')
			messages = ('Everything on a very small space.', 'Perfect size for the most players.', 'A big world.')
			mapsizes = (52,102,152)
			
			for i in range (0,3):
				
				entry_image = screen.menu_font.render(entries[i],1,(0,0,0))
				s.blit(entry_image,(150,120+i*30))#render entries
				
			s.blit(gra_files.gdic['display'][4],(120,115+num*30))#blit marker
				
			entry_image = screen.menu_font.render(messages[num],1,(255,255,255))
			s.blit(entry_image,(5,335))#render message
			if game_options.mousepad == 1:
				s.blit(gra_files.gdic['display'][8],(480,0)) #render mouse pad
			else:
				s_help = pygame.Surface((160,360))
				s_help.fill((48,48,48))
				s.blit(s_help,(480,0))
			
			if game_options.mousepad == 0:
				s_help = pygame.Surface((640,360))
				s_help.fill((48,48,48))
				s_help.blit(s,(80,0))
				s = s_help
			
			s = pygame.transform.scale(s,(screen.displayx,screen.displayy))
			screen.screen.blit(s,(0,0))
			
			pygame.display.flip()
			
		#Step 2: Choose
		
			ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
		
			if ui == 'w':
			
				num -= 1
				if num < 0:
					num = 2
				
			if ui == 's':
			
				num += 1
				if num > 2:
					num = 0
				
			if ui == 'e':
			
				mms = mapsizes[num]
				max_map_size = mms
				self.map_size = mms
				run = False
			
class mob():
	
	def __init__(self, name, on_map, attribute, pos =[40,40,0],glob_pos=[0,0],build='Manual'):
		
		self.name = name
		self.on_map = on_map
		self.attribute = attribute
		self.lp = attribute.max_lp
		self.mp = attribute.max_mp
		self.pos = pos	
		self.glob_pos = glob_pos

		
	def move(self, x=0, y=0):
		
		mc = self.move_check(x,y)
		tile_move_group = world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]+y][self.pos[0]+x].move_group
		player_move_groups = ['soil','low_liquid','holy','shop','house']
		
		swim_check = True
		
		for i in ('Head','Body','Legs','Feet'):
			if player.inventory.wearing[i] != player.inventory.nothing:
				swim_check = False
				
		if swim_check == True:
			player_move_groups.append('swim')
		
		move_check2 = False	
		
		for j in player_move_groups:
			if j == tile_move_group:
				move_check2 = True
		
		if mc == True:
			if x > 0 and move_check2 == True and self.pos[0] < max_map_size - 1:
				self.pos[0] += 1
			
			if x < 0 and move_check2 == True and self.pos[0] > 0:
				self.pos[0] -= 1
			
			if y > 0 and move_check2 == True and self.pos[1] < max_map_size - 1:
				self.pos[1] += 1
			
			if y < 0 and move_check2 == True and self.pos[1] > 0:
				self.pos[1] -= 1
				
		self.stand_check()
		
	def move_check(self,x,y):
		
		try:
			
			if world.maplist[self.pos[2]][self.on_map].npcs[self.pos[1]+y][self.pos[0]+x]:
				player.attack_monster(self.pos[0]+x,self.pos[1]+y)
				return False
			
			if world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]+y][self.pos[0]+x].destroy != False: #for digging
				
				if self.attribute.pickaxe_power + player.inventory.wearing['Hold(R)'].attribute.pickaxe_power >= world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]+y][self.pos[0]+x].destroy:
					if self == player:
						message.add(world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]+y][self.pos[0]+x].move_mes)
						
						try:
							material = world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]+y][self.pos[0]+x].conected_resources[0]
							mat_num = world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]+y][self.pos[0]+x].conected_resources[1]
							mes = player.inventory.materials.add(material,mat_num)
							message.add(mes)
						except:
							None
							
						if world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]+y][self.pos[0]+x].techID == tl.tlist['building'][3].techID: #this is a closed door
							world.maplist[self.pos[2]][self.on_map].countdowns.append(countdown('door', self.pos[0]+x, self.pos[1]+y,3))
							player.inventory.wearing['Hold(R)'].defensibility += 1 #open doors dosn't damage your tool
							
					world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]+y][self.pos[0]+x] = deepcopy(world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]+y][self.pos[0]+x].replace)
					
					if player.inventory.wearing['Hold(R)'] != player.inventory.nothing:
					
						player.inventory.wearing['Hold(R)'].take_damage()
					
						if player.inventory.wearing['Hold(R)'].state > 0:
							player.inventory.wearing['Hold(R)'].set_name()
						else:
							message.add('Your tool breaks into pieces.')
							player.inventory.wearing['Hold(R)'] = player.inventory.nothing
					
				else:
					if self == player:
							message.add('You are unable to destroy this with the tool in your hand.')
					
				return False
			
			else:
				None
				
			if world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]+y][self.pos[0]+x].move_group == 'tree':
				
				if player.inventory.wearing['Hold(R)'].classe == 'axe': #if player has a axe in his hand
										
					try:
						material = world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]+y][self.pos[0]+x].conected_resources[0]
						mat_num = world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]+y][self.pos[0]+x].conected_resources[1]
						mes = player.inventory.materials.add(material,mat_num)
						message.add(mes)
						world.maplist[self.pos[2]][self.on_map].make_monsters_angry(self.pos[0],self.pos[1],'tree')
					except:
						None
					
					world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]+y][self.pos[0]+x] = deepcopy(world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]+y][self.pos[0]+x].replace) #let the tree dissappear
					
					player.inventory.wearing['Hold(R)'].take_damage()
					
					if player.inventory.wearing['Hold(R)'].state > 0:
						player.inventory.wearing['Hold(R)'].set_name()
					else:
						message.add('Your axe breaks into pices.')
						player.inventory.wearing['Hold(R)'] = player.inventory.nothing		
						
					return False
					
				else:
					if self == player:
						message.add('You need a axe.')
					
					return False
			
			return True
			
		except:
			
			None
			
	def stand_check(self):
		
		radius = 4
		
		if player.pos[2] > 0:
			radius = 2
		elif player.pos[2] == 0:
			if time.hour > 19 or time.hour < 6:
				radius = 2 
			
		if player.buffs.light > 0:
			radius = 4
			
		if player.buffs.blind > 0:
			radius = 1
		
		message.add(world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].move_mes,True)
		
		if world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].damage > 0:
			self.lp = self.lp - world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].damage
			if self == player:
				try:
					message.add(world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].damage_mes + ' (' + str(world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].damage) + ' Damage)')
				except:
					None
		
		elif world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].damage < 0:
			if self.lp < self.attribute.max_lp:	
				self.lp = self.lp - world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].damage
				
		for y in range (-radius,radius+1):#line of sight
			for x in range (-radius,radius+1):
				try:
				
					dist = ((x)**2+(y)**2)**0.5
				
					if dist <= radius+1 or dist >= radius-1:
						
						run = True
						c = 0
						
						while run:
						
							try:
								yy = ((y*c)/dist)
							except:
								yy = 1
						
							try:
								xx = ((x*c)/dist)
							except:
								xx = 1
							
							view_x = int(xx) + self.pos[0]
							view_y = int(yy) + self.pos[1]
							
							world.maplist[self.pos[2]][self.on_map].known[view_y][view_x] = 1
							
							
							if world.maplist[self.pos[2]][self.on_map].tilemap[view_y][view_x].transparency == True and c < radius:
								c+=1
							else:
								run = False
				except:
					None
					
		if player.lp <= 0:
			screen.render_dead()
		
		bgm.check_for_song()
					
	def enter(self):
		
		if world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].use_group == 'stair_down':
			if world.maplist[self.pos[2]+1][self.on_map].tilemap[self.pos[1]][self.pos[0]].techID == tl.tlist['functional'][2].techID: #if there is a stair up below this
				player.pos[2] += 1
				player.stand_check()#to unveil the surroundings
			else:
				message.add('This stair seem to be blocked.')
			
		elif world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].use_group == 'stair_up': #this is a stair up
			if world.maplist[self.pos[2]-1][self.on_map].tilemap[self.pos[1]][self.pos[0]].techID == tl.tlist['functional'][1].techID: #if there is a stair down above
				player.pos[2] -= 1
				player.stand_check()#to unveil the surroundings
			else:
				message.add('This stair seem to be blocked.')
			
		elif world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].use_group == 'drink':#this is a low wather or a fontain
			#drink water
			if player.attribute.thirst < player.attribute.thirst_max:
				message.add('You take a sip of water.')
				player.attribute.thirst += 240 #this is 1/3 of the water te player needs per day
				if player.attribute.thirst > player.attribute.thirst_max:
					player.attribute.thirst = player.attribute.thirst_max+1#the +1 is because the player will lose one point at the same round so you would get just 99%
			else:
				message.add('You are not thirsty right now.')
				
		elif world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].use_group == 'resource':
			res = world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].conected_resources[0]
			num = world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].conected_resources[1]
			try:
				conected_tile = world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].conected_tiles[0]
			except:
				None
			test = player.inventory.materials.add(res,num)
			if test != 'Full!':
				message.add(test)
				replace = world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].replace
				try:
					world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]] = deepcopy(tl.tlist[conected_tile[0]][conected_tile[1]])
					world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].replace = replace
				except:
					world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]] = replace
			else:
				message.add(test)
				
		elif world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].use_group == 'sleep':#this is a bed
			#sleep a bit
			sleep = True
			
			while sleep:
				screen.render_load(12)
				time.tick()
				player.attribute.tiredness += 5
				if player.buffs.adrenalised_max > 0:
					player.buffs.adrenalised_max -= 5
				elif player.buffs.adrenalised_max < 0:
					player.buffs.adrenalised_max = 0
				
				if player.attribute.tiredness >= player.attribute.tiredness_max:#wake up because you've slept enough
					player.attribute.tiredness = player.attribute.tiredness_max +1 #the +1 is because the player will lose one point at the same round so you would get just 99%
					message.add('You feel refreshed.')
					sleep = False
					
				monster_test = False
					
				for y in range (player.pos[1]-1, player.pos[1]+1):#check for a monster
					for x in range (player.pos[0]-1, player.pos[0]+1):
						
						try:
							
							if world.maplist[self.pos[2]][self.on_map].npcs[self.pos[1]][self.pos[0]] != 0:#<-------change this so that friendly npcs are ignored 
								monster_test = True
								
						except:
							
							None
						
				if monster_test == True:#wake up because a monster borders the players sleep
					message.add('You wake up with a sense of danger.')
					sleep = False
		
		elif world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].use_group == 'gather':
			help_container = container([world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].conected_items])
			item_name = help_container.items[0].name
			test_loot = help_container.loot(0)
			if test_loot == True:
				string = '+[' + item_name + ']'
				message.add(string)
				world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]] = world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].replace
			else:
				message.add('Your inventory is full!')
				
		elif world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].use_group == 'gather_scrub':
			help_container = container([world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].conected_items])
			item_name = help_container.items[0].name
			test_loot = help_container.loot(0)
			if test_loot == True:
				string = 'You take ' + item_name + '.'
				message.add(string)
				cat = world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].conected_tiles[1][0]
				num = world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].conected_tiles[1][1]
				replace = world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].replace
				world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]] = tl.tlist[cat][num]
				world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].replace = replace
			else:
				message.add('Your inventory is full!')
				
		elif world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].use_group == 'carpenter': 
			#this is a carpenter's workbench
			
			run = True
			
			while run:
				
				if world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] != 0:
					if len(world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]].items) < 7:
						screen.render_request('[e] - produce something (-10 Wood)', '[b] - take a produced item', '[x] - leave')
					else:
						screen.render_request('[e] -     XXXXXXXXXXXX            ', '[b] - take a produced item', '[x] - leave')
				else:
					screen.render_request('[e] - produce something (-10 Wood)', '[b] -      XXXXXXXXXXXX   ', '[x] - leave')
					
				ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
				
				if ui == 'e':
					test = False
					
					if world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] != 0:
						if len(world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]].items) < 7:
							test = True
					else:
						test = True
					
					
					if test == True:
						
						if player.inventory.materials.wood >= 10:
							gc = screen.get_choice('What do you want to produce?', ('Carpenter\'s Workbench', 'Carver\'s Workbench', 'Stonecuter\'s Workbench', 'Forger\'s Workbench', 'Alchemist\'s Workshop', 'Furniture'),True)
							
							if gc < 5:# give the choosen workbench to the player
								items = (il.ilist['misc'][3],il.ilist['misc'][4],il.ilist['misc'][5],il.ilist['misc'][6],il.ilist['misc'][7])
								choose = gc
							elif gc == 5:
								items = (il.ilist['misc'][1], il.ilist['misc'][2],il.ilist['misc'][10],il.ilist['misc'][11],il.ilist['misc'][13])
								#chest, bed, table, w. seat, bookshelf
								choose = random.randint(0, len(items)-1)
							try:
								if world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] == 0: 
									world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] = container([items[choose]])
								else:
									world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]].items.append(items[choose])
									
								message_string = 'You produced a ' + items[choose].name + '.'
								message.add(message_string)
								player.inventory.materials.wood -= 10
							except:
								None
								
							run = False
						
						else:
							message.add('You have not enough wood!')
							run = False
						
				elif ui == 'b' and world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] != 0:
				
						world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]].inventory(False)
						run = False
						
				elif ui == 'x':
					
					run = False
					
		elif world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].use_group == 'carver': 
			#this is a carvers's workbench
			
			run = True
			
			while run:
				
				if world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] != 0:
					if len(world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]].items) < 7:
						screen.render_request('[e] - produce something (-5 Wood)', '[b] - take a produced item', '[x] - leave')
					else:
						screen.render_request('[e] -     XXXXXXXXXXXX            ', '[b] - take a produced item', '[x] - leave')
				else:
					screen.render_request('[e] - produce something (-5 Wood)', '[b] -      XXXXXXXXXXXX   ', '[x] - leave')
					
				ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
				
				if ui == 'e':
					test = False
					
					if world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] != 0:
						if len(world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]].items) < 7:
							test = True
					else:
						test = True
					
					
					if test == True:
						if player.inventory.materials.wood >= 5:
							
							final_choice = 'Foo'
							gc = screen.get_choice('What do you want to prodcuce exactly?', ('Tool', 'Weapon', 'Armor','Jewelry'), True)
							
							if gc == 0: #make a tool
								items = (il.ilist['misc'][14], il.ilist['misc'][44], item_wear('axe',0,0), item_wear('pickaxe',0,0))
								final_choice = screen.get_choice('What do you want to prodcuce exactly?', ('Fishing rod','Torch','Axe','Pickaxe'),True)
							elif gc == 1: #make a weapon
								items = (item_wear('spear',0,0), item_wear('sword',0,0), item_wear('hammer',0,0), item_wear('wand',0,0), item_wear('rune',0,0), item_wear('rune staff',0,0), item_wear('artefact',0,0))
							elif gc == 2: #make some armor
								items = (item_wear('shoes',0,0), item_wear('cuisse',0,0), item_wear('helmet',0,0), item_wear('armor',0,0))
								final_choice = screen.get_choice('What do you want to prodcuce?', ('Shoes','Cuisse','Helmet','Armor'), True)
							elif gc == 3:#make some jewlry
								items = (item_wear('ring',0,0),  item_wear('amulet',0,0),  item_wear('necklace',0,0), item_wear('talisman',0,0))
							
							if final_choice == 'Foo':	
								choose = random.randint(0, len(items)-1)
							else:
								choose = final_choice
							try:
								if world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] == 0: 
									world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] = container([items[choose]])
								else:
									world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]].items.append(items[choose])
								
								message_string = 'You produced a ' + items[choose].name + '.'
								message.add(message_string)
								player.inventory.materials.wood -= 5
							except:
								None
								
							run = False
						
						else:
							message.add('You have not enough wood!')
							run = False
						
				elif ui == 'b' and world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] != 0:
				
						world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]].inventory(False)
						run = False
						
				elif ui == 'x':
					
					run = False
									
		
		elif world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].use_group == 'stonecutter': 
			#this is a stonecutter's workbench
			
			run = True
			
			while run:
				
				if world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] != 0:
					if len(world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]].items) < 7:
						screen.render_request('[e] - produce something (-10 Stone)', '[b] - take a produced item', '[x] - leave')
					else:
						screen.render_request('[e] -     XXXXXXXXXXXX            ', '[b] - take a produced item', '[x] - leave')
				else:
					screen.render_request('[e] - produce something (-10 Stone)', '[b] -      XXXXXXXXXXXX   ', '[x] - leave')
					
				ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
				
				if ui == 'e':
					test = False
					
					if world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] != 0:
						if len(world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]].items) < 7:
							test = True
					else:
						test = True
					
					
					if test == True:
						if player.inventory.materials.stone >= 10:
							
							gc = screen.get_choice('What do you want to produce?' ,('Functional Things', 'Decorative Things'), True)
							
							if gc == 0: #make something functional
								items = (il.ilist['misc'][0], il.ilist['misc'][8], il.ilist['misc'][9])
								#items: fontain, furnace, altar
							else:#make something decorative
								items = (il.ilist['misc'][12],il.ilist['misc'][21])
								#items: stone seat, pilar ---> have to become more
							
							choose = random.randint(0, len(items)-1)
							try:
								if world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] == 0: 
									world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] = container([items[choose]])
								else:
									world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]].items.append(items[choose])
								
								message_string = 'You produced a ' + items[choose].name + '.'
								message.add(message_string)
								player.inventory.materials.stone -= 10
							except:
								None
								
							run = False
						
						else:
							message.add('You have not enough Stone!')
							run = False
						
				elif ui == 'b' and world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] != 0:
				
						world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]].inventory(False)
						run = False
						
				elif ui == 'x':
					
					run = False
					
		elif world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].use_group == 'forger': 
			#this is a forger's workbench or a master forge
			
			run = True
			
			while run:
				
				price = 5
				if world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].techID == tl.tlist['functional'][23].techID: #this is a master forge
					price = 15
				
				if world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] != 0:
					if len(world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]].items) < 7:
						string = '[e] - produce something (-' + str(price) + ' Ore)', '[b] - take a produced item', '[x] - leave'
						screen.render_request(string)
					else:
						screen.render_request('[e] -     XXXXXXXXXXXX            ', '[b] - take a produced item', '[x] - leave')
				else:
					string = '[e] - produce something (-' + str(price) + ' Ore)', '[b] -      XXXXXXXXXXXX   ', '[x] - leave'
					screen.render_request(string[0],string[1],string[2])
					
				ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
				
				if ui == 'e':
					test = False
					
					if world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] != 0:
						if len(world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]].items) < 7:
							test = True
					else:
						test = True
					
					
					if test == True:
						if player.inventory.materials.ore >= price:
							
							material = random.randint(6,20)#tin to magnicum
							if world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].techID == tl.tlist['functional'][23].techID: #this is a master forge
								material = 20 #magnicum only
							
							final_choice = 'Foo'
							gc = screen.get_choice('What do you want to procuce?', ('Tool', 'Weapon', 'Armor','Jewelry'), True)
							
							if gc == 0: #make a tool
								final_choice = screen.get_choice('What do you want to procuce exactly?', ('Axe', 'Pickaxe'), True)
								items = (item_wear('axe',material,0), item_wear('pickaxe',material,0)) 
							elif gc == 1: #make a weapon
								items = (item_wear('spear',material,0), item_wear('sword',material,0), item_wear('hammer',material,0), item_wear('wand',material,0), item_wear('rune',material,0), item_wear('rune staff',material,0), item_wear('artefact',material,0))
							elif gc == 2: #make some armor
								final_choice = screen.get_choice('What do you want to procuce exactly?', ('Shoes', 'Cuisse', 'Helmet', 'Armor'), True)
								items = (item_wear('shoes',material,0), item_wear('cuisse',material,0), item_wear('helmet',material,0), item_wear('armor',material,0))
							elif gc == 3:#make some  jewelry
								items = (item_wear('ring',material,0),  item_wear('amulet',material,0),  item_wear('necklace',material,0), item_wear('talisman',material,0))
							
							if final_choice == 'Foo':	
								choose = random.randint(0, len(items)-1)
							else:
								choose = final_choice
							try:
								if world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] == 0: 
									world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] = container([items[choose]])
								else:
									world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]].items.append(items[choose])
								
								message_string = 'You produced a ' + items[choose].name + '.'
								message.add(message_string)
								player.inventory.materials.ore -= price
							except:
								None
								
							run = False
						
						else:
							message.add('You have not enough ore!')
							run = False
						
				elif ui == 'b' and world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] != 0:
				
						world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]].inventory(False)
						run = False
						
				elif ui == 'x':
					
					run = False
		
		elif world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].use_group == 'alchemist': 
			#this is a alchemists's workshop
			
			run = True
			
			while run:
				
				if world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] != 0:
					if len(world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]].items) < 7:
						screen.render_request('[e] - brew a potion (-5 Herbs)', '[b] - take a potion', '[x] - leave')
					else:
						screen.render_request('[e] -     XXXXXXXXXXXX            ', '[b] - take a potion', '[x] - leave')
				else:
					screen.render_request('[e] - brew a potion (-5 Herbs)', '[b] -      XXXXXXXXXXXX   ', '[x] - leave')
					
				ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
				
				if ui == 'e':
					test = False
					
					if world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] != 0:
						if len(world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]].items) < 7:
							test = True
					else:
						test = True
					
					
					if test == True:
						if player.inventory.materials.herb >= 5:
							
							ordenary_potions = (il.ilist['food'][13],il.ilist['food'][14],il.ilist['food'][15],il.ilist['food'][16])
							#ordenary potions are: p.o. healing, p.o. feeding, p.o. refreshing, p.o. vitalising 
							strong_potions = (il.ilist['food'][17],il.ilist['food'][18],il.ilist['food'][19],il.ilist['food'][20])
							#strong potions are: s.p.o. healing, s.p.o. feeding, s.p.o. refreshing, s.p.o. vitalising 
							upgrade_potions = (il.ilist['food'][21],il.ilist['food'][22],il.ilist['food'][23],il.ilist['food'][24])
							#upgrade potions are: p.o. hunger, p.o. thirst, p.o. tiredness, p.o. life
							
							choose = random.randint(0,99) 
							
							if choose < 70: #make a ordenary potion(70%)
								items = ordenary_potions
							elif choose < 95:#make a strong potion(25%) 
								items = strong_potions
							else:#make a upgrade potion(5%)
								items = upgrade_potions
					
							choose = random.randint(0, len(items)-1)
							
							if world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] == 0: 
								world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] = container([items[choose]])
							else:
								world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]].items.append(items[choose])
								
							message_string = 'You brewed a ' + items[choose].name + '.'
							message.add(message_string)
							player.inventory.materials.herb -= 5
							run = False
						
						else:
							message.add('You have not enough herbs!')
							run = False
						
				elif ui == 'b' and world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] != 0:
				
						world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]].inventory(False)
						run = False
						
				elif ui == 'x':
					
					run = False
		
		elif world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].use_group == 'furnace': 
			#this is a furnace
			
			run = True
			
			while run:
				
				screen.render_request('[e] - fire up the furnace (-10 wood)', ' ', '[x] - leave')
					
				ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
				
				if ui == 'e':
					
					if player.inventory.materials. wood >= 10:
						
						message.add('You ligth up a fire.')
						
						for i in range (0,len(player.inventory.food)):
							if player.inventory.food[i] != player.inventory.nothing: 
								if player.inventory.food[i].techID == il.ilist['food'][4].techID: #this is a fish
									message.add('You grill a fish.')
									player.inventory.food[i] = deepcopy(il.ilist['food'][5])#turn a fish into a grilled fish
								elif player.inventory.food[i].techID == il.ilist['food'][6].techID: #this are crops
									message.add('You bake a bread.')
									player.inventory.food[i] = deepcopy(il.ilist['food'][7])#turn crops into bread
								elif player.inventory.food[i].techID == il.ilist['food'][7].techID: #this is a bread
									message.add('You bake a bread for a second time.')
									player.inventory.food[i] = deepcopy(il.ilist['food'][8])#turn a bread into rusk
								elif player.inventory.food[i].techID == il.ilist['food'][9].techID: #this is raw meat
									message.add('You grill raw meat.')
									player.inventory.food[i] = deepcopy(il.ilist['food'][10])#turn a fish into a grilled fish
								elif player.inventory.food[i].techID == il.ilist['food'][11].techID: #this is a cult. mushroom
									message.add('You grill a mushroom.')
									player.inventory.food[i] = deepcopy(il.ilist['food'][12])#turn a cult. mushroom into a grilled mushroom
								elif player.inventory.food[i].techID == il.ilist['food'][25].techID: #this is a jellyfish
									message.add('You grill a jellyfish.')
									player.inventory.food[i] = deepcopy(il.ilist['food'][26])#turn a jellyfish into a grilled jellyfish
								elif player.inventory.food[i].techID == il.ilist['food'][0].techID: #this are red berries
									message.add('You make some red jelly.')
									player.inventory.food[i] = deepcopy(il.ilist['food'][29])#turn red berries into red jelly
								elif player.inventory.food[i].techID == il.ilist['food'][27].techID: #this are blue berries
									message.add('You make some blue jelly.')
									player.inventory.food[i] = deepcopy(il.ilist['food'][30])#turn blue berries into blue jelly
								elif player.inventory.food[i].techID == il.ilist['food'][28].techID: #this are red berries
									message.add('You make some yellow jelly.')
									player.inventory.food[i] = deepcopy(il.ilist['food'][31])#turn yellow berries into yellow jelly
								
								####add more here
								
						run = False
						
					else:
							
						message.add('You have not enough wood!')
						run = False
						
				elif ui == 'x':
					
					run = False
		
		elif world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].use_group == 'altar':
			 #this is a altar
			
			run = True
			
			while run:
				
				screen.render_request('[e] - pray', '[b] - identify ', '[x] - leave')
					
				ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
				
				if ui == 'e':
					
					judgement = gods.judgement() # see if the player is supported by the gods
					
					if judgement == True:
						
						cursed_items = 0
						bodyparts = ('Hold(R)', 'Hold(L)', 'Head', 'Body', 'Legs', 'Feet', 'Hand', 'Neck')
						
						for i in bodyparts:#check if player wears some cursed equipment
							
							if player.inventory.wearing[i].cursed < 1 and i != player.inventory.nothing:
								cursed_items += 1
						
						if (player.lp*100)/player.attribute.max_lp < 20:#player has less then 20% of lp -> heal
							player.lp = player.attribute.max_lp
							message.add('The gods heal your wounds.')
							gods.mood -= 10
							run = False
							
						elif (player.attribute.hunger*100)/player.attribute.hunger_max < 20 or (player.attribute.thirst*100)/player.attribute.thirst_max < 20 or (player.attribute.tiredness*100)/player.attribute.tiredness_max < 20:
							#player is very hungry,thirsty or tired -> refresh
							player.attribute.hunger = player.attribute.hunger_max
							player.attribute.thirst = player.attribute.thirst_max
							player.attribute.tiredness = player.attribute.tiredness_max
							message.add('The gods rerfresh you.')
							gods.mood -= 10
							run = False
							
						elif cursed_items > 0:#player has some cursed items
							
							bodyparts = ('Hold(R)', 'Hold(L)', 'Head', 'Body', 'Legs', 'Feet', 'Hand', 'Neck')
							
							for j in bodyparts:
								
								if player.inventory.wearing[j].cursed < 1 and player.inventory.wearing[j] != player.inventory.nothing:
									player.inventory.wearing[j].cursed = 1
									player.inventory.wearing[j].set_name()
							
							message.add('The gods remove curses from your equipment.')
							gods.mood -= 10
							run = False
						
						else:
							message.add('The gods are pleased about you.')
							run = False
							
					else: 
						
						uncursed_items = 0
						bodyparts = ('Hold(R)', 'Hold(L)', 'Head', 'Body', 'Legs', 'Feet', 'Hand', 'Neck')
						
						for i in bodyparts:#check if player wears some cursed equipment
							
							if player.inventory.wearing[i].cursed > 0 and player.inventory.wearing[i] != player.inventory.nothing:
								uncursed_items += 1
						
						if uncursed_items > 0:
							
							for j in bodyparts:
								
								if player.inventory.wearing[j].cursed > 0 and player.inventory.wearing[j] != player.inventory.nothing:
									player.inventory.wearing[j].cursed = 0
									player.inventory.wearing[j].set_name()
							
							message.add('The gods are angry and curse your equipment.')
							run = False
						else:
							
							player.lp -= 5
							message.add('The gods are angry and hurt you')
							run = False
				
				
				elif ui == 'b':
					
					bodyparts = ('Hold(R)', 'Hold(L)', 'Head', 'Body', 'Legs', 'Feet', 'Hand', 'Neck')
					
					for i in bodyparts:
						
						if player.inventory.wearing[i] != player.inventory.nothing:
							player.inventory.wearing[i].identification()
							
					for j in range (0, len(player.inventory.equipment)):
						
						if player.inventory.equipment[j] != player.inventory.nothing:
							player.inventory.equipment[j].identification()
							
					message.add('Now you are aware of your equipments states.')
					run = False
					
				elif ui == 'x':
					
					run = False
		
		elif world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].use_group == 'go_desert':
			pos = world.maplist[self.pos[2]]['desert_0_0'].find_first(tl.tlist['extra'][7])
			pos[1] += 1
			player.pos[0] = pos[0]
			player.pos[1] = pos[1]
			player.pos[2] = 0#only to be sure
			player.on_map = 'desert_0_0'
			player.stand_check()
		
		elif world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].use_group == 'return_desert':
			pos = world.maplist[self.pos[2]]['local_0_0'].find_first(tl.tlist['extra'][6])
			pos[1] -= 1
			player.pos[0] = pos[0]
			player.pos[1] = pos[1]
			player.pos[2] = 0#only to be sure
			player.on_map = 'local_0_0'
			player.stand_check()
								
		elif world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] != 0:#interaction with a container eg.: a chest
			
			world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]].inventory()
		
		elif world.maplist[self.pos[2]][self.on_map].tilemap[self.pos[1]][self.pos[0]].techID == tl.tlist['shop'][0].techID:#this is shop floor
			
			if world.maplist[self.pos[2]][self.on_map].map_type == 'grot':
				list_items = ('Scroll of Return(1 Gem)','Enchanted Enhancement Powder(5 Gem)','Copper Pickaxe(3 Gem)','Copper Axe(3 Gem)', 'Grilled Fish(1 Gem)', 'Torch(1 Gem)')
				prices = (1,5,3,3,1,1)
				axe = item_wear('axe',11,0)
				pickaxe = item_wear('pickaxe',11,0)
				items = (il.ilist['misc'][33],il.ilist['misc'][42],pickaxe,axe,il.ilist['food'][5],il.ilist['misc'][44])
			elif world.maplist[self.pos[2]][self.on_map].map_type == 'elfish_fortress':
				list_items = ('Scroll of Return(1 Gem)','Mysterious Blue Crystal(10 Gem)','Steel Pickaxe(5 Gem)','Steel Axe(5 Gem)', 'Red Berries(1 Gem)', 'Torch(1 Gem)')
				prices = (1,10,5,5,1,1)
				axe = item_wear('axe',15,0)
				pickaxe = item_wear('pickaxe',15,0)
				items = (il.ilist['misc'][33],il.ilist['misc'][41],pickaxe,axe,il.ilist['food'][0],il.ilist['misc'][44])
			elif world.maplist[self.pos[2]][self.on_map].map_type == 'orcish_mines':
				list_items = ('Scroll of Return(1 Gem)','Bomb(7 Gem)','Titan Pickaxe(7 Gem)','Titan Axe(7 Gem)', 'Grilled Meat(1 Gem)', 'Torch(1 Gem)')
				prices = (1,7,7,7,1,1)
				axe = item_wear('axe',18,0)
				pickaxe = item_wear('pickaxe',18,0)
				items = (il.ilist['misc'][33],il.ilist['misc'][24],pickaxe,axe,il.ilist['food'][10],il.ilist['misc'][44])
			else:#only for fallback
				list_items = ('Scroll of Return(1 Gem)','Heavy Bag(5 Gem)','Wooden Pickaxe(1 Gem)','Wooden Axe(1 Gem)', 'Grilled Fish(1 Gem)', 'Torch(1 Gem)')
				prices = (1,5,1,1,1,1)
				axe = item_wear('axe',0,0)
				pickaxe = item_wear('pickaxe',0,0)
				items = (il.ilist['misc'][33],il.ilist['misc'][43],pickaxe,axe,il.ilist['food'][5],il.ilist['misc'][44])
			headline = 'You have ' + str(player.inventory.materials.gem) + ' gems. What do you want to buy?'
			choice = screen.get_choice(headline,list_items,True)
			if choice != 'Break':
				if prices[choice] <= player.inventory.materials.gem:
					world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] = container([items[choice]])
					test = world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]].loot(0)
					world.maplist[self.pos[2]][self.on_map].containers[self.pos[1]][self.pos[0]] = 0#del the container to be sure
					if test == True:
						player.inventory.materials.gem -= prices[choice]
						message.add('The shopkeeper tanks you for your purchacing.')
					else:
						message.add('Your bags are to full to buy this item.')
				else:
					message.add('You havn\'t enough gems to buy this item.')
			else:
				message.add('Never Mind.')
			
		else:
			message.add('There is nothing to interact with at this place.')
			
class player_class(mob):
	
	def __init__(self, name, on_map, attribute, inventory, pos =[10,10,0], build='Manual'):
		
		lname = save_path + os.sep + 'player.data'
		
		try:
			
			mob.__init__(self, name, on_map, attribute, pos)
			
			f = file(lname, 'r')
			screen.render_load(7)
			temp = p.load(f)
			
			self.name = temp.name
			self.on_map = temp.on_map
			
			self.gender = temp.gender
			self.style = temp.style
			self.difficulty = temp.difficulty
			
			#attribute
			self.attribute.p_strange = temp.attribute.p_strange
			self.attribute.p_defense = temp.attribute.p_defense
			self.attribute.m_strange = temp.attribute.m_strange
			self.attribute.m_defense = temp.attribute.m_defense
			self.attribute.luck = temp.attribute.luck
			self.attribute.max_lp = temp.attribute.max_lp
			self.attribute.max_mp = temp.attribute.max_mp
			self.lp = temp.lp
			self.mp = temp.mp
			self.attribute.hunger_max = temp.attribute.hunger_max
			self.attribute.hunger = temp.attribute.hunger
			self.attribute.thirst_max = temp.attribute.thirst_max
			self.attribute.thirst = temp.attribute.thirst
			self.attribute.tiredness_max = temp.attribute.tiredness_max
			self.attribute.tiredness = temp.attribute.tiredness
			self.attribute.pickaxe_power = temp.attribute.pickaxe_power
			
			self.inventory = temp.inventory
			self.pos = temp.pos
			
			self.buffs = temp.buffs
			self.xp = temp.xp
			self.lvl = temp.lvl
			
		except:
			if build == 'Manual':
				accept = False
				while accept == False:
				
					num = 0
					gender_list = ('FEMALE','MALE') 
					run = True
			
					while run:
					
						s = pygame.Surface((640,360))
					
						s.blit(gra_files.gdic['display'][1],(0,0)) #render background
				
						text_image = screen.menu_font.render('Choose gender:',1,(255,255,255))
						s.blit(text_image,(5,2))#menue title
				
						s.blit(gra_files.gdic['display'][4],(0,115+num*25))#blit marker
				
						for i in range (0,2): 
							string = gender_list[i]
							text_image = screen.menu_font.render(string,1,(0,0,0))
							s.blit(text_image,(21,120+i*25))#blit item names
					
						text_image = screen.menu_font.render('[e] Choose',1,(255,255,255))
						s.blit(text_image,(5,335))
					
						if game_options.mousepad == 1:
							s.blit(gra_files.gdic['display'][8],(480,0)) #render mouse pad
						else:
							s_help = pygame.Surface((160,360))
							s_help.fill((48,48,48))
							s.blit(s_help,(480,0))
					
						if game_options.mousepad == 0:
							s_help = pygame.Surface((640,360))
							s_help.fill((48,48,48))
							s_help.blit(s,(80,0))
							s = s_help
					
						s = pygame.transform.scale(s,(screen.displayx,screen.displayy))
						screen.screen.blit(s,(0,0))
					
						pygame.display.flip()
					
						ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
				
						if ui == 's':
							num += 1
							if num > 1:
								num = 0
						
						if ui == 'w':
							num -= 1
							if num < 0:
								num = 1
						
						if ui == 'e':
							self.gender = gender_list[num]
							run = False
					
					run2 = True
					num2 = 0
				
					while run2:
						s = pygame.Surface((640,360))
					
						s.blit(gra_files.gdic['display'][1],(0,0)) #render background
				
						text_image = screen.menu_font.render('Choose style:',1,(255,255,255))
						s.blit(text_image,(5,2))#menue title
				
						s.blit(gra_files.gdic['display'][4],(0,115+num2*32))#blit marker
				
						for i in range (1,5): 
							skinstring = 'SKIN_' + self.gender + '_' + str(i)
							hairstring = 'HAIR_' + self.gender + '_' +  str(i)
							s.blit(gra_files.gdic['char'][skinstring],(26,115+(i-1)*32))
							s.blit(gra_files.gdic['char'][hairstring],(26,115+(i-1)*32))
					
						text_image = screen.menu_font.render('[e] Choose',1,(255,255,255))
						s.blit(text_image,(5,335))
					
						if game_options.mousepad == 1:
							s.blit(gra_files.gdic['display'][8],(480,0)) #render mouse pad
						else:
							s_help = pygame.Surface((160,360))
							s_help.fill((48,48,48))
							s.blit(s_help,(480,0))
					
						if game_options.mousepad == 0:
							s_help = pygame.Surface((640,360))
							s_help.fill((48,48,48))
							s_help.blit(s,(80,0))
							s = s_help
					
						s = pygame.transform.scale(s,(screen.displayx,screen.displayy))
						screen.screen.blit(s,(0,0))
					
						pygame.display.flip()
				
						ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
				
						if ui == 's':
							num2 += 1
							if num2 > 3:
								num2 = 0
						
						if ui == 'w':
							num2 -= 1
							if num2 < 0:
								num2 = 3
						
						if ui == 'e':
							self.style = num2
							run2 = False
					
			
					num3 = 0
					dificulty_list = ('EASY','NORMAL','HARD','ROGUELIKE','SANDBOX')
					description_list = ('Lose resources on death.','Lose inventory on death.','Lose inventory and level on death.','LOSE EVERYTHING', 'MONSTERS IGNORE YOU') 
					run3 = True
			
					while run3:
					
						s = pygame.Surface((640,360))
					
						s.blit(gra_files.gdic['display'][1],(0,0)) #render background
				
						text_image = screen.menu_font.render('Choose Game Mode:',1,(255,255,255))
						s.blit(text_image,(5,2))#menue title
				
						s.blit(gra_files.gdic['display'][4],(0,115+num3*25))#blit marker
				
						for i in range (0,5): 
							string = dificulty_list[i]
							text_image = screen.menu_font.render(string,1,(0,0,0))
							s.blit(text_image,(21,120+i*25))#blit item names
					
							text_image = screen.menu_font.render(description_list[num3],1,(255,255,255))
							s.blit(text_image,(5,335))
						
						if game_options.mousepad == 1:
							s.blit(gra_files.gdic['display'][8],(480,0)) #render mouse pad
						else:
							s_help = pygame.Surface((160,360))
							s_help.fill((48,48,48))
							s.blit(s_help,(480,0))
					
						if game_options.mousepad == 0:
							s_help = pygame.Surface((640,360))
							s_help.fill((48,48,48))
							s_help.blit(s,(80,0))
							s = s_help
					
						s = pygame.transform.scale(s,(screen.displayx,screen.displayy))
						screen.screen.blit(s,(0,0))
					
						pygame.display.flip()
					
						ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
				
						if ui == 's':
							num3 += 1
							if num3 > 4:
								num3 = 0
						
						if ui == 'w':
							num3 -= 1
							if num3 < 0:
								num3 = 4
						
						if ui == 'e':
							self.difficulty = num3
							run3 = False
					
					if low_res == False:
						name = screen.string_input('Whats your name?', 15)
					else:
						name = 'PLAYER'
					
					if name == '':
						name = 'Nameless' 
				
					num4 = 0
					choose_list = ('Yes','No') 
					run4 = True
			
					while run4:
					
						s = pygame.Surface((640,360))
				
						s.blit(gra_files.gdic['display'][1],(0,0)) #render background
				
						text_image = screen.menu_font.render('Is everything alright?',1,(255,255,255))
						s.blit(text_image,(5,2))#menue title
					
						skinstring = 'SKIN_' + self.gender + '_' + str(self.style +1)
						s.blit(gra_files.gdic['char'][skinstring],(160,80))
						
						hairstring = 'HAIR_' + self.gender + '_' + str(self.style +1)
						s.blit(gra_files.gdic['char'][hairstring],(160,80))
					
						n_string = 'NAME: ' + name
						name_image = screen.menu_font.render(n_string,1,(0,0,0))
						s.blit(name_image,(160,120))
					
						d_list = ('Easy', 'Normal', 'Hard', 'Rougelike', 'Sandbox')
					
						d_string = 'Difficulty: ' + d_list[self.difficulty]
						name_image = screen.menu_font.render(d_string,1,(0,0,0))
						s.blit(name_image,(160,140))
					
						s.blit(gra_files.gdic['display'][4],(155,160+num4*25))#blit marker
				
						for i in range (0,2): 
							string = choose_list[i]
							text_image = screen.menu_font.render(string,1,(0,0,0))
							s.blit(text_image,(176,165+i*25))#blit item names
					
						text_image = screen.menu_font.render('[e] Choose',1,(255,255,255))
						s.blit(text_image,(5,335))
					
						if game_options.mousepad == 1:
							s.blit(gra_files.gdic['display'][8],(480,0)) #render mouse pad
						else:
							s_help = pygame.Surface((160,360))
							s_help.fill((48,48,48))
							s.blit(s_help,(480,0))
					
						if game_options.mousepad == 0:
							s_help = pygame.Surface((640,360))
							s_help.fill((48,48,48))
							s_help.blit(s,(80,0))
							s = s_help
					
						s = pygame.transform.scale(s,(screen.displayx,screen.displayy))
						screen.screen.blit(s,(0,0))
					
						pygame.display.flip()
					
						ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
				
						if ui == 's':
							num4 += 1
							if num4 > 1:
								num4 = 0
						
						if ui == 'w':
							num4 -= 1
							if num4 < 0:
								num4 = 1
						
						if ui == 'e':
						
							if num4 == 0:
								accept = True
							
							run4 = False
						
				if self.difficulty == 4:
				
					for i in range (0,len(world.maplist)-1):
					
						for y in range(0,max_map_size):
							for x in range(0,max_map_size):
							
								if world.maplist[i]['local_0_0'].npcs[y][x] != 0:
									world.maplist[i]['local_0_0'].npcs[y][x].AI_style = 'ignore'
								try:	
									if world.maplist[i]['desert_0_0'].npcs[y][x] != 0:
										world.maplist[i]['desert_0_0'].npcs[y][x].AI_style = 'ignore'
								except:
									None
					
			###############
			mob.__init__(self, name, on_map, attribute, pos)
		
			self.inventory = inventory
			
			self.xp = 0
			self.lvl = 0
			
			self.buffs = buffs()
			
			try:
				self.pos[0] = world.startx
				self.pos[1] = world.starty
			except:
				self.pos[0] = 0
				self.pos[1] = 0
			
			screen.render_load(5)
		
	def user_input(self):
		
		ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
		
		if ui == 'w':
			if screen.fire_mode == 0:
				self.move(0,-1)
				time.tick()
			else:
				self.player_fire((0,-1))
				screen.fire_mode = 0
				time.tick()
			
		if ui == 's':
			if screen.fire_mode == 0:
				self.move(0,1)
				time.tick()
			else:
				self.player_fire((0,1))
				screen.fire_mode = 0
				time.tick()
			
		if ui == 'a':
			if screen.fire_mode == 0:
				self.move(-1,0)
				time.tick()
			else:
				self.player_fire((-1,0))
				screen.fire_mode = 0
				time.tick()
			
		if ui == 'd':
			if screen.fire_mode == 0:
				self.move(1,0)
				time.tick()
			else:
				self.player_fire((1,0))
				screen.fire_mode = 0
				time.tick()
			
		if ui == 'e':
			if screen.fire_mode == 0:
				self.enter()
				time.tick()
		
		if ui == 'i':
			if screen.fire_mode == 0:
				self.inventory.inv_user_interaction()
				time.tick()
			
		if ui == 'b':
			if screen.fire_mode == 0:
				if world.maplist[self.pos[2]][self.on_map].build_type != 'None':
					self.built()
					time.tick()
				else:
					message.add('You can\'t build here!')
		
		if ui == 'f':
			if screen.fire_mode == 0:
				if player.inventory.wearing['Hold(L)'] != player.inventory.nothing:
					screen.fire_mode = 1
					message.add('You channelise your magic powers.')
					time.tick()
				else:
					message.add('You need a magic weapon.')
			else:
				screen.fire_mode = 0
				time.tick()
			
		if ui == 'none':
			time.tick()
			player.stand_check()
			
		if ui == 'x':
			screen.render_brake()
			
	def lvl_up(self):
		
		self.lvl += 1
		self.xp -= 100
		
		choices = []
		
		st_string = 'Strange(' + str(self.attribute.p_strange) + ' -> ' + str(self.attribute.p_strange+3) +')'
		choices.append(st_string)
		
		sk_string = 'Skill(' + str(self.attribute.p_defense) + ' -> ' + str(self.attribute.p_defense+3) +')'
		choices.append(sk_string)
		
		po_string = 'Power(' + str(self.attribute.m_strange) + ' -> ' + str(self.attribute.m_strange+3) +')'
		choices.append(po_string)
		
		wi_string = 'Will(' + str(self.attribute.m_defense) + ' -> ' + str(self.attribute.m_defense+3) +')'
		choices.append(wi_string)
		
		if self.attribute.max_lp < 20:
			he_string = 'Health(' + str(self.attribute.max_lp) + ' -> ' + str(self.attribute.max_lp+1) +')'
			choices.append(he_string)
		
		c = screen.get_choice('~*Level up! Please choose an attribute.*~',choices,False)
		
		if c == 0:
			self.attribute.p_strange += 3
		elif c == 1:
			self.attribute.p_defense += 3
		elif c == 2:
			self.attribute.m_strange += 3
		elif c == 3:
			self.attribute.m_defense += 3
		else:
			self.attribute.max_lp += 1
		
	def built(self):
		
		style = 'wall'
		
		xymin = 0
		xymax = 5
		
		xmin = xymin
		xmax = xymin
		ymin = xymin
		ymax = xymin
		
		run = True
		
		while run:
			
			res_need = screen.render_built(xmin,xmax,ymin,ymax,style)
			
			ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
			
			if ui == 'w':
				
				if style != 'Door' and style != 'Stair up' and style != 'Stair down':
					ymin += 1
				
					if ymin >= xymax:
						ymin = xymin
				
				else:
					if ymin >= -3:
						ymin -= 1
					
			if ui == 's':
				
				if style != 'Door' and style != 'Stair up' and style != 'Stair down':
					ymax += 1
				
					if ymax >= xymax:
						ymax = xymin
					
				else:
					if ymin <= 3:
						ymin += 1
					
			if ui == 'a':
				if style != 'Door' and style != 'Stair up' and style != 'Stair down':
					xmin += 1
				
					if xmin >= xymax:
						xmin = xymin
						
				else:
					if xmin >= -3:
						xmin -= 1
					
			if ui == 'd':
				if style != 'Door' and style != 'Stair up' and style != 'Stair down':
					xmax += 1
				
					if xmax >= xymax:
						xmax = xymin
				
				else:
					if xmin <= 3:
						xmin += 1
					
			
			if ui == 'b':
				
				xmax = xymin
				xmin = xymin
				ymax = xymin
				ymin = xymin
				
				if style == 'wall':
					style = 'floor'
					
				elif style == 'floor':
					style = 'Door'
					
				elif style == 'Door':
					if world.maplist[self.pos[2]][self.on_map].build_type != 'Part':
						style = 'Stair up'
					else:
						style = 'Agriculture'
					
				elif style == 'Stair up':
					style = 'Stair down'
				
				elif style == 'Stair down':
					style = 'Agriculture'
					
				elif style == 'Agriculture':
					style = 'remove'	
					
				elif style == 'remove':
					style = 'wall'
			
			if ui == 'e':
				if style == 'wall':
					if res_need[0] <= player.inventory.materials.wood and res_need[1] <= player.inventory.materials.stone:
					
						player.inventory.materials.wood -= res_need[0]
						player.inventory.materials.stone -= res_need[1]
					
						for y in range (-ymin,ymax+1):
							for x in range (-xmin,xmax+1):
				
								if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].move_group == 'soil' and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].damage == False and world.maplist[player.pos[2]][player.on_map].npcs[player.pos[1]+y][player.pos[0]+x] == 0:
									built_here = True
								elif world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].civilisation == True:
									built_here = True
								else: 
									built_here = False
									
								if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].build_here == False:
									built_here = False
							
								if built_here == True:
									
									world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]+y][player.pos[0]+x] = 0 #first of all erase all items that are at this pos
									
									if x == xmax or x == -xmin or y == ymax or y == -ymin:
										if x == xmax or x == -xmin:
												world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x] = tl.tlist[player.inventory.blueprint.place_cat][player.inventory.blueprint.place_num+1] #set a wall here
					
										if y == ymax or y == -ymin:
												world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x] = tl.tlist[player.inventory.blueprint.place_cat][player.inventory.blueprint.place_num+1] #set a wall here
									else:
										None
					else: 
						message.add('Not enough Resources.')
				
				elif style == 'floor':
					if res_need[0] <= player.inventory.materials.wood and res_need[1] <= player.inventory.materials.stone:
					
						player.inventory.materials.wood -= res_need[0]
						player.inventory.materials.stone -= res_need[1]
					
						for y in range (-ymin,ymax+1):
							for x in range (-xmin,xmax+1):
				
								if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].move_group == 'soil' and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].damage == False and world.maplist[player.pos[2]][player.on_map].npcs[player.pos[1]+y][player.pos[0]+x] == 0:
									built_here = True
								elif world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].civilisation == True:
									built_here = True
								else: 
									built_here = False
								
								if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].build_here == False:
									built_here = False
								
								if built_here == True:
									
									world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]+y][player.pos[0]+x] = 0 #first of all erase all items that are at this pos
									if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].civilisation == True and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].replace != None:
										world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].replace = tl.tlist[player.inventory.blueprint.place_cat][player.inventory.blueprint.place_num]
									else:
										world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x] = tl.tlist[player.inventory.blueprint.place_cat][player.inventory.blueprint.place_num] #set floor here
					
					else: 
						message.add('Not enough Resources.')
				
				elif style == 'Door':
					
					if res_need[0] <= player.inventory.materials.wood and res_need[1] <= player.inventory.materials.stone:
					
						player.inventory.materials.wood -= res_need[0]
						player.inventory.materials.stone -= res_need[1]
						
						if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].move_group == 'soil' and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].damage == False and world.maplist[player.pos[2]][player.on_map].npcs[player.pos[1]+ymin][player.pos[0]+xmin] == 0:
							built_here = True
						elif world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].civilisation == True:
							built_here = True
						else: 
							built_here = False
								
						if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].build_here == False:
							built_here = False
								
						if built_here == True:
								
							world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]+ymin][player.pos[0]+xmin] = 0 #first of all erase all items that are at this pos
									
							world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin] = tl.tlist['building'][3] #set door here
				
				elif style == 'Stair up':
					
					if res_need[0] <= player.inventory.materials.wood and res_need[1] <= player.inventory.materials.stone:
						if player.pos[2] > 0:
					
							if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].replace == None and world.maplist[player.pos[2]-1][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0+xmin]].build_here == True and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].build_here == True and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].move_group == 'soil' and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].damage == False:
								build_here = 0
							else: 
								build_here = 1
							
							if build_here == 0:
								world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]+ymin][player.pos[0]+xmin] = 0 #first of all erase all items that are at this pos
								world.maplist[player.pos[2]-1][player.on_map].containers[player.pos[1]+ymin][player.pos[0]+xmin] = 0
								player.inventory.materials.wood -= res_need[0]
								player.inventory.materials.stone -= res_need[1]
								world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin] = tl.tlist['functional'][2]
								world.maplist[player.pos[2]-1][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin] = tl.tlist['functional'][1]
							else:
								message.add('Not here.')
					else:
						message.add('Not enough Resources.')
			
				elif style == 'Stair down':
					
					if res_need[0] <= player.inventory.materials.wood and res_need[1] <= player.inventory.materials.stone:
						if player.pos[2] < 15:
							
							if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].replace == None and world.maplist[player.pos[2]+1][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].build_here == True and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin].build_here == True and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]].move_group == 'soil' and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]].damage == False:
								build_here = 0
							else: 
								build_here = 1
							
							if build_here == 0:
								world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]+ymin][player.pos[0]+xmin] = 0 #first of all erase all items that are at this pos
								world.maplist[player.pos[2]+1][player.on_map].containers[player.pos[1]+xmin][player.pos[0]+ymin] = 0
								player.inventory.materials.wood -= res_need[0]
								player.inventory.materials.stone -= res_need[1]
								world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin] = tl.tlist['functional'][1]
								world.maplist[player.pos[2]+1][player.on_map].tilemap[player.pos[1]+ymin][player.pos[0]+xmin] = tl.tlist['functional'][2]
							else:
								message.add('Not here.')
					else:
						message.add('Not enough Resources')
				
				elif style == 'Agriculture':
					if res_need[0] <= player.inventory.materials.seeds:
					
						player.inventory.materials.seeds -= res_need[0]
					
						for y in range (-ymin,ymax+1):
							for x in range (-xmin,xmax+1):
				
								if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].move_group == 'soil' and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].damage == False and world.maplist[player.pos[2]][player.on_map].npcs[player.pos[1]+y][player.pos[0]+x] == 0:
									built_here = True
								elif world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].civilisation == True:
									built_here = True
								else: 
									built_here = False
								
								if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].build_here == False:
									built_here = False
								
								if built_here == True:
									
									world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]+y][player.pos[0]+x] = 0 #first of all erase all items that are at this pos
									
									world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x] = tl.tlist['building'][4] #set aggriculture here
					
					else: 
						message.add('Not enough Resources.')
					
				elif style == 'remove':
					
					for y in range (-ymin,ymax+1):
							for x in range (-xmin,xmax+1):
					
								if player.pos[2] == 0:
									if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].civilisation == True and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].build_here == True:
										world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]+y][player.pos[0]+x] = 0 #first of all erase all items that are at this pos
										world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x] = tl.tlist['local'][0] #set gras here
								elif player.pos[2] != 0 and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].build_here == True:
									if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x].civilisation == True:
										world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]+y][player.pos[0]+x] = 0 #first of all erase all items that are at this pos
										world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]+y][player.pos[0]+x] = tl.tlist['global_caves'][0] #set cave ground here	
				
				run = False
			
					
			if ui == 'x':
				
				run = False
		
	def monster_attacks(self,x,y):
		#This function is called when a monster attacks the player. The x and the y variable are to define the monsters pos 
		
		random_attack = None
		
		if world.maplist[self.pos[2]][self.on_map].npcs[y][x].behavior == 'attack_random':
			coin_random = random.randint(0,1)
			if coin_random == 0:
				random_attack = 'melee'
			else:
				random_attack = 'magic'
		
		if world.maplist[self.pos[2]][self.on_map].npcs[y][x].behavior == 'attack_melee' or random_attack == 'melee':
			
			bodypart = world.maplist[self.pos[2]][self.on_map].npcs[y][x].attack_were[random.randint(0,len(world.maplist[self.pos[2]][self.on_map].npcs[y][x].attack_were))-1]
			
			monster_strange  = 0
			for i in range(0,world.maplist[self.pos[2]][self.on_map].npcs[y][x].basic_attribute.p_strange):
				 monster_strange += random.randint(1,6)
				 
			player_defense = 0
			for j in range(0,self.attribute.p_defense + self.inventory.wearing[bodypart].attribute.p_defense):
				player_defense += random.randint(1,6)
			
			if monster_strange >= player_defense:
				attack_success = True
			else:
				attack_success = False
				
			if attack_success == False:#give the monster a chance to have luck and hit the player
				chance = random.randint(0,25)
				if chance < world.maplist[self.pos[2]][self.on_map].npcs[y][x].basic_attribute.luck:
					attack_success = True
					
			if attack_success == True:
				
				chance = random.randint(0,25)
				
				if chance < world.maplist[self.pos[2]][self.on_map].npcs[y][x].basic_attribute.luck:#monster hits critical
					message_string = 'A ' + world.maplist[self.pos[2]][self.on_map].npcs[y][x].name + ' hits your ' + bodypart.lower() + ' critical!'
					screen.write_hit_matrix(player.pos[0],player.pos[1],5)
					message.add(message_string)
					player.lp -= 4
					if self.inventory.wearing[bodypart] != self.inventory.nothing:
						self.inventory.wearing[bodypart].take_damage()#your amor at this bodypart take twice damage
						self.inventory.wearing[bodypart].take_damage()
						self.inventory.wearing[bodypart].set_name()
				else:
					message_string = 'A ' + world.maplist[self.pos[2]][self.on_map].npcs[y][x].name + ' hits your ' + bodypart.lower() + '!'
					message.add(message_string)
					screen.write_hit_matrix(player.pos[0],player.pos[1],4)
					player.lp -= 2
					if self.inventory.wearing[bodypart] != self.inventory.nothing:
						self.inventory.wearing[bodypart].take_damage()
						self.inventory.wearing[bodypart].set_name()
						
				if world.maplist[self.pos[2]][self.on_map].npcs[y][x].possible_effect != None:
					
					chance = random.randint(0,99)
					
					if world.maplist[self.pos[2]][self.on_map].npcs[y][x].effect_probability > chance:
						player.buffs.set_buff(world.maplist[self.pos[2]][self.on_map].npcs[y][x].possible_effect,world.maplist[self.pos[2]][self.on_map].npcs[y][x].effect_duration)
						message.add(world.maplist[self.pos[2]][self.on_map].npcs[y][x].message)
				
			else:
				
				message_string = 'A ' + world.maplist[self.pos[2]][self.on_map].npcs[y][x].name + ' miss you!'
				message.add(message_string)
				screen.write_hit_matrix(player.pos[0],player.pos[1],3)
		
		elif world.maplist[self.pos[2]][self.on_map].npcs[y][x].behavior == 'attack_magic' or random_attack == 'magic':
			
			monster_strange = 0
			for i in range(world.maplist[self.pos[2]][self.on_map].npcs[y][x].basic_attribute.m_strange):
				monster_strange += random.randint(1,6)
				
			player_defense = 0
			for j in range(0,player.attribute.p_defense + player.inventory.wearing['Neck'].attribute.m_defense + self.inventory.wearing['Hand'].attribute.m_defense):
				player_defense += random.randint(1,6)
			
			if monster_strange >= player_defense:
				attack_success = True
			else:
				attack_success = False
				
			if attack_success == False:#give the monster a chance to have luck and hit the player
				chance = random.randint(0,25)
				if chance < world.maplist[self.pos[2]][self.on_map].npcs[y][x].basic_attribute.luck:
					attack_success = True
					
			if attack_success == True:
				
				chance = random.randint(0,25)
				
				if chance < world.maplist[self.pos[2]][self.on_map].npcs[y][x].basic_attribute.luck:#monster hits critical
					message_string = 'A ' + world.maplist[self.pos[2]][self.on_map].npcs[y][x].name + '\'s magic attack hits you critical!'
					message.add(message_string)
					screen.write_hit_matrix(player.pos[0],player.pos[1],5)
					player.lp -= 4
					if self.inventory.wearing['Neck'] != self.inventory.nothing:
						self.inventory.wearing['Neck'].take_damage()#your amor at this bodypart take twice damage
						self.inventory.wearing['Neck'].take_damage()
						self.inventory.wearing['Neck'].set_name()
						
					if self.inventory.wearing['Hand'] != self.inventory.nothing:
						self.inventory.wearing['Hand'].take_damage()#your amor at this bodypart take twice damage
						self.inventory.wearing['Hand'].take_damage()
						self.inventory.wearing['Hand'].set_name()	
				else:
					message_string = 'A ' + world.maplist[self.pos[2]][self.on_map].npcs[y][x].name + '\'s magic attack hits you!'
					message.add(message_string)
					screen.write_hit_matrix(player.pos[0],player.pos[1],4)
					player.lp -= 2
					
					if self.inventory.wearing['Neck'] != self.inventory.nothing:
						self.inventory.wearing['Neck'].take_damage()
						self.inventory.wearing['Neck'].set_name()
						
					if self.inventory.wearing['Hand'] != self.inventory.nothing:
						self.inventory.wearing['Hand'].take_damage()
						self.inventory.wearing['Hand'].set_name()
				
				if world.maplist[self.pos[2]][self.on_map].npcs[y][x].possible_effect != None:
					
					chance = random.randint(0,99)
					
					if world.maplist[self.pos[2]][self.on_map].npcs[y][x].effect_probability > chance:
						player.buffs.set_buff(world.maplist[self.pos[2]][self.on_map].npcs[y][x].possible_effect,world.maplist[self.pos[2]][self.on_map].npcs[y][x].effect_duration)
						message.add(world.maplist[self.pos[2]][self.on_map].npcs[y][x].message)
					
			else:
				
				message_string = 'A ' + world.maplist[self.pos[2]][self.on_map].npcs[y][x].name + '\'s magic attack miss you!'
				message.add(message_string)
				screen.write_hit_matrix(player.pos[0],player.pos[1],3)
		
		if self.lp <= 0:
			screen.render_dead()
	
	def attack_monster(self,x,y,style='melee'):
		#This function is called when the player try to move at the same position like a monster. The x and the y variable definates the monsters pos. 
		
		if world.maplist[self.pos[2]][self.on_map].npcs[y][x].behavior == 'talk':
			message.add(world.maplist[self.pos[2]][self.on_map].npcs[y][x].message)
			return 'Done'
		
		if style == 'magic':
			
			player_strange = 0
			for i in range(0,self.attribute.m_strange + self.inventory.wearing['Hold(L)'].attribute.m_strange + self.lvl):
				player_strange += random.randint(1,6)
				
			monster_defense = 0
			for j in range(0,world.maplist[self.pos[2]][self.on_map].npcs[y][x].basic_attribute.m_defense):
				monster_defense += random.randint(1,6)
			
			player_luck = self.attribute.luck + self.inventory.wearing['Hand'].attribute.luck +self.inventory.wearing['Neck'].attribute.luck
			
			if player_strange >= monster_defense:
				attack_success = True
			else:
				attack_success = False
				
			if attack_success == False:#let the player have luck and hit the monster
				chance = random.randint(0,25)
				if chance < self.attribute.luck:
					attack_success = True
					
			if attack_success == True:
				
				chance = random.randint(0,25)
				
				if chance < player_luck:#player hits critical
					message_string = 'Your magic attack hits the ' + world.maplist[self.pos[2]][self.on_map].npcs[y][x].name + ' critical!'
					message.add(message_string)
					screen.write_hit_matrix(x,y,5)
					world.maplist[self.pos[2]][self.on_map].npcs[y][x].lp -= 2
					 
					if world.maplist[self.pos[2]][self.on_map].npcs[y][x].lp <= 0:
						
						xp = world.maplist[self.pos[2]][self.on_map].npcs[y][x].lvl - self.lvl + 1
						if xp < 0:
							xp = 0
						self.xp += xp
						
						if self.xp >= 100:
							self.lvl_up()
						
						test = False
						while test == False:
							test = world.maplist[self.pos[2]][self.on_map].monster_die(x,y)	
						
					if self.inventory.wearing['Hold(L)'] != self.inventory.nothing:
						self.inventory.wearing['Hold(L)'].take_damage() 
					 
				else:
					message_string = 'Your magic attack hits the ' + world.maplist[self.pos[2]][self.on_map].npcs[y][x].name + '!'
					message.add(message_string)
					screen.write_hit_matrix(x,y,4)
					world.maplist[self.pos[2]][self.on_map].npcs[y][x].lp -= 1
					
					if world.maplist[self.pos[2]][self.on_map].npcs[y][x].lp <= 0:
						
						xp = world.maplist[self.pos[2]][self.on_map].npcs[y][x].lvl - self.lvl +1
						if xp < 0:
							xp = 0
						self.xp += xp
						
						if self.xp >= 100:
							self.lvl_up()
						
						test = False
						while test == False:
							test = world.maplist[self.pos[2]][self.on_map].monster_die(x,y)
					
					if self.inventory.wearing['Hold(L)'] != self.inventory.nothing:
						self.inventory.wearing['Hold(L)'].take_damage()
			else:
				
				message_string = 'You miss the ' + world.maplist[self.pos[2]][self.on_map].npcs[y][x].name + '.'
				message.add(message_string)
				screen.write_hit_matrix(x,y,3)
		else:
			
			player_strange = 0
			for i in range(0,player.attribute.p_strange + player.inventory.wearing['Hold(R)'].attribute.p_strange):
				player_strange += random.randint(1,6)
				
			monster_defense = 0
			for i in range(0,world.maplist[self.pos[2]][self.on_map].npcs[y][x].basic_attribute.p_defense):
				monster_defense += random.randint(1,6)
			
			player_luck = self.attribute.luck + self.inventory.wearing['Hand'].attribute.luck +self.inventory.wearing['Neck'].attribute.luck
				
			if player_strange >= monster_defense:
				attack_success = True
			else:
				attack_success = False
				
			if attack_success == False:#let the player have luck and hit the monster
				chance = random.randint(0,25)
				if chance < player_luck:
					attack_success = True
			
			if attack_success == True:
				
				chance = random.randint(0,25)
				
				if chance < player_luck:#player hits critical
					message_string = 'You hit the ' + world.maplist[self.pos[2]][self.on_map].npcs[y][x].name + ' critical!'
					message.add(message_string)
					screen.write_hit_matrix(x,y,5)
					world.maplist[self.pos[2]][self.on_map].npcs[y][x].lp -= 2
					 
					if world.maplist[self.pos[2]][self.on_map].npcs[y][x].lp <= 0:
						
						xp = world.maplist[self.pos[2]][self.on_map].npcs[y][x].lvl - self.lvl +1
						
						if xp < 0:
							xp = 0
						self.xp += xp
						
						if self.xp >= 100:
							self.lvl_up()
						
						test = False
						while test == False:
							test = world.maplist[self.pos[2]][self.on_map].monster_die(x,y)	
					 
					if self.inventory.wearing['Hold(R)'] != self.inventory.nothing:
						self.inventory.wearing['Hold(R)'].take_damage() 
					 
				else:
					message_string = 'You hit the ' + world.maplist[self.pos[2]][self.on_map].npcs[y][x].name + '!'
					message.add(message_string)
					screen.write_hit_matrix(x,y,4)
					world.maplist[self.pos[2]][self.on_map].npcs[y][x].lp -= 1
					
					if world.maplist[self.pos[2]][self.on_map].npcs[y][x].lp <= 0:
						
						xp = world.maplist[self.pos[2]][self.on_map].npcs[y][x].lvl - self.lvl + 1
						
						if xp < 0:
							xp = 0
						self.xp += xp
						
						if self.xp >= 100:
							self.lvl_up()
						
						test = False
						while test == False:
							test = world.maplist[self.pos[2]][self.on_map].monster_die(x,y)	
					
					if self.inventory.wearing['Hold(R)'] != self.inventory.nothing:
						self.inventory.wearing['Hold(R)'].take_damage()
			
			else:
				
				message_string = 'You miss the ' + world.maplist[self.pos[2]][self.on_map].npcs[y][x].name + '.'
				message.add(message_string)
				screen.write_hit_matrix(x,y,3)
	
	def player_fire(self,direction):
		
		#direction must be a tulpel like (0,1) [style: (x,y)]
		x=player.pos[0]
		y=player.pos[1]
		c = 1
		run = True
		
		while run:
			
			xx = player.pos[0] + (direction[0]*c)
			yy = player.pos[1] + (direction[1]*c)
			c += 1
			
			if world.maplist[self.pos[2]][self.on_map].npcs[yy][xx] == 0:
				screen.write_hit_matrix(xx,yy,1)
			elif world.maplist[self.pos[2]][self.on_map].npcs[yy][xx] != 0:#there is a monster here
				player.attack_monster(xx,yy,'magic')
				run = False
			
			if c > 4 or world.maplist[self.pos[2]][self.on_map].tilemap[yy][xx].transparency == False:
				run = False
				
				
	def respawn(self):
		
		self.pos[2] = 0
		self.pos[0] = world.startx
		self.pos[1] = world.starty
		self.on_map = 'local_0_0'
		
		self.xp = 0 #the player always lose all xp on dead
		self.lp = self.attribute.max_lp
		self.attribute.hunger = self.attribute.hunger_max
		self.attribute.thirst = self.attribute.thirst_max
		self.attribute.tiredness = self.attribute.tiredness_max
		
		if self.difficulty == 0:#the player plays on easy
			self.inventory.materials = materials()#reset materials
			if self.inventory.wearing['Hold(R)'].cursed == 0:
				self.inventory.wearing['Hold(R)'] = self.inventory.nothing
		elif self.difficulty == 1:#the player plays on normal
			self.inventory = inventory(5)#reset inventory
		elif self.difficulty == 2:#the player plays on hard
			self.inventory = inventory(5)#reset inventory
			self.lvl = 0#reset lvl
			self.attribute = attribute(2,2,2,2,2,10,10)#reset attribute
		elif self. difficulty == 3:#the player plays on Roguelike
			#del everything
			
			try:
				player_path = save_path + 'player.data'
				os.remove(player_path)
			except:
				None
									
			try:
				world_path = save_path + 'world.data'
				os.remove(world_path)
			except:
				None	
									
			try:
				gods_path = save_path + 'gods.data'
				os.remove(gods_path)
			except:
				None
									
			try:
				time_path = save_path + 'time.data'
				os.remove(time_path)
			except:
				None
		
		self.stand_check()
		
			
class messager():
	
	def __init__(self):
		self.mes_list = []
		self.last_mes = 'foo'
		self.mes_history = [[]]
		self.history_page = 0
		self.last_output = ('...','~*~')
		
	def add(self, new_message, check_if_new = False):
		# check_if_new is only needed by the (mob)player.stand_check function to proove there is only shown a new message about the ground when the player enters a new kind of ground
		if check_if_new == False:
			self.mes_list.append(new_message)
			self.mes_history[self.history_page].append(new_message)
			
			if len(self.mes_history[self.history_page]) == 7:
				self.mes_history.append([])
				if len(self.mes_history) > 10:
					del self.mes_history[0]
				else:
					self.history_page +=1
			
		elif check_if_new == True and self.last_mes != new_message:
			self.last_mes = new_message
			self.mes_list.append(new_message)
			
			self.mes_history[self.history_page].append(new_message)
			
			if len(self.mes_history[self.history_page]) == 7:
				self.mes_history.append([])
				if len(self.mes_history) > 10:
					del self.mes_history[0]
				else:
					self.history_page +=1
			
	def clear(self):
		
		del self.mes_list
		self.mes_list = []
		
	def render_history(self):
		
		page = self.history_page
		run = True
		
		while run:
			
			s = pygame.Surface((640,360))
			
			s.blit(gra_files.gdic['display'][1],(0,0)) #render background
			
			text_string = '~*~ Message History ~*~            Page(' + str(page+1) + ' of ' + str(len(self.mes_history)) +')'
			text_image = screen.menu_font.render(text_string,1,(255,255,255))
			s.blit(text_image,(5,2))#menue title
			
			for i in range (0, len(self.mes_history[page])):
				mes_image = screen.menu_font.render(self.mes_history[page][i],1,(0,0,0))
				s.blit(mes_image,(5,100+25*i))#messages
				
			text_image = screen.menu_font.render('[w,a] - Page up [s,d] - Page down [x] - leave',1,(255,255,255))
			s.blit(text_image,(5,335))
			
			if game_options.mousepad == 1:	
				s.blit(gra_files.gdic['display'][8],(480,0)) #render mouse pad
			else:
				s_help = pygame.Surface((160,360))
				s_help.fill((48,48,48))
				s.blit(s_help,(480,0))
			
			if game_options.mousepad == 0:
				s_help = pygame.Surface((640,360))
				s_help.fill((48,48,48))
				s_help.blit(s,(80,0))
				s = s_help
			
			s = pygame.transform.scale(s,(screen.displayx,screen.displayy))
			screen.screen.blit(s,(0,0))
			
			pygame.display.flip()
			
			ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
			
			if ui == 'w' or ui == 'a':
				page -= 1
				if page < 0:
					page = len(self.mes_history)-1
					
			if ui == 's' or ui == 'd':
				page += 1
				if page > len(self.mes_history)-1:
					page = 0
					
			if ui == 'x':
				run = False
			
	def sget(self,num):
		
		if num < len((self.mes_list))-1:
			s_list = (self.mes_list[num],self.mes_list[num+1])
		elif num < len((self.mes_list)):
			s_list = (self.mes_list[num],'~*~')
			self.last_output = s_list
		else:
			s_list = self.last_output
		
		return s_list
		
class inventory():
	
	def __init__(self, equipment=7, food=7, misc=7):
		
		self.nothing = item_wear('Nothing',21,0,0)
		self.wearing = {'Head' : self.nothing, 'Body' : self.nothing, 'Legs' : self.nothing, 'Feet' : self.nothing, 'Hand' : self.nothing, 'Neck' : self.nothing, 'Hold(R)' : self.nothing, 'Hold(L)' : self.nothing}
		self.item_change = self.nothing
		self.equipment = []
		self.food = []
		self.misc = []
		self.materials = materials()
		self.blueprint = il.ilist['misc'][15]#a ordenary blueprint
		self.inv_mes = '~*~'
		
		for i in range (0,equipment):
			self.equipment.append(self.nothing)
		for i in range (0,food):
			self.food.append(self.nothing)
		for i in range (0,misc):
			self.misc.append(self.nothing)
			
		#go on here
	
	def wear(self, slot):
		
		if self.equipment[slot] != self.nothing:
		
			self.inv_mes = 'Now you wear a  %s.' %(self.equipment[slot].name)
		
			if self.wearing[self.equipment[slot].worn_at] != self.nothing and self.wearing[self.equipment[slot].worn_at].cursed != 0:
				self.item_change = self.wearing[self.equipment[slot].worn_at]
				self.wearing[self.equipment[slot].worn_at] = self.equipment[slot]
				self.equipment[slot] = self.item_change
				self.item_change = self.nothing
			elif self.wearing[self.equipment[slot].worn_at].cursed == 0:
				self.inv_mes = 'You can\'t! It\'s cursed!'
				self.wearing[self.equipment[slot].worn_at].identification()
			else:
				self.wearing[self.equipment[slot].worn_at] = self.equipment[slot]
				self.equipment[slot] = self.nothing
		
	def unwear(self, slot):
		
		worn = list(self.wearing.keys())
		
		if self.wearing[worn[slot]].cursed != 0: #this is no cursed item
		
			num = -1
			found = -1
		
			for i in self.equipment:
			
				if found != -1:
					break
				
				num += 1
				if i == self.nothing:
					found = num
				
			if found > -1:
				self.equipment[num] = self.wearing[worn[slot]]
				self.inv_mes = 'You unwear a %s.' %( self.wearing[worn[slot]].name)
				self.wearing[worn[slot]] = self.nothing
			else:
				self.inv_mes = 'You have no free space in your inventory!'
		else: #this item is cursed
			
			self.inv_mes = 'You can\'t! It\'s cursed!'
			self.wearing[worn[slot]].identification()
			
	def drop(self,category, slot):
		
		worn = list(self.wearing.keys())
		try:
			field_full = False
			sacrifice = False
			
			string = 'foo'
			
			if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]].replace != None and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]].techID != tl.tlist['functional'][3].techID and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]].techID != tl.tlist['functional'][4].techID and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]].techID != tl.tlist['functional'][5].techID: #only at fields with empty ground the player can drop something. exeptions are full chests, empty chests and stacks. 
				field_full = True
				string = 'Not here!'
				
			if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]].techID == tl.tlist['functional'][3].techID or world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]].techID == tl.tlist['functional'][4].techID or world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]].techID == tl.tlist['functional'][5].techID:
				if 	world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]] != 0: #there are allready things here
					if len(world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]].items) > 6:
						field_full = True
						string = 'There are already too many items at this place!'
			
			if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]].techID == tl.tlist['functional'][15].techID:#this is a altar 
				field_full = False
				sacrifice = True
				
			if string != 'foo':
				self.inv_mes = string
			
		except: 
			field_full = False
			
		if category != 0 or self.wearing[worn[slot]].cursed != 0:#there is no worn cursed item you wanna drop
			if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]].damage == 0 and field_full == False: #you only can drop thing on save tiles with 7 or less other items on it
			
				if world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]] == 0: #if there is no container
					world.maplist[player.pos[2]][player.on_map].add_container([self.nothing],player.pos[0],player.pos[1]) #make new container
				
					if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]].techID != tl.tlist['functional'][3].techID and sacrifice == False: #if there is no empty chest at this pos and this is no sacrifice make a stack
						help_tile = deepcopy(world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]]) #get old tile at player pos
						world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]] = deepcopy(tl.tlist['functional'][5]) #set new tile on player pos
						world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]].replace = help_tile #set replace tile at the new position to the old tile at this pos
					elif world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]].techID == tl.tlist['functional'][3].techID:
						replace = deepcopy(world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]].replace)
						world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]] = deepcopy(tl.tlist['functional'][4])#else make a full chest out of the empty one
						world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]].replace = replace
					
				if category == 0:
					world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]].items.append(self.wearing[worn[slot]])
					if self.wearing[worn[slot]] != self.nothing: #this slot isn't empty
						self.inv_mes = 'You drop a %s.' %(self.wearing[worn[slot]].name)
					self.wearing[worn[slot]] = self.nothing
				elif category == 1:
					world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]].items.append(self.equipment[slot])
					if self.equipment[slot] != self.nothing:
						self.inv_mes = 'You drop a %s.' %(self.equipment[slot].name)
					self.equipment[slot] = self.nothing
				elif category == 2:
					world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]].items.append(self.food[slot])
					if self.food[slot] != self.nothing:
						self.inv_mes = 'You drop a %s.' %(self.food[slot].name)
					self.food[slot] = self.nothing
				elif category == 3:
					world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]].items.append(self.misc[slot])
					if self.misc[slot] != self.nothing:
						self.inv_mes = 'You drop a %s.' %(self.misc[slot].name)
					self.misc[slot] = self.nothing
				
				for i in range (0, len(world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]].items)): #check for empty slots and errase them if nessecary ---------- unsure because the -1
					try:#try-except is needed because the length of the list can change
						if world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]].items[i] == self.nothing:
							del world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]].items[i]
					except:
						None
						
				if sacrifice == True:
					
					for j in range (0, len(world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]].items)):
						
						equipment = False
						food = False
						mood_change = 0
						
						try:
							# if this is working this must be a equipment item
							if world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]].items[j].state > 40:#this is equipment in a good state
								equipment = True
								if world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]].items[j].material == 'wooden':
									mood_change += 1
								elif world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]].items[j].material == 'tin':
									mood_change += 2
								elif world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]].items[j].material == 'copper':
									mood_change += 4
								elif world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]].items[j].material == 'steel':
									mood_change += 6
								elif world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]].items[j].material == 'titan':
									mood_change += 8
								elif world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]].items[j].material == 'magnicum':
									mood_change += 10
						except:
							# if this is working this must be a food item
							if world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]].items[j].rotten == False: #this is unrotten food
								food = True
								mood_change += 2
								
								
						finally:
							 
							if equipment == False and food == False:
								mood_change = -1*(random.randint(1,10))
							
							if mood_change == 0:
								self.inv_mes = 'The gods accept your sacrifice.'
							elif mood_change > 0:
								self.inv_mes = 'The goods seem to be pleased...'
							else:
								self. inv_mes = 'It seems the gods dislike your gift...'
									 
							gods.mood += mood_change
							
							world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]] = 0 # del all sacrificed items 
								 
		else:#you try to drop a worn, cursed item
			
			self.inv_mes = 'You can\'t! It\'s cursed!'
			self.wearing[worn[slot]].identification()
		
	def use(self,slot):
		
		if self.misc[slot] != self.nothing:
			
			if self.misc[slot].use_name == 'place' or self.misc[slot].use_name == 'plant':
				
				if self.misc[slot].use_name == 'plant':
					grown_check = world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]].can_grown
				else:
					grown_check = True
				
				if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]].replace == None and world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]].damage == 0 and grown_check == True:
				
					replace = deepcopy(world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]])
					world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]] = deepcopy(tl.tlist[self.misc[slot].place_cat][self.misc[slot].place_num])
					world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]].replace = replace
					if self.misc[slot].use_name == 'plant':
						message.add('You planted a %s' %(self.misc[slot].name))
					else:
						message.add('You placed a %s' %(self.misc[slot].name))
					if self.misc[slot].name == 'Bomb':
						world.maplist[player.pos[2]][player.on_map].countdowns.append(countdown('bomb3',player.pos[0],player.pos[1],1))
					self.misc[slot] = self.nothing
					return True #if use returns a true this means after this action the inventory is closed. this action needs a turn
				else:
				
					self.inv_mes = 'Not here!'
					return False #this dosn't need a turn
			
			elif self.misc[slot].use_name == 'apply':#this is a blueprint. only blueprints are allowed to use 'apply'
				helpslot = player.inventory.blueprint
				player.inventory.blueprint = self.misc[slot]
				self.misc[slot] = helpslot
			
			elif self.misc[slot].name == 'Heart-Shaped Crystal':
				if player.attribute.max_lp < 20:
					if player.lp < player.attribute.max_lp:
						message.add('All your wounds are healed.')
					player.attribute.max_lp += 2
					player.lp = player.attribute.max_lp
					message.add('You feel more healthy now.')
				else:
					message.add('Nothing happens.')
				self.misc[slot] = self.nothing
				return True
			
			elif self.misc[slot].name == 'Mysterious Blue Crystal':
				if player.attribute.max_mp > 5:
					message.add('Your magic talents seem to grow.')
					player.attribute.max_lp -= 2
					if player.mp > player.attribute.max_mp:
						player.mp == player.attribute.max_mp
				else:
					message.add('Nothing happens.')
				self.misc[slot] = self.nothing
				return True
			
			elif self.misc[slot].name == 'Anchanted Enhancemen Powder':
				if self.wearing['Hold(R)'] != self.nothing:
					if self.wearing['Hold(R)'].plus < 2:
						mes = 'Your ' + self.wearing['Hold(R)'].name + ' glowes blue.'
						message.add(mes)
						self.wearing['Hold(R)'].plus += 1
						self.wearing['Hold(R)'].set_name()
						self.misc[slot] = self.nothing
					else:
						message.add('Nothing happens.')
					return True						
				else:
					self.inv_mes = 'You need to hold something inside your hand to use this.'
			
			elif self.misc[slot].name == 'Heavy Bag':
				message.add('You open the bag.')
				if self.materials.wood < self.materials.wood_max:
					wood_num = random.randint(1,9)
				if self.materials.stone < self.materials.stone_max:
					stone_num = random.randint(1,9)
				if self.materials.ore < self.materials.ore_max:
					ore_num = random.randint(-3,3)
					if ore_num < 0:
						ore_num = 0
				if self.materials.gem < self.materials.gem_max:
					gem_num = random.randint(-6,2)
					if gem_num < 0:
						gem_num = 0
				
				string = 'It contains: ' + str(wood_num) + ' wood, ' +str(stone_num) + ' stone'
				
				if ore_num > 0:
					string = string + ', ' + str(ore_num) + ' ore'
				if gem_num > 0:
					string = string + ', ' + str(gem_num) + ' gem'
					
				wood_num = self.materials.add('wood', wood_num)
				stone_num = self.materials.add('stone', stone_num)
				ore_num = self.materials.add('ore', ore_num)
				gem_num = self.materials.add('gem', gem_num)
				
				string = ''
				
				if wood_num != 'Full!':
					string = string + str(wood_num)
				if stone_num != 'Full!':	 
					string = string + ',' + str(stone_num)
				if ore_num != 'Full!':
					string = string + ',' + str(ore_num)
				if gem_num != 'Full!':
					string = string + ',' + str(gem_num)
					
				if wood_num+stone_num+ore_num+gem_num == 0:
					string = 'Your bags are to full to keep anything out of the bag.'
					
				message.add(string)
				
				return True
			
			elif self.misc[slot].use_name == 'read':#this is a scroll or a spellbook
				
				if self.misc[slot].name.count('Scroll') > 0:
					scroll = True
				else:
					scroll = False
					
				if player.mp < player.attribute.max_mp and scroll == False:
					self.inv_mes = 'You are not focused.'
					return False #this dosnt need a turn
					
				if self.misc[slot].effect == 0: #identify
					
					bodyparts = ('Head','Body','Legs','Feet','Hand','Neck','Hold(R)', 'Hold(L)')
					
					for i in bodyparts:
						if self.wearing[i] != self.nothing:
							self.wearing[i].identification()
							
					for j in range(0,len(self.equipment)):
						if self.equipment[j] != self.nothing:
							self.equipment[j].identification()
						
					message.add('Now you aware about your equipment\'s states.')
						
				elif self.misc[slot].effect == 1: #repair
					
					bodyparts = ('Head','Body','Legs','Feet','Hand','Neck','Hold(R)','Hold(L)')
					final_bodyparts = []
					
					for i in bodyparts:
						
						if self.wearing[i] != self.nothing and self.wearing[i].state != 0:
							final_bodyparts.append(i)
							
					if len(final_bodyparts) != 0:	
						ran = random.randint(0, len(final_bodyparts)-1)
						self.wearing[final_bodyparts[ran]].state = 100
						self.wearing[final_bodyparts[ran]].set_name()
						mes = 'Your ' + self.wearing[final_bodyparts[ran]].classe + ' is fully repaired now.'
						message.add(mes)
					else:
						message.add('Nothing seems to happen.')
						
				elif self.misc[slot].effect == 2: #healing
					
					if player.lp < player.attribute.max_lp:
						player.lp = player.attribute.max_lp
						message.add('Your wounds heal immediatly.')
					else:
						message.add('Nothing seems to happen.')
						
				elif self.misc[slot].effect == 3: #teleport
					
					pos_list = world.maplist[player.pos[2]][player.on_map].find_all_moveable(False)
					
					if len(pos_list) > 1:
						ran = random.randint(0,len(pos_list)-1)
						pos = pos_list[ran]
						player.pos[0] = pos[0]
						player.pos[1] = pos[1]
						player.stand_check()
						message.add('You teleport your self.')
					else:
						message.add('Nothing seems to happen')
					
						
				elif self.misc[slot].effect == 4:#return
					
					if player.pos[0] != world.startx or player.pos[1] != world.starty or player.pos[2] != 0:
						player.pos[0] = world.startx
						player.pos[1] = world.starty
						player.pos[2] = 0
						message.add('You returne home.')
					else:
						message.add('Nothing seems to happen.')

				elif self.misc[slot].effect == 5: #flames
					
					num_flames = 0
					
					for y in range(player.pos[1]-1,player.pos[1]+2):
						for x in range(player.pos[0]-1,player.pos[0]+2):
							
							if x != player.pos[0] or y !=player.pos[1]:
								if world.maplist[player.pos[2]][player.on_map].tilemap[y][x].replace == None and world.maplist[player.pos[2]][player.on_map].tilemap[y][x].move:
									replace = world.maplist[player.pos[2]][player.on_map].tilemap[y][x]
									world.maplist[player.pos[2]][player.on_map].tilemap[y][x] = deepcopy(tl.tlist['effect'][4])
									world.maplist[player.pos[2]][player.on_map].tilemap[y][x].replace = replace
									world.maplist[player.pos[2]][player.on_map].countdowns.append(countdown('flame',x,y,2))
									num_flames+=1
									if world.maplist[player.pos[2]][player.on_map].npcs[y][x] != 0 and world.maplist[player.pos[2]][player.on_map].npcs[y][x].ignore_damage == False:
										world.maplist[player.pos[2]][player.on_map].npcs[y][x] = 0
										world.maplist[player.pos[2]][player.on_map].make_monsters_angry(x,y)
								
					if num_flames != 0:
						message.add('Magical flames start to burn close to you.')
					else:
						message.add('Nothing seems to happen.')
				
				elif self.misc[slot].effect == 6:
					
					num_aura = 0
					
					for y in range(player.pos[1]-1,player.pos[1]+2):
						for x in range(player.pos[0]-1,player.pos[0]+2):
							
							if world.maplist[player.pos[2]][player.on_map].tilemap[y][x].replace == None and world.maplist[player.pos[2]][player.on_map].tilemap[y][x].move and world.maplist[player.pos[2]][player.on_map].tilemap[y][x].damage == False:
								replace = world.maplist[player.pos[2]][player.on_map].tilemap[y][x]
								world.maplist[player.pos[2]][player.on_map].tilemap[y][x] = deepcopy(tl.tlist['effect'][5])
								world.maplist[player.pos[2]][player.on_map].tilemap[y][x].replace = replace
								world.maplist[player.pos[2]][player.on_map].countdowns.append(countdown('healing_aura',x,y,10))
								num_aura+=1
								
					if num_aura != 0:
						message.add('A healing aura spreades under your feet.')
					else:
						message.add('Nothing seems to happen.')
				
				elif self.misc[slot].effect == 7:
					player.buffs.set_buff('light',180)
					message.add('A magical light surrounds your body.')
				
				if scroll == True:
					self.misc[slot] = self.nothing
					message.add('The scroll turns to dust.')
				else:
					player.mp = 0
					message.add('You lose your focus.')
				
				return True
				
			elif self.misc[slot].name == 'Fishing rod':
				
				chance = 0 
				
				for y in range (player.pos[1]-1, player.pos[1]+1):
					for x in range (player.pos[0]-1, player.pos[0]+1):
						
						if world.maplist[player.pos[2]][player.on_map].tilemap[y][x].techID == tl.tlist['misc'][0].techID: #this is low water
							chance += 1
						elif world.maplist[player.pos[2]][player.on_map].tilemap[y][x].techID == tl.tlist['misc'][3].techID: #this is water
							chance += 2
						
				if chance == 0:
					self.inv_mes ='Not here!'
					return False
					
				got_fish = random.randint(0,20)
				
				if chance > got_fish:
					status_quo = world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]] #save the container at this ülace
					coin = random.randint(0,99)
					
					if coin < 75:
						
						items = (il.ilist['food'][4],il.ilist['food'][25])#catch a fish or a jellyfish
						
						choose = random.randint(0,len(items)-1)
						
						world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]] = container([items[choose]])#set a temporary container
						test = world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]].loot(0)
						
						if test == True:
							message.add('You got a ' + items[choose].name + '.')
						else:
							message.add('You got a ' + items[choose].name + ', but you can\'t keep it.')
							
					else:
						#catch old shoes
						material = random.randint(6,20) #no wooden shoes. they would swim ;-)
						curse = random.randint(0,2)
						plus = random.randint(-2,2)
						state = random.randint(4,11)
						
						item = item_wear('shoes',material,plus,state,curse)
						
						world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]] = container([item])
						test = world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]].loot(0)
							
						if test == True:
							message.add('You got some old ' + item.name + '.')
						else:
							message.add('You got some old ' + item.name + ', but you can\'t keep it.')
							
					world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]] = status_quo #recover the old container 
				
				else:
					
					message.add('It seems nothing want to bite...')
				
				return True
			
			elif self.misc[slot].name == 'Torch':
				
				player.buffs.set_buff('light',180)
				self.misc[slot] = self.nothing
				message.add('The burning torch illumines your surroundings.')
				return True
							
	def eat(self,slot):
		
		if self.food[slot] != self.nothing:
			
			player.attribute.hunger += self.food[slot].satisfy_hunger
			if player.attribute.hunger > player.attribute.hunger_max:
				player.attribute.hunger = player.attribute.hunger_max+1 #the +1 is because the attribute will fall one point at the same turn
			
			player.attribute.thirst += self.food[slot].satisfy_thirst
			if player.attribute.thirst > player.attribute.thirst_max:
				player.attribute.thirst = player.attribute.thirst_max+1 #the +1 is because the attribute will fall one point at the same turn
			
			
			player.buffs.set_buff('adrenalised',self.food[slot].satisfy_tiredness)
			
			player.lp += self.food[slot].heal
			if player.lp > player.attribute.max_lp:
				player.lp = player.attribute.max_lp
			
			player.attribute.hunger_max += self.food[slot].rise_hunger_max
			player.attribute.thirst_max += self.food[slot].rise_thirst_max	
			player.attribute.tiredness_max += self.food[slot].rise_tiredness_max
			player.attribute.max_lp += self.food[slot].rise_lp_max
			
			player.inventory.materials.add('seeds', self.food[slot].give_seed)
			
			if self.food[slot].rotten == False:
				self.inv_mes = self.food[slot].eat_mes
			else:
				blind_coin = random.randint(0,1)
				if blind_coin == 1:
					blind_dur = random.randint(60,180)
					player.buffs.set_buff('blind',blind_dur)
					
				poison_coin = random.randint(0,1)
				if poison_coin == 1:
					posion_dur = random.randint(60,240)
					player.buffs.set_buff('poisoned',posion_dur)
					
				self.inv_mes = 'BAH! Rotten food...'
			
			self.food[slot] = self.nothing
			
	def render(self, category, slot):
		
		s = pygame.Surface((640,360))
		
		s.blit(gra_files.gdic['display'][1],(0,0)) #render background

		num = 0
		
		text_image = screen.menu_font.render('~*~ Inventory ~*~        [Press [x] to leave]',1,(255,255,255))
		s.blit(text_image,(5,2))#menue title
		
		for c in range(0,6):
			s.blit(gra_files.gdic['display'][2],(c*50,25))#blit empty tabs
			
		s.blit(gra_files.gdic['display'][3],(category*50,25))#blit used tab
		
		tab_names = ('Body','Equi.','Food','Misc', 'Reso.')
		
		for d in range (0,5):
			
			text_image = screen.font.render(tab_names[d],1,(0,0,0))
			s.blit(text_image,(d*50+5,27))#blit tb names
			
		if category == 0:
			h = list(self.wearing.keys())
			
			s.blit(gra_files.gdic['display'][4],(0,115+slot*25))#blit marker
			 
			for i in h:
				
				if slot == num and self.wearing[h[slot]] != self.nothing:
					string = i + ' : ' + self.wearing[i].name + '>([e]unwear, [b]drop)'
					text_image = screen.menu_font.render(string,1,(0,0,0))
					s.blit(text_image,(21,120+num*25))#blit item names
				
				else:
					
					string = i + ' : ' + self.wearing[i].name
					text_image = screen.menu_font.render(string,1,(0,0,0))
					s.blit(text_image,(21,120+num*25))#blit item names
				
				num += 1
			
		elif category == 1:
			
			for i in self.equipment:
			
				if slot == num:
					
					s.blit(gra_files.gdic['display'][4],(0,115+num*25))#blit marker
					if i != self.nothing:
						string = i.name + '>([e]wear, [b]drop)'
					else:
						string = i.name
					text_image = screen.menu_font.render(string,1,(0,0,0))
					s.blit(text_image,(21,120+num*25))#blit item names
				
				else:
					
					string = i.name
					text_image = screen.menu_font.render(string,1,(0,0,0))
					s.blit(text_image,(21,120+num*25))#blit item names
			
				num += 1
		
		elif category == 2:
			
			for i in self.food:
			
				if slot == num:
					
					s.blit(gra_files.gdic['display'][4],(0,115+num*25))#blit marker
					if i != self.nothing:
						string = i.name + '>([e]%s, [b]drop)' %(i.eat_name)
					else:
						string = i.name
					text_image = screen.menu_font.render(string,1,(0,0,0))
					s.blit(text_image,(21,120+num*25))#blit item names
				
				else:
					
					string = i.name
					text_image = screen.menu_font.render(string,1,(0,0,0))
					s.blit(text_image,(21,120+num*25))#blit item names
			
				num += 1
				
		elif category == 3:
			
			for i in self.misc:
			
				if slot == num:
					
					s.blit(gra_files.gdic['display'][4],(0,115+num*25))#blit marker
					if i != self.nothing:
						string = i.name + '>([e]%s, [b]drop)' %(i.use_name)
					else:
						string = i.name
						
					text_image = screen.menu_font.render(string,1,(0,0,0))
					s.blit(text_image,(21,120+num*25))#blit item names
				
				else:
					
					string = i.name
					text_image = screen.menu_font.render(string,1,(0,0,0))
					s.blit(text_image,(21,120+num*25))#blit item names
			
				num += 1
		
		elif category == 4:
			
			string = 'Wood: ' + str(self.materials.wood) + '/' + str(self.materials.wood_max)
			text_image = screen.menu_font.render(string,1,(0,0,0))
			s.blit(text_image,(21,100))#blit wood line
			
			string = 'Stone: ' + str(self.materials.stone) + '/' + str(self.materials.stone_max)
			text_image = screen.menu_font.render(string,1,(0,0,0))
			s.blit(text_image,(21,125))#blit stone line
			
			string = 'Ore: ' + str(self.materials.ore) + '/' + str(self.materials.ore_max)
			text_image = screen.menu_font.render(string,1,(0,0,0))
			s.blit(text_image,(21,150))#blit ore line
			
			string = 'Herbs: ' + str(self.materials.herb) + '/' + str(self.materials.herb_max)
			text_image = screen.menu_font.render(string,1,(0,0,0))
			s.blit(text_image,(21,175))#blit herbs line
			
			string = 'Gem: ' + str(self.materials.gem) + '/' + str(self.materials.gem_max)
			text_image = screen.menu_font.render(string,1,(0,0,0))
			s.blit(text_image,(21,200))#blit gem line
		
			string = 'Seeds: ' + str(self.materials.seeds) + '/' + str(self.materials.seeds_max)
			text_image = screen.menu_font.render(string,1,(0,0,0))
			s.blit(text_image,(21,225))#blit gem line
			
			string = 'Built with: ' + player.inventory.blueprint.name 
			text_image = screen.menu_font.render(string,1,(0,0,0))
			s.blit(text_image,(21,280))#blit blueprint line
		
		text_image = screen.font.render(self.inv_mes,1,(255,255,255))
		s.blit(text_image,(5,335))
		self.inv_mes = '~*~'
		
		if game_options.mousepad == 1:
			s.blit(gra_files.gdic['display'][8],(480,0)) #render mouse pad
		else:
			s_help = pygame.Surface((160,360))
			s_help.fill((48,48,48))
			s.blit(s_help,(480,0))
		
		if game_options.mousepad == 0:
			s_help = pygame.Surface((640,360))
			s_help.fill((48,48,48))
			s_help.blit(s,(80,0))
			s = s_help
		
		s = pygame.transform.scale(s,(screen.displayx,screen.displayy))
		screen.screen.blit(s,(0,0))
		
		pygame.display.flip()
				
	def inv_user_interaction(self):
		
		run = True
		category = 0
		slot = 0
		
		while run:
			
			self.render(category, slot)
			
			ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
			
			if ui == 'd':	
				slot = 0
				category += 1
				if category > 4: ######change######
					category = 0
			elif ui == 'a':
				slot = 0
				category -= 1
				if category < 0: ######change######
					category = 4
			elif ui == 'x':
				run = False
				break
			elif ui == 'w':
				slot -= 1
				if category == 0:
					if slot < 0:
						slot = len(self.wearing)-1
				elif category == 1:
					if slot < 0:
						slot = len(self.equipment)-1
				elif category == 2:
					if slot < 0:
						slot = len(self.food)-1
				elif category == 3:
					if slot < 0:
						slot = len(self.misc)-1
			elif ui == 's':
				slot += 1
				if category == 0:
					if slot == len(self.wearing):
						slot = 0
				elif category == 1:
					if slot == len(self.equipment):
						slot = 0
				elif category == 2:
					if slot == len(self.food):
						slot = 0
				elif category == 3:
					if slot == len(self.misc):
						slot = 0
			elif ui == 'e':
				
				worn = list(self.wearing.keys())
				
				if category == 0 and self.wearing[worn[slot]] != self.nothing:
					self.unwear(slot)
				elif category == 1:
					self.wear(slot)
				elif category == 2:
					self.eat(slot)
				elif category ==3:
					test = self.use(slot)
					if test == True:
						run = False
						
			elif ui == 'b':
				
				worn = list(self.wearing.keys())
				drop_test =  True
				if category == 0:
					if self.wearing[worn[slot]] == self.nothing:
						drop_test = False
				elif category == 1:
					if self.equipment[slot] == self.nothing:
						drop_test = False
				elif category == 2:
					if self.food[slot] == self.nothing:
						drop_test = False
				elif category == 3:
					if self.misc[slot] == self.nothing:
						drop_test = False
				elif category == 4:
					drop_test = False
					
				if drop_test == True:
					self.drop(category,slot)
		
class container():
	
	def __init__(self, items):
		
		self.items = items
		self.con_mes = '~*~'
					
	def loot(self,num,real_mes= False):
		
		if self.items[num].inv_slot == 'equipment':
			
			found_place = False
			
			for i in range (0, len(player.inventory.equipment)):
				
				if found_place != True:
					if player.inventory.equipment[i] == player.inventory.nothing:
						player.inventory.equipment[i] = self.items[num]
						self.con_mes = 'You looted a %s.' %(self.items[num].name)
						if real_mes == True:
							message.add('You looted a %s.' %(self.items[num].name))
						del self.items[num]
						found_place = True
			
		elif self.items[num].inv_slot == 'food':
			
			found_place = False
			
			for i in range (0, len(player.inventory.food)):
				
				if found_place != True:
					if player.inventory.food[i] == player.inventory.nothing:
						player.inventory.food[i] = self.items[num]
						self.con_mes = 'You looted a %s.' %(self.items[num].name)
						if real_mes == True:
							message.add('You looted a %s.' %(self.items[num].name))
						del self.items[num]
						found_place = True
		
		elif self.items[num].inv_slot == 'misc':
			
			found_place = False
			
			for i in range (0, len(player.inventory.misc)):
				
				if found_place != True:
					if player.inventory.misc[i]  == player.inventory.nothing:
						player.inventory.misc[i]  = self.items[num]
						self.con_mes = 'You looted a %s.' %(self.items[num].name)
						if real_mes == True:
							message.add('You looted a %s.' %(self.items[num].name))
						del self.items[num]
						found_place = True
		
		return found_place
						
	def inventory(self, tile_change = True):
		
		run = True
		
		while run:
			
			s = pygame.Surface((640,360))
			
			running = True
			
			num = 0
			
			self.con_mes = '~*~'
			
			while running:
				
				s = pygame.Surface((640,360))
				
				s.blit(gra_files.gdic['display'][1],(0,0)) #render background
		
				text_image = screen.menu_font.render('~*~ Loot ~*~        [Press [x] to leave]',1,(255,255,255))
				s.blit(text_image,(5,2))#menue title
			
				for i in range (0,len(self.items)):
					
					if i == num:
						s.blit(gra_files.gdic['display'][4],(0,95+num*25))#blit marker
						text_string = self.items[i].name + '>[e]loot'
						text_image = screen.menu_font.render(text_string,1,(0,0,0))
						s.blit(text_image,(21,100+i*25))#blit item name
					else:
						text_image = screen.menu_font.render(self.items[i].name,1,(0,0,0))
						s.blit(text_image,(21,100+i*25))#blit item name
				
				text_image = screen.menu_font.render(self.con_mes,1,(255,255,255))
				s.blit(text_image,(5,335))
				if game_options.mousepad == 1:
					s.blit(gra_files.gdic['display'][8],(480,0)) #render mouse pad
				else:
					s_help = pygame.Surface((160,360))
					s_help.fill((48,48,48))
					s.blit(s_help,(480,0))
				
				if game_options.mousepad == 0:
					s_help = pygame.Surface((640,360))
					s_help.fill((48,48,48))
					s_help.blit(s,(80,0))
					s = s_help
				
				s = pygame.transform.scale(s,(screen.displayx,screen.displayy))
				screen.screen.blit(s,(0,0))
				
				pygame.display.flip()
			
				ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
			
				if ui == 'x':
					running = False
					run = False
				elif ui == 'e':
					item_num = len(self.items)
					self.loot(num)
					if item_num > len(self.items):
						self.con_mes = '~*~'
						num = 0
					else:
						self.con_mes = 'You can\'t loot this...'
				elif ui == 'w':
					self.con_mes = '~*~'
					num -=1
					if num < 0:
						num = len(self.items)-1
				elif ui == 's':
					self.con_mes = '~*~'
					num += 1
					if num > len(self.items)-1:
						num = 0  
					
				if len(self.items) == 0 and tile_change == True:
					
					if world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]].techID != tl.tlist['functional'][4].techID:#this is no chest
						world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]] = world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]].replace
					else:
						replace = deepcopy(world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]].replace)
						world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]] = deepcopy(tl.tlist['functional'][3])
						world.maplist[player.pos[2]][player.on_map].tilemap[player.pos[1]][player.pos[0]].replace = replace
						
					world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]] = 0
					message.add('You looted everything.')
					run = False
					break
					
				elif len(self.items) == 0:
					world.maplist[player.pos[2]][player.on_map].containers[player.pos[1]][player.pos[0]] = 0
					message.add('You looted everything.')
					run = False
					break

class time_class():
	
	def __init__(self):
		
		name = save_path + os.sep + 'time.data'
		
		try:
			
			f = file(name, 'r')
			screen.render_load(6)
			temp = p.load(f)
			self.minute = temp.minute
			self.hour = temp.hour
			self.day = temp.day
			self.day_total = temp.day_total
			self.month = temp.month
			self.year = temp.year
			
		except:
			
			screen.render_load(8)
			
			self.minute = 0
			self.hour = 6
			self.day = 1
			self.day_total = 0
			self.month = 1
			self.year = 1
		
	def tick(self):
		
		for i in range (0,len(world.maplist[player.pos[2]][player.on_map].countdowns)): # check for countdown events
			
			if world.maplist[player.pos[2]][player.on_map].countdowns[i].x != player.pos[0] or world.maplist[player.pos[2]][player.on_map].countdowns[i].y != player.pos[1]:
				if world.maplist[player.pos[2]][player.on_map].npcs[player.pos[1]][player.pos[1]] == 0: #if there is no player or npc on the same tile like the countdown event
					test = world.maplist[player.pos[2]][player.on_map].countdowns[i].countdown()
			
					if test == True:
				
						if world.maplist[player.pos[2]][player.on_map].countdowns[i].kind == 'door':
							world.maplist[player.pos[2]][player.on_map].tilemap[world.maplist[player.pos[2]][player.on_map].countdowns[i].y][world.maplist[player.pos[2]][player.on_map].countdowns[i].x] = tl.tlist['building'][3]
							message.add('A door falls shut.')
							world.maplist[player.pos[2]][player.on_map].countdowns[i] = 'del'
							
						elif world.maplist[player.pos[2]][player.on_map].countdowns[i].kind == 'bomb3':
							replace =  world.maplist[player.pos[2]][player.on_map].tilemap[world.maplist[player.pos[2]][player.on_map].countdowns[i].y][world.maplist[player.pos[2]][player.on_map].countdowns[i].x].replace
							world.maplist[player.pos[2]][player.on_map].tilemap[world.maplist[player.pos[2]][player.on_map].countdowns[i].y][world.maplist[player.pos[2]][player.on_map].countdowns[i].x] = tl.tlist['effect'][1]
							world.maplist[player.pos[2]][player.on_map].tilemap[world.maplist[player.pos[2]][player.on_map].countdowns[i].y][world.maplist[player.pos[2]][player.on_map].countdowns[i].x].replace = replace
							world.maplist[player.pos[2]][player.on_map].countdowns.append(countdown('bomb2', world.maplist[player.pos[2]][player.on_map].countdowns[i].x, world.maplist[player.pos[2]][player.on_map].countdowns[i].y,1))
							world.maplist[player.pos[2]][player.on_map].countdowns[i] = 'del'
							
						elif world.maplist[player.pos[2]][player.on_map].countdowns[i].kind == 'bomb2':
							replace =  world.maplist[player.pos[2]][player.on_map].tilemap[world.maplist[player.pos[2]][player.on_map].countdowns[i].y][world.maplist[player.pos[2]][player.on_map].countdowns[i].x].replace
							world.maplist[player.pos[2]][player.on_map].tilemap[world.maplist[player.pos[2]][player.on_map].countdowns[i].y][world.maplist[player.pos[2]][player.on_map].countdowns[i].x] = tl.tlist['effect'][2]
							world.maplist[player.pos[2]][player.on_map].tilemap[world.maplist[player.pos[2]][player.on_map].countdowns[i].y][world.maplist[player.pos[2]][player.on_map].countdowns[i].x].replace = replace
							world.maplist[player.pos[2]][player.on_map].countdowns.append(countdown('bomb1', world.maplist[player.pos[2]][player.on_map].countdowns[i].x, world.maplist[player.pos[2]][player.on_map].countdowns[i].y,1))
							world.maplist[player.pos[2]][player.on_map].countdowns[i] = 'del'
							
						elif world.maplist[player.pos[2]][player.on_map].countdowns[i].kind == 'bomb1':
							
							for yy in range(world.maplist[player.pos[2]][player.on_map].countdowns[i].y-1,world.maplist[player.pos[2]][player.on_map].countdowns[i].y+2):
								for xx in range(world.maplist[player.pos[2]][player.on_map].countdowns[i].x-1,world.maplist[player.pos[2]][player.on_map].countdowns[i].x+2):
									
									world.maplist[player.pos[2]][player.on_map].npcs[yy][xx] = 0
									world.maplist[player.pos[2]][player.on_map].containers[yy][xx] = 0
									world.maplist[player.pos[2]][player.on_map].make_monsters_angry(xx,yy)
									
									if player.pos[0] == xx and player.pos[1] == yy:
										player.lp -= player.attribute.max_lp 
									
									if world.maplist[player.pos[2]][player.on_map].tilemap[yy][xx].replace != None:
										replace =  deepcopy(world.maplist[player.pos[2]][player.on_map].tilemap[yy][xx].replace)
									else:
										replace =  deepcopy(world.maplist[player.pos[2]][player.on_map].tilemap[yy][xx])
										
									world.maplist[player.pos[2]][player.on_map].tilemap[yy][xx] = deepcopy(tl.tlist['effect'][3])
									world.maplist[player.pos[2]][player.on_map].tilemap[yy][xx].replace = deepcopy(replace)
									world.maplist[player.pos[2]][player.on_map].countdowns.append(countdown('boom', xx, yy,1))
							
							world.maplist[player.pos[2]][player.on_map].countdowns[i] = 'del'
							message.add('BOOOM!')
						
						elif world.maplist[player.pos[2]][player.on_map].countdowns[i].kind == 'boom':
							world.maplist[player.pos[2]][player.on_map].tilemap[world.maplist[player.pos[2]][player.on_map].countdowns[i].y][world.maplist[player.pos[2]][player.on_map].countdowns[i].x] = world.maplist[player.pos[2]][player.on_map].tilemap[world.maplist[player.pos[2]][player.on_map].countdowns[i].y][world.maplist[player.pos[2]][player.on_map].countdowns[i].x].replace
							world.maplist[player.pos[2]][player.on_map].countdowns[i] = 'del'
							
						elif world.maplist[player.pos[2]][player.on_map].countdowns[i].kind == 'flame':
							world.maplist[player.pos[2]][player.on_map].tilemap[world.maplist[player.pos[2]][player.on_map].countdowns[i].y][world.maplist[player.pos[2]][player.on_map].countdowns[i].x] = world.maplist[player.pos[2]][player.on_map].tilemap[world.maplist[player.pos[2]][player.on_map].countdowns[i].y][world.maplist[player.pos[2]][player.on_map].countdowns[i].x].replace
							world.maplist[player.pos[2]][player.on_map].countdowns[i] = 'del'
							
						elif world.maplist[player.pos[2]][player.on_map].countdowns[i].kind == 'healing_aura':
							world.maplist[player.pos[2]][player.on_map].tilemap[world.maplist[player.pos[2]][player.on_map].countdowns[i].y][world.maplist[player.pos[2]][player.on_map].countdowns[i].x] = world.maplist[player.pos[2]][player.on_map].tilemap[world.maplist[player.pos[2]][player.on_map].countdowns[i].y][world.maplist[player.pos[2]][player.on_map].countdowns[i].x].replace
							world.maplist[player.pos[2]][player.on_map].countdowns[i] = 'del'
								
		
		newcountdown = []
		
		for k in world.maplist[player.pos[2]][player.on_map].countdowns:
			if k != 'del':
				newcountdown.append(k)
				
		world.maplist[player.pos[2]][player.on_map].countdowns = newcountdown
		
		self.minute += 1
		
		if player.buffs.hexed <= 0:
			change = 1
		else:
			change = 5
			
		if player.buffs.poisoned > 0:
			change = 2
			
		if player.attribute.hunger > 0:
			player.attribute.hunger -= change
		if player.attribute.thirst > 0:	
			player.attribute.thirst -= change
		if player.attribute.tiredness > 0 and player.buffs.adrenalised <= 0:
			player.attribute.tiredness -= change
		
		if player.attribute.hunger <= 0 or player.attribute.thirst <= 0 or player.attribute.tiredness <= 0:
			player.lp -= 1
			
		if self.minute % 5 == 0:#every 5th turn
			
			if player.buffs.bleeding <= 0 and player.buffs.poisoned <= 0 and player.lp < player.attribute.max_lp:
				player.lp += 1
			elif player.buffs.bleeding > 0:
				player.lp -= 1
				
			if player.buffs.confused <= 0:
				if player.mp < player.attribute.max_mp:
					player.mp += 1
					if player.mp == player.attribute.max_mp:
						message.add('You are focused again.') 
			else:
				player.mp = 0
				
		player.buffs.buff_tick()
		
		world.maplist[player.pos[2]][player.on_map].AI_move()
		
		if self.minute > 59:
			
			self.hour += 1
			self.minute = 0
			
			if self.hour > 23:
				
				self.day += 1
				self.day_total +=1
				self.hour = 0
				screen.render_load(5)
				save(world,player,time,gods,save_path,os.sep)#save the game
				
				if self.day > 28:
						
					self.month += 1
					self.day = 1
						
					if self.month > 13:
							
						self.year +=1
						self.month = 1
						self.day_total = 0 #eventualy will cause a little bug when the year is changing but prevent the number of total days of become endless big
						
						if self.year > 9999:
							self.year = 0 #just to be save ;-)

	def sget(self):
		
		monthnames = ('None', 'Prim', 'Secut', 'Trilus', 'Quarz', 'Vivis', 'Sis', 'Septur', 'Huiles', 'Neurat', 'Dixa', 'Seprim', 'Tweflaf', 'Dritum')
		
		if self.day == 1:
			daystring = '1st'
		elif self.day == 2:
			daystring = '2nd'
		else:
			daystring = str(self.day) + 'th'
			
		if self.hour > 11:
			hourstring = str(self.hour-12)
			ampmstring = 'PM'
		else:
			hourstring = str(self.hour)
			ampmstring = 'AM'	
			
		if len(hourstring) == 1:
			hourstring = '0' + hourstring
			
		if len(str(self.minute)) == 1:
			minutestring = '0' + str(self.minute)
		else:
			minutestring = str(self.minute)	
		
		date = daystring + ' ' + monthnames[self.month]
		time = hourstring + ':' + minutestring + ampmstring
		strings = (date,time)
		
		return strings
	
class gods_class():
	#this class stores the goods mood about the player
	def __init__(self):
		
		name = save_path + os.sep + 'gods.data'
		
		try:
			
			f = file(name, 'r')
			screen.render_load(14)
			temp = p.load(f)
			self.mood = temp.mood
			
		except:
			
			screen.render_load(13)
			self.mood = 10
			#the mood of goods is raised by good sacrifices at the altar(see mob.enter()) and sinks if their help is needed or the player give them crap
	
	def judgement(self):
		#this function check the mood of the gods and returns a False if they are unhappy about the player or a True if they are happy
		if self.mood > 0:
			return True
		else:
			return False
			
class bgM():
	
	def  __init__(self):
		
		self.song_played_now = 'No'
		self.last_song = 'No'
		
	def check_for_song(self,play_menu_sound = False):
		
		music_path = basic_path + os.sep + 'AUDIO' + os.sep + 'BGM' + os.sep
		
		if game_options.bgmmode == 1 and play_menu_sound == False:
			self.song_played_now = world.maplist[player.pos[2]][player.on_map].map_type
		else:
			
			pygame.mixer.music.stop()
		
		if self.song_played_now != self.last_song and play_menu_sound == False:
			
			try:
				pygame.mixer.music.stop()
			except:
				None
				
			track = music_path + self.song_played_now + '.ogg'
			
			pygame.mixer.music.load(track)
			pygame.mixer.music.play(-1)
		
		elif play_menu_sound == True and game_options.bgmmode == 1:
			
			track = music_path + 'menu.ogg'
			
			pygame.mixer.music.load(track)
			pygame.mixer.music.play(-1)
		
		self.last_song = self.song_played_now


def main():
	
	global screen
	global gra_files
	global tl
	global il
	global ml
	global bgm
	global world
	global gods
	global message
	global player
	global time
	global exitgame
	global playing
	
	screen = g_screen()
	gra_files = g_files()
	tl = tilelist()
	il = itemlist()
	ml = monsterlist()
	master_loop = True
	while master_loop:
		bgm = bgM()
		bgm.check_for_song(True)
		screen.render_main_menu()
		if playing == True:
			exitgame = False
			world = world_class(tl)
			gods = gods_class()
			message = messager()
			p_attribute = attribute(2,2,2,2,2,10,10)
			p_inventory = inventory()
			player = player_class ('Testificate', 'local_0_0', p_attribute,p_inventory)
			time = time_class()
			mes = 'Welcome to Roguebox Adventures[' + version +']'
			message.add(mes)
			player.stand_check()
		
			running = True
	
			while running:
		
				world.maplist[player.pos[2]][player.on_map].time_pass() #make the changes of passing time every new day 
		
				if len(message.mes_list) > 1:
		
					for i in range (0,len(message.mes_list)):
						a=screen.render(i)
				
						if a == False:
							getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
			
				else: 
					screen.render(0) 
		
				message.clear()
		
				move_border = 0
		
				bodyparts = ('Head', 'Body', 'Legs' , 'Feet')
		
				for i in bodyparts:
			
					if player.inventory.wearing[i] != player.inventory.nothing:
						move_border += 1
				
				if player.buffs.immobilized > 0:
					screen.reset_hit_matrix()
					ui = getch(screen.displayx,screen.displayy,game_options.sfxmode,game_options.turnmode,mouse=game_options.mousepad)
					if ui == 'x':
						screen.render_brake()
				else:
					move_chance = random.randint(1,9)
					if move_border < move_chance:
						screen.reset_hit_matrix()
						player.user_input()
		
				if exitgame == True:
					running = False
				
if __name__ == '__main__':
	
	main()
