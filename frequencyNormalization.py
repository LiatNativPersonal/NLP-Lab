# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 10:10:35 2018

@author: Lilach Naim & Liat Nativ
"""
from math import log
frequencyDB = "c:/Users/TAL-LAPTOP/Desktop/NLP Lab/code/reddit_word_freq_orig_case.txt"

def normalizeByFrequecny(wordnetResulsFile, normalizedWordnetResultsFile):
    frequencyDict = {}
    ranksDict = {}
    frequencyDict = createSortedFrequencyDictionary()
    ranksDict = createRankDict(frequencyDict)
#    for key, value in frequencyDict.items():
#        print (str(key) + "," + str(value))   
#    print ("######################")
#    for key, value in ranksDict.items():
#        print (key, value)
    print ("########1########")
    i = 0
   
    with open(normalizedWordnetResultsFile, 'w+') as output:
         print ("########2########")
         with open(wordnetResulsFile, 'r') as input:
            print ("########3########")
#            data = tuple(ast.literal_eval(line) for line in input)
            print ("########4########")
            for line in input:
                tupple = line.split()
                if i > 500:
                    break
                if len(tupple) != 3 :
                    continue
                if str(tupple[1]) == '0' and str(tupple[2]) == '0':
                    continue
                i += 1
                if (tupple[0] in frequencyDict.keys()):
                    print (str(tupple[1]) +"," + str(frequencyDict[tupple[0]]))
                    normalizedResult = float(tupple[1]) / log(float(frequencyDict[tupple[0]]))
                    strnorm = "%.3f" % normalizedResult
                    output.write(tupple[0]+ " " + strnorm + '\n')
            input.close()
            output.close()
#                    elif (tupple[0].lower() in frequencyDict.keys()):
#                        normalizedResult = tupple[1] / frequencyDict[tupple[0].lower()]
#                        output.write(tupple[0 + " " + ])
#                    elif (tupple[0].upper() in frequencyDict.keys()):
#                        normalizedResult = tupple[1] / frequencyDict[tupple[0].upper()]
#                        output.write(tupple[0 + " " + ])
#                    elif (tupple[0].title() in frequencyDict.keys()):
#                        normalizedResult = tupple[1] / frequencyDict[tupple[0].title()]
#                        output.write(tupple[0 + " " + ])
        
        
#    i=0
#    rankedList=[]
#    for value in sorted(frequencyDict.values()):
#        print(value)
#        if value in frequencyDict.keys():
#            rankedList[i] = frequencyDict[value]
#            i=i+1
#            
#    ranksDict = createRankDict(rankedList)
#    for key, value in ranksDict.items():
#        print (str(key) + "," + str(value))
    
    return

def createSortedFrequencyDictionary():
    frequencyDict = {}
    ctr = 0
    with open(frequencyDB, 'r', encoding = "utf8",  errors="ignore") as freqFile:          
        for line in freqFile:            
            try:
                (counter, word) = line.split()
                key = word  
                if not word.isalpha():
                    continue
                frequencyDict[key] = int(counter)                
                if ctr > 500:
                    break
                ctr = ctr + 1
            except:
                continue;
        freqFile.close()        
        return frequencyDict      
    
def createRankDict(frequencyDict):
    rankedDict={}
    i = 0
    for w in sorted(frequencyDict, key=frequencyDict.get, reverse=True):
        rankedDict[i]=w
        i += 1
    return rankedDict
    
    
#normalizeByFrequecny('wnNonNative.txt', 'wnNormalizedByFreqNonNative.txt')