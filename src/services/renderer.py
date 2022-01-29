import pygame

class Renderer:
    """A class that represents the handling of rendering in the game."""

    def __init__(self, display_width, display_height, display_color):
        """A constructor of the class that initializes the display.

        Attributes:
                self.display_width: display width
                self.display_height: display height
                self.display_color: display color
        """
        self.display_width = display_width
        self.display_height = display_height
        self.display_color = display_color
        pygame.display.set_mode((self.display_width, self.display_height))
        self.window = pygame.display.get_surface()
        self.window.fill(self.display_color)
