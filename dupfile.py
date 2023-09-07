import os

def createdictfiles(directory):
	dict={}
	filenames=os.listdir(directory)
	for fn in filenames:
		data=open(os.path.join(directory,fn),'rb').read()
		hash_code=hash(data)
		if hash_code not in dict:
			dict[hash_code]=set()
		dict[hash_code].add(fn)
	return dict

def FindDuplicate(directory):
	print('THE DUPLICATE FILES ARE:- ')
	groups=createdictfiles(directory)
	for index in groups:
		if (len(groups[index])>=2):
			print(groups[index])


def givedirectory(drive,directname):	
	for root,dirs,files in os.walk(drive,True):
		for dirname in dirs:
			if dirname==directname:
				FindDuplicate(os.path.join(root,directname))
			
				
def takedriveandfolder(drivename,directname):
	if drivename=='C':
		pathdrive=(drivename+':\\Users\\user\\Desktop\\')
		givedirectory(pathdrive,directname)
	elif drivename=='D':
		pathdrive=(drivename+':\\')
		givedirectory(pathdrive,directname)
	elif drivename=='E':
		pathdrive=(drivename+':\\')
		givedirectory(pathdrive,directname)	
		
		
drivename=input('ENTER DRIVE NAME: ').upper()		
directname=input('ENTER THE DIRECTORY NAME: ')
takedriveandfolder(drivename,directname)