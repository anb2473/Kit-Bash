def move_cursor(x, y):
    print(f"\033[{x};{y}]H")

def cursor_up(n):
    print(f"\033[{n}A")

def cursor_down(n):
    print(f"\033[{n}B")

def cursor_right(n):
    print(f"\033[{n}C")

def cursor_left(n):
    print(f"\033[{n}D")

def hide_cursor():
    print("\033[?25l")

def show_cursor():
    print("\033[?25h")

def save_cursor_position():
    print("\033[s")

def restor_cursor_postion():
    print("\033[u")
    