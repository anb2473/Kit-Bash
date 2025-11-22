from .. import Object
from .vbox_textures import *
import math
from ...logger import logger

class VBox(Object):
	def __init__(self, *children, bindings=[], **modifiers):
		super().__init__(bindings, *children, **modifiers)
        
		# Init border texture
		self.border_style = self.get_modifier("border_style", "_default")
		self.border_texture = vbox_border_textures.get(self.border_style)

		# Init layout
		self.padding = self.get_modifier("padding", "0")
		self.padding_left = int(self.get_modifier("padding_left", self.padding)) 
		self.padding_right = int(self.get_modifier("padding_right", self.padding))
		self.padding_top = int(self.get_modifier("padding_top", self.padding))
		self.padding_bottom = int(self.get_modifier("padding_bottom", self.padding))
		
		self.spacing = int(self.get_modifier("spacing", 0))

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

		# Add child ojects
		num_of_children = len(self.children)
		total_height = height - self.padding_top - self.padding_bottom
		height_per_child = math.floor((total_height - min(self.spacing * num_of_children, total_height)) / num_of_children) 
		y = self.padding_top
		for child in self.children:
			x = self.padding_left
			width = width - self.padding_left - self.padding_right
			height = height_per_child
			child_frame = child.render(width, height)
			frame = self.append_child_frame(frame, child_frame, x, y)
			y += height + self.spacing

		return frame
