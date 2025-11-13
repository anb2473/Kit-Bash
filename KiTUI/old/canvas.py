from win_validator import WinValidator
from utils import *
from root import Root
from obj import *
from config import *
import sys

class Canvas(WinValidator):
    def __init__(self, root):
        super().__init__()
        self.validate()
        self.root = root
        hide_cursor()
        clear_terminal()

    def render(self):
        print('\033[4A\033[2K', end='')
        for obj in self.root.scene:
            obj.render()
        sys.stdout.flush()

if __name__ == "__main__":
    root = Root()
    canvas = Canvas(root)
    root.add(Rectangle(8, 8, 15, 15, BLUE, texture=RECTANGLE_DOUBLE))
    root.add(Text(10, 10, "hello world", BLUE, BACKGROUND_RED, BOLD, ITALIC))
    while True:
        canvas.render()