import serial
import sys
import time

port = "/dev/tty.usbmodem1421"

s = serial.Serial(port, 9600, timeout=5)

data = s.readline()
print data


while data != "":
    # if data > max_num:
    #     max_num = data
    #     f.write("MAX: " + str(max_num))
    sys.stdout.write(data)
    sys.stdout.flush()
    data = s.readline()
