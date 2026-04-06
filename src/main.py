#importing
import pygame
from sys import exit

pygame.init()
#display surface
screen = pygame.display.set_mode((800,400))
#the title 
pygame.display.set_caption('Runner')
#for setting max frame rate
clock = pygame.time.Clock()

test_surface = pygame.Surface((100,200))
test_surface.fill('Green')

while True:
    #to close window or else it's stuck
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(test_surface,(0,0))

    #to draw all elements
    #update everything
    pygame.display.update()
    #setting max frame rate
    clock.tick(60)