# -*- coding: utf-8 -*-
import berserk
import chess
from IA import IAMove

class Lichess:
    """
        API that links the program and lichess.org
        (using https://github.com/rhgrant10/berserk)
        
        HOW TO USE THIS CLASS
            Instanciate this class with the Lichess bot token connection.
        HOW TO GET A LICHESS BOT TOKEN CONNECTION
            1) Create an account on https://lichess.org
            2) Go on https://lichess.org/account/oauth/token
            3) Click on "Generate a personal token"
            4) Name it, and give only the "Play as bot" permission
            5) Your personal token connection appears
        
        PROPERTIES
            token{String}
                The token connection to Lichess bot.
            api{berserk.clients.Client}
                API between Lichess and the program, with all properties and methods 
    """
    token=''
    api='{berserk.clients.Client}'
    
    def __init__(self, token):
        """
            Initialize the Lichess API for the given IA
            Example : Lichess('FN83ez2FZJxkUm5j')
    
            PARAM token{String} --> the token of user profile at https://lichess.org/account/oauth/token
            RETURN {None}
        """
        self.api = self.connect(token)
        self.token = token
    
    def connect(self, token):
        """
            Connect (or refresh) the IA to Lichess
            Example : Lichess.connect('FN83ez2FZJxkUm5j')
    
            PARAM token{String} --> the token of user profile at https://lichess.org/account/oauth/token
            RETURN {berserk.clients.Client} --> API between Lichess and the program, with all properties and methods
        """
        return berserk.Client(berserk.TokenSession(token))
    
    def games(self):
        """
            List all games to play by the connected bot
            Example : Lichess.games()
    
            RETURN {List} --> List of games to play
        """
        return list(self.api.games.get_ongoing())
    
    def move(self,gameId,move):
        """
            Play a move on the given game
            Example : Lichess.play('OY9lubYv','e2e4')
    
            PARAM gameId{String} --> the token of the game
            PARAM move{String} --> the move to do
        """
        self.api.bots.make_move(gameId,move)
    
    def fen(self,game):
        """
            Get the FEN format of the given Lichess game
            Example : Lichess.fen(Lichess.games()[0])
    
            PARAM game{Object} --> the Lichess game
            RETURN {String} --> The game in FEN format
        """
        return game['fen']+' '+game['color'][0]+' KQkq - 0 1' 

    def run(self):
        """
            Listen and play all unplayed games as Lichess bot
            Example : Lichess.run()
        """
        while(True):
            for game in self.games():
                if(game['isMyTurn']):
                    self.move(game['gameId'],IAMove(chess.Board(self.fen(game)))) #IAmove will become IA.move()

# You can launch this code with the official alpha-zoulou-tango Lichess bot : BrynanumBot !
# For that, uncomment this two lines and execute this file.
#lichess=Lichess('FN83ez2FZJxkUm5j')
#lichess.run()