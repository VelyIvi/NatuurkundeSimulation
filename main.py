import matplotlib.pyplot as plt

PI = 3.14159265359

height = 401000.0 #meters
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


timeList = []
heightList = []
speedList = []
accelList = []
airList = []

def calcGrav():
    force = gravityConstant * ((massEarth*mass)/(pow(height+earthRad, 2)))
    return force

#https://en.wikipedia.org/wiki/Density_of_air
SLSAPressure = 101325
SLSTemperature = 288.15
ESGAcceleration = 9.80665
LRTemperature = 0.0065
IGConstant = 8.31446
MolarMass = 0.0289652
def calcAirPressure():
    press = SLSAPressure*pow((1-(LRTemperature*height)/(SLSTemperature)), ((ESGAcceleration*MolarMass)/(IGConstant*LRTemperature)))
    return press
def calcAirDensity():
    press = calcAirPressure()
    density = (press*MolarMass)/(IGConstant*(SLSTemperature-LRTemperature*height))
    return density

def calcAirConst():
    density = calcAirDensity()
    AirConstant = (density*DragCoef*areaMove)/(2)
    return AirConstant


def calcAirRes():
    return calcAirConst()*v*v

accel = 0
while int(height) > 0:
    time += dT

    Air = calcAirRes()
    Grav = calcGrav()

    v = v+accel*dT
    accel = (Grav-Air)/mass
    height = height - v*dT
    timeList.append(time)
    heightList.append(height)
    speedList.append(v)
    airList.append(Air)
    accelList.append(accel)


plt.plot(speedList, airList, color='red', linewidth = .5)
# plt.title('height at any time')
plt.xlabel('speed')
plt.ylabel('air')
plt.grid(True)
plt.show()