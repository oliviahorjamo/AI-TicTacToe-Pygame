
import sys
import pygame
from services.game_board import GameBoard
from services.game_logic import GameLogic
from ui.game_menu_ui import GameMenuUi
from entities.ai_player import AiPlayer

def main():
    pygame.init()
    game_board = GameBoard()
    game = GameLogic()
    game_ui = GameMenuUi(game_board)
    ai_player = AiPlayer(game_board, game)
    board = game_board.board
    player = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if player == 1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed():
                        col = event.pos[0] // game_ui.square_size
                        row = event.pos[1] // game_ui.square_size
                        if row <= 24:
                            if game.check_for_space(row, col, board):
                                game_ui.draw_x(row, col)
                                game.insert_move(1, row, col, board)
                                cell = (row, col)
                                print('human move:', cell)
                                pygame.display.update()
                                if game.check_for_win(game_board.board):
                                    game_ui.draw_who_won(player)
                                else:
                                    player += 1
                    if game_ui.draw_new_game(pygame.mouse.get_pos()) is True:
                        main()
            else:
                game_ui.draw_show_ai_turn()
                pygame.display.update()
                pos = ai_player.find_best_move()[0]
                game.insert_move(2, pos[0], pos[1], board)
                game_ui.draw_circle(pos[0], pos[1])
                if game.check_for_win(game_board.board):
                    game_ui.draw_who_won(player)
                    player = 1
                    print('AI won')
                else:
                    player -= 1
                    game_ui.draw_show_human_turn()

        if game.check_for_tie(game_board.board) == 0:
            game_ui.draw_tie()
        game_ui.draw_game_board()
        game_ui.draw_new_game_button()
        pygame.display.update()


if __name__ == '__main__':
    main()
