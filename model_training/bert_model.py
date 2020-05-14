import numpy as np
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing import sequence

from bert import BertModelLayer
import bert

from spacy_transformers import TransformersLanguage, TransformersWordPiecer, TransformersTok2Vec
from load_transform import extract_from_mongodb, extract_data_from_json

import logging
# spacy-transformers pipeline for preprocessing
name = "bert-base-uncased"
nlp = TransformersLanguage(trf_name=name, meta={"lang": "en"})
nlp.add_pipe(nlp.create_pipe("sentencizer"))
nlp.add_pipe(TransformersWordPiecer.from_pretrained(nlp.vocab, name))
nlp.add_pipe(TransformersTok2Vec.from_pretrained(nlp.vocab, name))



def load_bert_model():
    """
    load the saved trained bert model
    """
    logging.critical("Loading BERT model...")
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json, custom_objects={"BertModelLayer": bert.BertModelLayer})
    # load weights into new model
    loaded_model.load_weights("model.h5")
    logging.critical("Model is ready.")
    return loaded_model

loaded_model = load_bert_model()

def sentiment_prediction(text):
    """
    Sentiment prediction by preproccessing the text with spacy into word id

    text: the comment for sentiment analysis (str)

    return: prediction - positive, negative or neuteral (str)
    """
    try:
        logging.critical(text)
        doc = nlp(text)
        word_id = doc._.trf_word_pieces
        word_id = sequence.pad_sequences([word_id], maxlen = 112, padding='pre')
        y_pred = loaded_model.predict(word_id, verbose=0)

        y_pred_bool = np.argmax(y_pred, axis=1)[0]
        if y_pred_bool == 0:
            prediction = "neutral"
        if y_pred_bool == 1:
            prediction = "positive"
        if y_pred_bool == 2:
            prediction = "negative"
        logging.critical(prediction)
    except:
        prediction = None
    return prediction


# if __name__ == '__main__':
#     json = extract_from_mongodb()
#     loaded_model = load_bert_model()
#     print(sentiment_prediction('kfc i ve been now working on food items iam happy how it turned out but the usage of bad colors affect the artworks if you want to see more such artworks please comment and do follow'
# ))
