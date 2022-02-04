
import sys
import pygame
from services.game_board import GameBoard
from services.game import Game
from ui.game_menu_ui import GameMenuUi
from entities.ai_player import AiPlayer


def main():
    pygame.init()
    game = Game()
    game_board = GameBoard()
    game_ui = GameMenuUi(game_board)
    ai_player = AiPlayer(game)
    ai_turn = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if ai_turn is True:
                move = ai_player.make_move(game_board.grid)
                game.insert_letter(2, move[0], move[1], game_board.grid)
                print(move[0], move[1])
                game_ui.draw_circle(move[0], move[1])
                ai_turn = False
            if ai_turn is False:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed():
                        pos_row = event.pos[0] // game_ui.square_size
                        pos_col = event.pos[1] // game_ui.square_size
                        if game.check_for_space(pos_row, pos_col, game_board.grid):
                            game.insert_letter(1, pos_row, pos_col, game_board.grid)
                            print(pos_row, pos_col)
                            print(game_board.print_grid())
                            game_ui.draw_x(pos_row, pos_col)
                            ai_turn = True
        game_ui.draw_change_turn(ai_turn)
        game_ui.draw_game_board()
        game_ui.draw_new_game_button()
        pygame.display.update()

if __name__ == '__main__':
    main()
