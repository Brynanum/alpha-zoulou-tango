# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 09:34:51 2019

@author: amau7
"""
import menu
import JvsP
import PvsP
import lichess

m=menu.Menu()
m.gameInit()

# player vs program game
if m.getOpponent()==0:
    gameP=JvsP.Game()
    gameP.color=m.getColor()
    gameP.Play()

# program vs program game
elif m.getOpponent()==1 :
    if m.getLichess():
        lich=lichess.Lichess('FN83ez2FZJxkUm5j')
        lich.run()
    else:
        CurrentSim=PvsP.Simulation()
        CurrentSim.Simulate()
    