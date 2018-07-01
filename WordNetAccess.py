# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from nltk.corpus import wordnet as wn
import ast
import os

def queryWordNet(inputFile, outputFile):
    if os.path.exists(outputFile):
        print("WordNet query tagging phase skipped")
        return
    with open(outputFile, 'a') as ouput:
        with open(inputFile, 'r') as input:
                data = tuple(ast.literal_eval(line) for line in input)
                for tupple in data:
        #    #        print(tupple)
                    if len(tupple) < 3 :
                        continue              
#                    print(get_number_of_syns(tupple))
#                    print(get_min_hypernym_path(tupple))
                    try:
                        #ouput.write(str(tupple[0]) + ',' + str(tupple[1]) + ',' + str(tupple[2]) + ',' + str(get_number_of_syns(tupple)) + ',' + str(get_min_hypernym_path(tupple)))
                        ouput.write(str(tupple[0]) + ' ' + str(get_number_of_syns(tupple)) + ' ' + str(get_min_hypernym_path(tupple)))
                        ouput.write('\n')
                    except:
                        continue
        ouput.close()
    
    
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

