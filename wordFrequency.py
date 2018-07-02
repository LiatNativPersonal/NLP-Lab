import sys
import os

non_native_directory_path = sys.argv[1]
native_directory_path = sys.argv[2]
OutputFileName = sys.argv[3]

OutputFile = open(OutputFileName,"w", encoding="utf-8")
nativeFileList = os.listdir(native_directory_path)
nonNativeFileList = os.listdir(non_native_directory_path)
sentenceArray = []
wordArray = []
wordFreqDictionary = {}

for file in nonNativeFileList:
    nonNativeFile = open(non_native_directory_path + "\\" + file, "r", encoding = "utf8",  errors = "ignore")  
    print("Running file " + str(file))
    for line in nonNativeFile:
        sentenceArray.append(line)

        
for file in nativeFileList:      
    nativeFile = open(native_directory_path + "\\" + file, "r", encoding = "utf8",  errors = "ignore")
    print("Running file " + str(file))
    for line in nativeFile:
        sentenceArray.append(line)
        
counter = 1        
for sentence in sentenceArray:
    wordsArray = sentence.split( )
    for word in wordsArray:
        if not word.isalpha():
            continue
        key = word
        if key in wordFreqDictionary.keys():
            wordFreqDictionary[key] = wordFreqDictionary[key] + 1
        else:
           wordFreqDictionary[key] = counter 
            
wordFreqArray = []
for key in wordFreqDictionary:
    line = str(wordFreqDictionary[key]) + " " + key + "\n"
    wordFreqArray.append(line)

for str in wordFreqArray:
    OutputFile.write(str) 
OutputFile.close() 
