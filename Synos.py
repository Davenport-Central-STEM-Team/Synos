import time

from MouseControl import MouseControl
from ReadGyro import ReadGyro


if __name__ == "__main__":
    # Do this if the program is invoked directly
    # This is where the main program runs
    Mouse = MouseControl()
    print("Imported Mouse Control")
    Gyro = ReadGyro(1, 1)
    print("Imported Gyro")

    Gyro.check_accel()
