# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 11:37:04 2018

@author: TAL-LAPTOP
"""
#import sys
import matplotlib.pyplot as plt

def extractInformation(input):
    print("extracting avg info reading file: " + input)
    synsSum = 0 
    lineNumber = 0 
    hyperPathSum = 0
    poly = []
#    hyper=[]
    with open(input, 'r') as input:
        for line in input:
            (word,synCount,minHyperPath) = line.split( )
            poly.append(synCount)
            synsSum += float(synCount)
            hyperPathSum += float(minHyperPath)
            lineNumber += 1
        input.close()
    synsAvg = float(synsSum / lineNumber)
    hyperPathAvg = float(hyperPathSum/ lineNumber)
    print ("Avg number of syns: " + str(synsAvg))
    print ("Avg length of hypernim path: " + str(hyperPathAvg))
    n, bins, patches = plt.hist(poly,15, facecolor='blue', alpha=0.5)
    
    plt.plot(bins)
    plt.pyplot.show
    
    
#inputFile = sys.argv[1]
#extractInformation('freqNormNonNativeToeflOut.txt')
extractInformation('freqNormNonNativeToeflOut.txt')
