import slack
import pyjokes
from sqlalchemy import create_engine
from config import SLACK_TOKEN


client = slack.WebClient(token=SLACK_TOKEN)

def slackbot():
    #repeat automatically
    prev_tweet = ''
    while True:
        # Do the slack post
        tweet_result = PG.execute('''SELECT kungflu."text" FROM kungflu LIMIT 1;''').fetchall()
        # logic to check if the tweet has already been posted, only post if its not already been posted
        if tweet_result != prev_tweet:
            prev_tweet = tweet_result
            response = client.chat_postMessage(channel='#kung_flu', text=f"Here is a tweet we scraped: {tweet_result}")
        #delay for one minute
        time.sleep(60)
