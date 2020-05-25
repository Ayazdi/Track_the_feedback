# Track The Feedback
![Data Pipeline](/data_pipeline.jpg)
## Description
**Track The Feedback** is a scraper/analyzer data pipeline. It extracts new feeds from social media with the given tags and transforms them into a data frame format using **pandas**. Additionally, the sentiment of the post's captions (limited to English for now) is analyzed by a custom pre-trained BERT model. Also, product's(c) logos are detected by fine-tuned Inception_v3 logo detector model (for more information see model's section below). The transformed and analyzed data then loads into an AWS RDS server on a PostgreSQL database. Finally, a Metabase dashboard (setup on AWS EC2) is created for exploratory data analysis and visualization. The ETL job of the data pipeline and deployment of the models are **docker** containerized due to various dependencies of each step. In order to go over the flow of the project an example of a product is given below.

Assigning Guinness as the tag in the pipeline:
![Image and caption analysis of the scraped data](/dashboard.png)
![Sentiment analyzed posts with Guinness logo detected](/sentiment_image.png)
![Other posts with Guinness logo detected in the images](/guinness_logos.png)
**Metabase Dashboard**: 	http://15.188.14.225/public/dashboard/0d6a1d14-24d8-497a-92e8-784d383efae4

## Models:
**Sentiment Analysis Model**: This model was trained on the Tweets Sentiment Extraction data set from Kaggle using a pre-trained BERT base(12/768) model and SpaCy-Transformers for data pre-processing. The model can predict the sentiment of the post (negative, positive, or neutral) with 85% accuracy and 87% average F1 score.

Data: https://www.kaggle.com/c/tweet-sentiment-extraction/data

**Logo Detection Model**: This model was trained on FLICKRLOGOS-32 data set provided by the University of Augsburg, Institute of Computer Science. From the 32 logo classes available in the data set only 8 of them that were beer logos were used and an extra logo class (Hop-House 13) was added to the data. A highly accurate model was obtained by the fine-tuning Inception_V3 model and Keras image data generator. Finally, precision and recall of a specific class (Guinness) were drastically improved by labeling and adding only 20 new images from the real data into train data for re-training the model. This task can be done on the other classes by following the code in manual_labeling_and_retrain notebook.

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

Step-by-step codes and description of the model's training available in models folder in jupyter-notebook formats.


## Tech used:
- Python
- Docker
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
1. Install Docker:
`https://docs.docker.com/get-docker/ `



2. Clone this repository: git clone 
`https://github.com/Ayazdi/Track_the_feedback.git` 

3. Download TensorFlow models from here:
`https://www.dropbox.com/s/vanhum3y5rb5x2d/models.zip?dl=0`
   
and unzip the files into etl folder
4. Enter your Instagram credentials, Postgres and the tag you want to scrape in the config_example.py and copy it into etl and instagram_scraper
5. Go to the main folder of the project in the terminal and run docker-compose build and afterward docker-compose up.

## Contacts:
https://www.linkedin.com/in/amirali-yazdi-872b5460/

## License
Free software: MIT License
