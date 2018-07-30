# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from nltk.corpus import wordnet as wn
import ast
import os
import nltk

def queryWordNet(inputFile, outputFilePolySemi, outputFileHypernymPath):
    if os.path.exists(outputFilePolySemi) or os.path.exists(outputFileHypernymPath):
        print("WordNet query tagging phase skipped")
        return
    print("Start WordNet query for polysemy, writing results to " + outputFilePolySemi)
    print("Start WordNet query for hypernym path, writing results to " + outputFileHypernymPath)
    with open(outputFilePolySemi, 'a') as outputPoly:
        with open(outputFileHypernymPath, 'a') as outputHyper:
            with open(inputFile, 'r') as input:
                tupplesNum = 0                
                data = tuple(ast.literal_eval(line) for line in input)
                for tupple in data:
                    tupplesNum += 1
    #                print(tupple)
                    if len(tupple) < 2 :                    
                        continue              
    #                    print(get_number_of_syns(tupple))
    #                    print(get_min_hypernym_path(tupple))
                    word = str(tupple[0])
                    pos_tag = str(tupple[1])
                    try:
                        #ouput.write(str(tupple[0]) + ',' + str(tupple[1]) + ',' + str(tupple[2]) + ',' + str(get_number_of_syns(tupple)) + ',' + str(get_min_hypernym_path(tupple)))
                        numberOfSenses = get_number_of_syns(word, pos_tag)
                        if numberOfSenses != 0 :
                            outputPoly.write(word + ' ' + pos_tag + ' ' + str(numberOfSenses) +  '\n')
                            if pos_tag != wn.ADJ and pos_tag != wn.ADV:
                                outputHyper.write(word + ' ' + pos_tag + ' '+ str(get_avg_min_hypernym_path(word, pos_tag)) + '\n')
                    except:
                        continue
            print(tupplesNum)     
    outputPoly.close()
    outputHyper.close()
    
    
def get_number_of_syns(word, pos_tag):   
    
    try:            
        return(len(wn.synsets(word, pos_tag)))            
    except ValueError:            
        return 0

def get_min_hypernym_path(lemma): 
#    expr = nltk.stem.WordNetLemmatizer().lemmatize(tupple[0],tupple[1])
    try:         
        ss = wn.synset(lemma)
    except:       
        return 0
    #print("Minimum hypernym path length:")
    return (max([len(path) for path in ss.hypernym_paths()]))
#    print("Maximum hypernym path length:")
#    print (max([len(path) for path in ss.hypernym_paths()]))

def get_avg_min_hypernym_path(word, pos_tag):
    lemma = nltk.stem.WordNetLemmatizer().lemmatize(word, pos_tag)
    total_senses = 0
    counter = 0    
    for syn in(wn.synsets(lemma, pos_tag)):
        total_senses += (max([len(path)  for path in syn.hypernym_paths()]))
        counter += 1
    if counter == 0:
        return 0
    return round(total_senses/counter)
    