# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 12:50:50 2018

@author: TAL-LAPTOP
"""

true_case_stat_file='C:\\Users\\TAL-LAPTOP\\Desktop\\NLP Lab\\w3.txt'
#d is the dictionary
d = {}
#Reading the file into dictionray
#Key is the trigram, seperated by spaces
#value is the counter
with open(true_case_stat_file) as f:
    
    for line in f:      
       (counter, trigram1, trigram2, trigram3) = line.split()
#       print(counter)
#       print(trigram1)         
      
       key =trigram1 + ' ' + trigram2 + ' ' + trigram3           
       d[key] = int(counter)         
#       print("key= " + key + "\nvalue= " + str(d[key]) + '\n')
#           print(key.split())
       f.close

#goint over the keys - changing case for the middle word only
#return the case with the highest frequancy
for key,value in d.items():
    counter=0
    result=''
    seperated_key = key.split(' ')
    lower = str(str(seperated_key[0]) + ' ' + str(seperated_key[1]).lower() + ' ' + str(seperated_key[2]))
    upper = str(str(seperated_key[0]) + ' ' + str(seperated_key[1]).upper() + ' ' + str(seperated_key[2]))
    title = str(str(seperated_key[0]) + ' ' + str(seperated_key[1]).title() + ' ' + str(seperated_key[2]))
#    print(str(seperated_key[1]))
    print(lower + ' ' + upper + ' ' + title)
    
    if lower in d.keys():
         counter= d[lower]    
         result=lower
    if upper in d.keys():           
         if counter < d[upper]:            
             result=key.upper()
             counter=d[upper]
    if title in d.keys():  
         if counter < d[title]:
             result=title
    else:
        result=key
#    
#    print("key: " +key)
#    print("TrueCase: "+ result)
#    print(key +', '+ str(value))
    
