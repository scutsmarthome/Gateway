import serial
import socket
import threading
import time

soc_msg=""
ser_msg=""
con=None

def InitSerial():
    print "Serial is initialling......"
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
    host = "192.168.1.1"
    port = 1235
    while(True):
        try:
            soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
        except socket.error:
            continue
        try:
            soc.bind((host,port))
        except socket.error:
            continue
        print "SocketInit Success!"
        soc.listen(1)
        print "Waiting for client......"
        break
    return soc
def readSocket():
    global soc_msg,con
    soc_msg=""
    while True:
        con,ipaddr=soc.accept()
        print "Got a Socconnect from %s"  %str(ipaddr)
        while True:
            try:
                soc_msg=con.recv(1024)
            except socket.error:
                print "The %s is disconnected" %str(ipaddr)
                break
def readSerial():
    global ser_msg
    ser_msg = ""
    while True:
        ser.flushInput()
        try:
            ser_msg = ser.readline()
        except serial.SerialException:
            con.send("serial error\n")
            print "readSerial error!\n"
            return 0
def writeSocket():
    global ser_msg,con
    while True:
        if len(ser_msg)!=0:
            if ser_msg[-1]=='\n':
                print ser_msg
                try:
                    con.send(ser_msg)
                    ser_msg = ""
                except socket.error:
                    print "writeSocket error!\n" 
                    continue   
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
            if WriteSer.isAlive()==False and WriteSer.isAlive()==False:
                ser = InitSerial()
                WriteSer = threading.Thread(target = writeSerial)
                ReadSer = threading.Thread(target = readSerial)  
                ReadSer.start()
                WriteSer.start() 