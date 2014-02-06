import pygame, sys, math
width = 900
height = 480
size = width,height

class Shot():
    def __init__(self, pos = (0,0)):
        self.image = pygame.image.load("Resources/Shot/Rocket.png")
        self.rect = self.image.get_rect()
        self.speedx = 7
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.radius = self.rect.width/2
        self.place(pos)
        self.living = True
    #telling the shot where to shoot from    
    def place(self, pos):
        self.rect.center = pos
    #updating the shot    
    def update(self):
        self.move()
    #telling the shot how to move    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
    #telling the shot to collide with pretty much everything        
    def collide(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.radius + other.radius > self.distanceToPoint(other.rect.center):
                    self.living = False
                    other.kill()
                    return True
        return False
    #telling the shot to hit the wall                
    def collideWall(self, width, height):
        if self.rect.left < 0:
            self.living = False
        if self.rect.right > width:
            self.living = False
        if self.rect.top < 0:
            self.living = False
        if self.rect.bottom > height:
            self.living = False
    #complicated math          
    def distanceToPoint(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
    
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
                    
    