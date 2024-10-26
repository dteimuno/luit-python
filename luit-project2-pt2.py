#!/usr/bin/env python3.13

import os 
#To generate OS current directory using the os module
cwd = os.getcwd() 

#import global module
import glob

#Will create a list that will be used to show files in the current directory
cd_files = []

for file in glob.glob(cwd + '/*'):
    #To create dictionary that contains file path and its size
    cd_dictionary = {'path': file, 'size': os.path.getsize(file)}
    #To append dictionary into list:
    cd_files.append(cd_dictionary)

#Printing cd_files vertically:    
for i in cd_files:   
    print(i)






