# File Duplicate Finder

## Description
The File Duplicate Finder is a Python program that helps you find duplicate files in a given directory in any of your disk drives. It uses file hashing techniques to identify files with identical content, allowing you to efficiently clean up your file system and save disk space.

## Features
- Finds duplicate files based on their content, not just their names
- Supports searching for duplicates within a specific directory or its subdirectories
- Generates a report of duplicate files
  
## Requirements
- Python 3.3
- os module
## Installation
 bash git clone https://github.com/Saptarshi2001/Duplicate-File-Finder.git
## Functions used:-
> takedriveandfolder(drivename,directoryname):
- This function takes in the drive and the directory name ,you need to search for.
> givedirectory(drive,directoryname):
- This function traverses the directory and checks in whether the directory is present or not,If it    is ,then it calls FindDuplicate function and gets the hash code.It then prints those values of the hash code whose length is more than or equals to two thus printing the duplicate files.
> createdictfiles(directoryname):
- This function takes in the directory name ,opens the files and then generates the hash code.     
## To search for duplicate files
- Run the python script:-
## Enter the drive name where you want to search
 > ENTER DRIVE NAME:
## Enter the directory name where you want to search
 > ENTER THE DIRECTORY NAME:
## Examples
 - ENTER DRIVE NAME: D
 - ENTER THE DIRECTORY NAME: matching
> THE DUPLICATE FILES ARE:- 
> {'myfile6.txt', 'myfile3.txt', 'myfile2.txt', 'myfile5.txt'}	

## Contributions
 - This library will be further improved and made better.Feel free to contribute to it.
   
