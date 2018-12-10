#python-chess import 
#https://github.com/niklasf/python-chess
import chess

#used to access Polyglot book
import chess.polyglot

#set the initial position
board = chess.Board("rnbqkb1r/pppppppp/5n2/8/3P4/8/PPP1PPPP/RNBQKBNR w KQkq - 1 2")
print(board)

#access the Polyglot book
with chess.polyglot.open_reader("bookfish.bin") as reader:
    for entry in reader.find_all(board):
        print(entry.move(), entry.weight, entry.learn)
