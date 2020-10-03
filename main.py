from urllib.request import urlopen as uReq
import requests
import tweepy
import time
import schedule

def post():
    # Get auth
    auth = tweepy.OAuthHandler('consumerkey', 'consumersecret')
    auth.set_access_token('token', 'tokensecret')

    api = tweepy.API(auth)

    #override tweepy.StreamListener to add logic to on_status
    class MyStreamListener(tweepy.StreamListener):
        def on_status(self, status):
            print(status.text)

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

    # Tweet
    # api.update_status(title)

schedule.every().day.at("10:00").do(post)

while True:
    schedule.run_pending()
    time.sleep(360)