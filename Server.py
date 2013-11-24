import serial
import socket
import threading

def InitSerial():
    dev0="/dev/ttyUSB0"
    dev1="/dev/ttyUSB1"
    baud = 9600
    while(True):
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
    host = "192.168.1.1"
    port = 1235
    while(True):
        try:
            soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
        except:
            continue
        try:
            soc.bind((host,port))
        except:
            continue
        soc.listen(1)
        break
    return soc
def SockettoSerial():
    while True:
        ser.flushOutput()
        client,ipaddr=soc.accept()
        print "Got a Socconnect from %s"  %str(ipaddr)
        soc_msg=client.recv(1024)
        print soc_msg
        if len(soc_msg)!=0:
            if soc_msg[-1]=='\n':
                client.close()
                print soc_msg
                ser.write(soc_msg)

def SerialtoScoket():
    while True:
        client,ipaddr=soc.accept()
        print "Got a Serconnect from %s"  %str(ipaddr)
        ser_msg = ser.readline() 
        ser.flushOutput()
        print ser_msg
        if len(ser_msg)!=0:
            client.send(ser_msg)
            print ser_msg
            client.close()

if __name__ == '__main__':
    ser=InitSerial()
    soc=InitSocket()
    thread1=threading.Thread(target=SerialtoScoket)
    thread2=threading.Thread(target=SockettoSerial)
    thread1.start()
    thread2.start()   