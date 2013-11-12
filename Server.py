import serial
import socket
import threading
import time

global ser,soc,client
def InitSerial():
    dev0="/dev/ttyUSB0"
    baud = 9600
    ser=serial.Serial(dev0,baud)
    return ser
def InitSocket():
    host = "192.168.1.1"
    port = 1235
    soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    soc.bind((host,port))
    soc.listen(1)
    return soc
class SockettoSerial(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.thread_stop = False
    def run(self): #Overwrite run() method, put what you want the thread do here
        while not self.thread_stop:
            ser.flushOutput()
            client,ipaddr=soc.accept()
            print "Got a connect from %s"  %str(ipaddr)
            soc_msg=client.recv(1024)
            print soc_msg
            if len(soc_msg)!=0:
                if soc_msg[-1]=='\n':
                    client.close()
                    print soc_msg
                    ser.write(soc_msg)
    def stop(self):
        self.thread_stop = True
class SerialtoScoket(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.thread_stop = False
    def run(self):
        while not self.thread_stop:
            client,ipaddr=soc.accept()
            ser_msg = ser.readline()
            print "Got a connect from %s"  %str(ipaddr)
            if len(ser_msg)!=0:  
                client.send(ser_msg)
                print ser_msg
                client.close()
    def stop(self):
        self.thread_stop = True
if __name__ == '__main__':
    ser=InitSerial()
    soc=InitSocket()
    client,ipaddr=soc.accept()
    thread1=SerialtoScoket()
    thread2=SockettoSerial()
    thread1.start()
    thread2.start()
    while True:
        time.sleep(10)
    thread1.stop()
    thread2.stop()
        
    
    
    