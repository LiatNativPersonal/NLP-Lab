# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 09:51:12 2018

@author: Lilach Naim & Liat Nativ
"""
import os
import nltk
from nltk.corpus import wordnet as wn
from nltk.wsd import lesk

def tagPartOfSpeech(sourceFile, destFile):
    if os.path.exists(destFile):
        print("POS tagging phase skipped")
        return
    with open(destFile, 'a+') as tagged:         
        with open(sourceFile, 'r', encoding="utf-8", errors="ignore") as orig: 
            for line in orig:
                   if line == "\n":
                       continue
                   tok_line = nltk.word_tokenize(line)
                   tagged_line=nltk.pos_tag(tok_line)
                   wordnet_tagged_line=[]
                   for pair in tagged_line:
                       if len(pair) < 2 :
                           continue
                       if not pair[1].isalpha():
                           continue
                       wordnet_pos = get_wordnet_pos(pair[1])
                       if wordnet_pos != '':                                                 
                           wordnet_tagged_line=(pair[0], wordnet_pos)
                           try:
                               
                               tagged.write(str(wordnet_tagged_line))
                               tagged.write("\n")
                           except:
                               continue
#                       if wordnet_pos != '':
#                           #word sense disambiguation
#                           result= str(lesk(line, pair[0], wordnet_pos))
#                           sense_num = result[len(result)-4:len(result)-2]
#                           if not sense_num.isdigit() :
#                               sense_num = '0';
#                           try:
#                               wordnet_tagged_line=(pair[0], wordnet_pos, sense_num)
#                               tagged.write(str(wordnet_tagged_line))
#                               tagged.write("\n")
#                           except:
#                               continue
                   
                   orig.close
        tagged.close
           


def get_wordnet_pos(tag):
   if tag.startswith('JJ')or tag.startswith('EX') or tag.startswith('IN') or tag.startswith('PDT') or tag.startswith('RP'):
       return wn.ADJ
   elif tag.startswith('VB'):
       return wn.VERB
   elif tag.startswith('NN') or tag.startswith('CD'):
       return wn.NOUN
   elif tag.startswith('RB'):
       return wn.ADV
   else:
        return ''
    