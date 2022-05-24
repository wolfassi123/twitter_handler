## This is where functions concerning Tweets are defined.
## Most of these functions' outputs can be modified. To modify them, check the documentation for every tweepy function call followung self.__client.
## This is the documentation : https://docs.tweepy.org/en/stable/client.html

from typing import Union
from aiohttp import ClientTimeout
from multipledispatch import dispatch
from tweepy import Client
from .. import client
from .. import configuration

## This class will have all of the functions that allow us to extract any sort of information out of a tweet.
class Tweet():
    def __init__(self,client: Client):
        self.__client = client
    
## This function will allow us to get a specific tweet knowing its id.
## This function will only return the id, the text and the date of the tweet.
## More options are available as part of the getTweetInfo function.
    def getTweet(self,id:int):
        response = self.__client.get_tweet(id = id,tweet_fields =['created_at'])
        tweetdata = response.data
        tweetid = tweetdata.id
        tweettext = tweetdata.text
        tweetdate = tweetdata.created_at
        tweet = dict()
        tweet['id'] = tweetid
        tweet['text'] = tweettext
        tweet['date'] = tweetdate
        return tweet

## This function will allow us to get all the usernames of the users that liked a specific tweet.
    def getLikingUsers(self,id:int):
        users = self.__client.get_liking_users(id = id)
        liking_users =[]
        for user in users.data:
            liking_users.append(user.username)
        return liking_users

## This function will allow us to get how many tweets matching the query have been tweeted, day by day.(Change granularity from day to hour or month)
    def getRecentTweetCount(self,query:str):
        counts = self.__client.get_recent_tweets_count(query = query,granularity = 'day')
        counts_data = counts.data
        per_day = dict()
        for count in counts_data:
            per_day[count['start']] = count['tweet_count']
        return per_day

## This function will return all of recent tweets that match a specific query.
    def getRecentTweet(self,query:str,max:int):
        response = self.__client.search_recent_tweets(query = query,max_results = max,user_auth = True)
        tweetsdata = response.data
        tweets = dict()
        for tweet in tweetsdata:
            tweet_id = tweet.id
            tweet_text = tweet.text
            tweets[tweet_id] = tweet_text
        tweets['number'] = max
        return tweets

## This function will allow us to get all of the mentioned informations concerning a specific tweet.
    def getTweetInfo(self,id:int, keys_list:list=[]):
        response = self.__client.get_tweet(id = id,tweet_fields = ['created_at',
        'public_metrics',
        'lang',
        'author_id',
        'conversation_id',
        'attachments',
        'in_reply_to_user_id',
        'possibly_sensitive',
        'referenced_tweets',
        'reply_settings',
        'source'])
        tweet = dict()
        tweetdata = response.data
        tweet['id'] = tweetdata.id
        for key in keys_list:
            if isinstance(key, str):
                tweet[key] = tweetdata[key]
        return tweet

## This function will return some of the standard and most used information concerning a tweet.
## Text, author_name, author_username, id, Number of Retweets, Quotes, Replies and Likes.
    def getTweetBasic(self,id:int):
        response = self.__client.get_tweet(id=id,tweet_fields=['public_metrics'],expansions=['author_id'])
        tweetdata = response.data
        tweetfields = tweetdata['public_metrics']
        userinfo = response.includes['users'][0]
        userinfodict = dict(userinfo)
        tweet = dict()
        tweet['id'] = tweetdata.id
        tweet['text'] = tweetdata.text
        tweet['author'] = userinfodict['name']
        tweet['author_username'] = userinfodict['username']
        tweet['retweet_count'] = tweetfields['retweet_count']
        tweet['reply_count'] = tweetfields['reply_count']
        tweet['like_Count'] = tweetfields['like_count']
        tweet['quote_count'] = tweetfields['quote_count']
        return tweet

## This function will return the annotations concerning a specific tweet, such as Topics and Entities.
    def getTweetAnnotations(self,id:int):
        response = self.__client.get_tweet(id = id,tweet_fields = ['context_annotations','entities','reply_settings'])
        tweetdata = response.data
        tweet = dict()
        tweet['annotations'] = tweetdata['context_annotations']
        tweet['entities'] = tweetdata['entities']
        return tweet
