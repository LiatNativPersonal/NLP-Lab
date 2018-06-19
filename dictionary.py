# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 12:50:50 2018

@author: TAL-LAPTOP
"""

true_case_stat_file='C:\\Users\\TAL-LAPTOP\\Desktop\\NLP Lab\\w3.txt'
d = {}
mone = 0
with open(true_case_stat_file) as f:
    
    for line in f:
        if mone<100:
           (counter, trigram1, trigram2, trigram3) = line.split()
    #       print(counter)
    #       print(trigram1)
           key=trigram1 + ' ' + trigram2 + ' ' + trigram3
           d[key] = int(counter)
           mone=mone+1
#           print("key= " + key + "\nvalue= " + str(d[key]) + '\n')
           f.close
    
for key,value in d.items():
    counter=0
    result=''
    if key.lower() in d.keys():
         counter= (d[key.lower()])    
         result=key.lower()
    if key.upper() in d.keys():           
         if counter < (d[key.upper()]):            
             result=key.upper()
             counter=(d[key.upper()])
    if key.title() in d.keys():  
         if counter < (d[key.title()]):
          result=key.title()  
    else:
        result=key
    
    print("key: " +key)
    print("TrueCase: "+ result)
#    print(key +', '+ str(value))
    
