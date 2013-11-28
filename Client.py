import serial
import socket
import threading
import time

def InitSerial():
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
                print "Serial init error!\n"
                continue
        break
    return ser
def InitSocket():
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
    return soc


    
def SockettoSerial():
    while True:
        soc_msg=None
        try:
            soc_msg=soc.recv(1024)
        except:
            print "socket disconnected!\n"
            soc.close()
            return 0
        if len(soc_msg)!=0:
            if soc_msg[-1]=='\n':
                print soc_msg
                try:
                    ser.write(soc_msg)
                except serial.SerialException:
                    soc.send("serial error!\n")
                    print "close sockettoserial"
                    return 0

def SerialtoScoket():
    while True:
        ser.flushInput()
        ser_msg = None
        try:
            ser_msg = ser.readline()
        except serial.SerialException:
            soc.send("serial error\n")
            print "close serialtosocket\n"
            return 0
        if len(ser_msg)!=0:
            print ser_msg
            try:
                soc.send(ser_msg)
            except:
                print "socket disconnected!\n"
                soc.close()
                return 0
        
if __name__ == '__main__':
    while True:
        soc=InitSocket()
        ser=InitSerial()
        socth=threading.Thread(target=SockettoSerial)
        serth=threading.Thread(target=SerialtoScoket)
        socth.start()
        serth.start()
        while True:
            if socth.isAlive()==False and serth.isAlive==False:
                break
                
    