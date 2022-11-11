import matplotlib.pyplot as plt

PI = 3.14159265359

height = float(401000.0) #meters
v = 0.0 #m/s

mass = 1.0 #kilos
ballRadius = 0.01 #m
areaMove = (4*PI*ballRadius*ballRadius)/2 #m^2
DragCoef = 0.47

time = 0.0
dT = 1 #seconds delta

massEarth = 5.972 * pow(10, 24)
gravityConstant = 6.67430* pow(10, -11)
earthRad = 6371000


timeList = []
heightList = []
speedList = []
accelList = []
airList = []
airPressureList = []


#https://en.wikipedia.org/wiki/Density_of_air
SLSAPressure = 101325.0
SLSTemperature = 288.15
ESGAcceleration = 9.80665
LRTemperature = 0.0065
IGConstant = 8.31446
MolarMass = 0.0289652

def lerp(A, B, t):
    print(A + (B-A)*t)
    return A + (B-A)*t
def calcGrav():
    return gravityConstant * ((massEarth*mass)/(pow(height+earthRad, 2)))

def calcAirPressure():
    if(height<=20000):
        pressure = SLSAPressure*pow((1-(LRTemperature*height)/SLSTemperature), ((ESGAcceleration*MolarMass)/(IGConstant*LRTemperature)))
        airPressureList.append(pressure)
        return pressure
    elif height > 20000:
        airPressureList.append(0)
        return 0

def calcAirDensity():
    press = calcAirPressure()
    return (press*MolarMass)/(IGConstant*(SLSTemperature-LRTemperature*height))

def calcAirConst():
    density = calcAirDensity()
    return (density*DragCoef*areaMove)/2


def calcAirRes():
    con = calcAirConst()
    return con*v*v

accel = 0

while height > 0.0:
    time += dT

    Air = calcAirRes()
    Grav = calcGrav()

    v += accel*dT
    accel = (Grav-Air)/mass
    height -= v*dT
    timeList.append(time)

    heightList.append(height)
    speedList.append(v)
    airList.append(Air)
    accelList.append(accel)


fig, axs = plt.subplots(2, 2)
# plt.gca().invert_xaxis()

axs[0,0].plot(timeList, heightList, color='red', linewidth = 1.5)
axs[0,0].set_xlabel('Time (s)')
axs[0,0].set_ylabel('Height (m)')

axs[1,0].plot(timeList, speedList, color='red', linewidth = 1.5)
axs[1,0].set_xlabel('Time (s)')
axs[1,0].set_ylabel('Speed (m/s)')

axs[0,1].plot(timeList, airList, color='red', linewidth = 1.5)
axs[0,1].set_xlabel('Time (s)')
axs[0,1].set_ylabel('Air Resistance (N)')


axs[1,1].plot(timeList, accelList, color='red', linewidth = 1.5)
axs[1,1].set_xlabel('Time (s)')
axs[1,1].set_ylabel('Acceleration (m/s/s)')

fig.tight_layout()

plt.show()