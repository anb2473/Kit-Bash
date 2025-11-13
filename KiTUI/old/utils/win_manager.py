import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_win_size():
    size = os.get_terminal_size()
    return size.columns, size.lines

