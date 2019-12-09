#!/usr/bin/env python3
import time

NULL_CHAR = chr(0)


def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())


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
        hexValue = hex(number)[1:]
        hexQ = '\x7f'
        print("Hex Value" + hexValue)
        print("Int Value", int(hexValue))
        return hexQ.decode()
    elif number >= 0:
        hexValue = hex(number)
        return chr(int(hexValue))
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
    print(signed_int_to_hex(x), signed_int_to_hex(y))
    write_report(NULL_CHAR + signed_int_to_hex(x) + signed_int_to_hex(y))


# move_mouse(127, 127)
# write_report(NULL_CHAR + chr(signed_int_to_hex(x)) + NULL_CHAR)
signed_int_to_hex(-127)