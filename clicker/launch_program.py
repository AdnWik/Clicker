import logging
from pynput.mouse import Button, Controller

def launch_program(eventType, **kwargs):
    mouse = Controller()

    if eventType == 'set_mouse_position':
        x = getattr(kwargs, 'x')
        y = getattr(kwargs, 'y')

        mouse.position = (x, y)
        logging.info('Now we have moved it to {0}'.format(mouse.position))

        # Move pointer relative to current position
        mouse.move(x, y)
'''
    # Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)

    # Double click; this is different from pressing and releasing
    # twice on macOS
    mouse.click(Button.left, 2)

    # Scroll two steps down
    mouse.scroll(0, 2)
'''