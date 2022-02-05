
import sys
import pygame
from services.game_board import GameBoard
from services.game import Game
from ui.game_menu_ui import GameMenuUi
from entities.ai_player import AiPlayer
from entities.human_player import HumanPlayer


def main():
    pygame.init()
    game_board = GameBoard()
    game = Game()
    game_ui = GameMenuUi(game_board)
    ai_player = AiPlayer(game_board, game)
    human_player = HumanPlayer(game_board, game)
    ai_turn = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if ai_turn is True:
                coordinates = ai_player.make_move()
                game_ui.draw_circle(coordinates[0], coordinates[1])
                if game.check_win(game_board.board, game_board.board_size):
                    print('ai won')
                ai_turn = False
            if ai_turn is False:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed():
                        pos_row = event.pos[0] // game_ui.square_size
                        pos_col = event.pos[1] // game_ui.square_size
                        if pos_col <= 19:
                            human_player.make_move(pos_row, pos_col)
                            game_ui.draw_x(pos_row, pos_col)
                            print(pos_row, pos_col)
                            if game.check_win(game_board.board, game_board.board_size):
                                sys.exit()
                            else:
                                ai_turn = True
                    if pygame.mouse.get_pressed():
                        if game_ui.new_game(pygame.mouse.get_pos()):
                            game_board.reset_game_board()
                            game_ui.reset_game_board()
        game_ui.draw_change_turn(ai_turn)
        game_ui.draw_game_board()
        game_ui.draw_new_game_button()
        pygame.display.update()

if __name__ == '__main__':
    main()
