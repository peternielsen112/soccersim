import pgzrun
import random
import pygame
import sys
from pygame.locals import *
import time

WIDTH = 765
HEIGHT = 480


class Game():
    def __init__(self):
        self.score = 0
        self.view = 'start'
    
game = Game()

BACKGROUND_IMAGE = 'field'

def update():
    pass

def draw():
    screen.clear()
    screen.blit(BACKGROUND_IMAGE, (0,0))

pgzrun.go()