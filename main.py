h = 100.0 #meters
v = 0 #m/s

m = 1 #kilos

gC = -9.81 

dT = .1 #seconds delta


accel = 0
while h > 0:
    print("Height: " , h ,"   Speed: " , v)
    v = v+accel*dT
    accel = gC/m
    h = h + v*dT
