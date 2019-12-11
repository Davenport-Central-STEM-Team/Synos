#!/usr/bin/env python3
import time

NULL_CHAR = chr(0)


def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode('latin-1'))


def write_null():
    write_report(NULL_CHAR*3)


def invert(number):
    return 5


def pixels_to_hex(pixels):
    return hex(pixels)


def signed_int_to_hex(input=0):

    number = int(input)

    if number < 0:
        number += (1 << 8)
        hexValue = hex(number)
        return chr(int(hexValue, 16))
    elif number >= 0:
        hexValue = hex(number)
        return chr(int(hexValue, 16))
    else:
        pass


def leftClick():
    write_report(chr(1) + NULL_CHAR * 2)
    time.sleep(0.1)
    write_null()


def rightClick():
    write_report(chr(2) + NULL_CHAR * 2)
    time.sleep(0.1)
    write_null()


def move_mouse(x, y):
    print(signed_int_to_hex(x))
    write_report(NULL_CHAR + signed_int_to_hex(x) + signed_int_to_hex(y))


def fuckit(hex):
    number = int(hex, 16)
    print(number)
    character = chr(number)
    print(character.encode('latin-1'))


move_mouse(-127, -127)
