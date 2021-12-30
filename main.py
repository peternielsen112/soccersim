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
PLAYER_SPEED = 5
PLAYER_1_START = (555,225)
PLAYER_2_START = (200,230)
BACKGROUND_IMAGE = 'field'

# Defining Game object class
class Game():
    def __init__(self):
        self.score = 0
        self.view = 'start'
        self.FRAMES = 0
        self.ballCollisions = 0

# Setting object game as type Game   
game = Game()

# Creating players
player_1 = Actor('ball',PLAYER_1_START)
player_2 = Actor('ball',PLAYER_2_START)


# Keyboard input
# Get Player 1's keyboard input
def GET_KEYBOARD(SPEED):
    if keyboard.LEFT:
        player_1.x -= SPEED
    elif keyboard.RIGHT:
        player_1.x += SPEED
    elif keyboard.DOWN:
        player_1.y += SPEED
    elif keyboard.UP:
        player_1.y -= SPEED
# Get Player 2's keyboard input
def GET_KEYBOARD_2(SPEED):
    if keyboard.a:
        player_2.x -= SPEED
    elif keyboard.d:
        player_2.x += SPEED
    elif keyboard.s:
        player_2.y += SPEED
    elif keyboard.w:
        player_2.y -= SPEED


# Testing for ball collisions
def testBallCollision():
    if player_1.colliderect(player_2):
        player_1.pos = PLAYER_1_START
        player_2.pos = PLAYER_2_START
        game.ballCollisions += 1
        game.score -= 10
        time.sleep(0.3)

# Testing score for game's end
def testScore():
    lose = f'''
You lose!!!

Score: {game.score}
Ball Collisions: {game.ballCollisions}
Frames: {game.FRAMES}
'''
    win = f'''
You win!!!

Score: {game.score}
Ball Collisions: {game.ballCollisions}
Frames: {game.FRAMES}
'''
    if game.score <= -100:
        print(lose)
        quit()
    elif game.score >= 100:
        print(win)
        quit()
    else:
        pass

# Update loop
def update():
    GET_KEYBOARD(PLAYER_SPEED)
    GET_KEYBOARD_2(PLAYER_SPEED)
    testBallCollision()
    testScore()
    game.FRAMES += 1

# Draw loop
def draw():
    screen.clear()
    screen.blit(BACKGROUND_IMAGE, (0,0))
    player_1.draw()
    player_2.draw()

# Wrap up with pgzrun.go() method to combine update and draw loops
pgzrun.go()