from colorama import init
from colorama import Fore, Back, Style
init()


def system_message(text, m_type: str = 'N') -> None:
    """
    :param text: Message text
    :param m_type: Specify color of text
        N - Neutral message with yellow color
        E - Error message
    :return:
    """

    match m_type:
        case 'E':
            print(Fore.YELLOW + Back.RED + Style.BRIGHT + 'S: | ERROR | ' + text)
        case 'N':
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + 'S: ', text)
