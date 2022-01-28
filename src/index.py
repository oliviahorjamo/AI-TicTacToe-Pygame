import pygame
import sys
from entities.ai_player import AiPlayer
from services.game_board import GameBoard
from services.game import Game
from services.renderer import Renderer
from ui.game_menu_ui import GameMenuUi


def main():
    pygame.init()
    game = Game()
    ai_player = AiPlayer()
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
                    if game_ui.new_game(pygame.mouse.get_pos()):
                        game_board.reset_game_board()
                        game_ui.reset_game_board()
                    if pos_col <= 19:
                        if game.check_for_space(pos_row, pos_col, game_board.grid):
                            print(pos_row, pos_col)
                            if human_turn == True:
                                game.insert_letter('X', pos_row, pos_col, game_board.grid)
                                game_ui.draw_x(pos_row, pos_col)

                                if game.check_win(game_board.grid, game_board.grid_size):
                                    sys.exit()
                                else:
                                    human_turn = False
                            else:
                                game.insert_letter('O', pos_row, pos_col, game_board.grid)
                                game_ui.draw_circle(pos_row, pos_col)
                                if game.check_win(game_board.grid, game_board.grid_size):
                                    sys.exit()
                                else:
                                    human_turn = True
        game_ui.draw_game_board()
        game_ui.draw_new_game_button()
        pygame.display.update()


if __name__ == '__main__':
    main()
