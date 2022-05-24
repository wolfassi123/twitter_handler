

from multiprocessing.connection import Client
import tweepy

class getUserBuilder():
    def __init__(self,client:tweepy.Client) -> None:
        self.__included_parameters = set()
        self.__client = client

    def include_created_at(self):
        self.__included_parameters.add('created_at')
        return self

    def execute(self):
        user = self.__client.get_user(username=user,user_fields=list(self.__included_parameters))
