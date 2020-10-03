import tweepy
import json

def post():
    twitter_file = open('twitter.json',)
    twitter_data = json.load(twitter_file)
    twitter_file.close

    consumerkey = twitter_data["consumerkey"]
    consumersecret = twitter_data["consumersecret"]
    token = twitter_data["token"]
    tokensecret = twitter_data["tokensecret"]

    # Get auth
    #auth = tweepy.OAuthHandler('consumerkey', 'consumersecret')
    #auth.set_access_token('token', 'tokensecret')

    #api = tweepy.API(auth)

    #override tweepy.StreamListener to add logic to on_status
    #class MyStreamListener(tweepy.StreamListener):
    #    def on_status(self, status):
    #        print(status.text)

    #myStreamListener = MyStreamListener()
    #myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

    # Tweet
    # api.update_status(title)

post()