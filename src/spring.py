import pygame 

class Spring:
    def __init__(self, p1, p2, rest_length, stiffness):
        def __init__(self, p1, p2, rest_length, stiffness):
            self.p1 = p1 
            self.p2 = p2 
            self.rest_length = rest_length 
            self.stiffness = stiffness 

        def update(self):
            #Finding the distance and direction b/t two particles
            direction = self.p2.position - self.p1.position
            distance = direction.length()

            if distance == 0:
                return #This will prevent a math error

            #How much will it stretch or squish
            displacement = distance - self.rest_length 

            #Hooke's Law F= stiffness * displacement so:-
            force_magnitude = self.stiffness * displacement 

            #To turn direction into vector of length 1
            direction = direction.normalize()    