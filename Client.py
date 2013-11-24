import serial
import socket
import threading

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
            continue
        try:
            soc.connect((host,port))
        except socket.error:
            continue
        except socket.timeout:
            continue
        break
    return soc
def SockettoSerial():
    soc = InitSocket()
    ser = InitSerial()
    while True:
        soc = InitSocket()
        soc_msg = soc.recv(1024)
        if len(soc_msg)!=0:
            if soc_msg[-1]=='\n':
                print soc_msg
                while True:
                    try:
                        ser.write(soc_msg)
                    except:
                        continue
                    break
def SerialtoScoket():
    ser=InitSerial()
    while True:
        ser.flushInput()
        ser_msg = ser.readline()
        if len(ser_msg)!=0:
            print ser_msg
            soc=InitSocket()
            while True:
                try:
                    soc.send(ser_msg)
                except:
                    continue
                break
            soc.close()
                      
if __name__ == '__main__':
    thread1=threading.Thread(target=SockettoSerial)
    thread2=threading.Thread(target=SerialtoScoket)
    thread1.start()
    thread2.start()