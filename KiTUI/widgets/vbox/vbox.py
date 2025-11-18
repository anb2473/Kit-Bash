from .. import Object
from .vbox_textures import *

class VBox(Object):
	def __init__(self, *children, bindings=[], **modifiers):
		super().__init__(bindings, *children, **modifiers)
        
		# Init border texture
		self.border_style = self.get_modifier("border_style", "_default")
		self.border_texture = vbox_border_textures.get(self.border_style)
        
	def on_focus(self, key):
		pass

	def append_child_frame(self, frame, child_frame, x, y):
		child_frame_lines = child_frame.split("\n")
		frame_lines = frame.split("\n")	
		for i, line in enumerate(child_frame_lines):
			rel_y = y + i
			if 0 <= rel_y < len(frame): # ensure y in bounds
				row = frame_lines[rel_y]
				new_row = row[:x] + line + row[(x + len(line) - 1):]
				frame_lines[rel_y] = new_row[:len(row)] # clip to ensure line remains in bounds
		return "\n".join(frame_lines)

	def render(self, width, height):
		if width < 2 or height < 2:
			return ""  # too small to draw a box

		# Generate VBOX frame
		top = self.read_texture(self.border_texture, TOP_LEFT) + self.read_texture(self.border_texture, BOTTOM) * (width - 2) \
				+ self.read_texture(self.border_texture, TOP_RIGHT)
		middle = (self.read_texture(self.border_texture, SIDE) + " " * (width - 2) + self.read_texture(self.border_texture, SIDE) \
				+ "\n") * (height - 2)
		bottom = self.read_texture(self.border_texture, BOTTOM_LEFT) + self.read_texture(self.border_texture, BOTTOM) * (width - 2) \
				+ self.read_texture(self.border_texture, BOTTOM_RIGHT)

		frame = top + "\n" + middle + bottom

		# Add child objects

		for child in self.children:
			x = 1
			y = 1
			width = width - 2
			height = 1
			child_frame = child.render(width, height)
			frame = self.append_child_frame(frame, child_frame, x, y)
		

		return frame
