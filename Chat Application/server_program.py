#!/usr/bin/python3

import socket
import threading 
import os
import subprocess

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
port = 12345


my_ip = subprocess.getoutput("ip -4 addr show enp0s3 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'")


s.bind( (my_ip,port) )

dest_ip = input("\n\tEnter IP address of the system to chat : ")


os.system("clear")

print("\n\t\tWelcome to P2P Chatting service")

print(f"You are now on line with {dest_ip}")


def send():
    while True:
        msg=input("\n\t\t\t\t >>>")

        if msg !=  " " :
            fmsg=msg.encode()
            s.sendto(fmsg,(dest_ip,port))
            if fmsg.decode() == "exit":
                s.sendto("The user on the other end is now offline,type exit to exit as well or wait for the user to show up....".encode(),(dest_ip,port))
                os._exit(1)


def recv():
    while True:
    
        msg = s.recvfrom(1024)
        recip=msg[1][0]
        #if msg[0].decode() == "exit":
         #   os._exit(1)
        
        print('\nReceived from '+ recip +" : " + msg[0].decode() + "\n\t\t\t\t\t\t\t" ,end="")
  
    



t1 = threading.Thread(target=send)
t2 = threading.Thread(target=recv)

t1.start()
t2.start()