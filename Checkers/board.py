import pygame
from .constants import *
from .Piece import Piece


class Board: #Handles the state of the actual game
    def __init__(self):
        self.board = []
        self.redLeft = self.whiteLeft = 12
        self.redKings = self.whiteKings = 0
        self.createBoardPieces()
        self.run = True

    def setBoard(self, window):
        window.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(window, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def MovePiece(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.Move(row, col)

        if row == ROWS - 1 or row == 0:
            if piece.color == RED and not piece.isKingPiece:
                self.redKings += 1
                piece.MakePieceAKing()
            if piece.color == WHITE and not piece.isKingPiece:
                self.whiteKings += 1
                piece.MakePieceAKing()

            # piece.MakePieceAKing()
            # if piece.col == WHITE:
            #     self.whiteKings += 1
            # else: self.redKings += 1


    def UndoMove(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.Move(row, col)

        if row == ROWS - 1 or row == 0:
            if piece.color == RED and not piece.isKingPiece:
                self.redKings += 1
                piece.MakePieceAKing()
            if piece.color == WHITE and not piece.isKingPiece:
                self.whiteKings += 1
                piece.MakePieceAKing()
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.redLeft -= 1
                else:
                    self.whiteLeft -= 1

                print(f"There are {self.redLeft} red pieces left and {self.whiteLeft} white pieces left")
                if self.markWinner() is not None:
                    print(f"The winner is {self.markWinner()}")
                    # pygame.quit()
                    # exit()

    #returns the current score of the board
    def evaluate(self):
        return self.whiteLeft - self.redLeft + (self.whiteKings * 0.5 - self.redKings * 0.5)

    def markWinner(self):
        if self.redLeft == 0:
            return WHITE
        elif self.whiteLeft == 0:
            return RED
        return None

    def GetPiece(self, row, col):
        return self.board[row][col]

    def createBoardPieces(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLUMNS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def Draw(self, window):
        self.setBoard(window)
        for row in range(ROWS):
            for col in range(COLUMNS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.DrawPiece(window)

    def GetValidMoves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == RED or piece.isKingPiece:
            moves.update(self._traverseLeft(row - 1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverseRight(row - 1, max(row - 3, -1), -1, piece.color, right))

        if piece.color == WHITE or piece.isKingPiece:
            moves.update(self._traverseLeft(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverseRight(row + 1, min(row + 3, ROWS), 1, piece.color, right))

        return moves

    def _traverseLeft(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.board[r][left] #get the current potential move
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverseLeft(r + step, row, step, color, left-1, skipped=last))
                    moves.update(self._traverseRight(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            left -= 1
        return moves

    def _traverseRight(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLUMNS:
                break
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r + 3, ROWS)

                    moves.update(self._traverseLeft(r + step, row, step, color, right-1, skipped=last))
                    moves.update(self._traverseRight(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            right += 1

        return moves