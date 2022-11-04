Height = 401000.0 #meters
v = 0.0 #m/s

mass = 1.0 #kilos


time = 0.0
dT = .1 #seconds delta


massEarth = 5.972 * pow(10, 24)
gravityConstant = 6.67430* pow(10, -11)
earthRad = 6371000
def CalcGrav():
    force = gravityConstant * ((massEarth*mass)/(pow(Height+earthRad, 2)))
    return force

accel = 0
while Height > 0:
    time += dT
    v = v+accel*dT
    Grav = CalcGrav()
    accel = Grav/mass
    Height = Height - v*dT
    print("Height: " , round(Height, 4) ,"   Speed: " , round(v, 4), "   Time: ", round(time, 4), " Gravity: ", round(Grav, 4))



