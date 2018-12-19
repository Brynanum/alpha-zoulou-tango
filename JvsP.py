# -*- coding: utf-8 -*-
import chess
import IA

##############################################################################
class Game:
    '''
        Create a chess game to play.
    
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
        text="Enter your move"
        if self.board.can_claim_draw():
            text+="(or claim draw)"
        move=input(text+":")
        try: 
            chess.Move.from_uci(move)
        except:
            self.PlayerTurn()
        if chess.Move.from_uci(move) in self.board.legal_moves: #move must be  in fromsquare+endsquare format
            self.board.push(chess.Move.from_uci(move))
            self.SaveMove(move)
        elif move=="draw" and self.board.can_claim_draw():
            self.board.is_game_over(claim_draw=True)
        else:
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
        print(self.board)
        while not(self.board.is_game_over()):
            if not(self.board.is_game_over()):
                if self.board.is_check():
                    print("Check!")
                currentTurn=0
                self.Turn(currentTurn)
                print("\nWhite move : " + str(self.moves[-1]))
                print(self.board)
            if not(self.board.is_game_over()):
                if self.board.is_check():
                    print("Check!")
                currentTurn=1
                self.Turn(currentTurn)
                print("\nBlack move : " + str(self.moves[-1]))
                print(self.board)
        self.moves.append(self.board.result(claim_draw=self.board.can_claim_draw()))
    
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
