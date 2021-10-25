import pygame
import random
from math import pi

pygame.init()
pygame.display.set_caption('Scary')
WINDOW_SIZE = (800,800)
screen = pygame.display.set_mode(WINDOW_SIZE,0,32)

class pumpkin:
    def __init__(self, x, y):
        self.xPos = x
        self.yPos = y
        self.length = random.randint(80, 200)
        self.width = random.randint(80, 150)
        self.color = (random.randint(-20, 20), random.randint(-10, 10), random.randint(-10, 10))
        self.Color = (234, 117, 24)
        if random.randint(0,100) == 1:
            self.Color = (234,244,244)
    def draw(self, screen):
        pygame.draw.rect(screen, (50, 200, 10), (self.xPos+self.length/2.5,self.yPos-15, 20, 20))#STEM
        pygame.draw.ellipse(screen, (self.Color[0]+self.color[0], self.Color[1]+self.color[1], self.Color[2]+self.color[2]), (self.xPos,self.yPos, self.length, self.width))

        pygame.draw.arc(screen, (0,0,0), (self.xPos+self.length/4,self.yPos+self.width/8,self.length/4,self.width/4), 0, pi, 4)#eyes
        pygame.draw.arc(screen, (0,0,0), (self.xPos+self.length/1.9,self.yPos+self.width/8,self.length/4,self.width/4), 0, pi, 4)#eyes

        pygame.draw.arc(screen, (0,0,0), (self.xPos+self.length/4,self.yPos+40,self.length/2,self.width/2), pi, 0, 7)#mouth
        


patch = list()

running = True

clock = pygame.time.Clock()

while running:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
    mousePos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed(3)

    screen.fill((0,0,0))
    
    if click[0]:
        patch.append(pumpkin(mousePos[0], mousePos[1]))
    if len(patch) > 0:
        if click[2]:
            patch.pop()
    if len(patch)%100 == 0:
        print(len(patch))
    for i in range(len(patch)):
        patch[i].draw(screen)
    pygame.display.flip()

pygame.quit()
