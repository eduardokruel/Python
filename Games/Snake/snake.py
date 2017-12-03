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

direction = "RIGHT"
changeTo = direction


# Game Over Function
def gameOver():
    myFont = pygame.font.SysFont("monaco", 100)
    gameOverSurf = myFont.render("Game Over!", True, red)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (360,30)
    playSurface.blit(gameOverSurf, gameOverRect)
    pygame.display.update()
    time.sleep(5)
    pygame.quit() # pygame exit
    sys.exit() # console exit


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # pygame exit
            sys.exit() # console exit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord("d"):
                changeTo = "RIGHT"
            if event.key == pygame.K_LEFT or event.key == ord("a"):
                changeTo = "LEFT"
            if event.key == pygame.K_UP or event.key == ord("w"):
                changeTo = "UP"
            if event.key == pygame.K_DOWN or event.key == ord("s"):
                changeTo = "DOWN"
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))


    if changeTo == "RIGHT" and not direction == "LEFT":
        direction = "RIGHT"
    if changeTo == "LEFT" and not direction == "RIGHT":
        direction = "LEFT"
    if changeTo == "UP" and not direction == "DOWN":
        direction = "UP"
    if changeTo == "DOWN" and not direction == "UP":
        direction = "DOWN"
