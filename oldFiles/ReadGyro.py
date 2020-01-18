#!/usr/bin/env python

from mpu9250 import Mpu9250
import time
import matplotlib.pyplot as plot
import MouseControl
# from scipy.interpolate import interp1d

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

        # Accelerometer Values
        self.xValues = []
        self.yValues = []
        self.zValues = []

        # Gyro Values
        self.rxValues = []
        self.ryValues = []
        self.rzValues = []

        self.times = []
        self.startTime = time.time()
        # Nick V is a possessive ass
        self.mouse = MouseControl.MouseControl()

        print("Init @: X - ", self.initGyro[0], "Y - ", self.initGyro[1],
              "Z - ", self.initGyro[2])

    def left_click(self):
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
        for i in range(1000):
            # Read Gyro
            self.rxValues.append(imu.gyro[0] / 250)
            self.ryValues.append(imu.gyro[1] / 250)
            self.rzValues.append(imu.gyro[2] / 250)

            # Read Accelerometer
            self.xValues.append(imu.accel[0] / 2)
            self.yValues.append(imu.accel[1] / 2)
            self.zValues.append(imu.accel[2] / 2)

            # if i % 10 == 0:
            #     self.times.append(time.time() - self.startT0ime)
            self.times.append(time.time() - self.startTime)

            print(imu.gyro[0] / 250)
            time.sleep(0.0001)

        # plot.plot(self.times, self.ryValues)
        # plot.show()
        #
        # self.ryValues = self.smooth(self.ryValues)
        # plot.plot(self.times, self.ryValues)
        # plot.show()
        #
        # self.ryValues = self.smoother(self.ryValues)
        # plot.plot(self.times, self.ryValues)
        # plot.show()

        plot.plot(self.times, self.rxValues)
        plot.plot(self.times, self.ryValues)
        plot.plot(self.times, self.rzValues)
        plot.show()

        plot.plot(self.times, self.xValues)
        plot.plot(self.times, self.yValues)
        plot.plot(self.times, self.zValues)
        plot.show()

    def smooth(self, data):
        temp_sum = 0
        new_list = []
        for i in enumerate(data)):
            # print(i)
            # print(list)
            # print(list[i])
            temp_sum += list[i]
            if (i + 1) % 10 == 0:
                new_list.append(temp_sum / 10)
                temp_sum = 0
        return new_list

    @staticmethod
    def smoother(raw_list):
        new_list = []
        for i in enumerate(raw_list)):
            if 0 < i < len(raw_list) - 1:
                new_list.append(0.25 * raw_list[i-1]
                                + 0.5 * raw_list[i]
                                + 0.25 * raw_list[i+1])
            else:
                new_list.append(raw_list[i])

        return new_list


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

readGyro.plot()
