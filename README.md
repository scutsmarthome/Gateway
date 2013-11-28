Gateway
=======
网关程序，服务端和客户端程序都写好了。客户端程序发现的bug已经修复，但服务端程序还存在缺陷，
对于客户端（即服务器）的连接，一次只能从客户端接收信息，一次只能发送信息。
虽然使用了多线程（其实网关的客户端程序也使用了多线程），但可能对于同一个端口，
一次只能被一个线程处理，所以端口的动能在发送和接收信息两个线程之间进行循环。
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
