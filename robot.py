import math

class Robot : 

    def __init__(self, x=0.0, y=0.0, angle=0.0) :
        """Liste des attributs du robot """
        self.x = x
        self.y = y
        self.angle = angle #en degres


    # Les methodes

    def avancer(self,distance) :
        if distance < 0 :
            raise ValueError("La distance doit être positive ou nulle")
        rad = math.radians(self.angle)
        self.x += distance * math.cos(rad)
        self.y += distance * math.sin(rad)

    def tourner(self,degres) :
        self.angle = (self.angle + degres)%360

    def position(self) :
        return round(self.x,2), round(self.y,2), self.angle

    def reset(self) :
        self.x = 0.0
        self.y = 0.0
        self.angle = 0.0