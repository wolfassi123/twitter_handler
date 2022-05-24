## This is where functions concerning Lists are defined.
## Most of these functions' outputs can be modified. To modify them, check the documentation for every tweepy function call followung self.__client.
## This is the documentation : https://docs.tweepy.org/en/stable/client.html

from typing import Union
from multipledispatch import dispatch
from tweepy import Client
# from user import User
from ..User.user import User
from pprint import pprint
import arabic_reshaper
from bidi.algorithm import get_display

## This function is used to showcase arabic tweets correctly.
def arabize(text):
    text = text
    reshaped_text = arabic_reshaper.reshape(text)    # correct its shape
    bidi_text = get_display(reshaped_text)
    return bidi_text

## This class will have all of the functions that allow us to extract any sort of information out of a list.
class List:
    def __init__(self,client: Client):
        self.__client = client

## This function will allow us to return the followers of a list.
    def getListFollowers(self,list_id:int):
        id_followers = self.__client.get_list_followers(id =list_id,user_auth=True)
        id_data = id_followers.data
        l = []
        for follower in id_data:
            l.append(follower.username)
        return l

## This function will allow us to return the members of a list.
    def getListMembers(self,list_id:int):
        list_members = self.__client.get_list_members(id = list_id)
        list_members_data = list_members.data
        l = []
        for list_member in list_members_data:
            l.append(list_member.username)
        return l

## This function will allow us to return the tweets of a list.
    def getListTweets(self,list_id:int):
        recent_list_tweets = self.__client.get_list_tweets(id = list_id,user_auth=True)
        recent_list_tweets_data = recent_list_tweets.data
        tweets = dict()
        for recent_tweet in recent_list_tweets_data:
            tweets[f"{recent_tweet.id}"] = arabize(recent_tweet.text)
        return tweets
