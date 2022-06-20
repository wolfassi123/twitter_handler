## This is where functions concerning Spaces are defined.
## Most of these functions' outputs can be modified. To modify them, check the documentation for every tweepy function call followung self.__client.
## This is the documentation : https://docs.tweepy.org/en/stable/client.html

from tweepy import Client

## This class will have all of the functions that allow us to extract any sort of information out of a space.
class Space():
    def __init__(self,client:Client):
        self.__client = client

    ## This function will allow us to get all the spaces that match the specific query that is passed.
    def getSpaces(self,query:str):
        spaces = self.__client.search_spaces(query = query,
        space_fields = ['created_at',
        'subscriber_count',
        'lang',
        'speaker_ids',
        'scheduled_start'])
        spaces_data = spaces.data
        spaces = dict()
        for space in spaces_data:
            l = []
            l.append(space['created_at'])
            l.append(space['subscriber_count'])
            l.append(space['scheduled_start'])
            l.append(space['lang'])
            l.append(space['speaker_ids'])
            spaces[f"{space.id}"] = l
        return spaces

    ## This function will allow us to get all the information needed by the user concerning a specific space.
    def getSpace(self,id:int,keys_list:list=[]):
        response = self.__client.get_space(id = id,space_fields = ['created_at',
        'subscriber_count',
        'lang',
        'speaker_ids',
        'scheduled_start',
        'started_at',
        'ended_at',
        'creator_id',
        'topic_ids',
        'updated_at'])
        # ,topic_fields = ['id','name','description']
        space_data = response.data
        space = dict()
        space['id'] = space_data.id
        for key in keys_list:
            if isinstance(key, str):
                space[key] = space_data[key]
        return space

    ## This function will allow us to get all the Tweets that are part of a specific Space.
    def getSpaceTweets(self,id):
        response = self.__client.get_space_tweets(id = id)
        tweets_data = response.data
        # print(tweets_data)
        l = []
        for tweet in tweets_data:
            l.append(tweet)
        return l