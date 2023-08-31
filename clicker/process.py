"""Process class"""
import json
import logging
from controller import Controller


class Process:
    """Process the program
    """

    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.steps = []
        self.controller = Controller()

    def load_steps(self):
        """Load program steps from JSON file
        """
        with open(self.file_path, 'r', encoding='utf-8') as file:
            self.steps = json.load(file)

    def start(self):
        """Executes the program from steps
        """
        options = {
            'set_mouse_position': self.controller.set_mouse_position,
            'press_mouse_button': self.controller.click_mouse_button,
            'wait': self.controller.wait,
            'keyboard_type': self.controller.keyboard_typing,
            'keyboard_press': self.controller.keyboard_click_button
        }

        for program_name in self.steps:
            for steps in self.steps[program_name]:
                try:
                    options[steps["eventType"]](**steps["payload"])
                    logging.debug('{} - {}'.format(steps["eventType"], steps["payload"]))
                except KeyError as error:
                    logging.debug('KeyError: {}'.format(error))
                    break
