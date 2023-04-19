from os import times
import pygame, sys

from pygame import time
from Settings import *
from Level import Levels

pygame.init()
screen = pygame.display.set_mode((screen_widht, Screen_Height))
clock = pygame.time.Clock()
level = Levels(level_map, screen)
timeMode = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
       


    screen.fill('#453363')
    level.run()

    pygame.display.update()
    clock.tick(timeMode)
