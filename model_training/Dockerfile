FROM behzadhakki/amirali_spacy:0.1


WORKDIR /app

RUN pip install pymongo
RUN pip install SQLAlchemy
RUN pip install psycopg2-binary
RUN pip install langdetect
RUN pip install Pillow

CMD python etl.py
