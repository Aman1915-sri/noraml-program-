'''import serial

ser=serial.Serial('',115200)



import serial  
         # import the module
ComPort = serial.Serial('dev/ttyUSB0') # open COM24
ComPort.baudrate = 115200 # set Baud rate to 9600
ComPort.bytesize = 8    # Number of data bits = 8
ComPort.parity   = 'N'  # No parity
ComPort.stopbits = 1    # Number of Stop bits = 1
# Write character 'A' to serial port
data = bytearray(b'A')
No = ComPort.write(data)
Serial.print("Hello World")

ComPort.close()  

import serial
ser = serial.Serial('sudo/dev/ttyUSB0')
timeout=1  # open serial port
print(ser.name)         # check which port was really used
ser.write(b'hello')     # write a string
ser.close() 

import serial

port = serial.Serial("dev/ttyUSB0", baudrate=115200, timeout=3.0)

while True:
    port.write("\r\nSay something:")
    rcv = port.read(10)
    port.write("\r\nYou sent:" + repr(rcv))
    
from machine import Pin

# create an I/O pin in output mode
p = Pin('X1', Pin.OUT)

# toggle the pin
p.high()
p.low()


import serial
import time


global ComPort
ComPort = [None]  



def check_port():
    
    if ComPort[0] != None:
        ComPort[0] = None

    print(ComPort)

    ComPort[0]= serial.Serial('/dev/ttyUSB0', baudrate=115200, bytesize=8, stopbits=1, timeout=500)
    print('s')
    ComPort.readline(b'IMP TEST ALL',encode())
    time.sleep(3)
    print(ComPort)
    ser.close()
    #ComPort[0].write("IMP TEST ALL\n".encode())
    #time.sleep(3)
    #ComPort[0].open()
    #values = bytearray(b'IMP TEST ALL')
    #ComPort.write(values)

    #data=bytearray(b'connection')
    #print(data)
    
    #print(ComPort[0].read(ComPort[0]))
    #print(ComPort[0].output)
    #data = bytearray(b'[10,20,30,40,50]')
    #print(data)
    #No = ComPort.write(data)
    
    
    


if __name__ == '__main__':
    check_port()
'''
import serial
import time
import mysql.connector


MCUserialport = ""

def port_check():
    global MCUserialport
    
    #MCUserialport= serial.Serial('/dev/ttyUSB0', baudrate=115200, bytesize=8, stopbits=1, timeout=500)
    MCUserialport= serial.Serial('/dev/ttyUSB0', baudrate=115200, timeout=500)
    print('port open ')






    
    '''
    MCUserialport.write("\n")
    time.sleep(0.1)
    read_prompt = MCUserialport.read(MCUserialport.inWaiting())
    print(read_prompt)'''
    out=MCUserialport.write("IMP TEST ALL\r\r")
    print('\nIMP TEST ALL\n')
    time.sleep(10)
    #print("out",out.readline())
    while True:

        read_data = MCUserialport.readline()
        print(read_data)
        #time.sleep(10)
        #print(type(read_data))
        #MCUserialport.write("\r\r\n")
        if 'VAD_CAM_2V8' in read_data:
            print("IMpedence test done")
            break






    






    MCUserialport.write("VOLT TEST ALL\r")
    print('\nVOLT TEST ALL\n')
    time.sleep(10)
    vol_data = []
    while True:

        read_data = MCUserialport.readline()
        print(read_data)
        read_dat=vol_data.append(read_data)
        print(vol_data)
        read_data= ''.join(vol_data)

        #if any("DONE!" in s for s in vol_data):
        if read_data.count("Measured") == 4:
            print("voltage check",vol_data )
            print("VOLT test done")
            break

    print(vol_data)






        


    
    MCUserialport.write("BUZZER ON\r")
    print('\nBUZZER ON\n')
    print ("done")
    time.sleep(1)

    

 
        




    MCUserialport.write("CAM_AVDD_2P8_EN\r")
    print('\nCAM_AVDD_2P8_EN\n')
    print("done")
    time.sleep(1)

    #while True:

    read_data = MCUserialport.readline()
    print(read_data)
        





    MCUserialport.write("CAM_AVDD_2P8_DI\r")
    print('\nCAM_AVDD_2P8_DI\n')
    print("done")
    time.sleep(1)

    #while True:

    read_data = MCUserialport.readline()
    print(read_data)
        






    MCUserialport.write("LED_R_EN / LED_R_DI\r")
    print('\nLED_R_EN / LED_R_DI\n')
    print("done")
    time.sleep(1)

    #while True:

    read_data = MCUserialport.readline()
    print(read_data)
        



def data_base():
    mydb=mysql.connector.connect(host='localhost',user='root',password='123',database='MUNA')
    cur=mydb.cursor()

    s="INSERT INTO  IMPEDENCE(TP03,TP06 ,TP05,TP04 ) values(%s,%s,%s,%s)"
    b=(VDD_CAM_1V2,VDD_CAM_1V8,VREG_BOB_3P3_3P5,VDD_CAM_2V8)
    cur.execute(s,b)
    mydb.commit()



    



if __name__ == '__main__':
    port_check()
    data_base()
