def show_menu(start_message: str, menu_options: list, submenu_name='') -> str:
    """Create numbered menu with submenu name

    Args:
        start_message (str): message before numbered options
        menu_options (list): options to be numbered
        submenu_name (str, optional): submenu name . Defaults to ''.

    Returns:
        str: numbered menu with submenu name
    """

    if submenu_name:
        result = submenu_name.upper().center(50, '-') + '\n'
    else:
        result = ''

    result += start_message + '\n'
    if menu_options:
        for number, option in enumerate(menu_options, 1):
            result += f'{number} - {option}\n'
    result += '\nOther - EXIT'
    return result
