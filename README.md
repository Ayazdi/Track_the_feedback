# Track The Feedback
A data pipeline to scrape and analyze posts from social media for tracking feedback on a specific beer product/brand.
![Data Pipeline](/data_pipeline.jpg)
## Description
Track The Feedback is a scraper/analyzer data pipeline for extracting posts from social media with the given tags and transform them into structured data(dataframe) using pandas. In addition, the sentiment of the post's captions(only English) are analyzed by custom pre-trained BERT model and beer logos get detected by fine-tuned Inception_v3 logo detector model (more details in the model section). Transformed and analyzed data load to an AWS RDS server on a PostgreSQL database. Finally, a Metabase dashboard(setup on AWS EC2) was created for exploratory data analysis and visualization. The ETL job of the data pipeline is docker containerized due to various dependencies of each step.

## Models:
Sentiment analysis model: This model was trained on the Tweets Sentiment Extraction data set from Kaggle using pre-trained BERT base(12/768) model and SpaCy-Transformers for data pre-processing. The model can predict the sentiment of the post (negative, positive or neutral) with 85% accuracy and 87% average F1 score.
Data: https://www.kaggle.com/c/tweet-sentiment-extraction/data

Logo detection model: This model was trained on FLICKRLOGOS-32 data set provided by University of Augsburg, Institute of Computer Science. From the 32 logo classes available in the data set only 8 of them that were beer logos was used and an extra logo class (Hop-House 13) was added to the data. Highly accurate model was obtained by fine tuning Inception_V3 model and Keras image data generator.
Classes:
 - Guinness
 - Hop-house 13
 - Fosters
 - Carlsberg
 - Becks
 - Corona
 - Heineken
 - Paulaner
 - No-logo

Data: https://www.uni-augsburg.de/en/fakultaet/fai/informatik/prof/mmc/research/datensatze/flickrlogos/

Step-by-step codes and description of the model training available in models folder in jupyter-notebook format.

## Tech used:
- Python
- Dockers
- MongoDB
- PostgreSQL
- AWS (RDS, EC2)
- SQLAlchemy
- pymongo
- TensorFlow
- Paperspace
- BERT
- SpaCy-Transformers  
- Inception-V3
- Metabase


## Usage:
1. Install Dockers
2. Clone this repository: git clone https://github.com/Ayazdi/Track_the_feedback.git
3. Download TensorFlow models from here: https://www.dropbox.com/s/vanhum3y5rb5x2d/models.zip?dl=0
and unzip the files into etl folder
4. Enter your Instagram credentials, Postgres and mongodb details in the config_example.py
5. Go to the main folder of the project in the terminal and run docker-compose build and afterwards docker-compose up.
