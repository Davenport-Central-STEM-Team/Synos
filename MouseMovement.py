#!/usr/bin/env python3
import time

NULL_CHAR = chr(0)


def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

def write_null():
    write_report(NULL_CHAR*3)


def pixels_to_hex(pixels):
    return hex(pixels)


def posIntToHex(pixels):
    if pixels >= 0:
        return chr(pixels)
    else:
        raise ArithmeticError("Number is not positive!")


def leftClick():
    write_report(chr(1) + NULL_CHAR * 2)
    time.sleep(0.1)
    write_null()


def rightClick():
    write_report(chr(2) + NULL_CHAR * 2)
    time.sleep(0.1)
    write_null()


while True:
    leftClick()
    time.sleep(0.5)
    rightClick()
    time.sleep(0.5)
