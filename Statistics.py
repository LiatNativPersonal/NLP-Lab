import sys
import numpy as np
from scipy import stats
import math

native_first_file = sys.argv[1]
nonNative_file = sys.argv[2]

nativeFile = open(native_first_file,"r")
nonNativeFile = open(nonNative_file,"r")

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



# NATIVE
for line in nativeFile:
    nativeLineArray.append(line)
    
for line in nativeLineArray:
    try:
        (word,cynsCount,minHyperPath) = line.split( )
        cynsNativeArray.append(int(cynsCount))
        minHyperPathNativeArray.append(int(minHyperPath))
    except:
        continue
    
# NON NATIVE    
for line in nonNativeFile:
    nonNativeLineArray.append(line)
    
for line in nonNativeLineArray:
    try:
        (word, cynsCount, minHyperPath) = line.split( )
        cynsNonNativeArray.append(int(cynsCount))
        minHyperPathNonNativeArray.append(int(minHyperPath))
    except:
        continue
    
maxLength = min(len(nativeLineArray), len(nonNativeLineArray))
    
np.random.shuffle(cynsNativeArray)
np.random.shuffle(minHyperPath)
np.random.shuffle(cynsNonNativeArray)
np.random.shuffle(minHyperPathNonNativeArray)
      
# STATISTICS
i = 0
cynsNativeAverageArray = []
cynsNonNativeAverageArray = []
minHyperpathNativeAverageArray = []
minHyperpathNonNativeAverageArray = []

numOfBlocks = math.floor(maxLength/blockSize)
for j in range(numOfStatististicsTests):
    for i in range(numOfBlocks):    
        
        cynsNativeArrayTemp = cynsNativeArray[i * blockSize : (i + 1) * blockSize]
        cynsNativeAverage = np.mean(cynsNativeArrayTemp)
        cynsNativeAverageArray.append(cynsNativeAverage)
        minHyperPathNativeArrayTemp = minHyperPathNativeArray[i * blockSize : (i + 1) * blockSize]
        minHyperpathNativeAverage = np.mean(minHyperPathNativeArrayTemp)
        minHyperpathNativeAverageArray.append(minHyperpathNativeAverage)
        cynsNonNativeArrayTemp = cynsNonNativeArray[i * blockSize : (i + 1) * blockSize]
        cynsNonNativeAverage = np.mean(cynsNonNativeArrayTemp)
        cynsNonNativeAverageArray.append(cynsNonNativeAverage)
        minHyperPathNonNativeArrayTemp = minHyperPathNonNativeArray[i * blockSize : (i + 1) * blockSize]
        minHyperpathNonNativeAverage = np.mean(minHyperPathNonNativeArrayTemp)
        minHyperpathNonNativeAverageArray.append(minHyperpathNonNativeAverage)
        
    [cynsStatistics, cynsPvalue] = stats.ttest_ind(cynsNativeAverageArray, cynsNonNativeAverageArray)
    [minStatistics, minPvalue] = stats.ttest_ind(minHyperpathNativeAverageArray, minHyperpathNonNativeAverageArray)
    
    print("T-Test")
    print(cynsStatistics, cynsPvalue)
    print(minStatistics, minPvalue)
    
    [cynsStatistics, cynsPvalue] = stats.wilcoxon(cynsNativeAverageArray, cynsNonNativeAverageArray)
    [minStatistics, minPvalue] = stats.wilcoxon(minHyperpathNativeAverageArray, minHyperpathNonNativeAverageArray)
    
    print("Wilcox")
    print(cynsStatistics, cynsPvalue)
    print(minStatistics, minPvalue)
    
    
    


