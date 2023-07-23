from menu import show_menu


print(' Welcome in Clicker! '.center(50, '='))
while True:
    message = 'Chose action'
    options = ['Available clikers', 'Record clicker']
    print(show_menu(options, start_message=message))
    user_choice = input('>>> ')

    if user_choice == '1':
        submenu = options[int(user_choice)-1]
        message = 'Which clicker do you want to run?'
        options = [1, 2]
        print(show_menu(options, submenu, end_message=message))
    else:
        break
