import pandas as pd
from sqlalchemy import create_engine, exc
from load_transform import extract_from_mongodb, extract_data_from_json
from bert_model import load_bert_model, sentiment_prediction
import time
import logging
from config import AWS_PG


# Postgres connection
PG = create_engine(AWS_PG)

def sentiment_analysis(df):
    df_analyse = df[(df['language']=='en') & (df['clean_text_en']!=None)]
    df_analyse['sentiment'] = df_analyse['clean_text_en'].apply(sentiment_prediction)
    df['sentiment'][df_analyse.index] = df_analyse['sentiment']
    return df

if __name__ == '__main__':
        # Extract
        posts = extract_from_mongodb()
        # Transform
        df = extract_data_from_json(posts)
        df = sentiment_analysis(df)
        # Load
        df.to_sql('test', PG, if_exists='replace')



# while True:
#     posts = extract_from_mongodb()
#     if posts:
#         df = extract_data_from_json(posts)
#         df = sentiment_analysis(df)
#         df.to_sql('test', PG, if_exists='replace')
#     time.sleep(30)
