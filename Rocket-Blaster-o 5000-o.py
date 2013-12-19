import pygame, sys, math, random, time
from pygame.locals import *
from Player import Player
from Shot import Shot
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



aliens = []
shots = []
player = Player("Resources/Player/Player.png", (5,5), (100, height/2), (100,40))
shot = Shot("Resources/Shot/Rocket.png", (50,20), (0,0))
#score = Score()
start = False
while True:
    bgImage = pygame.image.load("Resources/Start_Screen/StartScreen.png")
    
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

    st = time.time()
    bgImage = pygame.image.load("Resources/Background/Background.png")
    
    while start and player.living:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.direction("up")
                    
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.direction("down")
            
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.direction("right")
                    
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.direction("left")
                if event.key == pygame.K_SPACE:
                    shots += [Shot(player.rect.center)]
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.direction("stop up")
                    
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.direction("stop down")
                    
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.direction("stop right")
                    
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.direction("stop left")             
                    
        
        if len(aliens) < 12:
            if random.randint(0, 10) == 0:
                skin = ["Resources/Alien/mob1.png","Resources/Alien/mob2.png","Resources/Alien/mob3.png"] 
                alienSkin = skin[random.randint(0,2)]
                aliens += [Alien(alienSkin, (-5, 0), (100, 40), (width, random.randint(20, height-20)))]
            
        
        player.update()
        if player.rect.left < 0:
            player.rect.left = 0
        if player.rect.right > width:
            player.rect.right = width
        if player.rect.top < 0:
            player.rect.top = 0
        if player.rect.bottom > height:
            player.rect.bottom = height
        for alien in aliens:
            alien.update()
        #score.update()
        
        for alien in aliens:
            alien.collideWall(width, height)
            alien.collideAlien(player)
        
        pygame.time.get_ticks()
        timeSinceStart = time.time()-st
        #score.increase(value)
        
        for alien in aliens:
            if not alien.living:
                aliens.remove(alien)
        
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        for alien in aliens:
            screen.blit(alien.image, alien.rect)
        screen.blit(player.image, player.rect)
        #screen.blit(score.image, score.rect)
        #screen.blit(score.image, score.rect)
        #screen.blit(text, textpos)
        pygame.display.flip()
        clock.tick(60)
    
    bgImage = pygame.image.load("Resources/End_Screen/EndScreen.png")    
    
    while start and not player.living:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    start = False
                    aliens = []
                    player = Player("Resources/Player/Player.png", (5,5), (100, height/2), (100,40))
                
        
        screen.blit(bgImage, bgRect)
        pygame.display.flip()
        clock.tick(60)
    
            
            
