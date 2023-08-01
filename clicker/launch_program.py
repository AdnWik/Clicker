import logging
from time import sleep
import pynput


def launch_program(eventType, **kwargs):
    mouse = pynput.mouse.Controller()
    keyboard = pynput.keyboard.Controller()

    if eventType == 'set_mouse_position':
        x = kwargs['x']
        y = kwargs['y']

        mouse.position = (x, y)
        logging.info('Now we have moved it to {0}'.format(mouse.position))

    elif eventType == 'wait':
        seconds = kwargs['seconds']
        logging.info('Wait {0} seconds'.format(seconds))
        sec = kwargs['seconds']
        sleep(sec)

    elif eventType == 'press_mouse_button':
        button = kwargs['button']
        if button == 'left':
            mouse.press(pynput.mouse.Button.left)
            mouse.release(pynput.mouse.Button.left)
        elif button == 'right':
            mouse.press(pynput.mouse.Button.right)
            mouse.release(pynput.mouse.Button.right)

    elif eventType == 'keyboard_type':
        type_string = kwargs['type']
        keyboard.type(type_string)

    elif eventType == 'mouse_scroll':
        scroll = kwargs['scroll']
        mouse.scroll(0, scroll)

    elif eventType == 'keyboard_press':
        button = kwargs['button']
        keyboard.press(button)
        keyboard.release(button)
