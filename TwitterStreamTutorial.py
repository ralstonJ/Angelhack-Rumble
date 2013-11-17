#!/usr/bin/env python

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = 'CiQGfooRBKJRSrtaGl7GkQ'
csecret = 'G2o2pVeFaYlZdZAQL6NxkE3x7iW0U7kfoUKBTaOg'
atoken = '741285805-38CJ8saoV8UJx46L38bFiZMOSocC2XhtubOsot9x'
asecret = 'sNJUHNg4GzZDnIR82BeCkQK0ptgrOWsimO265BhB1YCtq'

class listener(StreamListener):

   def on_data(self, data):
      try:
         #tweet = data.split(',"text":"')[4].split('","source')[0]
         print data
         #saveThis = str(time.time())+'::'+tweet
         
         saveFile = open('all_tweets.csv','a')
         saveFile.write(data)
         saveFile.write('\n')
         saveFile.close()
         return True
      except BaseException, e:
         print 'failed ondata,',str(e)
         time.sleep(5)

   def on_error(self, status):
      print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["rob ford"])

