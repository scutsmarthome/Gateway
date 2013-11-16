import serial
import socket
import threading
import time

global ser,soc
def InitSerial():
    dev0="/dev/ttyUSB0"
    baud = 9600
    ser=serial.Serial(dev0,baud)
    return ser
def InitSocket():
    host = '192.168.1.20'
    port = 1235
    soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    soc.connect((host,port))
    return soc
class SockettoSerial(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.thread_stop = False
    def run(self): #Overwrite run() method, put what you want the thread do here
        soc = InitSocket()
        ser = InitSerial()
        while not self.thread_stop:
            soc = InitSocket()
            soc_msg = soc.recv(1024)
            if len(soc_msg)!=0:
                if soc_msg[-1]=='\n':
                    print soc_msg
                    ser.write(soc_msg)
    def stop(self):
        self.thread_stop = True
class SerialtoScoket(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.thread_stop = False
    def run(self):
        ser=InitSerial()
        while not self.thread_stop:
            ser.flushInput()
            ser_msg = ser.readline()
            if len(ser_msg)!=0:
                print ser_msg
                soc=InitSocket()
                soc.send(ser_msg)
                soc.close()
    def stop(self):
        self.thread_stop = True
if __name__ == '__main__':
    thread1=SockettoSerial()
    thread2=SerialtoScoket()
    thread1.start()
    thread2.start()
    while True:
        time.sleep(10)
    thread1.stop()
    thread2.stop()   