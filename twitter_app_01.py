from TwitterSearch import *
import dictionary
import keys
from tweepy import *


def find_keywords(data):
    words = data.split()
    query = []

    for word in words:
        if word.lower() in dictionary.computer_science:
            query.append("#" + word)

    return query

def search_results(words):

    #auth = OAuthHandler(keys.consumer_key, keys.consumer_secret)
    #auth.set_access_token(keys.access_token, keys.access_token_secret)

    try:

        tso = TwitterSearchOrder()
        tso.set_keywords(words)

        rilo_twitter = TwitterSearch(
            consumer_key = keys.consumer_key,
            consumer_secret = keys.consumer_secret,
            access_token = keys.access_token,
            access_token_secret = keys.access_token_secret
            )

        for tweet in rilo_twitter.search_tweets_iterable(tso):
            if  tweet['retweet_count'] > 150:
                #API.retweet(tweet['id'])
                print('@%s tweeted:  %s' % (tweet['user']['screen_name'], tweet['text']))
                print('\n\n\n')

    except TwitterSearchException as e:
        print (e)

def run_app(q):
    x = find_keywords(q)
    return search_results(x)
#print x
