# -*- coding: utf-8 -*-
import chess
import chess.svg
from IPython.display import SVG, display

class Image:
    """
        Create SVG python-chess pictures and display it
        
        HOW TO USE THIS CLASS
            1) Create an SVG pictures with Image.piece(), Image.board()...
            2) Display it with Image.display()
    """
    
    def display(svg):
        """
            Display with IPython the given SVG
            Example : Image.display(Image.piece('K')) display the piece of a white king
    
            PARAM svg{IPython.core.display.SVG} --> the SVG picture
            RETURN {None}
        """
        display(svg)
        
    def board(boardFEN,pieceActivePosition):
        """
            Generate an SVG picture of a board game
            Example : Image.board("8/8/8/8/4N3/8/8/8 w - - 0 1",chess.E4) create a SVG representing a board with a knight, and its possibilities to move
    
            PARAM boardFen{String} --> The chess board in FEN format
            PARAM pieceActivePosition{Int} --> The position of the last activated piece (use here chess.<case>)
            RETURN {IPython.core.display.SVG} --> The SVG picture
        """
        board = chess.Board(boardFEN)
        pieceActivePosition = board.attacks(pieceActivePosition)
        return SVG(chess.svg.board(board=board, squares=pieceActivePosition))
    
    def piece(piece):
        """
            Get an SVG picture of a piece (uppercase = white, lowercase = black)
            Example : Image.piece('K') create a SVG representing a white king.
    
            PARAM piece{Char} --> Letter than represent the piece in english official notation
            RETURN {IPython.core.display.SVG} --> The SVG picture
        """
        return SVG(chess.svg.piece(chess.Piece.from_symbol(piece)))