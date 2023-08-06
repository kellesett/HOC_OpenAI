from colorama import init
from colorama import Fore, Back, Style
init()


def system_message(*args, mode: str = 'N') -> None:
    """
    :param mode: Specify color of text
        N - Neutral message with yellow color
        E - Error message
    :return:
    """

    match mode:
        case 'E':
            print(Fore.YELLOW + Back.RED + Style.BRIGHT + '\nS: | ERROR | ', end='')
        case 'N':
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + 'S: ', end='')
    print(*args)
    print(Style.RESET_ALL, end='')
