#python-chess import 
#https://github.com/niklasf/python-chess
import chess

#used to access Polyglot book
import chess.polyglot

#set the initial position
board = chess.Board()
board.push(chess.Move.from_uci("e2e4"))
board.push(chess.Move.from_uci("d7d5"))
board.push(chess.Move.from_uci("g2g3"))
board.push(chess.Move.from_uci("b7b6"))
board.push(chess.Move.from_uci("f1g2"))
board.push(chess.Move.from_uci("c8d7"))
print (board)

#access the Polyglot book
with chess.polyglot.open_reader("bookfish.bin") as reader:
    for entry in reader.find_all(board):
        print(entry.move(), entry.weight, entry.learn)
