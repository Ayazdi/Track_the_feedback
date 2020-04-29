#----------------
# happens in dockers build

FROM python:3.6-slim

WORKDIR /app

RUN pip install pymongo
RUN pip install tweepy

#ADD ./tweetbot.py /app  if we use -v we don't need to add this line

#----------------------------
# happens in dockers run
CMD python get_tweets.py
