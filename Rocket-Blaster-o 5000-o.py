import pygame, sys, math, random, time
from pygame.locals import *
from Player import Player
#from Shot import Shot
#from Score import Score
from Alien import Alien
if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

width = 900
height = 480
size = width, height

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)
bgColor = r,g,b = 0,0,0
bgImage = pygame.image.load("Resources/Start_Screen/StartScreen.png")
bgRect = bgImage.get_rect()

alien = Alien("Resources/Alien/mob1.png", (-5, 0), (100, 40), (width, height/2))
player = Player("Resources/Player/Player.png", (5,5), (100, height/2), (100,40))
#shot = Shot("Resources/Shot/Rocket.png", (50,20), (0,0))
#score = Score()
start = False
while True:
    while not start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start = True
                    bgImage = pygame.image.load("Resources/Background/Background.png")

        screen.blit(bgImage, bgRect)
        pygame.display.flip()
        clock.tick(60)

    st = time.time()
    while start:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.direction("up")
                    
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.direction("down")
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.direction("stop up")
                    
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.direction("stop down")
    
        if player.living == False:
            bgImage = pygame.image.load("Resources/End_Screen/EndScreen.png")
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    bgImage = pygame.image.load("Resources/Start_Screen/StartScreen.png")
                    
                if event.key == pygame.K_Q or event.ket == pygame.K_ESCAPE:
                    quit()
        
        player.update()
        alien.update()
        #shot.update()
        #score.update()
        
        pygame.time.get_ticks()
        timeSinceStart = time.time()-st
        #score.increase()
        
        screen.fill(bgColor)
        screen.blit(alien.image, alien.rect)
        screen.blit(bgImage, bgRect)
        screen.blit(player.image, player.rect)
        #screen.blit(score.image, score.rect)
        #screen.blit(score.image, score.rect)
        #screen.blit(text, textpos)
        pygame.display.flip()
        clock.tick(60)
