from obj import Object
from .cursor import *

class Text(Object):
    def __init__(self, x, y, text, color=""):
        super().__init__(x, y)
        self.text, self.color = text, color

    def render(self):
        str_buffer = f"{self.color}{self.text}{self.color}"
        move_cursor(self.x, self.y)
        sys.stdout.write(str_buffer)
