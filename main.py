import pygame
from Checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from Checkers.GameLogic import GameLogic
from Checkers.board import Board
from minimax.algorithm import minimax, minimax_alpha_beta

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Checkers")

def GetRowAndColFromMouseClick(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = GameLogic(WIN)

    while run:
        clock.tick(FPS)
        if game.turn == WHITE:
            value, new_board = minimax_alpha_beta(game.get_board(), 4, WHITE, float('-inf'), float('inf'), game)
            # value, new_board = minimax(game.get_board(), 3, WHITE, game)
            game.ai_move(new_board)

        # if game.markWinner() is not None:
        #     print(game.markWinner())
        #     run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = GetRowAndColFromMouseClick(pos)
                if game.turn:
                    game.select(row, col)
        game.check_for_draw()

        game.update()
    # pygame.quit()


main()
