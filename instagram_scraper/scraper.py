from instagram_private_api import Client, ClientCompatPatch
from instagram_cache import to_json, from_json, onlogin_callback
from pymongo import MongoClient
from config import USER, PASS
import time
import logging
import json


# loading cashed logging setting for instagram
with open('my_setting.json') as file_data:
    cached_settings = json.load(file_data, object_hook=from_json)
device_id = cached_settings.get('device_id')

# reuse auth settings
api = Client(USER, PASS, settings=cached_settings)
uuid = Client.generate_uuid()

# Mongodb connection
client_mongo = MongoClient('192.168.99.100:27017')
db = client_mongo.mongodb

def scrape_new_feed(new_tag):
    """
    Scrape the posts in one json file and upload it to mongodb
    """
    tags = api.feed_tag(new_tag, uuid)
    db.insta_test.insert(tags)
    logging.critical("new posts are coming")
    return tags

if __name__ == '__main__':
     print("Please enter the tag you want to track:\n")
     TAG = input()
     while True:
         tags = scrape_new_feed(TAG)
         total_post = len(tags['items']) + len(tags['ranked_items'])
         logging.critical(f"{total_post} posts have been added to the database. waiting for 2 minutes...")
         time.sleep(120)
