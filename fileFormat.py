import  os, glob

basepath = '/home/vangs/Pictures/Sim-Ma/2014/'
os.chdir(basepath)
count = 1

with os.scandir(path='.') as it:
	for entry in it:
		if not entry.name.startswith('NEF') and entry.is_dir() and count<100:
			count +=1
			newDir= basepath + 'NEF.' + entry.name 

			try:
				os.mkdir(newDir)
				print('NewDir= ' + newDir)
			except FileExistsError:
				print( newDir + ' DirExists\n')
			else:
				currDir=basepath + entry.name + '/'
				os.chdir(currDir)
				print('Current Dir is=' + os.getcwd() + '\n')
				#Up to here I have created the new dir, and in old one
				file_names = os.listdir(currDir)
				for file_name in file_names:
					if os.path.splitext(file_name)[1] == ".NEF":
						os.rename( currDir + file_name, newDir + '/' + file_name)

