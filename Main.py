# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 22:50:45 2018

@author: TAL-LAPTOP
"""
#from nltk.corpus import wordnet as wn
from WordNetAccess import  queryWordNet
#from TofelPOSTagging import tag_part_of_speech
from TrueCase import correctCase
from POSTagging import tagPartOfSpeech
import ast
import sys
import os
import numpy as np

non_native_directory_path = sys.argv[1]
native_directory_path = sys.argv[2]
trigrams_file = sys.argv[3]
unigrams_file = sys.argv[4]
nonNativeOutputFileName = sys.argv[5]
nativeOutputFileName = sys.argv[6]
posNativOutputFileName = sys.argv[7]
posNonNativOutputFileName = sys.argv[8]
wordNetNativeOutputFileName = sys.argv[9]
wordNetNonNativeOutputFileName = sys.argv[10]
#trueCase = sys.argv[6]
trueCase = True



def main():
# TrueCase (if needed)
    if trueCase:
        correctCase(trigrams_file, unigrams_file, native_directory_path, non_native_directory_path, nonNativeOutputFileName, nativeOutputFileName)
    
    # Part of Speech Tagging
    # Convet to WordNet Tagging
    # Word Sense disambiguation
    tagPartOfSpeech(nativeOutputFileName, posNativOutputFileName)
    #tagPartOfSpeech(nonNativeOutputFileName, posNonNativOutputFileName)

    # Querty WordNet
    # Need to consider frequent word issue (noise - tend to have many senses):
    queryWordNet(posNativOutputFileName,wordNetNativeOutputFileName)
    # Staistial Analysis
    
    
    
    
    
    #print (wn.ADJ)
    #print (wn.VERB)
    #print (wn.NOUN)
    #print (wn.ADV)
    #ss= wn.synset('first.r.01')
    #print(ss)
    #print (min([len(path) for path in ss.hypernym_paths()]))
    new_line=[]
    orig_path='C:\\Users\\TAL-LAPTOP\\Desktop\\NLP Lab\\nli-shared-task-2017\\data\\essays\\dev\\tokenized'
    pos_path='C:\\Users\\TAL-LAPTOP\\Desktop\\NLP Lab\\nli-shared-task-2017\\data\\essays\\dev\\POSTag\\TOFEL_POS_TAGGED.txt'
    wordnet_results_path='C:\\Users\\TAL-LAPTOP\\Desktop\\NLP Lab\\nli-shared-task-2017\\data\\essays\\dev\\POSTag\\TOFEL_WORDNET_RESULTS.txt'
    #sentence = [('I', 'PRP'), ('fully', 'RB'), ('agree', 'VBP'), ('to', 'TO'), ('that', 'DT'), ('statement', 'NN'), ('because', 'IN'), ('of', 'IN'), ('the', 'DT'), ('following', 'JJ'), ('reasons', 'NNS'), ('.', '.')]
    #for pair in sentence:
    #    print(len(pair))
    #    new_line.append([pair[0], get_wordnet_pos(pair[1])])
    ##print(sentence)
    ##print(new_line)
    #open(wordnet_results_path, 'w+').close()
    ##tag_part_of_speech(orig_path, pos_path)
    #with open(wordnet_results_path, 'a') as wr:
    #    with open(pos_path, 'r') as tagged:
    #        data = tuple(ast.literal_eval(line) for line in tagged)
    #        for tagged_line in tagged:
    #             new_line = tagged_line.split(',')
    #    #         print(new_line)
    #        for tupple in data:
    #    #        print(tupple)
    #            if len(tupple) < 3 :
    #                continue              
    #            print(get_number_of_syns(tupple))
    #            print(get_min_hypernym_path(tupple))
    #            wr.write(str(tupple[0]) + ',' + str(tupple[1]) + ',' + str(tupple[2]) + ',' + str(get_number_of_syns(tupple)) + ',' + str(get_min_hypernym_path(tupple)))
    #            wr.write('\n')
    #    wr.close()
    #            
        
if __name__ == "__main__":
    main()
    

