import socket
from random import seed
from random import randint
import functools
import time

 

x=2
y=2
z=2
my_cords=[2,2,2]

 


UDP_IP = "127.0.0.1"
UDP_PORT_my = 5006

 


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT_my))

 

while True:
  data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
  mm=data.decode();
  cords=mm.split(',')
  rec_cords=[]
  for s in cords:
    #x=s.split(':')
    
    rec_cords.append(int(s[2]))
   
  
  print(rec_cords)
  time.sleep(10)
  if functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,my_cords,rec_cords), True): 
     signal=b'5006 is near'
     print(addr)
     sock.sendto(signal,(UDP_IP,5005))
  else: 
     print(addr)
     signal=b'5006 is far'
     sock.sendto(signal,(UDP_IP,5005))
  print("received message: %s" % data)