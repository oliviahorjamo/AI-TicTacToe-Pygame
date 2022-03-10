import pygame
from services.renderer import Renderer


class GameMenuUi:
    """_A class that represents the game ui.

    Attributes:
            self.render (object) = renderer
            self.window (object) = renders the window
            self.square_size (int) = size of each square in the game_board
            self.white (object) = white color
    """
    def __init__(self, game_board):
        """A constructor of the class that initializes the game ui.

        Args:
            game_board (matrix): the game board
        """
        self.render = Renderer(750, 800, (0, 0, 0))
        self.window = self.render.window
        self.square_size = 30
        self.white = (250, 250, 250)
        self.game_board = game_board

    def draw_game_board(self):
        """A method to draw the game board.
        """
        for row in range(len(self.game_board.board)):
            for col in range(len(self.game_board.board)):
                rect = pygame.Rect(self.square_size * row,
                                   self.square_size * col,
                                   self.square_size, self.square_size)
                pygame.draw.rect(self.window, self.white, rect, 1)

    def draw_x(self, pos_row, pos_col):
        """A method to draw the X.

        Args:
            pos_row (int): row position to draw the X
            pos_col (int): col position to draw the X
        """
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
        """A method to draw the circle.

        Args:
            pos_row (int): row position to draw the circle.
            pos_col (int): col position to draw the circle.
        """
        col_pos = pos_row * self.square_size + self.square_size // 2
        row_pos = pos_col * self.square_size + self.square_size // 2 - 1
        pygame.draw.circle(self.window, self.white, (row_pos, col_pos), 12, 3)

    def draw_new_game_button(self):
        """A method to draw the new game button.
        """
        button_location = pygame.Rect(625, 760, 115, 25)
        pygame.draw.rect(self.window, self.white, button_location)
        font = pygame.font.SysFont('Times New Roman', 20)
        text = font.render('NEW GAME', False, (0, 0, 0))
        self.render.window.blit(text, (625, 760, 115, 30))

    def draw_new_game(self, mouse):
        """A method to find out if the user is clicking the new game button.

        Args:
            mouse (tuple): location where the user clicks the screen.

        Returns:
            True (boolean): if the user clicks the new game button.
            False (boolean): if the user does not click the new game button.
        """
        if pygame.Rect((pygame.Rect(624, 760, 115, 25))).collidepoint(mouse):
            return True
        return False

    def draw_text(self, text):
        """A method to create base for text logic.

        Args:
            text (string): the text
        """
        font = pygame.font.SysFont('Times New Roman', 20)
        text = font.render(f'{text}', False, (250, 250, 250))
        self.render.window.blit(text, (20, 760, 115, 30))

    def draw_show_ai_turn(self):
        """A method to show that it is Ai's turn.
        """
        location = pygame.Rect(15, 760, 200, 25)
        pygame.draw.rect(self.window, (0, 0, 0), location)
        self.draw_text('AI IS THINKING...')

    def draw_show_human_turn(self):
        """A method to show that it is human's turn.
        """
        location = pygame.Rect(15, 760, 200, 25)
        pygame.draw.rect(self.window, (0, 0, 0), location)
        self.draw_text('YOUR TURN!')

    def draw_who_won(self, player):
        """A method to show who won the game

        Args:
            player (int): the player in turn.
        """
        location = pygame.Rect(15, 760, 200, 25)
        pygame.draw.rect(self.window, (0, 0, 0), location)
        if player == 1:
            self.draw_text('YOU WON!')
        else:
            self.draw_text('AI WON!')

    def draw_tie(self):
        """A method to show that there is a tie in the game.
        """
        location = pygame.Rect(15, 760, 200, 25)
        pygame.draw.rect(self.window, (0, 0, 0), location)
        self.draw_text('TIE!')
