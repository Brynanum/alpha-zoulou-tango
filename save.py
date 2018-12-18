# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 10:45:26 2018

@author: beuhorra
"""
import chess
import chess.pgn
import datetime

def readPGN(file):
    """
        read a game in PGN from a files and return the board of this game,the white name, the black name and the result of the game 
        Example: readPGN("file.txt") read file.txt 
        
        PARAM file{str} --> the name of the file
        RETURN {[board,str,str,str]} --> the board and headers for black,
    """
    pgn=open(file,encoding="utf-8-sig")
    first_game=chess.pgn.read_game(pgn)
    pgn.close()
    if first_game is not None:
        board = first_game.board()
        # Iterate through all moves and play them on a board.
        count=0
        for move in first_game.mainline_moves():
            board.push(move)
            count+=1
        if count%2!=0:
            print("\nit is Black's move\n")
        else:
            print("\nit is White's move\n")
        return [board,first_game.headers["White"],first_game.headers["Black"],first_game.headers["Result"]]
    else:
        return None    
    
def readFEN(file):
    """
        read a game in FEN from a files and return the board of this game
        Example: readFEN("file.txt") read file.txt and return the correspounding board
        
        PARAM file{str} --> the name of the file
        RETURN {board} --> the board of the game
    """
    fen=open(file,encoding="utf-8-sig")
    line=fen.readline()
    board=chess.Board(line)
    fen.close()
    return board

def saveFEN(board,file):
    """
        save the board of the game in a files and return true if the save is done
        Example: readPGN("file.txt") read file.txt and return the correspounding board
        
        PARAM file{board,str} --> the board, the name of the file
        RETURN {Boolean} 
    """
    f= open(file,"a")
    if f is not None:
        f.write(board.fen())
        f.close()
        return True
    else:
        return False