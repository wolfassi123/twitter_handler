## This is the list router. Here you will find all the API calls concerning lists.
## Each API call is defined in a simplistic matter, as each API call uses a already defined function that is defined as part of the refactor folder.
## To edit the functionality of the API call, you need to check which function it calls form the refactor folder, and change it from there.

from fastapi import APIRouter
from twitter_client import twitter_client

## Here we define the router, and specify which prefix it uses, as well as under which name tag it will apper on SWAGGER
router = APIRouter(
    prefix = '/list',
    tags=['Lists']
)

## We are defining an instance of the class List. We shall use this instance to call functions on tweepy.
twitter_list = twitter_client.list

## This API call allows us to get the number of followers of a specific twitter list.
@router.get('/followers/{id}')
def list_followers(id):
    return twitter_list.getListFollowers(id)

## This API call allows us to get the number of members of a specific twitter list.
## Members are the users whose tweets constitute the content of a list.
@router.get('/members/{id}')
def list_members(id):
    return twitter_list.getListMembers(id)

## This API call allows us to get the number of tweets of a specific list.
@router.get('/tweetss/{id}')
def list_tweets(id):
    return twitter_list.getListTweets(id)
