import sys

def move_cursor(x, y):
    sys.stdout.write(f"\033[{y};{x}H")

def cursor_up(n):
    sys.stdout.write(f"\033[{n}A")

def cursor_down(n):
    sys.stdout.write(f"\033[{n}B")

def cursor_right(n):
    sys.stdout.write(f"\033[{n}C")

def cursor_left(n):
    sys.stdout.write(f"\033[{n}D")

def hide_cursor():
    sys.stdout.write("\033[?25l")

def show_cursor():
    sys.stdout.write("\033[?25h")

def save_cursor_position():
    sys.stdout.write("\033[s")

def restor_cursor_postion():
    sys.stdout.write("\033[u")
    