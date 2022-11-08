PI = 3.14159265359

Height = 401000.0 #meters
v = 0.0 #m/s

mass = 1.0 #kilos
ballRadius = 0.01 #m
areaMove = (4*PI*ballRadius*ballRadius)/2 #m^2
DragCoef = 0.47

time = 0.0
dT = 10 #seconds delta

massEarth = 5.972 * pow(10, 24)
gravityConstant = 6.67430* pow(10, -11)
earthRad = 6371000


def calcGrav():
    force = gravityConstant * ((massEarth*mass)/(pow(Height+earthRad, 2)))
    return force


def calcAirDensity():
    return 1.204

def calcAirConst():
    density = calcAirDensity()
    AirConstant = (density*DragCoef*areaMove)/(2)
    return AirConstant


def calcAirRes():
    return calcAirConst()*v*v

accel = 0
while Height > 0:
    time += dT
    Air = calcAirRes()
    Grav = calcGrav()

    v = v+accel*dT
    accel = (Grav-Air)/mass
    Height = Height - v*dT
    print("Height: " , round(Height, 4) ,"   Speed: " , round(v, 4), "   Time: ", round(time, 4), " Gravity: ", round(Grav, 4), " AirRes: ", round(Air, 4))
