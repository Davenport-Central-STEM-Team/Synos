#!/usr/bin/env python

from mpu9250 import Mpu9250
from time import sleep

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

        print("Init @: X - ", self.initGyro[0], "Y - ", self.initGyro[1], "Z - ", self.initGyro[2])
        
    def check_angle(self):
        # Check if the status is triggered or not to start loop
        while not self.trigger_set:
            for int(i) in imu.gyro:
                if imu.gyro[i] > self.trigger_angle:
                    trigger_set = True
                    print("Gyro: ", imu.gyro, type(imu.gyro))

        sleep(2)
        self.trigger_set = False

    # @staticmethod
    # def getAccel():
    #     return imu.accel
    #
    # @staticmethod
    # def getGyro():
    #     return imu.gyro


gyro = ReadGyro(15)
sleep(10)
while True:
    gyro.check_angle()
