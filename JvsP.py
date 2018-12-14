# -*- coding: utf-8 -*-
import chess
import IA from IA

#Choix
typeGame = input("Choose your game type (0:PvsP | 1:JvsP): ")
if typeGame == "1":
    color = input("Choose your color (0: white | 1: black): ")
    
#Initialisation
board = chess.Board()
print(board)

#Gestion des tours
def ProgramTurn():
    move=IAMove()
    board.push(chess.Move.from_uci(move))

def PlayerTurn():
    text="Enter your move"
    if board.can_claim_draw():
        text+="(or claim draw)"
    move=input(text+":")
    if move in board.legal_moves:
        board.push(chess.Move.from_uci(move))
    elif move=="draw" and board.can_claim_draw():
        board.is_game_over(claim_draw=True)
    else:
        PlayerTurn()

Order=[None,None]
Order[color]=PlayerTurn()
Order[color-1]=ProgramTurn()

#Partie en cours
while not(board.is_game_over()):
    if not(board.is_game_over()):
        Order[0]
        print(board)
    if not(board.is_game_over()):
        Order[1]
        print(board)