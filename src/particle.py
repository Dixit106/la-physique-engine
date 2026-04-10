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

    def update(self, screen_width, screen_height):
        #Gravity(push or pull ? )
        gravity = pygame.math.Vector2(0, 0.5)
        self.apply_force(gravity)

        #Velocity changes postion (no shit sherlock)
        self.position += self.velocity 
        self.velocity += self.acceleration 
        self.velocity *= 0.99
        self.acceleration *= 0 #To reset acceleration for the next frame

        #The bounce
        if self.position.y > screen_height - self.radius:
            self.position.y = screen_height - self.radius
            self.velocity.y *= -0.8 #reverse velocity

            #FIX THE BOUNCE TOGETER
            if abs(self.velocity.y) < 1.0:
                self.velocity.y = 0 

        #Left and Right Wall Collisions
        if self.position.x > screen_width - self.radius:
            self.position.x = screen_width - self.radius
            self.velocity.x *= -0.8
        elif self.position.x < self.radius:
            self.position.x = self.radius
            self.velocity.x *= -0.8        

    def draw(self, screen):
        #Drawing a circle to represent particle
        pygame.draw.circle(screen, (255, 0, 0), self.position, self.radius)        