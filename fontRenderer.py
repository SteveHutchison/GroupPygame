#fontRenderer
import pygame

class FontRenderer:
	def __init__(self):
		self.font = pygame.font.Font(None, 36)
		self.title = pygame.font.Font(None, 72)
		self.font_colour = (255, 100, 50)
		self.title_colour = (255, 0, 0)

	# string = the prefix
	# var    = the variable
	# position = where you want it
	# target = what you want to render to
	def draw_stat(self, string, var, position, target):
		textString = self.font.render(string, 1, self.font_colour)
		varString = self.font.render(str(var), 1, self.font_colour)
		textPos = position
		varPos  = (position[0] + textString.get_width(), position[1])
		target.blit(textString, textPos)
		target.blit(varString, varPos)

	def draw(self, string, position, target):
		text = self.font.render(string, 1, self.font_colour)
		target.blit(text, position)

	def draw_title(self, string, position, target):
		text = self.title.render(string, 1, self.title_colour)
		target.blit(text, position)

