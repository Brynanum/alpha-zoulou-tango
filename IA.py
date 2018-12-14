# -*- coding: utf-8 -*-
import chess
import random

def IAMove(board):
    moves = board.legal_moves
    numero = random.randint(0,moves.count())
    i=0
    for move in moves:
        if i==numero:
            return move
        i+=1