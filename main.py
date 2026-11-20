from robot import Robot

cote = 10
r = Robot()

for i in range(4) :
    r.avancer(cote)
    r.tourner(90)
    print(r.position())

