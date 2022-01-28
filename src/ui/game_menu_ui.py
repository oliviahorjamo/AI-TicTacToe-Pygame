import pygame
from services.renderer import Renderer
from services.game_board import GameBoard

class GameMenuUi:
    def __init__(self):
        self.render = Renderer(800, 868, (0, 0, 0))
        self.window = self.render.window
        self.square_size = 32
        self.white = (250, 250, 250)
        self.game_board = GameBoard()

    def draw_game_board(self):
        for row in range(self.game_board.grid_size):
            for col in range(self.game_board.grid_size):
                rect = pygame.Rect(self.square_size * row,
                                    63 + self.square_size * col,
                                    self.square_size, self.square_size)
                pygame.draw.rect(self.window, self.white, rect, 1)

    def draw_x(self, pos_row, pos_col):
        row_pos = pos_row * self.square_size
        col_pos = pos_col * self.square_size
        if col_pos >= 60:
            pygame.draw.aaline(self.window,self.white,
                                    (row_pos, col_pos),
                                    (row_pos + self.square_size,
                                    col_pos + self.square_size),
                                    4)
            pygame.draw.aaline(self.window,self.white,
                                    (row_pos + 30, col_pos),
                                    (row_pos,
                                    col_pos + self.square_size),
                                    4)

    def draw_circle(self, pos_row, pos_col):
        row_pos = pos_row * self.square_size + self.square_size // 2
        col_pos = pos_col * self.square_size + self.square_size // 2 + 2
        if col_pos > 63:
            pygame.draw.circle(self.window, self.white, (row_pos, col_pos), 10, 2)


    def draw_new_game_button(self):
        button_location = pygame.Rect(620, 20, 115, 25)
        pygame.draw.rect(self.window, self.white, button_location)
        font = pygame.font.SysFont('Times New Roman', 20)
        text = font.render('NEW GAME', False, (0, 0, 0))
        self.render.window.blit(text, (620, 20, 115, 30))

    def new_game(self, mouse):
        if pygame.Rect((pygame.Rect(320, 20, 115, 25))).collidepoint(mouse):
            return True
        return False

    def whose_turn(self, player):
        font = pygame.font.SysFont('Times New Roman', 20)
        turn = f'In turn: Player{player}'
        text = font.render(turn, False, (250, 250, 250))
        self.render.window.blit(text, (620, 20, 115, 30))