#importing
import pygame
from sys import exit
from particle import Particle 

pygame.init()
#display surface
screen = pygame.display.set_mode((800,400))
#the title 
pygame.display.set_caption('Physics Engine')
#for setting max frame rate
clock = pygame.time.Clock()

#Test Particle
p1 = Particle(100, 200, 20)
#Movement
p1.velocity.x = 2 

while True:
    #to close window or else it's stuck
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.fill((0, 0, 0))

    #to draw all elements
    #update everything
    p1.update(800, 400)
    #setting max frame rate
    p1.draw(screen)

    pygame.display.update()
    clock.tick(60)
