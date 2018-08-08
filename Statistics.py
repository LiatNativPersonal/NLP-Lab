import sys
import numpy as np
from scipy import stats
import random

native_first_file = sys.argv[1]
nonNative_file = sys.argv[2]
statistics_ttest_file = sys.argv[3]
statistics_wilcoxon_file = sys.argv[4]

nativeFile = open(native_first_file,"r")
nonNativeFile = open(nonNative_file,"r")
statisticsTtestOutputFile = open(statistics_ttest_file,"w+")
statisticsWilcoxonOutputFile = open(statistics_wilcoxon_file,"w+")

nativeLineArray = []
nonNativeLineArray = []
lexicalFeatureNativeArray = []
lexicalFeatureNonNativeArray = []
lexicalFeatureNativeArrayTemp = []
lexicalFeatureNonNativeArrayTemp = []


blockSize = 1500
numOfStatististicsTests = 50
numOfBlocks = 300

# NATIVE
for line in nativeFile:
    nativeLineArray.append(line)
    
for line in nativeLineArray:
    (word, pos, lexicalFeature) = line.split( )
    lexicalFeatureNativeArray.append(float(lexicalFeature))
    
    
    
# NON NATIVE    
for line in nonNativeFile:
    nonNativeLineArray.append(line)
    
for line in nonNativeLineArray:
    (word, pos, lexicalFeature) = line.split( )
    lexicalFeatureNonNativeArray.append(float(lexicalFeature))

          
# STATISTICS
i = 0
lexicalFeatureNativeAverageArray = []
lexicalFeatureNonNativeAverageArray = []

for j in range(numOfStatististicsTests):
    size = blockSize * numOfBlocks
#    with  open('temp.txt', 'w') as tempOutput:
    lexicalFeatureNativeRandArray = random.sample(lexicalFeatureNativeArray, size)    
#        tempOutput.write("+++++++ Native ++++++++++\n")
#        tempOutput.write(str(lexicalFeatureNativeRandArray ))
#        tempOutput.write('\n\n')
    lexicalFeatureNonNativeRandArray = random.sample(lexicalFeatureNonNativeArray, size) 
#        tempOutput.write("+++++++ Non-Native ++++++++++\n")
#        tempOutput.write(str(lexicalFeatureNonNativeRandArray))
#    tempOutput.close()
    for i in range(numOfBlocks):    
        
        lexicalFeatureNativeArrayTemp = lexicalFeatureNativeRandArray[i * blockSize : (i + 1) * blockSize]
#        print(cynsNativeArrayTemp)
        lexicalFeatureNativeAverage = np.mean(lexicalFeatureNativeArrayTemp)
        lexicalFeatureNativeAverageArray.append(lexicalFeatureNativeAverage)
        
        lexicalFeatureNonNativeArrayTemp = lexicalFeatureNonNativeRandArray[i * blockSize : (i + 1) * blockSize]
        lexicalFeatureNonNativeAverage = np.mean(lexicalFeatureNonNativeArrayTemp)
        lexicalFeatureNonNativeAverageArray.append(lexicalFeatureNonNativeAverage)
        
        del lexicalFeatureNativeArrayTemp[:]
        del lexicalFeatureNonNativeArrayTemp[:]
        
    i = 0    
    [ttestLexicalFeatureStatistics, ttestLexicalFeaturePvalue] = stats.ttest_ind(lexicalFeatureNativeAverageArray, lexicalFeatureNonNativeAverageArray)
   

#    print("Native")
    statisticsTtestOutputFile.write(str(round(ttestLexicalFeatureStatistics,6)) + ", " + str(round(ttestLexicalFeaturePvalue,6)) +  "\n")
    
    [wilcoxLexicalFeatureStatistics, wilcoxLexicalFeaturePvalue] = stats.ranksums(lexicalFeatureNativeAverageArray, lexicalFeatureNonNativeAverageArray)
       
    statisticsWilcoxonOutputFile.write(str(round(wilcoxLexicalFeatureStatistics,6)) + ", " + str(round(wilcoxLexicalFeaturePvalue,6)) +  "\n")
    
    del lexicalFeatureNativeAverageArray[:]
    del lexicalFeatureNonNativeAverageArray[:]
       
    
statisticsTtestOutputFile.close()
statisticsWilcoxonOutputFile.close()
nativeFile.close()
nonNativeFile.close()
    
    
    
    


