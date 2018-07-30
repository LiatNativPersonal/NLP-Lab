import os
#import numpy as np
import random


def correctCase(trigrams_file, bigrams_file, unigrams_file, native_directory_path, non_native_directory_path, nonNativeOutputFileName, nativeOutputFileName):     
    if not os.path.exists(nonNativeOutputFileName) or not os.path.exists(nativeOutputFileName):
        print("Need to perform TrueCasing") 
        trigramsDB = open(trigrams_file,"r")
        bigramsDB = open(bigrams_file,"r")
        unigramsDB = open(unigrams_file,"r")
        trigramDictionary = createTrigramDictionary(trigramsDB)
        bigramDictionary = createBigramDictionary(bigramsDB)
        unigramDictionary = createUnigramDictionary(unigramsDB)
        nonNativeSentenceArray = []
        nonNativeNewSentenceArray = []
        nativeSentenceArray = []        
        nativeNewSentenceArray = []

        # NON NATIVE              
        if not os.path.exists(nonNativeOutputFileName):
            print("True-casing non-nativ data")
            nonNativeOutputFile = open(nonNativeOutputFileName,"w", encoding="utf-8")    
            nonNativeFileList = os.listdir(non_native_directory_path)   
            
            for file in nonNativeFileList:       
                nonNativeFile = open(non_native_directory_path + "\\" + file,"r", encoding = "utf8",  errors="ignore")
                print("Running file " + str(file))
                maxLength = 500000

                nonNativeSentenceArray += (createSentencesArray(nonNativeFile, maxLength))
                nonNativeFile.close()    
            for sentence in nonNativeSentenceArray:
                sentence = removeBrackets(sentence)
                sentence = handleTitle(sentence)
                sentence = handleUpperLowerCase(sentence, trigramDictionary, bigramDictionary, unigramDictionary)
                nonNativeNewSentenceArray.append(sentence)
            for sentence in nonNativeNewSentenceArray:
                    nonNativeOutputFile.write(sentence + "\n")     
            nonNativeOutputFile.close()
        else:
            print("Truecase phase for non-native skipped - data exist")
         # NATIVE   
        if not os.path.exists(nativeOutputFileName):
            nonNativelength = len(nonNativeSentenceArray)/6
            del nonNativeNewSentenceArray[:]
            del nonNativeSentenceArray[:]
            #nonNativelength = 2881049
            print("True-casing nativ data")
            nativeOutputFile = open(nativeOutputFileName,"w", encoding="utf-8")       
            nativeFileList = os.listdir(native_directory_path)
            for file in nativeFileList:       
                nativeFile = open(native_directory_path + "\\" + file, "r", encoding = "utf8",  errors = "ignore")
                print("Running file " + str(file))
                nativeSentenceArray += (createSentencesArray(nativeFile, nonNativelength))
                nativeFile.close() 
            for sentence in nativeSentenceArray:
                sentence = removeBrackets(sentence)
                sentence = handleTitle(sentence)
                sentence = handleUpperLowerCase(sentence, trigramDictionary, bigramDictionary, unigramDictionary)
                nativeNewSentenceArray.append(sentence)
            for sentence in nativeNewSentenceArray:
                    nativeOutputFile.write(sentence + "\n")     
            nativeOutputFile.close()
        else:
            print("Truecase phase for native skipped - data exist")
            
        del nativeNewSentenceArray[:]
        del nativeSentenceArray[:]
          
        trigramsDB.close()
        bigramsDB.close()
        unigramsDB.close()
    else:
        print("Truecase phase  skipped - data exist")
        

def createSentencesArray(file, maxLength):
    sentenceArray = []
    newSentenceArray = []
    maxLength = int(maxLength)
    for line in file:
        if not isLineEmpty(line):
            sentenceArray.append(line)
            
    arrayLength = len(sentenceArray)

    if arrayLength > maxLength:
        newSentenceArray = random.sample(sentenceArray,maxLength)
    else:
       newSentenceArray = sentenceArray
        
    return newSentenceArray

def createTrigramDictionary(triGramsFile):
    trigramDict = {}
    
    for line in triGramsFile:
         (counter, trigram1, trigram2, trigram3) = line.split()
         key = trigram1 + ' ' + trigram2 + ' ' + trigram3           
         trigramDict[key] = int(counter)
    return trigramDict 

