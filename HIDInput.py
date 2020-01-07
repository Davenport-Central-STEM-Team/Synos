#!/usr/bin/env python3
"""
HID Input Functions:

Provide functions to send HID Packets (report) to communication port (CommPort)
"""

__author__ = 'Nick Vazquez, Nick Wisong'
__copyright__ = 'Copyright 2019, DCHS STEM Team'
__license__ = 'MIT'
__version__ = '0.1.0'
__email__ = 'vazqueznicholas1@gmail.com'
__status__ = "In Development"
__class__ = None

NULL_CHAR = chr(0)
CommPort = '/dev/hidg0'


def write_report(report):
    with open(CommPort, 'rb+') as fd:
        fd.write(report.encode('latin-1'))


def write_report_keyboard(report):
    with open(CommPort, 'rb+') as fd:
        fd.write(report)


def write_null():
    write_report(NULL_CHAR * 3)
