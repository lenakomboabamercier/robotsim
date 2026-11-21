# PC 1
from robot import Robot

cote = 10
r = Robot()

for i in range(4) :
    r.avancer(cote)
    r.tourner(90)
    print(r.position())


r.avancer(-5)

print("Sur la table :", r.est_sur_table())