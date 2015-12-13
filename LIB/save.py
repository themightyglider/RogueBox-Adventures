import pickle as p

def save_everything(world,player,time,gods,path,sep):
	#this function is called if the game is closed
	#it needs the world object, the player object, the time object, the basic_path and os.sep from the main programm
	
	name1 = path + sep + 'SAVE' + sep + 'world.data'
	
	f = file(name1, 'w')
	p.dump(world,f)
	f.close()
	
	name2 = path + sep + 'SAVE' + sep + 'player.data'
	
	f = file(name2, 'w')
	p.dump(player,f)
	f.close()
	
	name3 = path + sep + 'SAVE' + sep + 'time.data'
	
	f = file(name3, 'w')
	p.dump(time,f)
	f.close()
	
	name4 = path + sep + 'SAVE' + sep + 'gods.data'
	
	f = file(name4, 'w')
	p.dump(gods,f)
	f.close()
