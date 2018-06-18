# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from nltk.corpus import wordnet as wn

def get_wordnet_pos(tag):
   if tag.startswith('JJ'):
       return wn.ADJ
   elif tag.startswith('VB'):
       return wn.VERB
   elif tag.startswith('NN'):
       return wn.NOUN
   elif tag.startswith('RB'):
       return wn.ADV
   else:
        return ''
    

    
def get_number_of_syns(tupple):     
    try:
        return(len(wn.synsets(tupple[0], tupple[1])))
    except ValueError:
        return ''

def get_min_hypernym_path(tupple): 
    expr = tupple[0] + '.' + tupple[1] + '.' + tupple[2]
    try:         
        ss = wn.synset(expr)
    except:
        return 0
    #print("Minimum hypernym path length:")
    return (min([len(path) for path in ss.hypernym_paths()]))
#    print("Maximum hypernym path length:")
#    print (max([len(path) for path in ss.hypernym_paths()]))

