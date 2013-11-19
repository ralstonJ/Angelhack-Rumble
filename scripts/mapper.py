#! /usr/bin/python

import sys, re, nltk
from nltk.corpus import stopwords
import collections 
import string

analysis = {}
wordanalysis = {}
found = True
count=0
for line in sys.stdin:
    #260097528899452929      595739778       "neutral"       Won the match #getin . P
    #tweet id	tweet_text	name	image	retweet	fav_count	verified
    #(tweetid,num,senti,tweets) = re.split("\t+",line.strip())
    (tweetid,tweets,name,image,retweet_cnt,fav_cnt,verified) = re.split("\t",line.strip())
    tweet = re.split("\s+", tweets.strip().lower())
    #adding tweet id to a dictionary
    f = open("/home/cube/research/Sentiment-Analysis-from-Social-Media/nltk/nrc_lexicons/unigrams-pmilexicon.tsv","r")
    f1 = open("/home/cube/research/Sentiment-Analysis-from-Social-Media/nltk/nrc_lexicons/bigrams-pmilexicon.tsv","r")
    sentimenthashtags = open("/home/cube/research/Sentiment-Analysis-from-Social-Media/nltk/nrc_lexicons/sentimenthashtags.tsv","r")
    stopwords = nltk.corpus.stopwords.words('english')
       
    for i in range(0, len(tweet)):
#       wordanalysis["name"] = name
#       wordanalysis["image"] = image
#       wordanalysis["retweet"] = retweet_cnt
#       wordanalysis["fav"] = fav_cnt if fav_cnt >0 else 0
#       wordanalysis["verified"] = 1 if verified is True else 0
       wordanalysis["sentimentoftweet"] = "unknwn"
       wordanalysis["word"] = tweet[i]
       wordanalysis["charcount"]= len(tweet[i])
       wordanalysis["longword"] = (len(tweet[i]) > 7)
       wordanalysis["first_uppercase"] = tweet[i].istitle()    
       wordanalysis["all_uppercase"] = tweet[i].isupper()
       wordanalysis["stop_words"] = (tweet[i].lower() in stopwords)
       wordanalysis["@"] = found if re.match("@",tweet[i]) else not(found)
       wordanalysis["#"] = found if re.match("#",tweet[i]) else not(found)
       wordanalysis["url"] = found if (re.match("http://",tweet[i])) else not(found)
       wordanalysis["!!!"] = found if (re.match("!!!",tweet[i])) else not(found)
       wordanalysis["\\?\\!"] = found if (re.match("\\?\\!",tweet[i])) else not(found)
       if re.match("#",tweet[i]):
          for wrd in sentimenthashtags:
           (term1,sentiment) = re.split("\t", wrd.strip())
           wordanalysis["sentimenthashtags"] = found if (re.match((tweet[i][1:(len(tweet[i]))]),term1.lower())) else not(found)
       
       #if words in lexicons - unigrams
       for line1 in f:
        (term2,sentimentScore,numPos,numNeg) = re.split("\t", line1.strip())    
        wordanalysis["nonzero_sscore"] = float(sentimentScore) if (float(sentimentScore) != 0) else 0
        wordanalysis["sscore>0"] = (float(sentimentScore) > 0)
        wordanalysis["sscore !=0"] = (float(sentimentScore) != 0)
#        wordanalysis["tweet_trail_unigram"] = found if re.match(tweet[(len(tweet)-1)],term2.lower()) else not(found)
 #       wordanalysis["tweet_lead_unigram"] = found  if re.match(tweet[0],term2.lower()) else not(found)

        if (term2.lower() in tweet):       
           wordanalysis["sscore"] = float(sentimentScore)
           break
        else:
           wordanalysis["sscore"] = False 

       #if words in lexicons - unigrams
       for line1 in f1:
        (term,sentimentScore,numPos,numNeg) = re.split("\t", line1.strip())
        wordanalysis["nonzero_sscore_bi"] = float(sentimentScore) if (float(sentimentScore) != 0) else 0
        wordanalysis["sscore>0_bi"] = (float(sentimentScore) > 0)
        wordanalysis["sscore !=0_bi"] = (float(sentimentScore) != 0)
#        wordanalysis["tweet_trail_unigram_bi"] = found if re.match(tweet[(len(tweet)-1)],term.lower()) else not(found)
#        wordanalysis["tweet_lead_unigram_bi"] = found  if re.match(tweet[0],term.lower()) else not(found)
       print "{",tweetid,":",wordanalysis,"}"
       
