import sys
import os
import numpy as np


def correctCase(trigrams_file, unigrams_file, native_directory_path, non_native_directory_path, nonNativeOutputFileName, nativeOutputFileName):
   
   
    
    if not os.path.exists(nonNativeOutputFileName) or not os.path.exists(nativeOutputFileName):
        print("Need to perform TrueCasing") 
        trigramsDB = open(trigrams_file,"r")
        unigramsDB = open(unigrams_file,"r")
        trigramDictionary = createTrigramDictionary(trigramsDB)
        unigramDictionary = createUnigramDictionary(unigramsDB)
        # NON NATIVE              
        if not os.path.exists(nonNativeOutputFileName):
            print("True-casing non-nativ data")
            nonNativeOutputFile = open(nonNativeOutputFileName,"w", encoding="utf-8")    
            nonNativeSentenceArray = []
            nonNativeNewSentenceArray = []
            nonNativeFileList = os.listdir(non_native_directory_path)   
            
            for file in nonNativeFileList:       
                nonNativeFile = open(non_native_directory_path + "\\" + file,"r", encoding = "utf8",  errors="ignore")
                print("Running file " + str(file))
                nonNativeSentenceArray += (createSentencesArray(nonNativeFile))
                nonNativeFile.close()
        
            for sentence in nonNativeSentenceArray:
                sentence = removeBrackets(sentence)
                sentence = handleTitle(sentence)
                sentence = handleUpperLowerCase(sentence, trigramDictionary, unigramDictionary)
                nonNativeNewSentenceArray.append(sentence)
            for sentence in nonNativeNewSentenceArray:
                    nonNativeOutputFile.write(sentence + "\n")     
            nonNativeOutputFile.close()
        else:
            print("Truecase phase for non-native skipped - data exist")
         # NATIVE   
        if not os.path.exists(nativeOutputFileName):
            print("True-casing nativ data")
            nativeOutputFile = open(nativeOutputFileName,"w", encoding="utf-8")
            nativeSentenceArray = []
            nativeNewSentenceArray = []       
            nativeFileList = os.listdir(native_directory_path)
            
            for file in nativeFileList:       
                nativeFile = open(native_directory_path + "\\" + file, "r", encoding = "utf8",  errors = "ignore")
                print("Running file " + str(file))
                nativeSentenceArray += (createSentencesArray(nativeFile))
                nativeFile.close()
                
            for sentence in nativeSentenceArray:
                sentence = removeBrackets(sentence)
                sentence = handleTitle(sentence)
                sentence = handleUpperLowerCase(sentence, trigramDictionary, unigramDictionary)
                nativeNewSentenceArray.append(sentence)
            for sentence in nativeNewSentenceArray:
                    nativeOutputFile.write(sentence + "\n")     
            nativeOutputFile.close()
        else:
            print("Truecase phase for native skipped - data exist")
          
        trigramsDB.close()
        unigramsDB.close()
    else:
        print("Truecase phase  skipped - data exist")
        
   

def createSentencesArray(file):
    sentenceArry = []
    for line in file:
        if not isLineEmpty(line):
            sentenceArry.append(line)
            
    np.random.shuffle(sentenceArry)
    
    arrayLength = len(sentenceArry)
    maxLength = 500000

    if arrayLength > maxLength:
        sentenceArry = sentenceArry[:maxLength]
    return sentenceArry

def createTrigramDictionary(triGramsFile):
    trigramDict = {}
    
    for line in triGramsFile:
         (counter, trigram1, trigram2, trigram3) = line.split()
         key = trigram1 + ' ' + trigram2 + ' ' + trigram3           
         trigramDict[key] = int(counter)
    return trigramDict  

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

def handleUpperLowerCase(sentence, trigramDictionary, unigramDictionary):    
    sentenceSplitWordArray = sentence.split()
    lengthSplitArray =  len(sentenceSplitWordArray) - 2
    counter = 0
    for index in range(lengthSplitArray):
        found = False
        middleWord = sentenceSplitWordArray[index + 1]
        trueCase = middleWord
        unigramLower = sentenceSplitWordArray[index + 1].lower()
        unigramUpper = sentenceSplitWordArray[index + 1].upper()
        unigramTitle = sentenceSplitWordArray[index + 1].title()
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



