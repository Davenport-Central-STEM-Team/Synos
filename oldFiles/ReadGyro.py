#!/usr/bin/env python

from mpu9250 import Mpu9250
import time
import matplotlib.pyplot as plot
import MouseControl

__author__ = 'Nick Wisong, Sarah Van Liere'
__copyright__ = 'Copyright 2019, DCHS STEM Team'
__license__ = 'MIT'
__version__ = '0.1.0'
__email__ = ''
__status__ = "In Development"
__class__ = None

imu = Mpu9250()


class ReadGyro(object):
    """ Instantiate the ReadGyro Class
        trigger_angle: Angle at which to output a trigger state (X, Y, Z Array of angles)
        initGyro: Angles at which the gyro was instantiated at
        trigger_set: Trigger state flag
    """

    def __init__(self, trigger_angle):
        # Take the passed trigger angle
        self.trigger_angle = trigger_angle
        self.initGyro = imu.gyro
        self.trigger_set = False
        self.xValues = []
        self.times = []
        self.startTime = time.time()
        # Nick V is a possessive ass
        self.mouse = MouseControl.MouseControl()

        print("Init @: X - ", self.initGyro[0], "Y - ", self.initGyro[1],
              "Z - ", self.initGyro[2])

    def check_angle(self):
        # Check if the status is triggered or not to start loop
        while not self.trigger_set:
            if imu.gyro[0] > self.trigger_angle:
                self.mouse.leftClick()
                # print("Gyro: ", imu.gyro, type(imu.gyro))
                print("Gyro: Triggered ", imu.gyro[0])
                trigger_set = True
                time.sleep(2)
            print("Hi :)")
            time.sleep(0.05)

        time.sleep(2)
        self.trigger_set = False

    def plot(self):
        for i in range(100):
            self.xValues.append(imu.gyro[0])
            self.times.append(time.time())
            print(imu.gyro[0])
            time.sleep(1)

        plot.plot(self.times, self.xValues)
        plot.show()

    # @staticmethod
    # def getAccel():
    #     return imu.accel
    #
    # @staticmethod
    # def getGyro():
    #     return imu.gyro


# gyro = ReadGyro(15)
# time.sleep(10)
# while True:
#     gyro.check_angle()

readGyro = ReadGyro(10)

# readGyro.plot()

readGyro.check_angle()
