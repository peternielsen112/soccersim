# Import statements
import pgzrun
import random
import pygame
import sys
from pygame.locals import *
import time

# Constants
WIDTH = 765
HEIGHT = 480

# Defining Game object class
class Game():
    def __init__(self):
        self.score = 0
        self.view = 'start'

# Setting object game as type Game   
game = Game()

# Defining Player object class
# class Player(Actor):
#     def __init__(self):
#         self.image = 'field'
#         self.pos = (0,0)

# Setting objects player_1 and player_2 as type Player
# player_1 = Player()
# player_2 = Player()

player_1 = Actor('field',(100,100))
player_2 = Actor('field',(-100,-100))

# Setting background image
BACKGROUND_IMAGE = 'field'

# Update loop
def update():
    pass

# Draw loop
def draw():
    screen.clear()
    screen.blit(BACKGROUND_IMAGE, (0,0))

# Wrap up with pgzrun.go() method to combine update and draw loops
pgzrun.go()