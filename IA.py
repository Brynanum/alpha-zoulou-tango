# -*- coding: utf-8 -*-
import chess
import random


##############################################################################
def IAMove(board):
    '''
        
        
        PARAM board{chess.Board} --> the board of the game
        RETURN move{chess.Move}
    '''
    moves = board.legal_moves
    numero = random.randint(0,moves.count())
    i=0
    for move in moves:
        if i==numero:
            return move
        i+=1