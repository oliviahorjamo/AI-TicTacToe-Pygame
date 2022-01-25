import pygame
from services.renderer import Renderer
from services.game_board import GameBoard

class GameMenuUi:
    def __init__(self):
        self.render = Renderer(450, 450, (0, 0, 0))
        self.window = self.render.window
        self.square_size = 30
        self.white = (250, 250, 250)
        self.game_board = GameBoard()

    def draw_game_board(self):

        for row in range(0, self.game_board.grid_size):
            for col in range(0, self.game_board.grid_size):
                rect = pygame.Rect(self.square_size * row,
                                    self.square_size * col,
                                    self.square_size, self.square_size)
                pygame.draw.rect(self.window, self.white, rect, 1)

    def draw_x(self, pos_row, pos_col): # tää kesken
        for i in range(6):
            pygame.draw.aaline(self.window, self.white, (pos_row + i, pos_col), (self.game_board.grid_size + pos_col + i, self.game_board.grid_size + pos_col), 1)


    def draw_circle(self):
        for row in range(self.game_board.grid_size):
            for col in range(self.game_board.grid_size):
                pygame.draw.circle()



    def draw_new_game_button(self):
        button_location = pygame.Rect(320, 10, 115, 25)
        pygame.draw.rect(self.window, self.white, button_location)
        font = pygame.font.SysFont('Times New Roman', 20)
        text = font.render('NEW GAME', False, (0, 0, 0))
        self.render.window.blit(text, (320, 10, 115, 30))

    def new_game(self, mouse):
        if pygame.Rect((pygame.Rect(320, 10, 115, 25))).collidepoint(mouse):
            return True
        return False
