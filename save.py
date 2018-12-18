# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 10:45:26 2018

@author: beuhorra
"""
import chess
import chess.pgn
import datetime

class Stream:
    """
        class that manage the method for saving and reading games from files
    """
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
            for move in first_game.mainline_moves():
                board.push(move)
            return [board,first_game.headers["White"],first_game.headers["Black"],first_game.headers["Result"]]
        else:
            return None    
    
    def savePGN(moveList,file,color,Result="*"):
        """
            save a game in PGN from a moveList 
            
            Example: Save(["a2a4","a7a5","d2d4","h7h5","b2b4","c7c5"],1,"file.txt") save the game in pgn format in file.txt 
            
            PARAM Result{str} -->values: 1-0 (White won), 0-1 (Black won), 1/2-1/2 (Draw), or * (other, e.g., the game is ongoing) 
            PARAM moveList{List(str)} --> list of the moves made in the game
            PARAM color --> the color used by the player, 0 if he is white,1 if he is black
            RETURN {Boolean} --> return True if the save is done, false
        """
        if moveList is not None and moveList!=[]:
            f= open(file,"a")
            game=chess.pgn.Game()
            if color==0:
                game.headers["White"]="1"
            else:
                game.headers["Black"]="1"
            game.headers["Result"]=Result
            game.headers["Date"]=datetime.datetime.now().strftime(("%Y.%m.%d"))
            node = game.add_variation(chess.Move.from_uci(moveList[0]))
            for i in range (1,len(moveList)-1):
                node = node.add_variation(chess.Move.from_uci(moveList[i]))
                
            f.write(str(game))
            f.write("\n")
            f.close
            return True
        else:
            return False
    
        
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
            save the board of the game in a file in FEN and return true if the save is done
            Example: saveFEN(board,"file.txt") save the game in FEN format in file.txt
            
            PARAM board{Board} --> the board of the game
            PARAM file{str} --> the name of the file
            RETURN {Boolean} 
        """
        f= open(file,"a")
        if f is not None:
            f.write(board.fen())
            f.close()
            return True
        else:
            return False