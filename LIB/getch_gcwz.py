import pygame
import time
import os
	
basic_path = os.path.dirname(os.path.realpath('getch.py')) #just get the execution path for resources
basic_path = basic_path.replace('/LIB','')
sfx_path = basic_path + os.sep + 'AUDIO' + os.sep + 'SFX' + os.sep
pygame.init()
clock = pygame.time.Clock()
sfxlist = {'wasd': pygame.mixer.Sound(sfx_path + 'wasd.ogg'), 'e' : pygame.mixer.Sound(sfx_path + 'e.ogg'), 'b' : pygame.mixer.Sound(sfx_path + 'b.ogg'), 'i' : pygame.mixer.Sound(sfx_path + 'i.ogg'), 'x' : pygame.mixer.Sound(sfx_path + 'x.ogg'), 'f' : pygame.mixer.Sound(sfx_path + 'f.ogg')}

key_name = {'e':'A','b':'B','x':'ST','f':'Y','i':'X','wasd':'D-PAD','ws':'D-PAD'}

def getch(x=640,y=360,sfx=0,mode=0,mouse=1):#x,y,mouse > /dev/null
	
	g = 'foo'
	run = 0
	
	while g == 'foo':
		clock.tick(30)
		run +=1
		for event in pygame.event.get():
							
			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_UP:
					g='w'
					
				if event.key == pygame.K_LEFT:
					g='a'
					
				if event.key == pygame.K_DOWN:
					g='s'
					
				if event.key == pygame.K_RIGHT:
					g='d'
					
				if event.key == pygame.K_LCTRL: #e=a
					g='e'
					
				if event.key == pygame.K_LSHIFT: #x=i
					g='i'
				
				if event.key == pygame.K_LALT:  #b=b
					g='b'
				
				if event.key == pygame.K_RETURN: #start=x
					g='x'
					
				if event.key == pygame.K_SPACE: #y=f
					g='f'
					
		if run > 59:
			if mode == 1:
				g='none'
			run = 0
			
		if sfx == 1:
			if g == 'w' or g == 'a' or g == 's' or g == 'd':
				file_name = 'wasd'
			else:
				file_name = g
						
			if g != 'none' and g != 'foo':
				try:
					sfxlist[file_name].play(maxtime=1000)
				except:
					None
					
	return g
