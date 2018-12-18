# -*- coding: utf-8 -*-
import berserk

class Lichess:
    """
        API that links the program and lichess.org
        (using https://github.com/rhgrant10/berserk)
        
        HOW TO USE THIS CLASS
            1) Instanciate this class with your personal token connection (see HOW TO GET A PERSONAL TOKEN CONNECTION)
            2) Use properties and methods of Berserk library with Lichess.api
        HOW TO GET A PERSONAL TOKEN CONNECTION
            1) Connect (or create an account) on https://lichess.org
            2) Go on https://lichess.org/account/oauth/token
            3) Click on "Generate a personal token"
            4) Allow all functionnalities with the key (give all permissions)
            5) Your personal token connection appears
        
        PROPERTIES
            token{String}
                The token connection to Lichess.
                This token created by user : Connect, go on https://lichess.org/account/oauth/token, give all permissions, and validate.
            api{berserk.clients.Client}
                API between Lichess and the program, with all properties and methods 
    """
    token=''
    api='{berserk.clients.Client}'
    
    def __init__(self, token):
        """
            Initialize the Lichess API for the given user
            Example : Lichess('77k3YfMQJRwqv8aX')
    
            PARAM token{String} --> the token of user profile at https://lichess.org/account/oauth/token
            RETURN {None}
        """
        self.api = self.connect(token)
        self.token = token
    
    def connect(self, token):
        """
            Connect or refresh the user connection to Lichess
            Example : Lichess.connect('77k3YfMQJRwqv8aX')
    
            PARAM token{String} --> the token of user profile at https://lichess.org/account/oauth/token
            RETURN {berserk.clients.Client} --> API between Lichess and the program, with all properties and methods
        """
        return berserk.Client(berserk.TokenSession(token))