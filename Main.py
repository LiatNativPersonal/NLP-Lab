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
from frequencyNormalization import normalizeByFrequecny
import sys


non_native_directory_path = sys.argv[1]
native_directory_path = sys.argv[2]
trigrams_file = sys.argv[3]
bigrams_file = sys.argv[4]
unigrams_file = sys.argv[5]
nonNativeOutputFileName = sys.argv[6]
nativeOutputFileName = sys.argv[7]
posNonNativeOutputFileName = sys.argv[8]
posNativeOutputFileName = sys.argv[9]
wordNetNonNativeOutputFileName = sys.argv[10]
wordNetNativeOutputFileName = sys.argv[11]
normalizeByFrequency = True

def main():
    #perforn true-casing
    #correctCase(trigrams_file, bigrams_file, unigrams_file, native_directory_path, non_native_directory_path, nonNativeOutputFileName, nativeOutputFileName)    
    
    # Part of Speech Tagging
    # Convet to WordNet Tagging
    # Word Sense disambiguation
    tagPartOfSpeech(nativeOutputFileName, posNativeOutputFileName)
    #tagPartOfSpeech(nonNativeOutputFileName, posNonNativeOutputFileName)

    # Querty WordNet
    # Need to consider frequent word issue (noise - tend to have many senses):
    #queryWordNet(posNonNativeOutputFileName,wordNetNonNativeOutputFileName)
    queryWordNet(posNativeOutputFileName,wordNetNativeOutputFileName)
    
#    if normalizeByFrequency:
#        normalizeByFrequecny(wordNetNonNativeOutputFileName, normalizedWordnetResultsFile)
        
    
    # Staistial Analysis on results
    # normalization phase
    #stastical analysis on normelized resutls
    #Statistical significance Analysis
    
    
    
    

if __name__ == "__main__":
    main()
    

