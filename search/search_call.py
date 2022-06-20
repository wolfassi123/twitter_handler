import os
from client import configuration

from dotenv import load_dotenv

from client import client

load_dotenv()
 
api_key = os.getenv('api_key')
api_key_secret = os.getenv('api_key_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')
bearer_token = os.getenv('bearer_token')

con = configuration.Configuration(
    api_key=api_key,
    api_key_secret=api_key_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
    bearer_token=bearer_token,
)


c = client.Client(con)
# user = c.user
# name = user.getUserInfo("JadSadaka")
# print(name)
# answer = user.getUserInfo("JadSadaka",'public_metrics')
# print(answer)
# answer = user.getUserFollowers("fadybaly")
# print(answer)
# answer = user.getUserFollowings("fadybaly")
# print(answer)
# answer = user.getUserMentions("fadybaly")
# print(answer)
# answer = user.getUserTImeline("fadybaly")
# print(answer)
# answer = user.getBookmarks("fadybaly")
# print(answer)
# answer = user.getListFollows("fadybaly")
# print(answer)
# answer = user.getListMemberships("fadybaly")
# print(answer)
# answer = user.getOwnedLists("fadybaly")
# print(answer)
# l = c.list
# answer = l.getListFollowers(786644677743312897)
# print(answer)
# answer = l.getListMembers(786644677743312897)
# print(answer)
# answer = l.getListTweets(786644677743312897)
# print(answer)
# s = c.space
# answer = s.getSpaces('covid')
# print(answer)
# answer = s.getSpace('1OyJADQvrdrGb')
# print(answer)
# answer = s.getSpaceTweets('1OyJADQvrdrGb')
# print(answer)
# t = c.tweet
# answer = t.getTweet(1517414653340626944)
# print(answer)
# answer = t.getLikingUsers(1517414653340626944)
# print(answer)
# answer = t.getRecentTweetCount(1517414653340626944,'messi')
# print(answer)
# answer = t.getRecentTweet('messi',10)
# print(answer)
# answer = t.getTweetInfo(1517414653340626944,'created_at','public_metrics')
# print(answer)
# answer = t.getTweetBasic(1517414653340626944)
# print(answer)
# answer = t.getTweetAnnotations(1517414653340626944)
# print(answer)
# u = c.user
# answer  = u.getUserInfo('fadybaly',['created_at','public_metrics'])
# print(answer)
# answer2 = u.getListFollows('fadybaly')
# print(answer2)

# t = c.tweet
# answer = t.getRecentTweetCount('messi')
# print(answer)

# s = c.space
# answer = s.getSpace('1ypKdEONEnQGW',['lang'])
# print(answer)
