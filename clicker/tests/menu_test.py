from clicker.menu import show_menu


def test_show_menu():
    subemnu = 'submenu test'
    start_message = 'start'
    stop_message = 'stop'
    options = ['option_1', 'option_2', 'option_3']

    result = """-------------------SUBMENU TEST-------------------
start

1 - option_1
2 - option_2
3 - option_3

stop"""

    assert show_menu(options, subemnu, start_message, stop_message) == result
