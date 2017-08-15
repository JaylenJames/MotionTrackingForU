import mraa
from SF_9DOF import IMU
from  math import *


def sensor_reader ():
    jaylen_data = IMU()
    jaylen_data.initialize()

    #enable sensors here
    jaylen_data.enable_accel()
    jaylen_data.enable_gyro()
    
    #declaring the range of the accelerometer
    jaylen_data.accel_range("8G")

    jaylen_data.read_accel()
    jaylen_data.read_gyro()

    ax = jaylen_data.ax
    ay = jaylen_data.ay
    az = jaylen_data.az

    gx = jaylen_data.gx
    gy = jaylen_data.gy
    gz = jaylen_data.gz

    return ax, ay, az

def initialization(ax, ay, az):

    theta1 = asin(-ax/9.8)
    theta2 = atan(ay/az)


    e4 = sqrt(1 + cos(theta1) + cos(theta2) + cos(theta1)*cos(theta2))/(2)
    e1 = sin(theta2)*(1+cos(theta1))/(4*e4)
    e2 = sin(theta1)*(1+cos(theta2))/(4*e4)
    e3 = -sin(theta1)*sin(theta2)/(4*e4)

    
    return e1, e2, e3, e4

ax, ay, az = sensor_reader()

print initialization(ax, ay, az)


print sensor_reader ()






