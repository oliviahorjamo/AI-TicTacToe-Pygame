import pygame
from services.renderer import Renderer


class GameMenuUi:
    def __init__(self, game_board):
        self.render = Renderer(750, 800, (0, 0, 0))
        self.window = self.render.window
        self.square_size = 30
        self.white = (250, 250, 250)
        self.game_board = game_board

    def draw_game_board(self):
        for row in range(len(self.game_board.board)):
            for col in range(len(self.game_board.board)):
                rect = pygame.Rect(self.square_size * row,
                                   self.square_size * col,
                                   self.square_size, self.square_size)
                pygame.draw.rect(self.window, self.white, rect, 1)

    def draw_x(self, pos_row, pos_col):
        col_pos = pos_row * self.square_size
        row_pos = pos_col * self.square_size
        pygame.draw.line(self.window, self.white,
                         (row_pos, col_pos),
                         (row_pos + self.square_size,
                          col_pos + self.square_size),
                         4)
        pygame.draw.line(self.window, self.white,
                         (row_pos + 30, col_pos),
                         (row_pos,
                          col_pos + self.square_size),
                         4)

    def draw_circle(self, pos_row, pos_col):
        col_pos = pos_row * self.square_size + self.square_size // 2
        row_pos = pos_col * self.square_size + self.square_size // 2 - 1
        pygame.draw.circle(self.window, self.white, (row_pos, col_pos), 12, 3)

    def draw_new_game_button(self):
        button_location = pygame.Rect(625, 760, 115, 25)
        pygame.draw.rect(self.window, self.white, button_location)
        font = pygame.font.SysFont('Times New Roman', 20)
        text = font.render('NEW GAME', False, (0, 0, 0))
        self.render.window.blit(text, (625, 760, 115, 30))

    def draw_new_game(self, mouse):
        if pygame.Rect((pygame.Rect(624, 760, 115, 25))).collidepoint(mouse):
            return True
        return False

    def draw_whose_turn(self, text):
        font = pygame.font.SysFont('Times New Roman', 20)
        text = font.render(f'{text}', False, (250, 250, 250))
        self.render.window.blit(text, (20, 760, 115, 30))

    def draw_show_ai_turn(self):
        location = pygame.Rect(15, 760, 200, 25)
        pygame.draw.rect(self.window, (0, 0, 0), location)
        self.draw_whose_turn('AI IS THINKING...')

    def draw_show_human_turn(self):
        location = pygame.Rect(15, 760, 200, 25)
        pygame.draw.rect(self.window, (0, 0, 0), location)
        self.draw_whose_turn('YOUR TURN!')

    def draw_reset_game_board(self):
        self.draw_game_board()
        pygame.display.update()
        self.window.fill((0, 0, 0))
