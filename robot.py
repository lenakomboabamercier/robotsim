# Petit simulateur de déplacement d'un robot

import math

VITESSE_MAX = 1.0

class Robot : 

    def __init__(self, x=0.0, y=0.0, angle=0.0) :
        """Liste des attributs du robot """
        self.x = x
        self.y = y
        self.angle = angle #en degres
        self.batterie = 100


    # Les methodes

    def avancer(self,distance) :
        if distance < 0 :
            raise ValueError("La distance doit être positive ou nulle")
        rad = math.radians(self.angle)
        self.x += distance * math.cos(rad)
        self.y += distance * math.sin(rad)
        self.batterie -=distance * 0.1

    def tourner(self,degres) :
        """Tourne le robot. L'angle reste entre 0 et 359."""
        self.angle = (self.angle + degres)%360

    def position(self) :
        return round(self.x,2), round(self.y,2), self.angle

    def reset(self) :
        self.x = 0.0
        self.y = 0.0
        self.angle = 0.0

    def detecteur_obstacle(self,capteur,distance_obstacle,seuil=10.0):
        mesure = capteur.mesurer(distance_obstacle)
        return mesure is not None and mesure<seuil

    def est_sur_la_table(self,largeur=300,hauteur=200) :
        return 0 <= self.x <=largeur and 0 <=self.y <= hauteur

#modifié depuis le PC 2