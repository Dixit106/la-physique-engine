#importing
import pygame
from sys import exit
from particle import Particle
from spring import Spring  

pygame.init()
#display surface
screen = pygame.display.set_mode((800,400))
#the title 
pygame.display.set_caption('Demo: Falling Ball with Infinite Energy Physics Engine')
#for setting max frame rate
clock = pygame.time.Clock()

#Test Particle
p1 = Particle(100, 50, 20)
p1.velocity.x = 15

#Linking the spring
num_particles = 8
spacing = 30 

gravity = pygame.math.Vector2(0, 0.5)

while True:
    #to close window or else it's stuck
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    

    p1.apply_force(gravity)
    p1.update(800, 400)

    p1.draw(screen)

    pygame.display.update()
    clock.tick(60)        