import pygame
import time
import os
	
basic_path = os.path.dirname(os.path.realpath('getch.py')) #just get the execution path for resources
basic_path = basic_path.replace('/LIB','')
sfx_path = basic_path + os.sep + 'AUDIO' + os.sep + 'SFX' + os.sep
pygame.init()
clock = pygame.time.Clock()
sfxlist = {'wasd': pygame.mixer.Sound(sfx_path + 'wasd.ogg'), 'e' : pygame.mixer.Sound(sfx_path + 'e.ogg'), 'b' : pygame.mixer.Sound(sfx_path + 'b.ogg'), 'i' : pygame.mixer.Sound(sfx_path + 'i.ogg'), 'x' : pygame.mixer.Sound(sfx_path + 'x.ogg'), 'f' : pygame.mixer.Sound(sfx_path + 'f.ogg')}


def getch(x=640,y=360,sfx=0,mode=0,mouse=1):#x and y are the resolution of the surface
	
	g = 'foo'
	run = 0
	try:
		j = pygame.joystick.Joystick(0)
		j.init()
	except:
		None
	
	while g == 'foo':
		clock.tick(30)
		run +=1
		for event in pygame.event.get():
			
			try:		
				button_out = []
				
				for b in range (0,4): 
					button = j.get_button(b)
					if button == True:
						button_out.append(1)
					else:
						button_out.append(0)
					
					hat = j.get_hat(0)
						
				if hat[1] == 1:
					g='w'
				elif hat[1] == -1:
					g='s'
				elif hat[0] == 1:
					g='d'
				elif hat[0] == -1:
					g='a'
				elif button_out[0] == 1:
					g='e'
				elif button_out[1] == 1:
					g='x'
				elif button_out[2] == 1:
					g='b'
				elif button_out[3] == 1:
					g='i'
				elif button_out[4] == 1:
					g='f'
					
			except:
				None	
				
							
			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_w or event.key == pygame.K_UP:
					g='w'
					
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					g='a'
					
				if event.key == pygame.K_s or event.key == pygame.K_DOWN:
					g='s'
					
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					g='d'
					
				if event.key == pygame.K_e or event.key == pygame.K_RETURN:
					g='e'
					
				if event.key == pygame.K_i or event.key == pygame.K_BACKSPACE:
					g='i'
				
				if event.key == pygame.K_b or event.key == pygame.K_SPACE:
					g='b'
				
				if event.key == pygame.K_x or event.key == pygame.K_ESCAPE:
					g='x'
					
				if event.key == pygame.K_f:
					g='f'
			
			if mouse == 1:
					
				mouse_pos = pygame.mouse.get_pos()
				mouse_press = pygame.mouse.get_pressed()
				
				if mouse_pos[0] > (534*x)/640 and mouse_pos[0] < (586*x)/640 and mouse_pos[1] > (0*y)/360 and mouse_pos[1] < (52*y)/360 and mouse_press[0] == True:
					g='w'
			
				if mouse_pos[0] > (483*x)/640 and mouse_pos[0] < (533*x)/640 and mouse_pos[1] > (53*y)/360 and mouse_pos[1] < (104*y)/360 and mouse_press[0] == True:
					g='a'
				
				if mouse_pos[0] > (586*x)/640 and mouse_pos[0] < (638*x/640) and mouse_pos[1] > (53*y)/360 and mouse_pos[1] < (104*y)/360 and mouse_press[0] == True:
					g='d'
				
				if mouse_pos[0] > (534*x)/640 and mouse_pos[0] < (586*x)/640 and mouse_pos[1] > (105*y)/360 and mouse_pos[1] < (157*y)/360 and mouse_press[0] == True:
					g='s'
				
				if mouse_pos[0] > (483*x)/640 and mouse_pos[0] < (533*x)/640 and mouse_pos[1] > (202*y)/360 and mouse_pos[1] < (254*y)/360 and mouse_press[0] == True:
					g='e'
				
				if mouse_pos[0] > (534*x)/640 and mouse_pos[0] < (585*x)/640 and mouse_pos[1] > (202*y)/360 and mouse_pos[1] < (254*y)/360 and mouse_press[0] == True:
					g='b'
				
				if mouse_pos[0] > (586*x)/640 and mouse_pos[0] < (638*x)/640 and mouse_pos[1] > (202*y)/360 and mouse_pos[1] < (254*y)/360 and mouse_press[0] == True:
					g='i'
				
				if mouse_pos[0] > (534*x)/640 and mouse_pos[0] < (585*x)/640 and mouse_pos[1] > (255*y)/360 and mouse_pos[1] < (307*y)/360 and mouse_press[0] == True:
					g='x'
				
				if mouse_pos[0] > (534*x)/640 and mouse_pos[0] < (586*x)/640 and mouse_pos[1] > (53*y)/360 and mouse_pos[1] < (104*y)/360 and mouse_press[0] == True:
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
