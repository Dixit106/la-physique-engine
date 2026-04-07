#importing
import pygame
from sys import exit
from particle import Particle
from spring import Spring  

pygame.init()
#display surface
screen = pygame.display.set_mode((800,400))
#the title 
pygame.display.set_caption('Jelly Engine')
#for setting max frame rate
clock = pygame.time.Clock()

#Test Particle
p1 = Particle(300, 100, 20)
p2 = Particle(450, 100, 20)

#Linking the spring
link = Spring(p1, p2, 100, 0.05)

while True:
    #to close window or else it's stuck
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.fill((0, 0, 0))

    #will have to link the spring first so it applies forces
    link.update()

    #to draw all elements
    #update everything
    p1.update(800, 400)
    p2.update(800, 400)
    #setting max frame rate
    link.draw(screen)
    p1.draw(screen)
    p2.draw(screen)

    pygame.display.update()
    clock.tick(60)
