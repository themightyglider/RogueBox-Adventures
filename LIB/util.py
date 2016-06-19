import pickle as p
from version import release_number

try:
	from urllib import urlopen
except:
	import urllib.request.urlopen as urlopen

def save(world,player,time,gods,path,sep):
	#this function is called if the game is closed
	#it needs the world object, the player object, the time object, the basic_path and os.sep from the main programm
	
	name1 = path + sep + 'world.data'
	
	f = file(name1, 'w+')
	p.dump(world,f)
	f.close()
	
	name2 = path + sep + 'player.data'
	
	f = file(name2, 'w+')
	p.dump(player,f)
	f.close()
	
	name3 = path + sep + 'time.data'
	
	f = file(name3, 'w+')
	p.dump(time,f)
	f.close()
	
	name4 = path + sep + 'gods.data'
	
	f = file(name4, 'w+')
	p.dump(gods,f)
	f.close()

def check_version():
	#this function compares the release_number from version.py whit a number that from the https://themightyglider.github.io/version.htm
	#and returns: 'This version is up to date', 'Old version!!! Please update.', 'Can't reach server!'
	try:
		f = urlopen('https://themightyglider.github.io/version.htm')
		vers_test = int(f.read())
		
		if release_number ==  vers_test:
			return 'This version is up to date.'
		else:
			return 'Old version!!! Please update.'
	except:
			return 'Can\'t reach server!'
