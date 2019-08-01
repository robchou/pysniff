#/usr/bin/env python

#
# Simplest Form Of Packet sniffer in python
# Works On Linux Platform 
 
#import module
import os
import socket

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip
 
# create an INET, raw socket
# *nix
if(os.name == "posix"):
   s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
# Windows
else:
   # Get local IP address
   s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_IP)
   s.bind((get_host_ip(),0))
   s.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
   s.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)
 
# receive a packet
while True:

   # print output on terminal
   print(s.recvfrom(65565))
