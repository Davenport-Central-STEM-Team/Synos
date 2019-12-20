#!/usr/bin/env python3
import HIDInput as Hid

""" 
HID Keyboard Control:

Provide functions to control HID keyboard emulated on device
Communicates intentions to HIDInput class
"""

__author__ = 'Nick Vazquez, Nick Wisong'
__copyright__ = 'Copyright 2019, DCHS STEM Team'
__license__ = 'MIT'
__version__ = '0.1.0'
__email__ = ''
__status__ = "In Development"
__class__ = None

# TODO: Example Code
# # Press a
# # 0\0\x4\0\0\0\0\0
# write_report(NULL_CHAR*2+chr(4)+NULL_CHAR*5)
# # Release keys
# write_report(NULL_CHAR*8)
# # Press SHIFT + a = A
# write_report(chr(32)+NULL_CHAR+chr(4)+NULL_CHAR*5)
#
# # Press b
# write_report(NULL_CHAR*2+chr(5)+NULL_CHAR*5)
# # Release keys
# write_report(NULL_CHAR*8)
# # Press SHIFT + b = B
# write_report(chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5)
#
# # Press SPACE key
# write_report(NULL_CHAR*2+chr(44)+NULL_CHAR*5)
#
# # Press c key
# write_report(NULL_CHAR*2+chr(6)+NULL_CHAR*5)
# # Press d key
# write_report(NULL_CHAR*2+chr(7)+NULL_CHAR*5)
#
# # Press RETURN/ENTER key
# write_report(NULL_CHAR*2+chr(40)+NULL_CHAR*5)
#
# # Press e key
# write_report(NULL_CHAR*2+chr(8)+NULL_CHAR*5)
# # Press f key
# write_report(NULL_CHAR*2+chr(9)+NULL_CHAR*5)
#
# # Release all keys
# write_report(NULL_CHAR*8)

Hid.write_report_keyboard(Hid.NULL_CHAR*2 + chr(4) + Hid.NULL_CHAR*5)
print("IUGHNGSJG")

