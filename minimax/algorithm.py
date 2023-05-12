from copy import deepcopy
import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)


def minimax_alpha_beta(position, depth, maximizingPlayer, alpha, beta, game):
    if depth == 0 or position.markWinner() is not None:
        return position.evaluate(), position

    if maximizingPlayer:
        maxEvaluation = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            # board.make_move(move)
            evaluationResult = minimax_alpha_beta(move, depth - 1, False, alpha, beta, game)[0]
            # board.undo_move(move)
            # maxEvaluation = max(maxEvaluation, evaluationResult)
            if evaluationResult > maxEvaluation:
                maxEvaluation = evaluationResult
                best_move = move
            alpha = max(alpha, evaluationResult)
            if beta <= alpha:
                best_move = move
                break
        return maxEvaluation, best_move
    else:
        minEvaluation = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluationResult = minimax_alpha_beta(move, depth - 1, True, alpha, beta, game)[0]
            # board.undo_move(move)
            # minEvaluation = min(minEvaluation, evaluationResult)
            if evaluationResult < minEvaluation:
                minEvaluation = evaluationResult
                best_move = move
            beta = min(beta, evaluationResult)
            if beta <= alpha:
                best_move = move
                break
        return minEvaluation, best_move


def minimax(position, depth, max_player, game):
    if depth == 0 or position.markWinner() is not None:
        return position.evaluate(), position
    
    if max_player: #if true, then we are trying to maximize
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth - 1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        return minEval, best_move


def simulate_move(piece, move, board, game, skip):
    board.MovePiece(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.GetValidMoves(piece)
        for move, skip in valid_moves.items():
            #draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.GetPiece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
            #moves.append([new_board, piece])
    
    return moves

def draw_moves(game, board, piece):
    valid_moves = board.GetValidMoves(piece)
    board.Draw(game.window)
    pygame.draw.circle(game.window, (0, 255, 0), (piece.x, piece.y), 50, 5)
    game.drawvalidmoves(valid_moves.keys())
    pygame.display.update()
    pygame.time.delay(100)