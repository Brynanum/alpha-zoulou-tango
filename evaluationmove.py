# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 08:38:50 2018

@author: amau7
"""
import chess
import chess.polyglot

def evaluationMove(currentBoard):
    """ 
        return an evaluation of all the possible moves
        Example: evaluationMove(board) return the tab evaluation -> [[d3d5,400],[a5a7,4555]]
        
        PARAM currentBoard {String} --> the board in fen notation
        RETURN evaluationTab{[[String,Integer],...]} --> return the start position and end position of the move and the weight of this move for each possible move 
    """
    board = chess.Board(currentBoard)
    evaluationTab=[[]]
    i=0
    with chess.polyglot.open_reader("bookfish.bin") as reader:
        for entry in reader.find_all(board):
            evaluationTab[i].append(entry.move())
            evaluationTab[i].append(entry.weight)
        return evaluationTab
    
print(evaluationMove("rnbqkbnr/pppp1ppp/8/4p3/4P3/2N5/PPPP1PPP/R1BQKBNR b KQkq - 1 2"))