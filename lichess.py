# -*- coding: utf-8 -*-
import berserk

class Lichess:
    """
        API that links the program and lichess.org
        (using https://github.com/rhgrant10/berserk)
        
        PROPERTIES :
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