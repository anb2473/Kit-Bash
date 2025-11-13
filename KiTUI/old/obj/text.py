from obj import Object
from .cursor import *

class Text(Object):
    def __init__(self, x, y, text, *modifiers):
        super().__init__(x, y)
        self.text, self.modifiers = text, modifiers

    def render(self):
        str_buffer = f"{''.join(modifier for modifier in self.modifiers)}{self.text}\033[0m"
        move_cursor(self.x, self.y)
        sys.stdout.write(str_buffer)
