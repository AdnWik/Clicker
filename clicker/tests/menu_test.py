from clicker.menu import show_menu


def test_show_menu_all_options():
    subemnu = 'submenu test'
    start_message = 'start'
    stop_message = 'stop'
    options = ['option_1', 'option_2', 'option_3']

    result = show_menu(options, subemnu, start_message, stop_message).split('\n')

    submenu_result = subemnu.upper().center(50, '-')
    start_result = start_message
    options_result = f'2 - {options[1]}'
    stop_result = stop_message

    assert submenu_result == result[0]
    assert start_result == result[1]
    assert options_result == result[4]
    assert stop_result == result[-1]


def test_show_menu_without_submenu():
    start_message = 'start'
    stop_message = 'stop'
    options = ['option_1', 'option_2', 'option_3']

    result = show_menu(options, start_message=start_message, end_message=stop_message).split('\n')

    start_result = start_message
    options_result = f'2 - {options[1]}'
    stop_result = stop_message

    assert start_result == result[0]
    assert options_result == result[3]
    assert stop_result == result[-1]


def test_show_menu_without_start_message():
    subemnu = 'submenu test'
    stop_message = 'stop'
    options = ['option_1', 'option_2', 'option_3']

    result = show_menu(options, subemnu, end_message=stop_message).split('\n')

    submenu_result = subemnu.upper().center(50, '-')
    options_result = f'2 - {options[1]}'
    stop_result = stop_message

    assert submenu_result == result[0]
    assert options_result == result[2]
    assert stop_result == result[-1]


def test_show_menu_without_end_message():
    subemnu = 'submenu test'
    start_message = 'start'
    options = ['option_1', 'option_2', 'option_3']

    result = show_menu(options, subemnu, start_message).split('\n')

    submenu_result = subemnu.upper().center(50, '-')
    start_result = start_message
    options_result = f'2 - {options[1]}'

    assert submenu_result == result[0]
    assert start_result == result[1]
    assert options_result == result[4]
