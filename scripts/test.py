#!/usr/bin/env

from TwitterSearch import *
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.setKeywords(['Guttenberg', 'Doktorarbeit']) # let's define all words we would like to have a look for
    tso.setLanguage('de') # we want to see German tweets only
    tso.setCount(7) # please dear Mr Twitter, only give us 7 results per page
    tso.setIncludeEntities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'CiQGfooRBKJRSrtaGl7GkQ',
        consumer_secret = 'G2o2pVeFaYlZdZAQL6NxkE3x7iW0U7kfoUKBTaOg',
        access_token = '38CJ8saoV8UJx46L38bFiZMOSocC2XhtubOsot9x',
        access_token_secret = 'sNJUHNg4GzZDnIR82BeCkQK0ptgrOWsimO265BhB1YCtq'
     )

    for tweet in ts.searchTweetsIterable(tso): # this is where the fun actually starts :)
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
