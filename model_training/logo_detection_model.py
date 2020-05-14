import numpy as np
from tensorflow.keras.models import model_from_json
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import logging
from PIL import Image
import urllib.request
import numpy as np


labels = {0: 'guinness',
         1: 'hop-house',
         2: 'fosters',
         3: 'carlsberg',
         4: 'becks',
         5: 'corona',
         6: 'heineken',
         7: 'paulaner',
         8: 'no-logo'}

def load_logo_model(model):
    """
    load the saved trained logo detection model
    """
    # logging.critical("Loading logo detection model...")
    json_file = open(f'{model}.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(f"{model}.h5")
    # logging.critical("Model is ready.")
    return loaded_model


model = load_logo_model('beer_logo_model')


def logo_detection(image_url):
    """
    Detects beer logos in every images

    image_url: posts images urls (str)

    return: detected logo in the image or no-logo (str)
    """
    # load image from the url
    img = Image.open(urllib.request.urlopen(image_url))

    # trasnform to a desireable tensor for the model
    img = img.resize((224,224), Image.ANTIALIAS)

    x = img_to_array(img)/255.
    x = x.reshape((1,) + x.shape)

    # prediction
    result = model.predict(x)
    prediction = np.argmax(result)

    prediction = labels[prediction]
    logging.critical(prediction)

    return prediction
