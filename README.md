# Track The Feedback
A data pipeline to scrape and analyze posts from social media for tracking feedback on a specific beer product/brand.
![Data Pipeline](/data_pipeline.jpg)
## Description
Track The Feedback is a scraper/analyzer data pipeline for extracting posts from social media with the given tags and transform them into structured data(dataframe) using pandas. In addition, the sentiment of the post's captions are analyzed by custom pre-trained BERT model and beer logos get detected by fine-tuned Inception_v3 logo detector model (more details in the model section)

## Usage:
1. Install Dockers
2. Clone this repository: git clone https://github.com/Ayazdi/Track_the_feedback.git
3. Download tensorflow models from here: https://www.dropbox.com/s/vanhum3y5rb5x2d/models.zip?dl=0
and unzip the files into etl folder
4. Enter your Instagram credentials, Postgres and mongodb details in the config_example.py
5. Go to the main folder of the project in the terminal and run docker-compose build and afterwards docker-compose up.

## Models:
Sentiment analysis:



## Tech used:
 - Python
 - Dockers
 - mongoDB
 - PostgreS
 - AWS (RDS, EC2)
 - SQLAlchemy
 - pymongo
 - BERT   
 - Inception-V3
 - Metabase
