import pygame, sys, math, random, time
from pygame.locals import *

width = 900
height = 480
size = width, height

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)
bgColor = r,g,b = 0,0,0
bgImage = pygame.image.load("Resources/Start_Screen/StartScreen.png")
bgRect = bgImage.get_rect()

start = False
while True:
    while not start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        bgImage = pygame.image.load("Resources/Background/Background.png")
                        start = True
            
            screen.blit(bgImage, bgRect)
            pygame.display.flip()
            clock.tick(60)

            