import unicodedata
import os
import struct
#import serial
import serial
import string
import time
import datetime
import os
from serial.tools import list_ports_windows
import time
import sys 

UARTport = [None]
UARTserialport = [None]
MCUport = [None]
MCUserialport = [None]


def check_usb_port():
	global UARTport
	global UARTserialport

	if UARTserialport[0] != None:
		UARTserialport[0] = None
	time.sleep(2)
	for port, desc, hwid in sorted(list_ports_windows.comports()):
		print("{}: {} [{}]".format(port, desc, hwid)+"\n")
		if UARTserialport[0] == None:
			if "CHERRY_UART" in hwid:
				UARTport[0] = port
				UARTserialport[0] = serial.Serial(UARTport[0], 115200,timeout=1)
				print("\nCommunication_Link = {}\n".format(UARTserialport[0]))
				print(UARTport[0])

def check_mcu_port():
	global MCUport
	global MCUserialport

	if MCUserialport[0] != None:
		MCUserialport[0] = None
	time.sleep(2)
	for port, desc, hwid in sorted(list_ports_windows.comports()):
		#print("{}: {} [{}]".format(port, desc, hwid)+"\n")
		if MCUserialport[0] == None:
			if "STM32_MCU" in hwid:
				MCUport[0] = port
				MCUserialport[0] = serial.Serial(MCUport[0], 115200,timeout=1)
				print("\nCommunication_Link = {}\n".format(MCUserialport[0]))
				print(MCUport[0])


				
if __name__ == '__main__':
	check_usb_port()
	check_mcu_port()
