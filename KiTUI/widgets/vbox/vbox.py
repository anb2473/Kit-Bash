from .. import Object

class VBox(Object):
    def __init__(self, bindings=[], *children, **modifiers):
        super().__init__(bindings, children, modifiers)

    def on_focus(self, key):
        pass

    def render(self, width, height):
        if width < 2 or height < 2:
            return ""  # too small to draw a box

        top = "┌" + "─" * (width - 2) + "┐"
        middle = ("│" + " " * (width - 2) + "│\n") * (height - 2)
        bottom = "└" + "─" * (width - 2) + "┘"

        return top + "\n" + middle + bottom