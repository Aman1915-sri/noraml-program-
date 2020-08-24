import serial 
import time
MCUserialport=""
def check_port():
    global MCUserialport
    MCUserialport[0] = serial.Serial("/dev/ttyUSB0", 115200,timeout=5)
    print("MCU open")

if __name__ == '__main__':
    check_port()

