import json
import logging
from controller import Controller

class Process:

    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.steps = []
        self.controller = Controller()

    def load_steps(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            self.steps = json.load(file)

    def start(self):
        options = {
            'set_mouse_position': self.controller.set_mouse_position
        }

        for program_name in self.steps:
            for steps in self.steps[program_name]:
                try:
                    options[steps["eventType"]](**steps["payload"])
                    logging.debug('{} - {}'.format(steps["eventType"], steps["payload"]))
                except KeyError as error:
                    logging.debug('KeyError: {}'.format(error))
                    break
