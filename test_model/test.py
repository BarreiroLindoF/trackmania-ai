import tensorflow as tf
import numpy as np
from utils.grab_window import screenshot
from utils.keys import pressKey
from datetime import datetime

from utils.key_handler import key_check, press_key, UP

model = tf.keras.models.load_model('../models/saved/cnn.h5')
FPS = 30
TIME_BETWEEN_CAPTURE = 1 / FPS # How many seconds between capture to make it 30 FPS

LAST_CAPTURE_TIME = datetime.now()

for i in range(10000000):

    now = datetime.now()

    if (now - LAST_CAPTURE_TIME).total_seconds() < TIME_BETWEEN_CAPTURE:
        continue

    LAST_CAPTURE_TIME = now

    image = screenshot('Trackmania')
    image_array = tf.keras.preprocessing.image.img_to_array(image.resize((180, 180)))
    image_array = np.expand_dims(image_array, axis=0)
    predictions = model.predict(image_array)
    pressKey(np.argmax(predictions))

