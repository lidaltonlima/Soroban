import pygame
from pygame.locals import *
from sys import exit
import objects


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Soroban')

count = objects.Count(screen, (255, 0, 0), (0, 255, 0), 100, 100, 50)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()  
    count.draw(100, 100)
    
    pygame.display.update()
