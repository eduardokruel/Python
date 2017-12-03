# Snake Game
# By Eduardo Kruel

# Imports
import pygame
import sys
import random
import time

# Error check
check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized!")

# Play Surface
playSurface = pygame.display.set_mode((720,460))
pygame.display.set_caption('Snake Game by Eduardo Kruel')
time.sleep(5)

# Colors
red = pygame.Color(214,73,51) # Gameover
lightGreen = pygame.Color(171,255,79) # Snake
grey = pygame.Color(56,56,56) # Score
green = pygame.Color(41,191,18) # Food
lightBlue = pygame.Color(141,228,255) # Background

# FPS controller
fpsControler = pygame.time.Clock()

# Important variables
snakePos = [100,50]
snakeBody = [[100,50],[90,50],[80,50]]

foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True
