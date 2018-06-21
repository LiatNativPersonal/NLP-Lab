import sys
import os
import numpy as np

#non_native_directory_path = sys.argv[1]
#native_directory_path = sys.argv[2]
#two_grams_file = sys.argv[3]
#three_grams_file = sys.argv[4]
#nonNativeOutputFileName = sys.argv[5]
#nativeOutputFileName = sys.argv[6]

def correctCase(trigrams_file, native_directory_path, non_native_directory_path, nonNativeOutputFileName, nativeOutputFileName):
    trigramsDB = open(trigrams_file,"r")
    trigramDictionary = createTrigramDictionary(trigramsDB)
    nonNativeOutputFile = open(nonNativeOutputFileName,"w", encoding="utf-8")
    nativeOutputFile = open(nativeOutputFileName,"w", encoding="utf-8")
    nonNativeSentenceArray = []
    nonNativeNewSentenceArray = []
    nativeSentenceArray = []
    nativeNewSentenceArray = []
   
    
    counter = 0
    nativeFileList = os.listdir(native_directory_path)
    nonNativeFileList = os.listdir(non_native_directory_path)
    # NON NATIVE
    for file in nonNativeFileList:       
        nonNativeFile = open(non_native_directory_path + "\\" + file,"r", encoding = "utf8",  errors="ignore")
        print("Running file " + str(file))
        counter = counter + 1
        nonNativeSentenceArray = createSentencesArray(nonNativeFile)
        nonNativeFile.close()
        
    counter = 1
    for sentence in nonNativeSentenceArray:
        #print(counter)
        sentence = removeBrackets(sentence)
        sentence = handleTitle(sentence)
        sentence = handleUpperLowerCase(sentence, trigramDictionary)
        counter = counter + 1
        nonNativeNewSentenceArray.append(sentence)
        
    for sentence in nonNativeNewSentenceArray:
        nonNativeOutputFile.write(sentence + "\n")     
    nonNativeOutputFile.close()
    
  

        
    # NATIVE:
    #for file in nativeFileList:
    #    nativeFile = open(native_directory_path + "\\" + file,"r", encoding = "utf8")
    #    for line in nativeFile:
    #        nativeSentenceArray.append(line)
    #    np.random.shuffle(nativeSentenceArray)
    #    arrayLength = len(nativeSentenceArray) 
    #    maxLength = 500000
    #    if arrayLength > maxLength:
    #        nativeSentenceShortArray = nativeSentenceArray[:maxLength]
    #    else:
    #        nativeSentenceShortArray = nativeSentenceArray
    #    nativeFile.close()
    #
    #counter = 1
    #for sentence in nativeSentenceShortArray:
    #    sentence = removeBrackets(sentence)
    #    print(counter)
    #    sentence = handleTitle(sentence)
    #    counter = counter + 1
    #    #sentence = handleUpperLowerCase(sentence)
    #    nativeNewSentenceArray.append(sentence)
    #    
    #for sentence in nativeNewSentenceArray:
    #    nativeOutputFile.write(sentence)     
    #nativeOutputFile.close()
    #
    #for index in range(5):
    #    np.random.shuffle(nonNativeNewSentenceArray)
    #    np.random.shuffle(nativeNewSentenceArray)
    
  
    trigramsDB.close()

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
         key =trigram1 + ' ' + trigram2 + ' ' + trigram3           
         trigramDict[key] = int(counter)
    return trigramDict         




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

def handleUpperLowerCase(sentence, trigramDictionary):    
    sentenceSplitWordArray = sentence.split()
    lengthSplitArray =  len(sentenceSplitWordArray) - 2
#    print(sentence)
    counter = 0
    for index in range(lengthSplitArray):
        found = False
        middleWord = sentenceSplitWordArray[index + 1]
        trueCase=middleWord
        trigramLower = sentenceSplitWordArray[index] + " " + sentenceSplitWordArray[index + 1].lower() + " " + sentenceSplitWordArray[index + 2]
        trigramUpper = sentenceSplitWordArray[index] + " " + sentenceSplitWordArray[index + 1].upper() + " " + sentenceSplitWordArray[index + 2]
        trigramTitle = sentenceSplitWordArray[index] + " " + sentenceSplitWordArray[index + 1].title() + " " + sentenceSplitWordArray[index + 2]
        print (trigramLower)
        print (trigramUpper)
        print (trigramTitle)
        if trigramLower in trigramDictionary.keys():
            counter= trigramDictionary[trigramLower]    
            trueCase=middleWord.lower()
            found = True           
        if trigramUpper in trigramDictionary.keys():           
           if counter < trigramDictionary[trigramUpper]:            
              trueCase = middleWord.upper()
              counter=trigramDictionary[trigramUpper]              
           found = True
        if trigramTitle in trigramDictionary.keys():  
           if counter < trigramDictionary[trigramTitle]:
               trueCase=middleWord.title()               
           found=True
           
        if found:
            print("TrueCase = " + trueCase + "counter = " + str(counter))
            sentenceSplitWordArray[index+1] = trueCase
#        else: # could not find trigram - fall back to unigram        
#     
#            
#            for key,value in trigramDictionary.items(): 
#      
#                gramsSplitArray = key.split()
#                gramsStr = gramsSplitArray[2]
#                currMaxValue = int(gramsSplitArray[0])
#                print(oneWordStr)
#                print(gramsStr)
#                if oneWordStr.lower() == gramsStr.lower():
#                    flag = 1
#                    if currMaxValue > maxValue:
#                        maxValue = currMaxValue
#                        upperLowerCase = gramsSplitArray[2]
#                        sentenceSplitWordArray[index+1] = upperLowerCase
#                elif flag == 1:
#                    break
#            
                
    sentence = " ".join(sentenceSplitWordArray)
    return sentence



