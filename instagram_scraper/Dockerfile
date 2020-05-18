FROM python:3.6-slim

WORKDIR /app

RUN pip install pymongo
RUN pip install SQLAlchemy
RUN pip install psycopg2-binary
RUN pip install instagram_private_api


CMD python scraper.py
