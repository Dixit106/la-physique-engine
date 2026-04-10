#importing
import pygame
from sys import exit
from particle import Particle
from spring import Spring  

pygame.init()
#display surface
screen = pygame.display.set_mode((800,400))
#the title 
pygame.display.set_caption('Chain Prototype')
#for setting max frame rate
clock = pygame.time.Clock()

#Test Particle
particles = []
springs = []

#Linking the spring
num_particles = 8
spacing = 30 

for i in range(num_particles):
    p = Particle(400, 50 + (i * spacing), 15)
    particles.append(p)

#To connect them with springs
for i in range(num_particles - 1):
    s = Spring(particles[i], particles[i+1], spacing, 0.2)
    springs.append(s)    

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
            for p in particles: 
                if mouse_pos.distance_to(p.position) < p.radius:
                    dragged_particle = p
                    break 

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


    particles[0].position.x = 400
    particles[0].position.y = 50
    particles[0].velocity *= 0  

    for s in springs:
        s.update()

    for p in particles:
        p.update(800, 400)

    screen.fill((20, 20, 30))

    for s in springs:
        s.draw(screen)

    for p in particles:
        p.draw(screen)

    pygame.display.update()
    clock.tick(60)                                       
