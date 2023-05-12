import pygame.draw

from .constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN

class Piece:
    PADDING = 10
    BORDER = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.isKingPiece = False
        self.x = 0
        self.y = 0
        self.CalculatePostion()

    def CalculatePostion(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def MakePieceAKing(self):
        self.isKingPiece = True

    def DrawPiece(self, window):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(window, GREY, (self.x, self.y,), radius + self.BORDER)
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)
        if(self.isKingPiece):
            window.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))


    def Move(self, row, col):
        self.row = row
        self.col = col
        self.CalculatePostion()


    def __repr__(self):
        return  str(self.color)

