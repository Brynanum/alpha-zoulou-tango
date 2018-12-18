#python-chess import
#https://github.com/niklasf/python-chess
import chess
import save
#set the board to its initial position
#corresponding to: rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
board = chess.Board()

#print the board on the console
#print(board)

#SVG render for the board is possible in Jupyter Notebook
#board

#get all the legal moves for the current position
moves = board.legal_moves

#how many moves are available?
#print(moves.count())

#iterate over all the moves
for move in moves: 
    
    #display the move
    #print(move)
    
    #save the current position
    current_board = board
    
    #do the move
    board.push(move)
    
    #display the board
    #print(board)
    
    #number of black moves
    #print("Black moves:" + str(board.legal_moves.count()))
    
    #undo the move
    board.pop()
    
    #do we have a winner?
    if (board.is_game_over()):
        print("The game is over")
        print(board.result())
        
#test=save.readPGN("save.txt")
#save.savePGN(test[0],1)
print(save.Stream.savePGN(["a2a4","a7a5","d2d4","h7h5","b2b4","c7c5"],"t.txt",1))
t=save.Stream.readPGN("t.txt")
save.Stream.saveFEN(t[0],"lol.txt")