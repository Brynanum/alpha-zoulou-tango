# -*- coding: utf-8 -*-
import chess
import chess.svg
from IPython.display import SVG, display

class Image:
	def display(boardFEN,pieceActivePosition):
		board = chess.Board(boardFEN)
		pieceActivePosition = board.attacks(pieceActivePosition)
		display_svg(SVG(chess.svg.board(board=board, squares=pieceActivePosition)))

	def piece(piece):
		return chess.svg.piece(chess.Piece.from_symbol(piece))

display(SVG(Image.piece('R')))
