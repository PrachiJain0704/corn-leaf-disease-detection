import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from tensorflow.keras.utils import load_img
import pathlib
import PIL
import numpy as np

def names(number):
    if number==0:
        return "It's a leaf with disease BLIGHT"
    elif number==1:
        return "It's a leaf with disease Common Rust"
    elif number==2:
        return "It's a leaf with disease Gray_Leaf_Spot"
    elif number==3:
        return "It's a Healthy leaf"

def Predictions(img,model):
    # imgage = load_img(img,target_size=(224, 224),grayscale=False,
    # color_mode='rgb')
    x = np.array(img.resize((224,224)))
    x = x.reshape(1,224,224,3)
    res = model.predict_on_batch(x)
    classification = np.where(res == np.amax(res))[1][0]
    return str(res[0][classification]*100) + '% Confidence.- ' + names(classification)

def predict(files):
    classes = ['Blight', 'Common_Rust', 'Gray_Leaf_Spot', 'Healthy']

    image_height=180
    image_width=180

    model = load_model('VGG16Model.h5')
    res = Predictions(files,model)

    return res

    
          
    