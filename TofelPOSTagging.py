# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 14:22:59 2018

@author: TAL-LAPTOP
"""

import os
import nltk
from nltk.wsd import lesk
from WordNetAccess import get_wordnet_pos

def tag_part_of_speech(orig_path, pos_path):

    open(pos_path, 'w+').close()
    with open(pos_path, 'a') as tagged:    
        for path in os.listdir(orig_path):
           file_name = os.path.basename(path)  
           with open(os.path.join(orig_path,file_name), 'r') as orig: 
              
               for line in orig:   
                   if line == "\n":
                       continue
                   tok_line = nltk.word_tokenize(line)
                   tagged_line=nltk.pos_tag(tok_line)
                   wordnet_tagged_line=[]
                   for pair in tagged_line:                      
                       if len(pair) < 2 :
                           continue
                       if get_wordnet_pos(pair[1]) != '':
                           wordnet_pos=get_wordnet_pos(pair[1]) 
                           result= str(lesk(line, pair[0], wordnet_pos))
                           sense_num = result[len(result)-4:len(result)-2]
                           if not sense_num.isdigit() :
                               sense_num = '0';                           
                           wordnet_tagged_line=(pair[0], wordnet_pos, sense_num)
                           tagged.write(str(wordnet_tagged_line))
                           tagged.write("\n")                  
                   
               orig.close
           tagged.close
   
           
           
           