def createBigramDictionary(biGramsFile):
    bigramDict = {}
    
    for line in biGramsFile:
         (counter, bigram1, bigram2) = line.split()
         key = bigram1 + ' ' + bigram2           
         bigramDict[key] = int(counter)
    return bigramDict  

def createUnigramDictionary(uniGramsFile):
    unigramDict = {}
    
    for line in uniGramsFile:
         (counter, unigram1) = line.split()
         key = unigram1           
         unigramDict[key] = int(counter)
    return unigramDict          

def isLineEmpty(line):
    return len(line.strip()) == 0

def removeBrackets(sentence):
    subString = sentence[sentence.find('['):sentence.find(']')+1]
    sentence = sentence.replace(subString,'', 1)
    subString = sentence[sentence.find('['):sentence.find(']')+1]
    sentence = sentence.replace(subString, '', 1)
    return sentence

def handleTitle(sentence):
    sentenceWordArray = []
    sentenceWordArray = sentence.split()
    index = 0
    flag = 1
    if len(sentence) == 0:
        return sentence
    while flag == 1:
        if sentenceWordArray[index].isalpha():
            sentenceWordArray[index] = sentenceWordArray[index].title()
            flag = 0
        else:
            index = index + 1
            if index >= len(sentenceWordArray):
                flag = 0
    sentence = ' '.join(sentenceWordArray) 
    return sentence

def handleUpperLowerCase(sentence, trigramDictionary, bigramDictionary, unigramDictionary): 
    sentenceSplitWordArray = sentence.split()
    lengthSplitArray =  len(sentenceSplitWordArray) - 2
    for index in range(lengthSplitArray):
        found = False
        counter = 0
        middleWord = sentenceSplitWordArray[index + 1]
        trueCase = middleWord
        unigramLower = sentenceSplitWordArray[index + 1].lower()
        unigramUpper = sentenceSplitWordArray[index + 1].upper()
        unigramTitle = sentenceSplitWordArray[index + 1].title()
        bigramLower = sentenceSplitWordArray[index] + " " + unigramLower
        bigramUpper = sentenceSplitWordArray[index] + " " + unigramUpper
        bigramTitle = sentenceSplitWordArray[index] + " " + unigramTitle
        trigramLower = sentenceSplitWordArray[index] + " " + unigramLower + " " + sentenceSplitWordArray[index + 2]
        trigramUpper = sentenceSplitWordArray[index] + " " + unigramUpper + " " + sentenceSplitWordArray[index + 2]
        trigramTitle = sentenceSplitWordArray[index] + " " + unigramTitle + " " + sentenceSplitWordArray[index + 2]   
        if trigramLower in trigramDictionary.keys():
            counter = trigramDictionary[trigramLower]    
            trueCase = middleWord.lower()
            found = True           
        if trigramUpper in trigramDictionary.keys():           
           if counter < trigramDictionary[trigramUpper]:            
              trueCase = middleWord.upper()
              counter = trigramDictionary[trigramUpper]              
           found = True
        if trigramTitle in trigramDictionary.keys():  
           if counter < trigramDictionary[trigramTitle]:
               trueCase = middleWord.title()               
           found = True
           
        if found:
            sentenceSplitWordArray[index+1] = trueCase
        else:
            if bigramLower in bigramDictionary.keys():
                counter = bigramDictionary[bigramLower]    
                trueCase = middleWord.lower()
                found = True           
            if bigramUpper in bigramDictionary.keys():           
                if counter < bigramDictionary[bigramUpper]:            
                    trueCase = middleWord.upper()
                    counter = bigramDictionary[bigramUpper]              
                found = True
            if bigramTitle in bigramDictionary.keys():  
                if counter < bigramDictionary[bigramTitle]:
                    trueCase = middleWord.title()               
                found = True
           
            if found:
                sentenceSplitWordArray[index+1] = trueCase
            else: # could not find trigram - fall back to unigram
                if unigramLower in unigramDictionary.keys():
                    counter = unigramDictionary[unigramLower]    
                    trueCase = middleWord.lower()
                if unigramUpper in unigramDictionary.keys():           
                    if counter < unigramDictionary[unigramUpper]:            
                        trueCase = middleWord.upper()
                        counter = unigramDictionary[unigramUpper]              
                if unigramTitle in unigramDictionary.keys():  
                    if counter < unigramDictionary[unigramTitle]:
                        trueCase = middleWord.title()               
                sentenceSplitWordArray[index+1] = trueCase
                
    sentence = " ".join(sentenceSplitWordArray)
    return sentence



