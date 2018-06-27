import sys

bigrams_first_file = sys.argv[1]
bigrams_second_file = sys.argv[2]
trigrams_file = sys.argv[3]
unigramOutputFileName = sys.argv[4]

biGramsFirstFile = open(bigrams_first_file,"r")
biGramsSecondFile = open(bigrams_second_file,"r")
triGramsFile = open(trigrams_file,"r")
unigramOutputFile = open(unigramOutputFileName,"w", encoding="utf-8")

def createTrigramDictionary(triGramsFile):
    trigramDict = {}
    
    for line in triGramsFile:
        (counter, trigram1, trigram2, trigram3) = line.split()
        key = trigram2 
        if key in trigramDict.keys():
            if int(counter) > trigramDict[key]:
                trigramDict[key] = int(counter)
        else:
            trigramDict[key] = int(counter)
    return trigramDict  

def createFirstBigramDictionary(biGramsFirstFile):
    bigramDict = {}
    
    for line in biGramsFirstFile:
        (counter, bigram1, bigram2) = line.split()
        key = bigram1 
        if key in bigramDict.keys():
            if int(counter) > bigramDict[key]:
                 bigramDict[key] = int(counter)
        else:
            bigramDict[key] = int(counter)
    return bigramDict

def createSecondBigramDictionary(biGramsSecondFile):
    bigramDict = {}
    
    for line in biGramsSecondFile:
        (counter, bigram1, bigram2) = line.split()
        key = bigram2
        if key in bigramDict.keys():
             if int(counter) > bigramDict[key]:
                 bigramDict[key] = int(counter)
        else:
            bigramDict[key] = int(counter)
    return bigramDict

def mergeDictonaries(dict1, dict2):
    dict3 = {}
    s1 = set(dict1)
    s2 = set(dict2)
    for i in s1-s2:
        dict3[i] = dict1[i]
    for i in s2-s1:
        dict3[i] = dict2[i]
    for i in s1.intersection(s2):
        dict3[i] = dict1[i] if dict1[i] >= dict2[i] else dict2[i]
    return dict3

unigramArray = []
 
firstBigramDictionary = createFirstBigramDictionary(biGramsFirstFile)
secondBigramDictionary = createSecondBigramDictionary(biGramsSecondFile)
thigramDictionary = createTrigramDictionary(triGramsFile)
bigramDictionary = mergeDictonaries(firstBigramDictionary, secondBigramDictionary)
unigramDictionary = mergeDictonaries(bigramDictionary, thigramDictionary)
for key in unigramDictionary:
    line = str(unigramDictionary[key]) + " " + key + "\n"
    unigramArray.append(line)

for str in unigramArray:
    unigramOutputFile.write(str)        
unigramOutputFile.close()
biGramsFirstFile.close()
biGramsSecondFile.close()
triGramsFile.close()

