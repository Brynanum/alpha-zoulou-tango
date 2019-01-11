# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 11:13:07 2018

@author: amau7
"""

class Menu:
    """ 
        Interface that allow to enter the game and chose the different parameters 
        """
    opponent=''
    color=-1
    lichess=False
    
    def __init__(self):
        """
            Create a default menu 
            PARAM self{Menu}

        """
        opponent=self.opponent
        color=self.color
        lichess=self.lichess
    
    def gameInit(self):
        """ 
            initialise the different paramater needed to launch a game
            
            PARAM self{Menu}
            RETURN {None}
        """
        print("What type of game do you want to play?")
        temp=''
        # opponent's choice
        while temp!='1' and temp!='2':
            temp=input(" '1'.player vs program \n '2'.program vs program\n")
            if temp!='1' and temp!='2':
                print("\nplease enter '1' or '2'")
                
        if temp=='1' :
            print("player vs program")
            self.setOpponent(0)

        elif temp=='2':
            print("program vs program")
            self.setOpponent(1)
        bot=temp
        # if it's a player vs program game ask to user what is the color he want
        if bot=='1':
            temp=''
            while temp!='1' and temp!='2':
                temp=input("Chose your color\n'1'.White '2'.Black\n")
                if temp!='1' and temp!='2':
                    print("\nplease enter '1' or '2'")
            self.setColor(temp)
            if temp=='1' :
                print("You choose white")
                self.setColor(0)

            elif temp=='2':
                print("You choose black")
                self.setColor(1)
        else:
            temp=''
            # ask if the user want to use lychess and play with our AI vs the Lichess AI
            while temp!='1' and temp!='2':
                temp=input("Do you want to use Lichess?\n'1'.Yes '2'.No\n")
                if temp!='1' and temp!='2':
                    print("\nPlease enter '1' or '2'")
            if temp=='1' :
                print("You choose to use Lichess")
                self.setLichess(True)

            elif temp=='2':
                print("You choose to not use Lichess")
                self.setLichess(False)

    def setOpponent(self,op):
        """ 
            Set the opponent of the game            
            PARAM self {Menu}
                  op {Int}-> the opponent 0 for player vs program, 1 for program vs program 
        """
        self.opponent=op
    
    def setColor(self,col):
        """ 
            Set the color of the player            
            PARAM self {Menu}
                  col {Int}-> the color 0 for white, 1 for black 
        """
        self.color=col
        
    def setLichess(self,lic):
        """ 
            Set if you want to use Lichess or not            
            PARAM self {Menu}
                  lic {Boolean}-> True if you want to use Lichess, False if you don't want to
        """
        self.lichess=lic
    
    def getOpponent(self):
        """ 
            Get the opponent of the game            
            PARAM self {Menu}
            
            RETURN {Int}-> the opponent, 0 for player vs program, 1 for program vs program
        """
        return self.opponent
    
    def getColor(self):
        """ 
            Get the color of the player            
            PARAM self {Menu}
    
            RETURN {Int}-> the color, 0 for white, 1 black
        """
        return self.color
    
    def getLichess(self):
        """ 
            Get if you chose to use Lichess           
            PARAM self {Menu}
    
            RETURN {Boolean}->  True if you wanted to use Lichess, False if you don't wanted to
        """
        return self.lichess
