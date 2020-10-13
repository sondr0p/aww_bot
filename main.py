import tweepy
import json
import praw
import pprint
from urllib.request import urlretrieve

def GetTwitterAPI(fileName):
    # grab keys from file
    twitter_file = open(fileName,)
    twitter_data = json.load(twitter_file)
    twitter_file.close
    
    # authenticate
    auth = tweepy.OAuthHandler(twitter_data["consumerkey"], twitter_data["consumersecret"])
    auth.set_access_token(twitter_data["token"], twitter_data["tokensecret"])

    api = tweepy.API(auth)
    return api

def GetRedditAPI(fileName):
    # grab keys from file
    reddit_file = open(fileName,)
    reddit_data = json.load(reddit_file)
    reddit_file.close

    # create 
    api = praw.Reddit(client_id=reddit_data["client_id"],
                    client_secret=reddit_data["client_secret"],
                    password=reddit_data["password"],
                    user_agent="testscript",
                    username=reddit_data["username"])

    return api

TwitterAPI = GetTwitterAPI("twitter.json")
RedditAPI = GetRedditAPI("reddit.json")
subreddit = RedditAPI.subreddit("aww")
for submission in subreddit.top("day", limit=1):
    url = submission.media['reddit_video']['fallback_url']
    print(url)
    name = "some.mp4"
    urlretrieve(url, name)
    #pprint.pprint(vars(submission))