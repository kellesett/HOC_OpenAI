from config_data.config import *
from scripts.open_window import open_window
from packages.console_design import system_message
from colorama import Fore, Back, Style


if __name__ == "__main__":
    system_message('Your personal bot console ready for farming!')

    while True:
        print(Fore.GREEN + Back.BLACK + Style.BRIGHT + 'User: ', end='')
        print(Style.RESET_ALL)
        command = input('>> ')

        match command:
            case 'quit':
                break
            case 'open':
                open_window(W_PATH, W_NAME, W_WIDTH, W_HEIGHT)
            case 'help':
                system_message('Here is commands list\n -> ' + '\n -> '.join(['{} - {}'.format(*com) for com in COMMANDS]))
            case _:
                system_message('Undefined command. Try help to see all available commands.')
