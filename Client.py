import serial
import socket
import threading
import time

soc_msg=""
ser_msg=""

def InitSerial():
    print "Serial is initialling...."
    dev0="/dev/ttyUSB0"
    dev1="/dev/ttyUSB1"
baud = 9600
    while True:
        try:
            ser=serial.Serial(dev0,baud)
        except:
            try:
                ser=serial.Serial(dev1,baud)
            except:
                time.sleep(1)
                print "Serial inite error!"
                continue
        break
    print "SerialInit Success!"
    return ser
def InitSocket():
    print "Socket is initialling...."
    host = '192.168.1.20'
    port = 1235
    while True:
        try:
            soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
        except socket.error:
            soc=None
            continue
        try:
            soc.connect((host,port))
        except socket.error:
            soc.close()
            soc=None
            continue
        break
    print "SocketInit Success!"
    return soc

def readSocket():
    global soc_msg
    soc_msg = ""
    while True:
        try:
            soc_msg=soc.recv(1024)
        except socket.error:
            soc.close()
            print "readSocket error!\n"
            return 0
def readSerial():
    global ser_msg
    ser_msg = ""
    while True:
        ser.flushInput()
        try:
            ser_msg = ser.readline()
        except serial.SerialException:
            soc.send("serial error\n")
            print "readSerial error!\n"
            return 0
def writeSocket():
    global ser_msg
    while True:
        if ReadSoc.isAlive()==False:
            soc.close()
            print "writeSocket error!\n"
            return 0
        if len(ser_msg)!=0:
            if ser_msg[-1]=='\n':
                print ser_msg
                try:
                    soc.send(ser_msg)
                    ser_msg = ""
                except:
                    soc.close()
                    print "writeSocket error!\n"
                    return 0
def writeSerial():
    global soc_msg
    while True:
        if ReadSer.isAlive()==False:
            print "writeSerial error!\n"
            return 0
        if len(soc_msg)!=0:
            if soc_msg[-1]=='\n':
                print soc_msg
                try:
                    ser.write(soc_msg)
                    soc_msg = ""
                except serial.SerialException:
                    soc.send("serial error!\n")
                    print "writeSerial error!\n"
                    return 0
if __name__ == '__main__':
        ser = InitSerial()
        WriteSer = threading.Thread(target = writeSerial)
        ReadSer = threading.Thread(target = readSerial)  
        ReadSer.start()
        WriteSer.start()
        soc = InitSocket()
        ReadSoc = threading.Thread(target = readSocket)   
        WriteSoc = threading.Thread(target = writeSocket)    
        ReadSoc.start()
        WriteSoc.start()
        
        while True:
            if ReadSoc.isAlive()==False and WriteSoc.isAlive()==False:
                soc = InitSocket()
                ReadSoc = threading.Thread(target = readSocket)   
                WriteSoc = threading.Thread(target = writeSocket)    
                ReadSoc.start()
                WriteSoc.start()
            if WriteSer.isAlive()==False and WriteSer.isAlive()==False:
                ser = InitSerial()
                WriteSer = threading.Thread(target = writeSerial)
                ReadSer = threading.Thread(target = readSerial)  
                ReadSer.start()
                WriteSer.start()
                
                
