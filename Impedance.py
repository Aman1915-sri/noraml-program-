import unicodedata
import serial
import os
import struct
import string
import time
import datetime
import ctypes
import sys 
import yaml
from array import array
import easygui
from easygui import buttonbox
from Check_port import *

 
imp_split = [0]
DUT_5V_IMP_IN = ['X']
AREF = ['X']
VCC_3V3_1 = ['X']
VCC_3V3_WI_FI = ['X']
VCC_3V3 = ['X']
P1_IMP = ['X']
P2_IMP = ['X']
P3_IMP = ['X']

''' 
HEADER 
TEST_NAME         : Impedance
TEST_RUN_SEQUENCE : 1
TEST_PRIORITY     : HIGH
TEST_RUN_EFFORT   : AUTOMATE
TEST_TAG          : None
TEST_RETURN       : STATUS
'''


with open ("..//Configurations//config.yaml","r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)


DUT_5V_IMP_IN_I_MIN = config["Impedance"]["DUT_5V_IMP_IN_I_MIN"]
AREF_I_MIN = config["Impedance"]["AREF_I_MIN"]
VCC_3V3_1_I_MIN = config["Impedance"]["VCC_3V3_1_I_MIN"]
VCC_3V3_WI_FI_I_MIN = config["Impedance"]["VCC_3V3_WI_FI_I_MIN"]
VCC_3V3_I_MIN = config["Impedance"]["VCC_3V3_I_MIN"]
P1_IMP_I_MIN = config["Impedance"]["P1_IMP_I_MIN"]
P2_IMP_I_MIN = config["Impedance"]["P2_IMP_I_MIN"]
P3_IMP_I_MIN = config["Impedance"]["P3_IMP_I_MIN"]



DUT_5V_IMP_IN_I_MAX = config["Impedance"]["DUT_5V_IMP_IN_I_MAX"]
AREF_I_MAX = config["Impedance"]["AREF_I_MAX"]
VCC_3V3_1_I_MAX = config["Impedance"]["VCC_3V3_1_I_MAX"]
VCC_3V3_WI_FI_I_MAX = config["Impedance"]["VCC_3V3_WI_FI_I_MAX"]
VCC_3V3_I_MAX = config["Impedance"]["VCC_3V3_I_MAX"]
P1_IMP_I_MAX = config["Impedance"]["P1_IMP_I_MAX"]
P2_IMP_I_MAX = config["Impedance"]["P2_IMP_I_MAX"]
P3_IMP_I_MAX = config["Impedance"]["P3_IMP_I_MAX"]


impedance_status_f = [0]
impedance_status = [0]

def Impedance():

    test_return = ""
    test_log = []
    test_output = ""

    try:

        print('{:*^65s}'.format(""))
        print('{: ^65s}'.format(""))
        print('{:^65s}'.format("Impedance_started"))
        print('{: ^65s}'.format(""))
        print('{:*^65s}'.format(""))


        ct_disable()
        time.sleep(0.2)
        power_off()
        #easygui.msgbox("Please check all JLink connection should be removed ",title="IMPEDANCE")
        time.sleep(3)
        
        MCUserialport[0].write(str.encode("\r"))

        time.sleep(1)
        MCUserialport[0].write(str.encode("IMP TEST ALL\r\n"))

        repeater = 0
        read_buffer = ""

        while True:
            

            read_data = ""
            read_data = MCUserialport[0].readline()
            read_data = read_data.decode("utf-8")
            repeater+=1
            print(repeater)
            #print(read_data)

            print("\nDATA == {}\n".format(read_buffer))

            if "DONE!" in read_data:

                #print(read_data)
                
                imp_split[0] = str(str(str(read_data).split("IMP_TEST_START@")[1]).split("DONE!")[0]).split(",")
                
                for i in range(0,7):
                    print(imp_split[0][i])
                
                if(float(imp_split[0][0]) >= float(DUT_5V_IMP_IN_I_MIN) and float(imp_split[0][0]) <= float(DUT_5V_IMP_IN_I_MAX) ):

                    print("\nDUT_5V_IMP_IN = PASS ( "+str(float(DUT_5V_IMP_IN_I_MIN))+" < "+str(imp_split[0][0])+" > "+str(float(DUT_5V_IMP_IN_I_MAX))+" )")
                    DUT_5V_IMP_IN[0] = "PASS" 
                else:
                    print("\nDUT_5V_IMP_IN = FAIL ( "+str(float(DUT_5V_IMP_IN_I_MIN))+" < "+str(imp_split[0][0])+" > "+str(float(DUT_5V_IMP_IN_I_MAX))+" )")
                    DUT_5V_IMP_IN[0] = "FAIL"


                if(float(imp_split[0][1]) >= float(AREF_I_MIN) and float(imp_split[0][1]) <= float(AREF_I_MAX) ):
                    print("\nAREF = PASS         ( "+str(float(AREF_I_MIN))+" < "+str(imp_split[0][1])+" > "+str(float(AREF_I_MAX))+" )")
                    AREF[0] ="PASS" 
                else:
                    print("\nAREF = FAIL         ( "+str(float(AREF_I_MIN))+" < "+str(imp_split[0][1])+" > "+str(float(AREF_I_MAX))+" )") 
                    AREF[0] ="FAIL"   


                if(float(imp_split[0][2]) >= float(VCC_3V3_1_I_MIN) and float(imp_split[0][2]) <= float(VCC_3V3_1_I_MAX)):
                    print("\nVREF = PASS            ( "+str(float(VCC_3V3_1_I_MIN))+" < "+str(imp_split[0][2])+" > "+str(float(VCC_3V3_1_I_MAX))+" )")
                    VCC_3V3_1[0] ="PASS" 
                else:
                    print("\nVREF = FAIL            ( "+str(float(VCC_3V3_1_I_MIN))+" < "+str(imp_split[0][2])+" > "+str(float(VCC_3V3_1_I_MAX))+" )")
                    VCC_3V3_1[0] ="FAIL"     

                if(float(imp_split[0][3]) >= float(VCC_3V3_WI_FI_I_MIN) and float(imp_split[0][3]) <= float(VCC_3V3_WI_FI_I_MAX) ):

                    print("\nVCC_3V3_WI_FI = PASS        ( "+str(float(VCC_3V3_WI_FI_I_MIN))+" < "+str(imp_split[0][3])+" > "+str(float(VCC_3V3_WI_FI_I_MAX))+" )")
                    VCC_3V3_WI_FI[0] = "PASS"
                else:
                    print("\nVCC_3V3_WI_FI = FAIL        ( "+str(float(VCC_3V3_WI_FI_I_MIN))+" < "+str(imp_split[0][3])+" > "+str(float(VCC_3V3_WI_FI_I_MAX))+" )")
                    VCC_3V3_WI_FI[0] = "FAIL"


                if(float(imp_split[0][4]) >= float(VCC_3V3_I_MIN) and float(imp_split[0][4]) <= float(VCC_3V3_I_MAX) ):
                    print("\nVCC_3V3 = PASS        ( "+str(float(VCC_3V3_I_MIN))+" < "+str(imp_split[0][4])+" > "+str(float(VCC_3V3_I_MAX))+" )")
                    VCC_3V3[0] ="PASS" 
                else:
                    print("\nVCC_3V3 = FAIL        ( "+str(float(VCC_3V3_I_MIN))+" < "+str(imp_split[0][4])+" > "+str(float(VCC_3V3_I_MAX))+" )")    
                    VCC_3V3[0] ="FAIL"   


                if(float(imp_split[0][5]) >= float(P1_IMP_I_MIN) and float(imp_split[0][5]) <= float(P1_IMP_I_MAX)):
                    print("\nP1_IMP = PASS        ( "+str(float(P1_IMP_I_MIN))+" < "+str(imp_split[0][5])+" > "+str(float(P1_IMP_I_MAX))+" )")
                    P1_IMP[0] ="PASS" 
                else:
                    print("\nP1_IMP = FAIL        ( "+str(float(P1_IMP_I_MIN))+" < "+str(imp_split[0][5])+" > "+str(float(P1_IMP_I_MAX))+" )")
                    P1_IMP[0] ="FAIL"
                        
                if(float(imp_split[0][6]) >= float(P2_IMP_I_MIN) and float(imp_split[0][6]) <= float(P2_IMP_I_MAX) ):

                    print("\nP2_IMP = PASS      ( "+str(float(P2_IMP_I_MIN))+" < "+str(imp_split[0][6])+" > "+str(float(P2_IMP_I_MAX))+" )")
                    P2_IMP[0] = "PASS"
                else:
                    print("\nP2_IMP = FAIL      ( "+str(float(P2_IMP_I_MIN))+" < "+str(imp_split[0][6])+" > "+str(float(P2_IMP_I_MAX))+" )")
                    P2_IMP[0] = "FAIL"


                if(float(imp_split[0][7]) >= float(P3_IMP_I_MIN) and float(imp_split[0][7]) <= float(P3_IMP_I_MAX) ):
                    print("\nP3_IMP = PASS       ( "+str(float(P3_IMP_I_MIN))+" < "+str(imp_split[0][7])+" > "+str(float(P3_IMP_I_MAX))+" )")
                    P3_IMP[0] ="PASS" 
                else:
                    print("\nP3_IMP = FAIL       ( "+str(float(P3_IMP_I_MIN))+" < "+str(imp_split[0][7])+" > "+str(float(P3_IMP_I_MAX))+" )")    
                    P3_IMP[0] ="FAIL"   
   


                if(DUT_5V_IMP_IN[0] == "PASS" and AREF[0] == "PASS" and VCC_3V3_1[0] == "PASS" and VCC_3V3_WI_FI[0] == "PASS" and \
                    VCC_3V3[0] == "PASS" and P1_IMP[0] == "PASS" and P2_IMP[0] == "PASS" and P3_IMP[0] == "PASS"):


                    print("\nIMPEDANCE TEST PASS")
                    impedance_status_f[0]=1

                    break
                else:
                    print("\nIMPEDANCE TEST FAIL")
                    impedance_status_f[0]=0
                    #easygui.msgbox("Impedance FAIL ",title="IMPEDANCE")
                    return
                    
            
            elif "DONE!" not in read_data and repeater>10:
                print("IMPEDANCE TEST FAIL")
                impedance_status_f[0]=0

                easygui.msgbox("Impedance FAIL ",title="IMPEDANCE")
                return
                
                  
    
    except ValueError:
        easygui.msgbox("Give proper baud rate ",title="IMPEDANCE")
        print("Give proper baud rate")
        impedance_status_f[0]=0

    except serial.SerialException as e:
        easygui.msgbox("Console removed from the system ",title="IMPEDANCE")
        print("Console removed from the system")
        impedance_status_f[0]=0
             
    except Exception as error:
        ex = print('Error is : ' + repr(error))
        
        print("IMPEDANCE TEST FAIL")
        impedance_status_f[0]=0
        easygui.msgbox("Impedance FAIL ",title="IMPEDANCE")
        
    
 



def generate_report_impedance():
    global impedance_status_f
    global impedance_status

    Impedance()

    if impedance_status_f[0] == 1:
        impedance_status[0] = 'PASS'
    else:
        impedance_status[0] = 'FAIL'

if __name__ == '__main__':
    generate_report_impedance()