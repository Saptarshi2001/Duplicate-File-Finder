import os

def createdictfiles(directoryname):
	try:
		dict={}
		filenames=os.listdir(directoryname)
		for fn in filenames:
			with open(os.path.join(directoryname,fn),'rb') as files:
				data=files.read()
				hash_code=hash(data)
				if hash_code not in dict:
					dict[hash_code]=set()
				dict[hash_code].add(fn)
			
	except:
		print('HASH CODE NOT GENERATED' )
	return dict

def FindDuplicate(directoryname):
	try:
		groups=createdictfiles(directoryname)
		for index in groups:	
			if (len(groups[index])>=2):
				print('THE DUPLICATE FILES ARE:- ')
				print(groups[index])
	except:
		print('NO GROUPS PRINTED')
		
def givedirectory(drive,directoryname):
	try:
		for root,dirs,files in os.walk(drive,True):	
			for dirname in dirs:	
				if dirname==directoryname:		
					FindDuplicate(os.path.join(root,directoryname))
	except:
		print('NO DIRECTORY NAME MATCHED')
		
				
def takedriveandfolder(drivename,directoryname):
	try:
		if drivename=='C':
			pathdrive=(drivename+':\\Users\\user\\Desktop\\')
			givedirectory(pathdrive,directoryname)
		elif drivename=='D':
			pathdrive=(drivename+':\\')
			givedirectory(pathdrive,directoryname)
		elif drivename=='E':
			pathdrive=(drivename+':\\')
			givedirectory(pathdrive,directoryname)	
	except:
		print('INCORRECT INPUT')
		
drivename=input('ENTER DRIVE NAME: ').upper()		
directoryname=input('ENTER THE DIRECTORY NAME: ')
takedriveandfolder(drivename,directoryname)