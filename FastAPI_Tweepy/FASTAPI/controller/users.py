## This is the user router. Here you will find all the API calls concerning users.
## Each API call is defined in a simplistic matter, as each API call uses a already defined function that is defined as part of the refactor folder.
## To edit the functionality of the API call, you need to check which function it calls form the "refactor" folder, and change it from there.

from typing import List, Union
from fastapi import APIRouter, Query
from FASTAPI import database
from twitter_client import twitter_client

## Here we define the router, and specify which prefix it uses, as well as under which name tag it will apper on SWAGGER
router = APIRouter(
    prefix = '/user',
    tags=['Users']
)

# get_db = database.get_db

## We are defining an instance of the class User. We shall use this instance to call functions on tweepy.
twitter_user = twitter_client.user

## This API call will return all the username of the followers of a specific user.
@router.get('/user_followers/{id}')
def user_followers(id):
    return twitter_user.getUserFollowers(id)

## This API call will return all the username of the users that a specific user follows.
@router.get('/user_followings/{id}')
def user_followings(id):
    return twitter_user.getUserFollowings(id)

## This API call will return all of the tweets where a specific user (his username) is mentioned in a tweet.
@router.get('/user_mentions/{id}')
def user_mentions(id):
    return twitter_user.getUserMentions(id)

## This API call will return a specific user's timeline. Dates of when to start and end can be modified.
@router.get('/user_timeline/{id}')
def user_timeline(id):
    return twitter_user.getUserTimeline(id)

## This API call will return a specific user's bookmarks.
@router.get('/user_bookmarks/{id}')
def user_bookmarks(id):
    return twitter_user.getBookmarks(id)

## This API call will return all the list that a specific user follows.
@router.get('/user_list_follows/{id}')
def user_list_follows(id):
    return twitter_user.getListFollows(id)

## This API call will return all the lists that a specific user is member of.
## It means lists which include this user's tweets as part of its content.
@router.get('/user_list_memberships/{id}')
def user_list_memberships(id):
    return twitter_user.getListMemberships(id)

## This API call will return all the lists that are owned by a specific user.
@router.get('/user_list_ownerships/{id}')
def user_list_ownerships(id):
    return twitter_user.getOwnedLists(id)

## This API call will return all of the mentioned information concerning a specific user.
@router.get('/user_info/{id}')
def user_info(id, q: Union[List[str], None] = Query(default=[])):
    query_items = {"q": q}
    q_list = query_items['q']
    return twitter_user.getUserInfo(id, q_list)

# user_info/fadybaly&q=created_at&q=publi