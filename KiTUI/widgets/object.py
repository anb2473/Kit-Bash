class Object:
    def __init__(self, bindings=[], *children, **modifiers):
        self.children, self.modifiers = children, modifiers
        self.bindings = [self.parse_binding(b) for b in bindings]

    def parse_binding(self, key: str):
        key = key.lower()
        if key.startswith("ctrl+"):
            char = key[-1]
            return ord(char) & 0x1f
        elif key == "esc":
            return 27
        elif key == "enter":
            return 10
        elif key == "none":
            return -1
        else:
            # assume a single character
            return ord(key)
    
    def get_modifier(self, name, default=True):
        if name in self.modifiers:
            return self.modifiers[name]
        else:
            return default
    
    def read_texture(self, texture, kind):
        try:
            return texture[kind]
        except IndexError:
            return ""

    def on_focus(self, key):
        pass

    def render(self):
        pass
