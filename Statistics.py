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
statisticsTtestOutputFile = open(statistics_ttest_file,"w")
statisticsWilcoxonOutputFile = open(statistics_wilcoxon_file,"w")

nativeLineArray = []
nonNativeLineArray = []
cynsNativeArray = []
cynsNonNativeArray = []
minHyperPathNativeArray = []
minHyperPathNonNativeArray = []
cynsNativeArrayTemp = []
cynsNonNativeArrayTemp = []
minHyperPathNativeArrayTemp = []
minHyperPathNonNativeArrayTemp = []

blockSize = 2000
numOfStatististicsTests = 50
numOfBlocks = 500

# NATIVE
for line in nativeFile:
    nativeLineArray.append(line)
    
for line in nativeLineArray:
    (word,cynsCount,minHyperPath) = line.split( )
    cynsNativeArray.append(float(cynsCount))
    minHyperPathNativeArray.append(float(minHyperPath))
    
    
# NON NATIVE    
for line in nonNativeFile:
    nonNativeLineArray.append(line)
    
for line in nonNativeLineArray:
    (word, cynsCount, minHyperPath) = line.split( )
    cynsNonNativeArray.append(float(cynsCount))
    minHyperPathNonNativeArray.append(float(minHyperPath))
          
# STATISTICS
i = 0
cynsNativeAverageArray = []
cynsNonNativeAverageArray = []
minHyperpathNativeAverageArray = []
minHyperpathNonNativeAverageArray = []

for j in range(numOfStatististicsTests):
    size = blockSize * numOfBlocks
    cynsNativeRandArray = random.sample(cynsNativeArray, size)
    minHyperPathNativeRandArray = random.sample(minHyperPathNativeArray, size)
    cynsNonNativeRandArray = random.sample(cynsNonNativeArray, size)
    minHyperPathNonNativeRandArray = random.sample(minHyperPathNonNativeArray, size)
    for i in range(numOfBlocks):    
        
        cynsNativeArrayTemp = cynsNativeRandArray[i * blockSize : (i + 1) * blockSize]
        print(cynsNativeArrayTemp)
        cynsNativeAverage = np.mean(cynsNativeArrayTemp)
        cynsNativeAverageArray.append(cynsNativeAverage)
        minHyperPathNativeArrayTemp = minHyperPathNativeRandArray[i * blockSize : (i + 1) * blockSize]
        minHyperpathNativeAverage = np.mean(minHyperPathNativeArrayTemp)
        minHyperpathNativeAverageArray.append(minHyperpathNativeAverage)
        cynsNonNativeArrayTemp = cynsNonNativeRandArray[i * blockSize : (i + 1) * blockSize]
        cynsNonNativeAverage = np.mean(cynsNonNativeArrayTemp)
        cynsNonNativeAverageArray.append(cynsNonNativeAverage)
        minHyperPathNonNativeArrayTemp = minHyperPathNonNativeRandArray[i * blockSize : (i + 1) * blockSize]
        minHyperpathNonNativeAverage = np.mean(minHyperPathNonNativeArrayTemp)
        minHyperpathNonNativeAverageArray.append(minHyperpathNonNativeAverage)
        del cynsNativeArrayTemp[:]
        del minHyperPathNativeArrayTemp[:]
        del cynsNonNativeArrayTemp[:]
        del minHyperPathNonNativeArrayTemp[:]
    i = 0    
    [ttestCynsStatistics, ttestCynsPvalue] = stats.ttest_ind(cynsNonNativeAverageArray, cynsNativeAverageArray)
    [ttestMinStatistics, ttestMinPvalue] = stats.ttest_ind(minHyperpathNonNativeAverageArray, minHyperpathNativeAverageArray)

    print("Native")
    statisticsTtestOutputFile.write(str(ttestCynsStatistics) + " " + str(ttestCynsPvalue) + " " + str(ttestMinStatistics) + " " + str(ttestMinPvalue) + "\n")
    
    [wilcoxCynsStatistics, wilcoxCynsPvalue] = stats.ranksums(cynsNativeAverageArray, cynsNonNativeAverageArray)
    [wilcoxMinStatistics, wilcoxMinPvalue] = stats.ranksums(minHyperpathNativeAverageArray, minHyperpathNonNativeAverageArray)
    
    statisticsWilcoxonOutputFile.write(str(wilcoxCynsStatistics) + " " + str(wilcoxCynsPvalue) + " " + str(wilcoxMinStatistics) + " " + str(wilcoxMinPvalue) + "\n")
    
    del cynsNativeAverageArray[:]
    del cynsNonNativeAverageArray[:]
    del minHyperpathNativeAverageArray[:]
    del minHyperpathNonNativeAverageArray[:]
    
    
statisticsTtestOutputFile.close()
statisticsWilcoxonOutputFile.close()
nativeFile.close()
nonNativeFile.close()
    
    
    
    


