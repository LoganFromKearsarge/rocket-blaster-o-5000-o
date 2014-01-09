import pygame, sys, math, time
from pygame.locals import *
if not pygame.font: print 'Warning, fonts disabled'
width = 900
height = 480
size = (width,height)
pygame.font.init()
font = pygame.font.Font(None, 36)

class Score():
    def __init__(self, value=0, pos = (100,height/8)):
        self.image = font.render(str(value), 1, (100,200,50))
        self.rect = self.image.get_rect()
        self.value = value
        self.place = pos
        self.amount = 0
    
    def place(self):
        self.rect.center = pt
        
    def increase(self, amount):
        self.value += amount
    
    def update(self):
        self.image = font.render(str(self.value), 1, (100,200,50))
        
    def reset(self):
        self.value = 0