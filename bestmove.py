# -*- coding: utf-8 -*-
import chess
import chess.polyglot


# Meilleur coup possible
def bestMove(currentBoard): # currentBoard is a FEN position
    board = chess.Board(currentBoard)
    weight = 0
    bestmove = ""
    with chess.polyglot.open_reader("bookfish.bin") as reader:
        for entry in reader.find_all(board):
            if entry.weight > weight:
                weight=entry.weight
                bestmove=entry.move()
    return bestmove

test=bestMove("rnbqkb1r/pp1ppp1p/5n2/2p3p1/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq - 0 4")
print(test)