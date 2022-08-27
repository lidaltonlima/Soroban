from msilib.schema import Feature
import pygame
from pygame.locals import *
from sys import exit
import objects


pygame.init()
screen = pygame.display.set_mode((640, 400))
pygame.display.set_caption('Soroban')

#count = objects.Count(screen, (255, 0, 0), (0, 255, 0), 100, 100, 50)
frame = objects.Frame(screen, (255, 0, 0), (0, 255, 0), (0, 0, 255), 600, 250, 10, 10, 10)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()  
            
    frame.draw(20, 20)
    
    pygame.display.update()
