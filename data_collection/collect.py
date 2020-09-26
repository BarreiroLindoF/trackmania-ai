from utils.grab_window import screenshot
import pynput
import numpy as np
import cv2
from datetime import datetime

CURRENT_KEYS = set()
TRAINING_DATA = {'fw_left': [], 'fw_right': [], 'bw_left': [], 'bw_right': [], 'fw': [], 'left': [], 'bw': [], 'right': []}
FPS = 30
TIME_BETWEEN_CAPTURE = 1 / FPS # How many seconds between capture to make it 30 FPS

LAST_CAPTURE_TIME = datetime.now()

keys_to_listen_for = {pynput.keyboard.Key.up, pynput.keyboard.Key.left,
                      pynput.keyboard.Key.down, pynput.keyboard.Key.right}

combinations = [{pynput.keyboard.Key.up, pynput.keyboard.Key.left},
                {pynput.keyboard.Key.up, pynput.keyboard.Key.right},
                {pynput.keyboard.Key.down, pynput.keyboard.Key.left},
                {pynput.keyboard.Key.down, pynput.keyboard.Key.right}]

def on_press(key):
    global CURRENT_KEYS, TRAINING_DATA, keys_to_listen_for, combinations, TIME_BETWEEN_CAPTURE, LAST_CAPTURE_TIME

    now = datetime.now()

    if (now - LAST_CAPTURE_TIME).total_seconds() < TIME_BETWEEN_CAPTURE:
        return

    LAST_CAPTURE_TIME = now

    """Save image and key output to list and append to TRAINING_DATA."""
    output = []

    if key == pynput.keyboard.KeyCode(char='p'):
        raise Exception

    if key in keys_to_listen_for:
        CURRENT_KEYS.add(key)
        if all(k in CURRENT_KEYS for k in combinations[0]):
            output = 'fw_left'
        elif all(k in CURRENT_KEYS for k in combinations[1]):
            output = 'fw_right'
        elif all(k in CURRENT_KEYS for k in combinations[2]):
            output = 'bw_left'
        elif all(k in CURRENT_KEYS for k in combinations[3]):
            output = 'bw_right'
        elif key == pynput.keyboard.Key.up:
            output = 'fw'
        elif key == pynput.keyboard.Key.left:
            output = 'left'
        elif key == pynput.keyboard.Key.down:
            output = 'bw'
        elif key == pynput.keyboard.Key.right:
            output = 'right'

    image = screenshot('Trackmania')
    images = TRAINING_DATA.get(output)
    images.append(image)


def on_release(key):
    global CURRENT_KEYS
    """Remove last key that was added to CURRENT_KEYS."""
    try:
        CURRENT_KEYS.remove(key)

    except KeyError:
        pass


with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    try:
        listener.join()
    except:
        pass

for key in TRAINING_DATA.keys():
    images = TRAINING_DATA[key]
    image_nb = 0
    for image in images:
        image.save('../data/' + key + '/' + str(image_nb) + '.jpeg')
        image_nb += 1



    # if key in keys_to_listen_for:
    #     CURRENT_KEYS.add(key)
    #     if all(k in CURRENT_KEYS for k in combinations[0]):
    #         output = [1, 0, 0, 0, 0, 0, 0, 0]
    #     elif all(k in CURRENT_KEYS for k in combinations[1]):
    #         output = [0, 1, 0, 0, 0, 0, 0, 0]
    #     elif all(k in CURRENT_KEYS for k in combinations[2]):
    #         output = [0, 0, 1, 0, 0, 0, 0, 0]
    #     elif all(k in CURRENT_KEYS for k in combinations[3]):
    #         output = [0, 0, 0, 1, 0, 0, 0, 0]
    #     elif key == pynput.keyboard.Key.up:
    #         output = [0, 0, 0, 0, 1, 0, 0, 0]
    #     elif key == pynput.keyboard.Key.left:
    #         output = [0, 0, 0, 0, 0, 1, 0, 0]
    #     elif key == pynput.keyboard.Key.down:
    #         output = [0, 0, 0, 0, 0, 0, 1, 0]
    #     elif key == pynput.keyboard.Key.right:
    #         output = [0, 0, 0, 0, 0, 0, 0, 1]

