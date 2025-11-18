from .. import Object
from .vbox_textures import *

class VBox(Object):
    def __init__(self, bindings=[], *children, **modifiers):
        super().__init__(bindings, *children, **modifiers)
        
        # Init border texture
        self.border_style = self.get_modifier("border_style", "_default")
        self.border_texture = vbox_border_textures.get(self.border_style)
        
    def on_focus(self, key):
        pass

    def render(self, width, height):
        if width < 2 or height < 2:
            return ""  # too small to draw a box

        top = self.read_texture(self.border_texture, TOP_LEFT) + self.read_texture(self.border_texture, BOTTOM) * (width - 2) \
                + self.read_texture(self.border_texture, TOP_RIGHT)
        middle = (self.read_texture(self.border_texture, SIDE) + " " * (width - 2) + self.read_texture(self.border_texture, SIDE) \
                + "\n") * (height - 2)
        bottom = self.read_texture(self.border_texture, BOTTOM_LEFT) + self.read_texture(self.border_texture, BOTTOM) * (width - 2) \
                + self.read_texture(self.border_texture, BOTTOM_RIGHT)

        return top + "\n" + middle + bottom
