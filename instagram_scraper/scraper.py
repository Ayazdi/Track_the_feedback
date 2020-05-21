""""
This module scrape new instagram posts with the given tags and upload them as
json files to mongodb every 2 minutes.

"""
from config import USER, PASS, TAG
from instagram_private_api import Client
from instagram_cache import from_json
from pymongo import MongoClient
import time
import logging
import json


# loading cashed logging setting for instagram
with open('my_setting.json') as file_data:
    cached_settings = json.load(file_data, object_hook=from_json)
device_id = cached_settings.get('device_id')

# Reuse auth settings
api = Client(USER, PASS, settings=cached_settings)
uuid = Client.generate_uuid()

# Mongodb connection
client_mongo = MongoClient('mongodb')
db = client_mongo.mongodb


def scrape_new_feed(new_tag):
    """
    Scrape the posts in one json file and upload it to mongodb
    """
    tags = api.feed_tag(new_tag, uuid)
    db.instagram.insert(tags)
    logging.critical("New posts are coming!!!")


if __name__ == '__main__':
     while True:
         scrape_new_feed(TAG)
         logging.critical("Posts have been added to the database. Waiting for 10 minute...")
         time.sleep(600)
