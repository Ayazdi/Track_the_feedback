# Track The Feedback
A data pipeline to scrape and analyze posts from social media for tracking feedback on a specific beer product/brand.
![Data Pipeline](/data_pipeline.jpg)
## Description
Track The Feedback is a scraper/analyzer data pipeline for extracting posts from social media with the given tags and transform them into structured data(dataframe) using pandas. Posts captions

## Usage:
1. install Dockers
2. Clone this repository: git clone https://github.com/Ayazdi/Track_the_feedback.git
3. Download tensorflow models from here: https://www.dropbox.com/s/vanhum3y5rb5x2d/models.zip?dl=0
and unzip the files into etl folder
4. Enter your Instagram credentials, Postgres and mongodb details in the config_example.py
5. Run docker-compose build and docker-compose up in the main folder

## Models:
Sentiment analysis: 



## Tech used:
 - Python
 - Dockers
 - Mongodb
 - Postgres
 - AWS (RDS, EC2)
 - SQLAlchemy
 - pymongo
 - BERT   
 - Inception-V3
 - Metabase
