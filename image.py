# -*- coding: utf-8 -*-
import chess
import chess.svg
from IPython.display import SVG

class Image:
	symbols={
		'K':SVG(chess.svg.piece(chess.Piece.from_symbol('K'))),
		'Q':SVG(chess.svg.piece(chess.Piece.from_symbol('Q'))),
		'B':SVG(chess.svg.piece(chess.Piece.from_symbol('B'))),
		'N':SVG(chess.svg.piece(chess.Piece.from_symbol('N'))),
		'R':SVG(chess.svg.piece(chess.Piece.from_symbol('R'))),
		'P':SVG(chess.svg.piece(chess.Piece.from_symbol('P'))),
		'k':SVG(chess.svg.piece(chess.Piece.from_symbol('k'))),
		'q':SVG(chess.svg.piece(chess.Piece.from_symbol('q'))),
		'b':SVG(chess.svg.piece(chess.Piece.from_symbol('b'))),
		'n':SVG(chess.svg.piece(chess.Piece.from_symbol('n'))),
		'r':SVG(chess.svg.piece(chess.Piece.from_symbol('r'))),
		'p':SVG(chess.svg.piece(chess.Piece.from_symbol('p')))
	}
    
	def display(self):
		self.displayBoard()
		self.displaySymbols()

	def displayBoard(self,boardFEN,symbolActive):
		board = chess.Board(boardFEN)
		squares = board.attacks(symbolActive)
		SVG(chess.svg.board(board=board, squares=squares))

	def displaySymbols(self):
		[...]

Image.symbols['K']
Image.displayBoard("8/8/8/8/4N3/8/8/8 w - - 0 1",chess.E4)
