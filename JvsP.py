# -*- coding: utf-8 -*-
import chess
import IA

#Initialization
color = 0
moves = []
board = chess.Board()

##############################################################################
def ProgramTurn(board):
    '''
        Call IA to play the program turn and play the move.
        
        PARAM board{chess.Board} --> the board of the game
        RETURN {None}
    '''
    move=IA.IAMove(board)
    board.push(move)
    SaveMove(move)

##############################################################################
def PlayerTurn(board):
    '''
        Ask Player to enter a valid move and play the move or end the game with draw.
        
        PARAM board{chess.Board} --> the board of the game
        RETURN {None}
    '''
    text="Enter your move"
    if board.can_claim_draw():
        text+="(or claim draw)"
    move=input(text+":")
    if chess.Move.from_uci(move) in board.legal_moves: #move must be  in fromsquare+endsquare format
        board.push(chess.Move.from_uci(move))
        SaveMove(move)
    elif move=="draw" and board.can_claim_draw():
        board.is_game_over(claim_draw=True)
    else:
        PlayerTurn(board)
##############################################################################        
def Turn(n,board):
    '''
        Choose the player of the current color turn.
        
        PARAM n{int} --> Current color
        PARAM board{chess.Board} --> the board of the game
        RETURN PlayerTurn(board) or ProgramTurn(board)
    '''
    
    if n==color:
        return PlayerTurn(board)
    else:
        return ProgramTurn(board)   
##############################################################################
def PlayerColor():
    '''
        Ask the player to choose his/her color.
        
        RETURN color{int}
    '''
    color = int(input("Choose your color (0: white | 1: black): "))
    if color not in [0,1]:
        PlayerColor()
    return color
##############################################################################     
def Play(board):
    '''
        Play the game until the game is over and set the score.
        
        PARAM board{chess.Board} --> the board of the game
        RETURN {None}
    '''
    
    while not(board.is_game_over()):
        if not(board.is_game_over()):
            if board.is_check():
                print("Check!")
            currentTurn=0
            Turn(currentTurn,board)
            print("\nWhite move : " + str(moves[-1]))
            print(board)
        if not(board.is_game_over()):
            if board.is_check():
                print("Check!")
            currentTurn=1
            Turn(currentTurn,board)
            print("\nBlack move : " + str(moves[-1]))
            print(board)
    moves.append(board.result(claim_draw=board.can_claim_draw()))
    
##############################################################################
def SaveMove(move):
    '''
        Add the last move to the moves list.
        
        PARAM move{chess.Move} --> the last move played
        RETURN {None}
    '''
    moves.append(move)
    
#Current game
color = PlayerColor()
print(board)
#Play(board)