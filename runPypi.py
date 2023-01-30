import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
import pathlib
import PIL
import numpy as np
classes = ['Blight', 'Common_Rust', 'Gray_Leaf_Spot', 'Healthy']

image_height=180
image_width=180

model = load_model('cnnModel.h5')


corn_rust_url = "healthy_leaf.jpg"
corn_rust_path = pathlib.Path(corn_rust_url)

img = keras.preprocessing.image.load_img(
    corn_rust_path, target_size=(image_height, image_width)
)
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(classes[np.argmax(score)], 100 * np.max(score))
)