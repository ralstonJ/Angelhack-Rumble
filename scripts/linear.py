#! /usr/bin/python2.7

import sys
import re
import nltk
from nltk.corpus import stopwords
import ast
from collections import defaultdict

def gen_with_appropriate_name():
     for n, line in enumerate(sys.stdin, 1):
        d = ast.literal_eval(line)
        items = d.values()[0].items() #all values of dictionary
        k = d.keys()[0]
        items.sort(key = lambda itm: itm[0]) #sorted values of dictionary
        yield {k: {i+1:item[1] for i,item in enumerate(items)}}
        
d = gen_with_appropriate_name()
# prime the generator

for thing in d:
    first =  str(thing.keys()[0])
    second =  thing.values()[0]
    print first + ' ' + ' '.join('{}:{}'.format(*item) for item in second.iteritems())
