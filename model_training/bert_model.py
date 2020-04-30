import bert
# from bert import BertModelLayer
from tensorflow.keras.models import model_from_json

def read_model():
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json, custom_objects={"BertModelLayer": bert.BertModelLayer})
    # load weights into new model
    loaded_model.load_weights("model.h5")
    return print(loaded_model.summary())
