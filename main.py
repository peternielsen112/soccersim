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

# Creating players
player_1 = Actor('ball',(100,100))
player_2 = Actor('ball',(200,200))

# Setting background image
BACKGROUND_IMAGE = 'field'

# Update loop
def update():
    pass

# Draw loop
def draw():
    screen.clear()
    screen.blit(BACKGROUND_IMAGE, (0,0))
    player_1.draw()
    player_2.draw()

# Wrap up with pgzrun.go() method to combine update and draw loops
pgzrun.go()