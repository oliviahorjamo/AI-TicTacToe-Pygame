
import sys
import pygame
from services.game_board import GameBoard
from services.game import Game
from ui.game_menu_ui import GameMenuUi
from entities.ai_player import AiPlayer

def main():
    pygame.init()
    game_board = GameBoard()
    game = Game()
    game_ui = GameMenuUi(game_board)
    ai_player = AiPlayer(game)
    ai_turn = False
    ai_move = 2
    human_move = 1
    board = game_board.board


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if ai_turn == False:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed():
                        col = event.pos[0] // game_ui.square_size
                        row = event.pos[1] // game_ui.square_size
                        if col <= 19:
                            if game.check_for_space(row, col, board):
                                game.insert_move(human_move, row, col, board)
                                game_ui.draw_x(row, col)
                                if game.check_for_win(board, human_move):
                                    print('YOU WON!')

                                else:
                                    ai_turn = True
            if ai_turn == True:
                pos = ai_player.find_best_move(board)
                game.insert_move(ai_move, pos[0], pos[1], board)
                game_ui.draw_circle(pos[0], pos[1])
                if game.check_for_win(board, ai_move):
                    print('AI WON!')
                else:
                    ai_turn = False

        game_ui.draw_game_board()
        game_ui.draw_new_game_button()
        pygame.display.update()

if __name__ == '__main__':
    main()
