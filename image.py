# -*- coding: utf-8 -*-
import chess
import chess.svg
from IPython.display import SVG, display

class Image:
    def display(svg):
        display(svg)
        
    def board(boardFEN,pieceActivePosition):
        board = chess.Board(boardFEN)
        pieceActivePosition = board.attacks(pieceActivePosition)
        return SVG(chess.svg.board(board=board, squares=pieceActivePosition))

    def piece(piece):
        return SVG(chess.svg.piece(chess.Piece.from_symbol(piece)))

Image.display(Image.board("N7/8/8/8/8/8/8/8 w - - 0 1",chess.A8))