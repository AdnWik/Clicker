from pathlib import Path
import json
import logging
from menu import show_menu
from launch_program import launch_program

logging.basicConfig(level=logging.DEBUG)

CUR_DIR = Path.cwd()
FOLDER = "clicker"
FOLDER_NAME = "programs"
FOLDER_PATH = Path.joinpath(CUR_DIR, FOLDER)
FOLDER_PATH = Path.joinpath(FOLDER_PATH, FOLDER_NAME)

print(' Welcome in Clicker! '.center(50, '='))
while True:
    message = 'Chose action'
    options = ['Available clikers', 'Record clicker']
    print(show_menu(options, start_message=message))
    user_choice = input('>>> ')

    if user_choice == '1':
        submenu = options[int(user_choice)-1]
        message = 'Which clicker do you want to run?'
        options = [file_name.stem for file_name in Path.iterdir(FOLDER_PATH)]
        print(show_menu(options, submenu, end_message=message))

        user_choice = input('>>> ')
        try:
            user_choice_idx = int(user_choice) - 1
        except ValueError:
            user_choice_idx = -1

        if user_choice_idx in range(0, len(options)):
            file_name = f'{options[user_choice_idx]}.json'
            file_path = Path.joinpath(FOLDER_PATH, file_name)
            with open(file_path, 'r', encoding='utf-8') as data:
                content = data.read()
                content = json.loads(content)

                for program_name, data in content.items():
                    print(program_name)
                    for step in data:
                        eventType = step['eventType']
                        kwargs = step['payload']
                        #launch_program(step['eventType'], step['payload'])

    else:
        break
