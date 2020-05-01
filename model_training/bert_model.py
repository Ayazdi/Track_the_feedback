import numpy as np
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing import sequence

from bert import BertModelLayer
import bert

from spacy_transformers import TransformersLanguage, TransformersWordPiecer, TransformersTok2Vec


name = "bert-base-uncased"
nlp = TransformersLanguage(trf_name=name, meta={"lang": "en"})
nlp.add_pipe(nlp.create_pipe("sentencizer"))
nlp.add_pipe(TransformersWordPiecer.from_pretrained(nlp.vocab, name))
nlp.add_pipe(TransformersTok2Vec.from_pretrained(nlp.vocab, name))



def load_bert_model():
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json, custom_objects={"BertModelLayer": bert.BertModelLayer})
    # load weights into new model
    return loaded_model.load_weights("model.h5")


def sentiment_prediction(text):
    doc = nlp(text)
    word_id = doc._.trf_word_pieces
    word_id = sequence.pad_sequences([word_id], maxlen = 112, padding='pre')
    y_pred = loaded_model.predict(word_id, verbose=0)
    y_pred_bool = np.argmax(y_pred, axis=1)[0]

    if y_pred_bool == 0:
        prediction = "neuteral"
    if y_pred_bool == 1:
        prediction = "positive"
    else:
        prediction = "negative"

    return prediction


if __name__ == '__main__':

    loaded_model = load_bert_model()
    sentiment_prediction('I love Spiced Academy')
