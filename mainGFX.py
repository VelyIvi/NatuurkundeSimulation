# Import module
import tkinter as tk
import matplotlib.pyplot as plt


# Create object
root = tk.Tk()


PI = 3.14159265359

height = float(401000.0) #meters
v = 0.0 #m/s

mass = 1.0 #kilos
ballRadius = 0.01 #m
areaMove = (4*PI*ballRadius*ballRadius)/2 #m^2
DragCoef = 0.47

time = 0.0
dT = 0.01 #seconds delta

massEarth = 5.972 * pow(10, 24)
gravityConstant = 6.67430* pow(10, -11)
earthRad = 6371000

#https://en.wikipedia.org/wiki/Density_of_air
SLSAPressure = 101325.0
SLSTemperature = 288.15
ESGAcceleration = 9.80665
LRTemperature = 0.0065
IGConstant = 8.31446
MolarMass = 0.0289652


timeList = []
heightList = []
speedList = []
accelList = []
airList = []
airPressureList = []
jouleList = []
gravList = []

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
    return con*pow(v,2)

accel = 0
joule = 0

while height > 0.0:
    time += dT

    Air = calcAirRes()
    Grav = calcGrav()

    accel = (Grav-Air)/mass
    v += accel * dT
    height -= v * dT
    joule = 1/2 * mass * v*v

    timeList.append(time)
    heightList.append(height)
    speedList.append(v)
    airList.append(Air)
    accelList.append(accel)
    jouleList.append(joule)
    gravList.append(Grav)


options1 = [
    "Tijd",
    "Hoogte"
]

options1execute = [
    timeList,
    heightList
]

options1label = [
    "Tijd (s)",
    "Hoogte (m)"
]

options2 = [
    "Hoogte",
    "Snelheid",
    "Luchtweerstand",
    "Acceleratie",
    "Energie",
    "Zwaartekracht",
    "Luchtdruk"
]

options2execute = [
    heightList,
    speedList,
    airList,
    accelList,
    jouleList,
    gravList,
    airPressureList
]

options2label = [
    "Hoogte (m)",
    "Snelheid (m/s)",
    "Luchtweerstand (N)",
    "Acceleratie (m/s/s)",
    "Energie (J)",
    "Zwaartekracht (N)",
    "Luchtdruk (Pa)"
]


def sGraph():
    result1 = options1.index(clicked1.get())
    result2 = options2.index(clicked2.get())
    plt.plot(options1execute[result1], options2execute[result2], color='red', linewidth=1.5)
    plt.xlabel(options1label[result1])
    plt.ylabel(options2label[result2])
    if clicked1.get() == "Hoogte":
        plt.gca().invert_xaxis()
    plt.show()


# Adjust size
root.geometry( "400x400" )


# Dropdown menu options


clicked1 = tk.StringVar()
        
clicked1.set(options1[0])

clicked2 = tk.StringVar()

clicked2.set(options2[0])

drop1 = tk.OptionMenu( root , clicked1 , *options1 )
drop1.pack()

drop2 = tk.OptionMenu( root , clicked2 , *options2 )
drop2.pack()
# Create button, it will change label text
button = tk.Button(root , text = "Show Graph", command=sGraph).pack()

root.mainloop()