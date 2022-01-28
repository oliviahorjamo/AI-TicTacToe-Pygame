import pygame
import sys
from entities.ai_player import AiPlayer
from entities.human_player import HumanPlayer
from services.game_board import GameBoard
from services.game import Game
from services.renderer import Renderer
from ui.game_menu_ui import GameMenuUi


def main():
    pygame.init()
    game = Game()
    ai_player = AiPlayer()
    renderer = Renderer(450, 450, (0, 0, 0))
    game_ui = GameMenuUi()
    game_board = GameBoard()
    human_turn = False



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if pygame.mouse.get_pressed():
                    pos_row = event.pos[0] // game_ui.square_size
                    pos_col = event.pos[1] // game_ui.square_size
                    if game.check_for_space(pos_row, pos_col, game_board.grid):
                        if human_turn == True:
                            game.insert_letter('X', pos_row, pos_col, game_board.grid)
                            game_ui.draw_x(pos_row, pos_col)
                            human_turn = False
                        else:
                            game.insert_letter('O', pos_row, pos_col, game_board.grid)
                            game_ui.draw_circle(pos_row, pos_col)
                            human_turn = True


        game_ui.draw_game_board()
        game_ui.draw_new_game_button()
        pygame.display.update()


if __name__ == '__main__':
    main()
