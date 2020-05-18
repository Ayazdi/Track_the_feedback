
import pandas as pd
from sqlalchemy import create_engine, exc
from load_transform import extract_from_mongodb, extract_data_from_json
from bert_model import load_bert_model, sentiment_prediction
from logo_detection_model import logo_detection
import time
import logging
from config import AWS_PG


# Postgres connection
PG = create_engine(AWS_PG)
# Remove duplicates in Postgres
QUERY = """ DELETE FROM heineken T1
            USING   heineken T2
            WHERE   T1.ctid < T2.ctid
            AND T1.date_time = T2.date_time;
        """


def sentiment_analysis_on_scraped_data(df):
    """
    Analyse the sentiment of the cleaned caption in the dataframe using the
    BERT sentiment analysis model and fill the sentiment column with the results.

    return: dataframe with sentiment analysis of the posts
    """
    df_analyse = df[(df['language'] == 'en') & (df['clean_text_en'] != None)]  # Only the English captions
    df_analyse['sentiment'] = df_analyse['clean_text_en'].apply(sentiment_prediction)
    df['sentiment'][df_analyse.index] = df_analyse['sentiment']
    return df


if __name__ == '__main__':
    while True:
        # Extract
        posts = extract_from_mongodb()
        if posts:
            total_post = len(posts['items']) + len(posts['ranked_items'])
            logging.critical(f"{total_post} posts have been extracted from mongodb")

            # Transform
            df = extract_data_from_json(posts)
            logging.critical("Sentiment analysis on the clean text has been started")
            df_analized = sentiment_analysis_on_scraped_data(df)
            logging.critical("Sentiment analysis is finished")
            logging.critical("Logo detection on the images has been started")
            df_analized['logos'] = df_analized['urls'].apply(logo_detection)
            logging.critical("Logo detection is finished")

            # Load
            logging.critical("Uploading data to AWS database")
            df_analized.to_sql('heineken', PG, if_exists='append')
            PG.execute(QUERY)  # removing the duplicates
            logging.critical("Waiting for 10 minutes...")
        time.sleep(600)
