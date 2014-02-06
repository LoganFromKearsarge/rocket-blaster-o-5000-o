import pygame, sys, math, time
from pygame.locals import *
if not pygame.font: print 'Warning, fonts disabled'
width = 900
height = 480
size = (width,height)
pygame.font.init()
font = pygame.font.Font(None, 36)

class Score():
    def __init__(self, value=0, pos = (12.5,12.5)):
        self.image = font.render(str(value), 1, (100,200,50))
        self.rect = self.image.get_rect()
        self.value = value
        self.pos = pos
        self.place(pos)
        self.amount = 0
    #setting the scores position
    def place(self, pt):
        self.rect.center = pt
    #defining how much the score increases   
    def increase(self, amount):
        self.value += amount
    #defining how much the score decreases
    def decrease(self, amount):
        self.value -= amount
    #tellin the score it should update
    def update(self):
        self.image = font.render(str(self.value), 1, (100,200,50))
    #telling the score to reset    
    def reset(self):
        self.place(self.pos)
        self.value = 0


