import os, sys, re

p_include=re.compile(r'#include.*\.ti')
p_variable=re.compile(r".*\=.*")
p_filename=re.compile(r'\/.*\/.*.ti')
dict_variable={}
list_includeFiles=[]

def generateDict(ti_file):        
    with open(ti_file) as f:
        lines= f.readlines()
    for line in lines:    
        # print(line)
        if p_variable.findall(line):            
            k,v = line.split("=")            
            if not k in dict_variable:
                dict_variable[k] = v.strip()
        elif p_include.findall(line): 
            includeFile = p_filename.findall(line)[0].lstrip("\/")
            if not includeFile in list_includeFiles:
                list_includeFiles.append(includeFile)

dir=sys.argv[1] #from cmdline run python3 generateDict.py 3/a.ti
generateDict(dir)   

if list_includeFiles:
    for includeFile in list_includeFiles:                
        generateDict(includeFile) 
              
print (dict_variable)
