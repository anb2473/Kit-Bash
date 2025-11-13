from obj import *

class Root:
    def __init__(self):
        self.scene = []

    def add(self, obj):
        if not isinstance(obj, Object):
            raise ValueError("Cannot mount non object to root")
        self.scene.append(obj)