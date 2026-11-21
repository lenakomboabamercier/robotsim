# PC 2
class Capteur :
    def __init__(self,portee_max=50.0):
        self.portee_max = portee_max
        self.distance = None
 
    def mesurer(self,distance_obstacle):
        if distance_obstacle > self.portee_max :
            self.distance = None
        else :
            self.distance = distance_obstacle
        return self.distance