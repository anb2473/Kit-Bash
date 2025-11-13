from obj import Object
from .cursor import *

class Rectangle(Object):
    def __init__(self, x, y, width, height, *modifiers, texture=["╭", "─", "╮", "│", "╰", "╯"], ):
        super().__init__(x, y)
        self.width, self.height, self.modifiers = width, height, modifiers
        self.texture = texture

    def render(self):
        # Top border
        move_cursor(self.x, self.y)
        sys.stdout.write(f"{''.join(self.modifiers)}{self.texture[0]}{self.texture[1] * (self.width - 2) }{self.texture[2]}\033[0m")

        # Middle rows (only draw borders, skip inner spaces)
        for row in range(1, self.height - 1):
            # Left wall
            move_cursor(self.x, self.y + row)
            sys.stdout.write(f"{''.join(self.modifiers)}{self.texture[3]}\033[0m")

            # Right wall — jump instead of printing spaces
            if self.width > 1:
                move_cursor(self.x + self.width - 1, self.y + row)
                sys.stdout.write(f"{''.join(self.modifiers)}{self.texture[3]}\033[0m")

        # Bottom border
        if self.height > 1:
            move_cursor(self.x, self.y + self.height - 1)
            sys.stdout.write(f"{''.join(self.modifiers)}{self.texture[4]}{self.texture[1] * (self.width - 2)}{self.texture[5]}\033[0m")