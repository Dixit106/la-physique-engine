import pygame 

class Particle:
    def __init__(self, x, y, radius):
        #Pygame's built-in vector for position, velocity, and acceleration :)
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, 0)
        self.radius = radius
        self.mass = 1.0 

    def apply_force(self, force):   
        #F=ma, so a=F/m
        self.acceleration += force / self.mass   

    def update(self):
        #Gravity(push or pull ? )
        gravity = pygame.math.Vector2(0, 0.5)
        self.apply_force(gravity)

        #Velocity changes postion (no shit sherlock)
        self.position += self.velocity
        self.velocity += self.acceleration 
        self.acceleration *= 0 #To reset acceleration for the next frame

    def draw(self, screen):
        #Drawing a circle to represent particle
        pygame.draw.circle(screen, (255, 0, 0), (int(self.position.x), int(self.position.y)), self.radius)        