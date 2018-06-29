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
import sys


non_native_directory_path = sys.argv[1]
native_directory_path = sys.argv[2]
trigrams_file = sys.argv[3]
unigrams_file = sys.argv[4]
nonNativeOutputFileName = sys.argv[5]
nativeOutputFileName = sys.argv[6]
posNativeOutputFileName = sys.argv[7]
posNonNativeOutputFileName = sys.argv[8]
wordNetNativeOutputFileName = sys.argv[9]
wordNetNonNativeOutputFileName = sys.argv[10]


def main():
    #perforn true-casing
    correctCase(trigrams_file, unigrams_file, native_directory_path, non_native_directory_path, nonNativeOutputFileName, nativeOutputFileName)
    
    # Part of Speech Tagging
    # Convet to WordNet Tagging
    # Word Sense disambiguation
    tagPartOfSpeech(nativeOutputFileName, posNativeOutputFileName)
    tagPartOfSpeech(nonNativeOutputFileName, posNonNativeOutputFileName)

    # Querty WordNet
    # Need to consider frequent word issue (noise - tend to have many senses):
    queryWordNet(posNonNativeOutputFileName,wordNetNonNativeOutputFileName)
    # Staistial Analysis on results
    # normalization phase
    #stastical analysis on normelized resutls
    #Statistical significance Analysis
    
    
    
    

if __name__ == "__main__":
    main()
    

