# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 11:20:40 2018

@author: TAL-LAPTOP
"""
import random
import nltk
from nltk.corpus import wordnet as wn

arr = ["liat", "lilach", "moran", "gilad", "hofit", "dolev", "loay"]
arr2 = ["dd", "ccc", "ddd"]
word = nltk.stem.WordNetLemmatizer().lemmatize('dogs','n')
print(word)

#for syn in(wn.synsets('pretty','r')):
#    print(syn)
#    for path in syn.hypernym_paths():
#        print(path)
#        print (len(path))
   
    
#lemma = nltk.stem.WordNetLemmatizer().lemmatize('pretty','r')
total_senses = 0
#    print (str(total_senses))
#    if not total_senses.isdigit():
#        total_senses = 0
counter = 0    
for syn in(wn.synsets('mayonnaise', 'n')):
    max_path = 0
    for path in syn.hypernym_paths():
        print(path)
        if len(path) > max_path :
            max_path = len(path)
    total_senses += max_path
    counter += 1
print( round(total_senses/counter)  )


#print(len(wn.synsets('pretty','r')))
#print(len((wn.synset('pretty' + '.r.01')).hypernym_paths()))
#pretty = wn.synset('own.v.01')
#print(pretty)
#print(pretty.hypernym_paths())
##print(max(len(wn.synsets('pretty','r').hypernym_paths())))
#print(wn.ADV)
#arr2 += random.sample(arr, 3)
#print (arr2)
#arr = arr2
#print(arr)
#print (len(arr))
#print (len(arr2))
#nltk.help.upenn_tagset()
#total_senses = 0
#counter = 0
#print(nltk.pos_tag(nltk.word_tokenize("can do")))
#print (wn.synset('also.r.01'))
#print (wn.synsets('dog','n'))
#for syn in(wn.synsets('also')):
#    if 'also' in str(syn):
#        print(syn)
#        print ([len(path)for path in syn.hypernym_paths()])
#        total_senses += (min([len(path)  for path in syn.hypernym_paths()]))
#        counter += 1
#        print ("avarage senses number is " + str(total_senses/counter))
#    else:
#        print("no synsets")

