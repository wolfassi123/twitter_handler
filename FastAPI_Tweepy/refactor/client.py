from tweepy import Client as clt

from .User.user import User
from .Lists.list import List
from .Space.space import Space
from .Tweets.tweets import Tweet

from .configuration import Configuration

class Client():
    def __init__(self, configuration:Configuration):
        self.__configuration = configuration
        self.__client = clt(bearer_token=configuration.bearer_token,
        consumer_key = configuration.api_key,
        consumer_secret = configuration.api_key_secret,
        access_token = configuration.access_token,
        access_token_secret = configuration.access_token_secret)
        self.__user = User(self.__client)
        self.__list = List(self.__client)
        self.__space = Space(self.__client)
        self.__tweet = Tweet(self.__client)
        
    @property
    def user(self):
        return self.__user
    @property
    def list(self):
        return self.__list
    @property
    def space(self):
        return self.__space
    @property
    def tweet(self):
        return self.__tweet