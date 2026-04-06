import pygame 

class Particle:
    def __init__(self, x, y, radius):
        #Pygame's built-in vector for position, velocity, and acceleration :)
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, 0)
        self.radius = radius 

    def update(self):
        #Velocity changes postion (no shit sherlock)
        self.position += self.velocity 

    def draw(self, screen):
        #Drawing a circle to represent particle
        pygame.draw.circle(screen, (255, 0, 0), (int(self.position.x), int(self.position.y)), self.radius)        