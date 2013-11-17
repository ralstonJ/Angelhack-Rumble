#!/usr/bin/env python

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json

ckey = 'CiQGfooRBKJRSrtaGl7GkQ'
csecret = 'G2o2pVeFaYlZdZAQL6NxkE3x7iW0U7kfoUKBTaOg'
atoken = '741285805-38CJ8saoV8UJx46L38bFiZMOSocC2XhtubOsot9x'
asecret = 'sNJUHNg4GzZDnIR82BeCkQK0ptgrOWsimO265BhB1YCtq'
tweet = ""
class listener(StreamListener):

   def on_data(self, data):
      try: 
         x = json.loads(data)
         ids  = x['id']
         tweet = x['text'] 
         user_name = x['user']['name'] 
         profile_img_url = x['user']['profile_image_url']
         retweet_count = x['retweet_count']
         favorite_count = x['favorite_count']
         verified = x['user']['verified']        
         print ids,"\t",tweet,"\t",user_name,"\t",profile_img_url,"\t",retweet_count,"\t",favorite_count,"\t",verified
         return True
      except BaseException, e:
         print 'failed ondata,',str(e)
         time.sleep(3)

   def on_error(self, status):
      print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["rob ford"])

