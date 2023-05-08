import pygame
from Checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED
from Checkers.GameLogic import GameLogic
from Checkers.board import Board
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Checkers")

def GetRowAndColFromMouseClick(pos):
    x,y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return  row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = GameLogic(WIN)


    while run:
        clock.tick(FPS)

        if game.markWinner() != None:
            print(game.markWinner())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = GetRowAndColFromMouseClick(pos)
                game.select(row, col)

        game.update()
    pygame.quit()

main()