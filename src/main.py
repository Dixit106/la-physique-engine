#importing
import pygame

pygame.init()
#display surface
screen = pygame.display.set_mode((800,400))

while True:
    #to close window or else it's stuck
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    #to draw all elements
    #update everything
    pygame.display.update()