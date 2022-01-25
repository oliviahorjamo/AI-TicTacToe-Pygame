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
    game_board = GameBoard()
    ai_player = AiPlayer()
    renderer = Renderer(450, 450, (0, 0, 0))
    game_ui = GameMenuUi()
    human_player = HumanPlayer()
    human_turn = True


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed():
                    pos_row = event.pos[0] // game_ui.square_size
                    pos_col = event.pos[1] // game_ui.square_size
                    if game.check_for_space(pos_row, pos_col):
                        if human_turn == True:
                            human_player.make_move(game_ui.draw_x(pos_row, pos_col), pos_row, pos_col)
                            #human_turn == False
                        #if human_turn == False
                            #ai_player.make_move(game_ui.draw_circle())
                            #human_turn == True
        game_ui.draw_game_board()
        pygame.display.update()

if __name__ == '__main__':
    main()
