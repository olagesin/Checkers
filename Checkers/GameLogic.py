import pygame
from .board import *
from .constants import *

class GameLogic:
    def __init__(self, window):
        self._init()
        self.window = window

    def update(self):
        if self.board is not None:
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
            pygame.draw.circle(self.window, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                                   row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def markWinner(self):
        return self.board.markWinner()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.GetPiece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.validMoves = self.board.GetValidMoves(piece)
            return True
        return False

    def check_for_draw(self):
        if self.board is not None:
            pieces = self.board.get_all_pieces(self.turn)
            possible_moves = []
            for piece in pieces:
                possible_moves.append(self.board.GetValidMoves(piece))

            if not any(possible_moves):
                #print(f"The game ended in a draw because {self.turn} has no moves left.")
                pygame.quit()
                exit()

    def _move(self, row, col):
        if self.board is not None:
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

    def ai_move(self, board):
        self.board = board
        self.changeTurn()

    def get_board(self):
        return self.board