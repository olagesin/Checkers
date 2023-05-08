import pygame
from .board import *
from .constants import *

class GameLogic:
    def __init__(self, window):
        self._init()
        self.window = window

    def update(self):
        self.board.Draw(self.window)
        self.drawvalidmoves(self.validMoves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.validMoves = {}

    def reset(self):
        self._init()

    def drawvalidmoves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.window, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE //2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def markWinner(self):
        return self.board.markWinner()

    def select(self, row, col):
        if(self.selected):
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.GetPiece(row, col)
        if(piece != 0 and piece.color == self.turn):
            self.selected = piece
            self.validMoves = self.board.GetValidMoves(piece)
            return True
        return False

    def _move(self, row, col):
        piece = self.board.GetPiece(row, col)
        if self.selected and piece == 0 and (row, col) in self.validMoves:
            self.board.MovePiece(self.selected, row, col)
            skipped = self.validMoves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.changeTurn()
        else:
            return False
        return True
    def changeTurn(self):
        self.validMoves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED
