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

#to keep track which ball we r holding
dragged_particle = None 

while True:
    #to close window or else it's stuck
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        #when mouse is pressed down 
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos())
            #to check if mouse is inside p1 or p2 
            if mouse_pos.distance_to(p1.position) < p1.radius:
                dragged_particle = p1 
            elif mouse_pos.distance_to(p2.position) < p2.radius: 
                dragged_particle = p2 

        #when mouse released 
        elif event.type == pygame.MOUSEBUTTONUP:
            dragged_particle = None 

    #if dragging particle snap it to mouse
    if dragged_particle: 
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dragged_particle.position.x = mouse_x 
        dragged_particle.position.y = mouse_y 
        #setting velocity 0 so no momentum builds up
        dragged_particle.velocity *= 0                        

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
