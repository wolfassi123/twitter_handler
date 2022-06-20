## This is the tweet router. Here you will find all the API calls concerning tweets.
## Each API call is defined in a simplistic matter, as each API call uses a already defined function that is defined as part of the refactor folder.
## To edit the functionality of the API call, you need to check which function it calls form the refactor folder, and change it from there.

from typing import List, Union
from fastapi import APIRouter, Query
from client.twitter_client import twitter_client

## Here we define the router, and specify which prefix it uses, as well as under which name tag it will apper on SWAGGER
router = APIRouter(prefix="/tweet", tags=["Tweets"])


## We are defining an instance of the class Tweet. We shall use this instance to call functions on tweepy.
twitter_tweet = twitter_client.tweet

## This API call allows us to retrieve the most recent tweets that match the query we passed.
## It will not return more than {count} tweets.
@router.get("/recent_tweets/{subject}/{count}")
def get_recent_tweets(subject, count):
    return twitter_tweet.getRecentTweet(subject, count)


## This API call allows us to retrieve the tweet whose ID was passed as argument.
## This API call only returns the id and the text of a tweet.
## For further parameters check other API calls.
@router.get("/tweet/{id}")
def get_tweet(id):
    return twitter_tweet.getTweet(id)


## This API call allows to retrieve the username of users that liked the tweet.
@router.get("/liking_user/{id}")
def liking_users(id):
    return twitter_tweet.getLikingUsers(id)


## This API call will return the amount tweets that match the query, day by day, for a length of 1 week.
## The above mentioned options can be changed.
@router.get("/recent_tweet_count/{query}")
def count_recent_tweet(query):
    return twitter_tweet.getRecentTweetCount(query)


## This API call will return some standard informations about a tweet.
## These informations are : Number of Retweets, Quotes, Likes and Comments along with username and name of its author.
@router.get("/tweet_basic/{id}")
def basic_tweet_info(id):
    return twitter_tweet.getTweetBasic(id)


## This API call will return the annotations (Entities, Topics) of a tweet.
@router.get("/tweet_annotations/{id}")
def tweet_annotations(id):
    return twitter_tweet.getTweetAnnotations(id)


## This API call will return all of the info passed by the user concerning the Tweet.
@router.get("/tweet_info/{id}")
def tweet_info(id, q: Union[List[str], None] = Query(default=[])):
    query_items = {"q": q}
    q_list = query_items["q"]
    return twitter_tweet.getTweetInfo(id, q_list)
