"""Controler class"""
from time import sleep
import pynput


class Controller:
    """Controler for mouse and keyboard
    """

    def __init__(self) -> None:
        self.mouse = pynput.mouse.Controller()
        self.keyboard = pynput.keyboard.Controller()

    @staticmethod
    def wait(seconds: int):
        """Sleep program

        Args:
            seconds (int): waiting time in seconds
        """
        sleep(seconds)

    def set_mouse_position(self, x: int, y: int):
        """Set mouse position in pixels

        Args:
            x (int): x coordinates in pixels
            y (int): y coordinates in pixels
        """
        self.mouse.position = (x, y)

    def mouse_scroll(self, scroll: int):
        """Scroll on mouse

        Args:
            scroll (int): scroll value
        """
        self.mouse.scroll(0, scroll)

    def click_mouse_button(self, button: str):
        """Click mouse button

        Args:
            button (str): Mouse button to click
        """
        self.mouse.press(button)
        sleep(0.1)
        self.mouse.release(button)

    def move_and_click(self, x, y, button):
        """Move mouse and click button

        Args:
            x (_type_): x coordinates in pixels
            y (_type_): y coordinates in pixels
            button (_type_): mouse button to click
        """
        self.set_mouse_position(x, y)
        self.click_mouse_button(button)

    def keyboard_typing(self, text: str):
        """Typing on keyboard

        Args:
            text (str): text to type
        """
        self.keyboard.type(text)

    def keyboard_click_button(self, button: str):
        """Click button on keyboard

        Args:
            button (str): button name
        """
        self.keyboard.press(button)
        sleep(0.1)
        self.keyboard.release(button)

    def keyboard_typing_and_click(self, text: str, button: str):
        """Typing on keyboard and click button

        Args:
            text (str): text to typing
            button (str): button to click
        """
        self.keyboard_typing(text)
        self.keyboard_click_button(button)
