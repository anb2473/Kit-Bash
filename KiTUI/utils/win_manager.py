import os

def get_win_size():
    size = os.get_terminal_size()
    return size.columns, size.lines