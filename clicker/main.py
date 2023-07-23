from menu import show_menu


print(' Welcome in Clicker! '.center(50, '='))
while True:
    message = 'What do you want to do?'
    options = ['Test', 'tests']
    print(show_menu(message, options))
    user_choice = input('>>> ')

    if user_choice == '1':
        pass
    else:
        break
