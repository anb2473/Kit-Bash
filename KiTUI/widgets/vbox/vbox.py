from widgets.object import Object
import keyboard

class VBox(Object):
    def __init__(self, bindings=[], *children, **modifiers):
        super().__init__(bindings, children, modifiers)

    def on_focus(self):
        pass

    def render(self):
        pass