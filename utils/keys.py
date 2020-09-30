from utils.key_handler import press_key, release_key, UP, DOWN, LEFT, RIGHT


def forward():
    press_key(UP)
    release_key(DOWN)
    release_key(LEFT)
    release_key(RIGHT)


def left():
    release_key(UP)
    release_key(DOWN)
    press_key(LEFT)
    release_key(RIGHT)


def right():
    release_key(UP)
    release_key(DOWN)
    release_key(LEFT)
    press_key(RIGHT)


def reverse():
    release_key(UP)
    press_key(DOWN)
    release_key(LEFT)
    release_key(RIGHT)


def forward_left():
    press_key(UP)
    release_key(DOWN)
    press_key(LEFT)
    release_key(RIGHT)


def forward_right():
    press_key(UP)
    release_key(DOWN)
    release_key(LEFT)
    press_key(RIGHT)


def reverse_left():
    release_key(UP)
    press_key(DOWN)
    press_key(LEFT)
    release_key(RIGHT)


def reverse_right():
    release_key(UP)
    press_key(DOWN)
    release_key(LEFT)
    press_key(RIGHT)


def pressKey(state_id: int):
    if state_id == 0:
        reverse()
    elif state_id == 1:
        reverse_left()
    elif state_id == 2:
        reverse_right()
    elif state_id == 3:
        forward()
    elif state_id == 4:
        forward_left()
    elif state_id == 5:
        forward_right()
    elif state_id == 6:
        left()
    elif state_id == 7:
        right()
