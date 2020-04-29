""" Scrape Tweets with tweepy and save them in Mongodb as JSON file"""
import config
import json
import logging
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
from pymongo import MongoClient


def authenticate():
    """Function for handling Twitter Authentication"""
    auth = OAuthHandler(config.CONSUMER_API_KEY, config.CONSUMER_API_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

    return auth


class TwitterListener(StreamListener):

    def on_data(self, data):

        """Whatever we put in this method defines what is done with
        every single tweet as it is intercepted in real-time"""

        t = json.loads(data)

        tweet = {
        'text': t["text"],
        'username': t['user']['screen_name'],
        'followers_count': t['user']['followers_count'],
        'date_created': t["created_at"],
        'friends_count': t['user']['friends_count']
        }

        logging.critical(f'\n\n\nTWEET INCOMING: {tweet["text"]}\n\n\n')

        client = MongoClient('mongodb')
        db = client.mongodb
        db.kung_tweets.insert(t)

    def on_error(self, status):

        if status == 420:
            print(status)
            return False


if __name__ == '__main__':

    auth = authenticate()
    listener = TwitterListener()
    stream = Stream(auth, listener)
    stream.filter(track=['kungflu', "Kung flu", "Chinese Flu", "Chinese Virus"], languages=['en'])
