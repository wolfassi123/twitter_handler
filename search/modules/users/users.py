## This is where functions concerning Users are defined.
## Most of these functions' outputs can be modified. To modify them, check the documentation for every tweepy function call followung self.__client.
## This is the documentation : https://docs.tweepy.org/en/stable/client.html


from multipledispatch import dispatch
from tweepy import Client

## This class will have all of the functions that allow us to extract any sort of information out of a user.
class User:
    def __init__(self, client: Client):
        self.__client = client

    ## This is the function that allows us to seperate between passing a string(username) or an int(id) along with the desired informations.
    def getUserInfo(self,info, requested_fields:list = []):
         return self._getUserInfo(info,requested_fields)

    ## The two dispatch are used to call the same function, but once by using the username of a user, and once using the id.
    ## the _getUserInfo will allow us to get information concerning the specific user.
    @dispatch(int, list)
    def _getUserInfo(self, info: int, requested_fields:list=[]):
        user = self.__client.get_user(
            id=info,
            user_fields=[
                "created_at",
                "description",
                "entities",
                "verified",
                "public_metrics",
                "protected",
            ],
        )
        userdata = user.data
        user_data = dict()
        user_data["username"] = userdata.username
        user_data["id"] = userdata.id
        if requested_fields:
            for arg in requested_fields:
                user_data[arg] = userdata[arg]
        return user_data
        
    @dispatch(str,list)
    def _getUserInfo(self, info: str, requested_fields:list = []):
        # print(type(self.__client))
        user = self.__client.get_user(
            username=info,
            user_fields=[
                "created_at",
                "description",
                "entities",
                "verified",
                "public_metrics",
                "protected",
            ],
        )

        userdata = user.data
        user_data = dict()
        user_data["username"] = userdata.username
        user_data["id"] = userdata.id
        if requested_fields:
            for arg in requested_fields:
                user_data[arg] = userdata[arg]
        return user_data

    ## This function will allow us to get the usernames of a certain user's followers.
    def getUserFollowers(self, info):
        user = self.getUserInfo(info)
        userid = user["id"]
        userfollowers = self.__client.get_users_followers(id=userid)
        userfollowers_data = userfollowers.data
        followers = []
        for follower in userfollowers_data:
            followers.append(follower.username)
            #print(follower.id)
        return followers

    ## This function will allow us to get the usernames of a certain user's followings (Who the user follows)
    def getUserFollowings(self, user):
        user = self.getUserInfo(user)
        userid = user["id"]
        userfollowings = self.__client.get_users_following(id=userid)
        userfollowings_data = userfollowings.data
        friends = []
        for friend in userfollowings_data:
            # friends.append(self.getUserInfo(friend))
            friends.append(friend.username)
        return friends

    ## This function will allow us to get the tweets where a certain user is mentioned.
    def getUserMentions(self, user):
        user = self.getUserInfo(user)
        # user_data = user.data
        userid = user['id']
        user_tweets = self.__client.get_users_mentions(id=userid)
        tweets = {}
        for tweet in user_tweets.data:
            tweets[f"{tweet.id}"] = tweet.text
        return tweets

    ## This function will allow us to get the Timeline of a certain user.
    def getUserTimeline(self, user):
        user = self.getUserInfo(user)
        userid = user["id"]
        user_tweets = self.__client.get_users_tweets(id=userid,tweet_fields = ['public_metrics'])
        user_tweets_data = user_tweets.data
        tweets = {}
        for tweet in user_tweets.data:
            tweet_data = {}
            tweet_data['text'] = tweet.text
            tweet_data['public_metrics'] = tweet['public_metrics']
            tweets[f"{tweet.id}"] = tweet_data
        return tweets

    ## This function will allow us to get the Timeline of a certain user.
    def getBookmarks(self, user):
        user = self.getUserInfo(user)
        userid = user["id"]
        bookmarks = self.__client.get_bookmarks(id=userid, user_auth=True)
        return bookmarks

    ## This funciton will allow us to get all the list that a specific user follows.
    def getListFollows(self, user):
        user = self.getUserInfo(user)
        userid = user["id"]
        list_follows = self.__client.get_followed_lists(id=userid, user_auth=True)
        return list_follows

    ## This function will allow us to get all the lists of which a certain user is a members (his tweets are part of these lists' content)
    def getListMemberships(self, user):
        user = self.getUserInfo(user)
        userid = user["id"]
        list_memberships = self.__client.get_list_memberships(id=userid)
        return list_memberships

    ## This function will allows us to get all lists of which the specific user owns.
    def getOwnedLists(self, user):
        user = self.getUserInfo(user)
        userid = user["id"]
        owned_lists = self.__client.get_owned_lists(id=userid, user_auth=True)
        return owned_lists
