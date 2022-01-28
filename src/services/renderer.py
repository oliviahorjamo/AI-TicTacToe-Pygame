import pygame

class Renderer:
    def __init__(self, display_width, display_height, display_color):
        self.display_width = display_width
        self.display_height = display_height
        self.display_color = display_color
        pygame.display.set_mode((self.display_width, self.display_height))
        self.window = pygame.display.get_surface()
        self.window.fill(self.display_color)

