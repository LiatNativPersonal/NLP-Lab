# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 10:10:35 2018

@author: Lilach Naim & Liat Nativ
"""
from math import log, floor
import os
#polyFrequencyDB = "c:/Users/TAL-LAPTOP/Desktop/NLP Lab/frequencyCalculation/outputs/polyFreqRank.txt"
#hyperFrequencyDB = "c:/Users/TAL-LAPTOP/Desktop/NLP Lab/frequencyCalculation/outputs/HyperFreqRank.txt"

def splitToFrequencyBins(wordnetResulsFile, frequencyDB, binsNumber):
    binsDict = {}
    rankDict={}
    for i in range( binsNumber+1):
        binsDict[i] = []    
    with open(frequencyDB, 'r', encoding = "utf8",  errors="ignore") as freqFile:  
        print('frequency is stored in file ' + frequencyDB)        
        for line in freqFile:            
            (strrank, taggedToken) = line.split()
            rank = int(strrank)
            rankDict[taggedToken] = rank
    freqFile.close()    
            
    with open(wordnetResulsFile, 'r') as inputFile:
        print('Processing wordnet query results stored in file ' + wordnetResulsFile)
        for line in inputFile:
            (word, pos, value) = line.split()                                
            for i in range(1, binsNumber):
                key = word +','+ pos
                if key in rankDict.keys():
                    index = floor(log(rankDict[key],10))
                    if index >= binsNumber:
                        binsDict[binsNumber].append(line)
                    else:
                        binsDict[index].append(line)
                        
    inputFile.close()
        
    for bin,lines in binsDict.items():
        filename = 'bin' + str(bin) + wordnetResulsFile
        with open(filename, 'w', encoding = "utf8") as output:
            for line in lines:            
                output.write(line)
        output.close()
                
           
                
                    

def normalizeByFrequecny(wordnetResulsFile, normalizedWordnetResultsFile):
    if os.path.exists(normalizedWordnetResultsFile):
        print("normalization phase skipped")
        return
    print("Start normalizing wordNet results by frequency, writing results to " + normalizedWordnetResultsFile)
    frequencyDict = {}
    frequencyDict = createSortedFrequencyDictionary()    
    err_count=0
    with open(normalizedWordnetResultsFile, 'w+') as output:         
         with open(wordnetResulsFile, 'r') as input:
            for line in input:
                tupple = line.split()                
                if len(tupple) != 3 :
                    err_count += 1
                    continue
                if str(tupple[1]) == '0' and str(tupple[2]) == '0':
                    err_count += 1
                    continue                
                normalizedResult = 0
                epsilon = 0.00001
                frequency = 0
                if (tupple[0].lower() in frequencyDict.keys()):
                        frequency = frequencyDict[tupple[0].lower()]
                if (tupple[0].upper() in frequencyDict.keys()):
                        frequency += frequencyDict[tupple[0].upper()]
                elif (tupple[0].title() in frequencyDict.keys()):
                        frequency += frequencyDict[tupple[0].title()]
                if frequency == 0:
                    err_count += 1
                    continue
                normalizedResult = float(tupple[1]) / float(log(frequency+epsilon))
                strnorm = "%.3f" % normalizedResult
                output.write(tupple[0]+ " " + strnorm +" " + tupple[2]+'\n')                
            input.close()
            output.close()
            print ("numeber of wrong lines: " + str(err_count))
    return

def normalizeByRank(wordnetResulsFile, normalizedWordnetResultsFile):
    if os.path.exists(normalizedWordnetResultsFile):
        print("normalization phase skipped")
        return
    print("Start normalizing wordNet results by ranks, writing results to " + normalizedWordnetResultsFile)
    frequencyDict = {}
    frequencyDict = createSortedFrequencyDictionary()
    ranksDict = {}
    ranksDict = createRankDict(frequencyDict)
    err_count=0
    with open(normalizedWordnetResultsFile, 'w+') as output:         
         with open(wordnetResulsFile, 'r') as input:
            for line in input:
                tupple = line.split()                
                if len(tupple) != 3 :
                    err_count += 1
                    continue
                if str(tupple[1]) == '0' and str(tupple[2]) == '0':
                    err_count += 1
                    continue                
                normalizedResult = ""
                epsilon = 0.00001
                if (tupple[0] in ranksDict.keys()):
                    normalizedResult = float(tupple[1]) / log(float(ranksDict[tupple[0]])+epsilon)                    
                elif (tupple[0].lower() in ranksDict.keys()):
                        normalizedResult = float(tupple[1]) / log(float(ranksDict[tupple[0].lower()])+epsilon)                        
                elif (tupple[0].upper() in ranksDict.keys()):
                        normalizedResult = float(tupple[1]) / log(float(ranksDict[tupple[0].upper()])+epsilon)                        
                elif (tupple[0].title() in ranksDict.keys()):
                        normalizedResult = float(tupple[1]) / log(float(ranksDict[tupple[0].title()])+epsilon)
                if normalizedResult == "":
                    err_count += 1
                    continue
                strnorm = "%.3f" % normalizedResult
                output.write(tupple[0]+ " " + strnorm +" " + tupple[2]+'\n')                 
            input.close()
            output.close()
            print ("numeber of wrong lines: " + str(err_count))
    return
def createSortedFrequencyDictionary():
    frequencyDict = {}
#    ctr = 0
    with open(polyFrequencyDB, 'r', encoding = "utf8",  errors="ignore") as freqFile:          
        for line in freqFile:            
            try:
                (counter, word) = line.split()
                key = word  
                if not word.isalpha():
                    continue
                frequencyDict[key] = int(counter)                
#                if ctr > 500:
#                    break
#                ctr = ctr + 1
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