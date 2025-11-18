from .. import Object
import textwrap

class Label(Object):
	def __init__(self, content="", bindings=[], *children, **modifiers):
		super().__init__(bindings, *children, **modifiers)
		
		self.content = content

	def render(self, width, height):
		wrapped = textwrap.wrap(self.content, width=width)
		trimmed_lines = wrapped[:height]
		return "\n".join(trimmed_lines)
