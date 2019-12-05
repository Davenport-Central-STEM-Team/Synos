#!/usr/bin/env python3
NULL_CHAR = chr(0)


# def write_report(report):
#     with open('/dev/hidg0', 'rb+') as fd:
#         fd.write(report.encode())
#
# # Press a
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
def signed16(value):
    return -(value & 0x80000000) | (value & 0x7fffffff)


def pixels_to_hex(pixels):
    print(hex(pixels))


def posIntToHex(pixels):
    if pixels >= 0:
        return chr(pixels)
    else:
        raise ArithmeticError("Number is not positive!")

# print(signed16(int('0x7f', 16)))
# pixels_to_hex(-127)
# print(chr(-127) == '\xFFFFFF81')
try:
    print(posIntToHex(-127))
except ArithmeticError:
    print("You done fucked up.")
except:
    print("IDEK what u did, bro")
