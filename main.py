import pygame
from pygame.locals import *
from sys import exit
import objects

# Global Vars
sb_width = 1060
sb_height = 280

# Main setups
pygame.init()
screen = pygame.display.set_mode((1100, 400))
pygame.display.set_caption('Soroban')

# Create objects
count = objects.Count(screen, (255, 0, 0), (0, 255, 0), 50, 30, 20)
frame = objects.Frame(screen, (255, 0, 0), (0, 255, 0), (0, 0, 255), sb_width, sb_height, 12, 19, 8)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    frame.draw(20, 20)
    count.draw(80, 80)
    
    pygame.display.update()
