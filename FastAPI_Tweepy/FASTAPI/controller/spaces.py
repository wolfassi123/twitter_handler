## This is the space router. Here you will find all the API calls concerning spaces.
## Each API call is defined in a simplistic matter, as each API call uses a already defined function that is defined as part of the refactor folder.
## To edit the functionality of the API call, you need to check which function it calls form the refactor folder, and change it from there.

from typing import List, Union
from fastapi import APIRouter, Query
from FASTAPI import database
from twitter_client import twitter_client

## Here we define the router, and specify which prefix it uses, as well as under which name tag it will apper on SWAGGER
router = APIRouter(
    prefix = '/space',
    tags=['Spaces']
)

# get_db = database.get_db

## We are defining an instance of the class Space. We shall use this instance to call functions on tweepy.
twitter_space = twitter_client.space


## This API call allows us to retrieve scheduled spaces that match the specific query that we passed.
@router.get('/spaces/{query}')
def spaces(query):
    return twitter_space.getSpaces(query)

## This API call allows us to retrieve the tweets of a specific space.
@router.get('/space_tweet/{id}')
def space_tweets(id):
    return twitter_space.getSpaceTweets(id)

## This API call allows us to retrieve the information we need about a specific space.
@router.get('/space/{id}')
def space_info(id,q: Union[List[str], None] = Query(default=[])):
    query_items = {"q": q}
    q_list = query_items['q']
    # q_tuple = ()
    # for que in q_list:
    #     q_tuple.append(que)
    q_tuple = tuple(q_list)
    return twitter_space.getSpace(id,q_tuple)