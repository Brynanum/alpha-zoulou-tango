# -*- coding: utf-8 -*-
import bestmove
import random

##############################################################################
def IAMove(board):
    '''
        Select a random move in the list legal_move if no best move available.
        
        PARAM board{chess.Board} --> the board of the game
        RETURN move{chess.Move}
    '''
    if bestmove.bestMove(board)==None:
        moves = board.legal_moves
        numero = random.randint(0,moves.count()-1)
        i=0
        for move in moves:
            if i==numero:
                return move
            i+=1
    else:
        return bestmove.bestMove(board)