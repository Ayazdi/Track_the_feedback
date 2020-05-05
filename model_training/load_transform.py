import pandas as pd
from pymongo import MongoClient
from sqlalchemy import create_engine, exc
import random
import re
from langdetect import detect

# mongodb connection
client_mongo = MongoClient('192.168.99.100:27017')
db = client_mongo.mongodb

def extract_from_mongodb():
    """gets a random set of posts in a json format from mongodb"""
    posts = list(db.instagram_randoms.find())
    if posts:
        tags = random.choice(posts)
        return tags

def extract_data_from_json(posts):
    """
    Extract all the information of each post from the json file and store them in a list.

    posts: a json file that contain multiple posts

    return: multiple lists contaning the information
    """

    urls = []
    taken_at = []
    num_likes = []
    num_comments = []
    users_fullname = []
    users_id = []
    captions = []
    language = []
    caption_tags = []
    clean_text = []
    locations = []
    longitude = []
    latitude = []
    user_pk = []
    num_followers= []
    num_followings=[]
    ranked = []

    for post_type in ['ranked_items', 'items']:
        for item in posts[post_type]:
            if 'image_versions2' in item.keys(): #only grabbing pictures (no videos or carousels)
                if post_type == "ranked_items":
                    # Number of followers and followings of the ranked user
                    # user_info = api.user_detail_info(pk)
                    # followers = user_info['user_detail']['user']['follower_count']
                    # followings = user_info['user_detail']['user']['following_count']

                    num_followers.append(None)
                    num_followings.append(None)
                    ranked.append(1)
                else:
                    num_followers.append(None)
                    num_followings.append(None)
                    ranked.append(0)


                # Name, id and user primary key
                full_name = item['user']['full_name']
                user_id = item['user']['username']
                pk = item['user']['pk']

                users_fullname.append(full_name)
                users_id.append(user_id)
                user_pk.append(pk)

                # Date and time
                taken = pd.to_datetime(item['taken_at'], unit ='s')
                taken_at.append(taken)

                # Image url
                url = item['image_versions2']['candidates'][1]['url']
                urls.append(url)

                # Number of likes
                try:
                    likes = item['like_count']
                except KeyError:
                    likes = 0
                num_likes.append(likes)

                # Number of comments
                try:
                    comments = item['comment_count']
                except KeyError:
                    comments = 0
                num_comments.append(comments)

                # Caption
                try:
                    caption = item['caption']['text']
                except KeyError:
                    caption = None
                captions.append(caption)

                # Location, longitude and latitude of the post
                try:
                    loc = item['location']['name']
                except KeyError:
                    loc = None
                locations.append(loc)

                try:
                    lng = float(item['location']['lng'])
                except KeyError:
                    lng = None
                longitude.append(lng)

                try:
                    lat = float(item['location']['lat'])
                except KeyError:
                    lat = None
                latitude.append(lat)

                # Hashtags
                hashtags = re.findall("#\S+", caption.lower())
                hashtags = ','.join(hashtags)
                hashtags = re.sub("#",' ', hashtags)
                if hashtags == '':
                    hashtags = None
                caption_tags.append(hashtags)

                # Clean caption with links, hastag or special character
                text = re.sub("#\S+",'', caption)
                text = re.sub("@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+", ' ', str(text).lower()).strip()
                if text != "":
                    clean_text.append(text)
                else:
                    clean_text.append(None)


                # Written language of the post
                try:
                    lan = detect(text)
                except:
                    lan = "unkown"
                language.append(lan)

    df = pd.DataFrame({'date_time':taken_at,
               'users_id':users_id,
               'users_fullname': users_fullname,
               'user_pk':user_pk,
               'num_followers':num_followers,
               'num_followings':num_followings,
               'urls': urls,
               'num_likes':num_likes,
               'num_comments':num_comments,
               'captions':captions,
               'language': language,
               'caption_tags':caption_tags,
               'clean_text_en':clean_text,
               'sentiment':None,
               'locations':locations,
               'longitude':longitude,
               'latitude':latitude,
               'ranked':ranked
                } )
    return df
