Gateway
=======
版本更新记录：
--------------------------
### Ver1.3:
    在服务端关闭socket之后，无法再主动重连，因而不能接收来自服务器端的信息，在本版本中，已对这个bug进行了修复
### Ver2.0
    对程序的多线程实现方式进行了更改，更改之后的程序易于理解。对客户端程序进行了异常处理，考虑的情况有在服务端
    断开socket，串口通信被停止或意外中断，或者串口，socket发送数据失败几种情形，当系统回复正常之后，程序能够继
    续正常执行。
### Ver2.1
    对客户端和服务端的程序都进行了异常处理，但服务端程序的缺陷依旧存在
### Ver3.0
    重大修改，将之前的双线程改为了四线程，从而可以达到socket的断线自动重连功能，经过仔细测试，暂时没有发现bug
    将网关做为服务端的也重新写了一下，经过仔细测试，暂时没有发现bug
