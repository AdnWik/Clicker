from clicker.menu import show_menu


def test_show_menu():
    subemnu = 'submenu test'
    start_message = 'start'
    stop_message = 'stop'
    options = ['option-1', 'option_2', 'option_3']

    print(show_menu(options, subemnu, start_message, stop_message))