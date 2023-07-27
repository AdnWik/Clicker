from pathlib import Path
from menu import show_menu

CUR_DIR = Path.cwd()

print(' Welcome in Clicker! '.center(50, '='))
while True:
    message = 'Chose action'
    options = ['Available clikers', 'Record clicker']
    print(show_menu(options, start_message=message))
    user_choice = input('>>> ')

    if user_choice == '1':
        folder = "clicker"
        folder_name = "programs"
        folder_path = Path.joinpath(CUR_DIR, folder)
        folder_path = Path.joinpath(folder_path, folder_name)

        submenu = options[int(user_choice)-1]
        message = 'Which clicker do you want to run?'
        options = [file_name.stem for file_name in Path.iterdir(folder_path)]
        print(show_menu(options, submenu, end_message=message))
    else:
        break
