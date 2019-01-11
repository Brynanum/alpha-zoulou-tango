# -*- coding: utf-8 -*-
import chess
import IA
import save
import sys


##############################################################################
class Game:
    '''
        Create a chess game to play.
        HOW TO USE THIS CLASS AND PLAY
            Execute this file.
    '''
    ##############################################################################
    def __init__(self):
        '''
            Construct the game on a new board.
            
            RETURN {None}
        '''
        self.board=chess.Board()
        self.color=0
        self.moves=[]
    
    ##############################################################################
    def ProgramTurn(self):
        '''
            Call AI to play the program turn and play the move.

            RETURN {None}
        '''
        move=IA.IAMove(self.board)
            
        self.board.push(move)
        self.SaveMove(move)


    ##############################################################################
    def PlayerTurn(self):
        '''
            Ask Player to enter a valid move and play the move or end the game with draw.
            
            RETURN {None}
        '''
        text="Enter your move "
        if self.board.can_claim_draw():
            text+="(or claim draw) "
        text+="or write 'SaveInPGN'/'SaveInFEN' to save the current game"
        command=input(text+":")
        if command.lower()=='saveinpgn':
            #save.Stream.savePGN(self.moves,"PGNSave.txt",self.color,self.board.result())
            print("You saved in PGN format.\n")
            sys.exit(0)
            
        elif command.lower()=='saveinfen':
            save.Stream.saveFEN(self.board,"FENSave.txt")
            print("You saved in FEN format.\n")
            sys.exit(0)
        
        try: 
            chess.Move.from_uci(command)
            if chess.Move.from_uci(command) in self.board.legal_moves: #move must be  in fromsquare+endsquare format
                self.board.push(chess.Move.from_uci(command))
                self.SaveMove(command)
            elif command=="draw" and self.board.can_claim_draw():
                self.board.is_game_over(claim_draw=True)
            else:
                print('Invalid input, please use a possible move.')
                self.PlayerTurn()
        except:
            print('Invalid input, please use the fromsquare+endsquare format \nlike "e2e3" or "e2e3q" to promote a Pawn.')
            print('Or use "SaveInPGN"/"SaveInFEN" to save your game')
            self.PlayerTurn()
        
    
    ##############################################################################        
    def Turn(self,n):
        '''
            Choose the player of the current color turn.
            
            PARAM n{int} --> Current color
            RETURN PlayerTurn(board) or ProgramTurn(board)
        '''
        
        if n==self.color:
            return self.PlayerTurn()
        else:
            return self.ProgramTurn()  
    
    ##############################################################################
    def PlayerColor(self):
        '''
            Ask the player to choose his/her color.
            
            RETURN {None}
        '''
        self.color = int(input("Choose your color (0: white | 1: black): "))
        if self.color not in [0,1]:
            self.PlayerColor()
    
    ##############################################################################     
    def Play(self):
        '''
            Play the game until the game is over and set the score.
            
            RETURN {None}
        '''
        print('\nGame initialization complete : \n')
        print('BLACK Side')
        self.DisplayBoard()
        print('WHITE Side')
        while not(self.board.is_game_over()):
            if not(self.board.is_game_over()):
                if self.board.is_check():
                    print("Check !")
                currentTurn=0
                self.Turn(currentTurn)
                print("\nWhite move : " + str(self.moves[-1]))
                self.DisplayBoard()
            if not(self.board.is_game_over()):
                if self.board.is_check():
                    print("Check !")
                currentTurn=1
                self.Turn(currentTurn)
                print("\nBlack move : " + str(self.moves[-1]))
                self.DisplayBoard()
        self.moves.append(self.board.result(claim_draw=self.board.can_claim_draw()))
        
    ##############################################################################
    def DisplayBoard(self):
        '''
            Display the chess board with numbers in the left column and letters in the bottom line
            
            RETURN {None}
        '''
        board = str(self.board)
        i=0
        while(i<8):
            print(8-i,'|',board.split('\n')[i])
            i+=1
            
        print("    ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        print("    A B C D E F G H")
    ##############################################################################
    def SaveMove(self,move):
        '''
            Add the last move to the moves list.
            
            PARAM move{chess.Move} --> the last move played
            RETURN {None}
        '''
        self.moves.append(move)
    
#Current game
CurrentGame=Game()
CurrentGame.PlayerColor()
CurrentGame.Play()