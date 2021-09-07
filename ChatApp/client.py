import socket
import threading
import os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("\t\t\t**********JERRY**********")

server_ip = input("Enter Tom's IP: ")
server_port = 1234

data = "trying to connect to you...";
s.sendto(data.encode(), (server_ip, server_port))

print("Your request has been sent to IP ",server_ip)

def send():
    while True:
        data2 = input()
        if(data2 == "exit"):
            os._exit(1)
        else:
            s.sendto(data2.encode(), (server_ip, server_port))

def recv():
    while True:
        data1 = s.recvfrom(1024)
        print("\t\t\t@TOM: ",data1[0].decode())

t1 = threading.Thread(target=recv)
t2 = threading.Thread(target=send)
t1.start()
t2.start()

