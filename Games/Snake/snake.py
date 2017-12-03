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
