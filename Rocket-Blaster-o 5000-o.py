import pygame, sys, math, random, time
from pygame.locals import *
from Player import Player
from Shot import Shot
from Alien import Alien
from Score import Score
if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

width = 900
height = 480
size = width, height

pygame.init()

screen = pygame.display.set_mode(size)
bgColor = r,g,b = 0,0,0
bgImage = pygame.image.load("Resources/Start_Screen/StartScreen.png")
bgRect = bgImage.get_rect()

player = Player("Resources/Player/Player.png", (5,5), (100, height/2), (100,40))
shot = Shot("Resources/Shot/Rocket.png")
score = Score()

start = False
while True:
    while not start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        start = True
            
            screen.blit(bgImage, bgRect)
            pygame.display.flip()
            clock.tick(60)

            bgImage = pygame.image.load("Resources/Background/Background.png")

    while start:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.direction("up")
                    
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.direction("down")
                    
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    bgImage = pygame.image.load("Background.png")
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.direction("stop up")
                    
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.direction("stop down")
                    
        
        player.update()
        shot.update()
        alien.update()
        score.update()
        endScreen.update()
        startScreen.update()
        
        pygame.time.get_ticks()
        st = time.time()
        timeSinceStart = time.time()-st
        score.increase()
        
        
        screen.fill(bgColor)
        screen.blit(score.image, score.rect)
        screen.blit(bgImage, bgRect)
        screen.blit(player.image, player.rect)
        screen.blit(text, textpos)
        pyame.display.flip()
        clk.tick(60)