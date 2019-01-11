# -*- coding: utf-8 -*-
import chess 
import chess.polyglot

def bestMove(board):
    '''
    Find the best move of the current board from bookfish.bin book.
    PARAM board {chess.Board} --> current board

    RETURN bestmove{chess.Move}
    
    '''
    weight = 0
    bestmove = None
    with chess.polyglot.open_reader("bookfish.bin") as reader:
        for entry in reader.find_all(board):
            if entry.weight > weight:
                weight=entry.weight
                bestmove=entry.move()
    return bestmove