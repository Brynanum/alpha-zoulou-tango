#python-chess import 
#https://github.com/niklasf/python-chess
import chess

#used to access Polyglot book
import chess.polyglot

#set the initial position
board = chess.Board()
board.push(chess.Move.from_uci("d2d4"))
board.push(chess.Move.from_uci("g8f6"))
board.push(chess.Move.from_uci("c2c4"))
board.push(chess.Move.from_uci("g7g6"))
board.push(chess.Move.from_uci("b1c3"))
board.push(chess.Move.from_uci("d7d5"))
board.push(chess.Move.from_uci("c4d5"))
board.push(chess.Move.from_uci("f6d5"))
board.push(chess.Move.from_uci("e2e4"))
board.push(chess.Move.from_uci("d5c3"))
board.push(chess.Move.from_uci("b2c3"))
board.push(chess.Move.from_uci("f8g7"))
print(board)

#access the Polyglot book
with chess.polyglot.open_reader("bookfish.bin") as reader:
    for entry in reader.find_all(board):
        print(entry.move(), entry.weight, entry.learn)
