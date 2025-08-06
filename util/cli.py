import os
import time
from typing import List

from prettytable import PrettyTable

def clear_screen() -> None:
    """Clears the terminal screen."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def show_messages(messages: List[str], duration: int = 5, clear_first: bool = True) -> None:
    """Displays a list of messages on the terminal screen."""
    if not messages:
        return

    if clear_first:
        clear_screen()

    for message in messages:
        print(message)

    time.sleep(duration)

def show_message(message: str, duration: int = 5, clear_first: bool = True) -> None:
    """Displays a single message on the terminal screen."""
    show_messages([message], duration, clear_first)

def show_metrics(table: PrettyTable, clear_first: bool = True, clear_table: bool = True) -> None:
    """Displays a table on the terminal screen."""
    if clear_first:
        clear_screen()

    print(table)

    if clear_table:
        table.clear_rows()
