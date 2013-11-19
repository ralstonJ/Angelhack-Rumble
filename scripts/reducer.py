#! /usr/bin/python2.7

import sys
import re
import nltk
from nltk.corpus import stopwords
import ast
from collections import defaultdict

dicts = {}
inner_dict = {}
count =0
def analyze_tweets():
 
   for line in sys.stdin:
       d = ast.literal_eval(line)
       for k,v in d.items():
          inner_dict = dicts.setdefault(k, {})
          inner_dict['longword'] = inner_dict.get('longword', 0) + v.get('longword', 0)
          inner_dict['charcount'] = inner_dict.get('charcount', 0) + v.get('charcount', 0)
          inner_dict['first_uppercase'] = inner_dict.get('first_uppercase', 0) + v.get('first_uppercase', 0)
          inner_dict['all_uppercase'] = inner_dict.get('all_uppercase', 0) + v.get('all_uppercase', 0)
          inner_dict['stop_words'] = inner_dict.get('stop_words', 0) + v.get('stop_words', 0)	
          inner_dict['@'] = inner_dict.get('@', 0) + v.get('@', 0)	
          inner_dict['#'] = inner_dict.get('#', 0) + v.get('#', 0)
	  inner_dict['sentimenthashtags'] = inner_dict.get('sentimenthashtags', 0) + v.get('sentimenthashtags', 0) 
          inner_dict['url'] = inner_dict.get('url', 0) + v.get('url', 0)
          inner_dict['!!!'] = inner_dict.get('!!!', 0) + v.get('!!!', 0)
          inner_dict['sscore'] = inner_dict.get('sscore', 0) + v.get('sscore', 0)
          inner_dict['\\?\\!'] = inner_dict.get('\\?\\!', 0) + v.get('\\?\\!', 0)
          inner_dict['sscore>0'] = inner_dict.get('sscore>0', 0) + v.get('sscore>0', 0)
          inner_dict['sscore !=0'] = inner_dict.get('sscore !=0', 0) + v.get('sscore !=0', 0)
          inner_dict['nonzero_sscore'] = inner_dict.get('nonzero_sscore', 0) + v.get('nonzero_sscore', 0)
          inner_dict['nonzero_sscore_bi'] = inner_dict.get('nonzero_sscore_bi', 0) + v.get('nonzero_sscore_bi', 0)
          inner_dict['sscore>0_bi'] = inner_dict.get('sscore>0_bi', 0) + v.get('sscore>0_bi', 0)
          inner_dict['sscore !=0_bi'] = inner_dict.get('sscore !=0_bi', 0) + v.get('sscore !=0_bi', 0)
          inner_dict['sentimentoftweet'] = v.get('sentimentoftweet')
#          inner_dict['retweet'] = v.get('retweet')
#          inner_dict['fav_cnt'] = v.get('fav')
#          inner_dict['verified'] = v.get('verified') 

   fdic = open("/home/cube/rumble/data/tweets_api_id_linear","w")
   for key, value in dicts.items():       
      fdic.write('{'+str(key)+':'+str(value)+'}\n')
      if dicts[key]['sentimentoftweet'] == 'positive':
         del dicts[key]['sentimentoftweet']
         print {'+1': dicts[key]}
      elif dicts[key]['sentimentoftweet'] == 'negative':
         del dicts[key]['sentimentoftweet']
         print {'-1': dicts[key]}
      elif dicts[key]['sentimentoftweet'] == 'neutral':
         del dicts[key]['sentimentoftweet']
         print {'0': dicts[key]}
      elif dicts[key]['sentimentoftweet'] == 'unknwn':
         del dicts[key]['sentimentoftweet']
         print {'2': dicts[key]}
 
   fdic.close()
if __name__ == "__main__":

   analyze_tweets()
