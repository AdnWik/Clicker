def show_menu(menu_options: list,
              submenu_name='',
              start_message='',
              end_message=''
              ) -> str:
    # TODO:
    if submenu_name:
        result = submenu_name.upper().center(50, '-') + '\n'
    else:
        result = ''

    if start_message:
        result += start_message + '\n\n'

    if menu_options:
        for number, option in enumerate(menu_options, 1):
            result += f'{number} - {option}\n'

    if end_message:
        result += '\n' + end_message
    else:
        result += '\nOther - EXIT'

    return result
