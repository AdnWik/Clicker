import logging
from time import sleep
import pynput


class Controler:

    def __init__(self) -> None:
        self.mouse = pynput.mouse.Controller()
        self.keyboard = pynput.keyboard.Controller()

    def set_mouse_possition(self, x, y):
        self.mouse.position(x, y)

    def click_mouse_button(self, button):
        self.mouse.press(button)
        sleep(0.1)
        self.mouse.release(button)

    def move_and_click(self, x, y, button):
        self.mouse.position(x, y)
        self.mouse.press(button)
        sleep(0.1)
        self.mouse.release(button)

    def typing(self, text):
        self.keyboard.type(text)



def launch_program(eventType, **kwargs):
    """ TODO: """
    mouse = pynput.mouse.Controller()
    keyboard = pynput.keyboard.Controller()

    if eventType == 'set_mouse_position':
        x = kwargs['x']
        y = kwargs['y']

        mouse.position = (x, y)
        logging.info('Now we have moved it to %s', mouse.position)

    elif eventType == 'wait':
        seconds = kwargs['seconds']
        logging.info('Wait %s seconds', seconds)
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
        if button == 'enter':
            keyboard.press(pynput.keyboard.Key.enter)
            keyboard.release(pynput.keyboard.Key.enter)
            logging.info('Press key %s', button)
