# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 12:34:50 2018

@author: TAL-LAPTOP

"""
from nltk.corpus import wordnet as wn
import nltk
import matplotlib
import numpy as np
expr = 'student.n.02'

#ss = wn.synset(expr)
#print (min([len(path) for path in ss.hypernym_paths()]))
#print(nltk.stem.WordNetLemmatizer().lemmatize('Students','n'))
print(len(wn.synsets('mammal', 'n')))
#x=[1, 2, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 8, 8, 9]
#matplotlib.pyplot.hist(x)
#print (wn.ADJ)
#population = [1, 3, 4, 5, 6, 8 ,5, 6 ,7, 8, 9, 3, 2, 1, 3, 4, 5, 6]
#print(np.random.choice(population, 5, False))
#print(np.random.choice(population, 5))
#print(np.random.choice(population, 5,False))
#print(np.random.choice(population, 5))