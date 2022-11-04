h = 401000.0 #meters
v = 0.0 #m/s

m = 1.0 #kilos

gC = 9.81

time = 0.0
dT = .1 #seconds delta


accel = 0
while h > 0:
    time += dT
    v = v+accel*dT
    accel = gC/m
    h = h - v*dT
    print("Height: " , round(h, 4) ,"   Speed: " , round(v, 4), "   Time: ", round(time, 4))
