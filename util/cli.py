import os
import time
from typing import List

def clear_screen() -> None:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def show_messages(messages: List[str], duration: int = 5, clear_first: bool = True) -> None:
    if not messages:
        return

    if clear_first:
        clear_screen()

    for message in messages:
        print(message)

    time.sleep(duration)

def show_message(message: str, duration: int = 5, clear_first: bool = True) -> None:
    show_messages([message], duration, clear_first)
