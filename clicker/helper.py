"""Read mouse position every two seconds"""
from pynput import mouse


def on_click(x, y, button, pressed):
    """Print mouse position on click

    Args:
        x (_type_): position x in pixels
        y (_type_): position y in pixels
        button (_type_): _description_
        pressed (_type_): _description_
    """
    print(f'x: {x} y: {y}')


with mouse.Listener(on_click=on_click) as listner:
    listner.join()
