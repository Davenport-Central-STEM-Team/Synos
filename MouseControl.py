#!/usr/bin/env python3
import time
import HIDInput as Hid
import math

""" 
HID Mouse Control:

Provide functions to control on-screen cursor
Communicates intentions to HIDInput Class
"""

__author__ = 'Nick Vazquez, Nick Wisong'
__copyright__ = 'Copyright 2019, DCHS STEM Team'
__license__ = 'MIT'
__version__ = '0.1.0'
__email__ = 'vazqueznicholas1@gmail.com'
__status__ = "In Development"
__class__ = None


class MouseControl:

    # Angle for continuous movement
    angle = 0
    # Speed for continuous movement
    speed = 0
    # Boolean for if cursor is currently performing continuous movement
    cursorIsMoving = False

    """ Return angle for continuous movement """
    @property
    def getAngle(self):
        return self.angle

    """ Return speed for continuous movement """
    @property
    def getSpeed(self):
        return self.speed

    """ Convert a signed integer to its' corresponding 32 bit hex value
    :param intIn: signed 32 bit integer to be converted
    :type intIn: int
    :returns: 32 bit hex value for intIn
    :raises: ValueError when number is not interpretable by function
    """
    @staticmethod
    def signed_int_to_hex(intIn=0):

        # TODO: Would it be possible to remove this because of the "intIn=0"?
        number = int(intIn)

        if number == 0:
            return Hid.NULL_CHAR
        elif number < 0:
            number += (1 << 8)
            hexValue = hex(number)
            return chr(int(hexValue, 16))
        elif number >= 0:
            hexValue = hex(number)
            return chr(int(hexValue, 16))
        else:
            raise ValueError("Value was not interpretable")

    """ Perform cursor left click"""
    @staticmethod
    def leftClick():
        Hid.write_report(chr(1) + Hid.NULL_CHAR * 2)
        time.sleep(0.1)
        Hid.write_null()

    """ Perform cursor right click """
    @staticmethod
    def rightClick():
        Hid.write_report(chr(2) + Hid.NULL_CHAR * 2)
        time.sleep(0.1)
        Hid.write_null()

    """ Move on-screen cursor
    :param x: Pixels to move in X direction
    :param y: Pixels to move in Y direction - Made negative to work with coordinate plane better (HID defines positive 
    Y movement as negative input)
    :type x: int
    :type y: int
    """
    def moveCursorXY(self, x, y):
        Hid.write_report(Hid.NULL_CHAR + self.signed_int_to_hex(x) + self.signed_int_to_hex(-y))

    """ Move on-screen cursor with angle and speed"""
    # def moveCursorTheta(self):
    #     xMove = round(math.cos(self.angle) * self.speed)
    #     yMove = round(math.sin(self.angle) * self.speed)
    #     print("Cursor X:", xMove, "Cursor Y", yMove)
    #     self.moveCursorXY(xMove, yMove)
