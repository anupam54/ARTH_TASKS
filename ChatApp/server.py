import socket
import os
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = "192.168.43.18"
port = 1234

s.bind((ip, port))

print("\t\t\t**********TOM**********")

connection_establishment = s.recvfrom(1024)
client_ip = connection_establishment[1][0]
client_port = connection_establishment[1][1]
print("Jerry from IP "+client_ip +" "+ connection_establishment[0].decode())

def recv():
    while True:
        data1 = s.recvfrom(1024)
        print("\t\t\t@JERRY: ", data1[0].decode())

def send():
    while True:
        data2 = input()
        if(data2 == "exit"):
            os._exit(1)
        else:
            s.sendto(data2.encode(), (client_ip, client_port))
			
t1 = threading.Thread(target=recv)
t2 = threading.Thread(target=send)
t1.start()
t2.start()
