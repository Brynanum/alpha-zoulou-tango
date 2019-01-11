# -*- coding: utf-8 -*-
import chess
import time
import IA
import save
import datetime

##############################################################################
class Simulation:
    '''
        Create a chess game  simulation.
    '''
    ##############################################################################
    def __init__(self):
        '''
            Construct the game on a new board.
            
            RETURN {None}
        '''
        self.board=chess.Board()
        self.moves=[]
        self.saveNumber=1
        
    ##############################################################################        
    def White(self):
        '''
            Call AI to play the white side.
            
            RETURN {None}
        '''
        move=IA.IAMove(self.board)
        if move!=None:
            self.board.push(move)
            self.moves.append(move)
        else:
            self.White()
    
    ##############################################################################   
    def Black(self):
        '''
            Call AI to play the black side.
            
            RETURN {None}
        '''
        move=IA.IAMove(self.board)
        if move!=None:
            self.board.push(move)
            self.moves.append(move)
        else:
            self.Black()
        
    ############################################################################## 
    def saveGame(self):
        '''
            Save the game.
            
            RETURN {None}
        '''
        save.Stream.saveFEN(self.board,"save/"+str(datetime.datetime.now().strftime(("%Y%m%d%H%M%S")))+"save"+str(self.saveNumber)+".txt")
        self.saveNumber+=1
    ##############################################################################    
    def Simulate(self):
        '''
            Simulate a chess game.
            
            RETURN {None}
        '''
        status=input("Enter 'play' to start the simulation:")
        if status=='play':
            print(self.board)
            while not(self.board.is_game_over()):
                self.saveGame()
                if not(self.board.is_game_over()):
                    self.White()
                    print("\nWhite move : " + str(self.moves[-1]))
                    print(self.board)
                if not(self.board.is_game_over()):
                    self.Black()
                    print("\nBlack move : " + str(self.moves[-1]))
                    print(self.board)
                time.sleep(1)
            print("Simulation is over. Result: ", self.board.result)
        else:
            self.Simulate()

#Current simulation
CurrentSim=Simulation()
CurrentSim.Simulate()