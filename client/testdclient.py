import socket
import os
import time
HOST = ""
PORT = 8080
def client_fn1(datax,ip):
   HOST=ip
   c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   connected=c.connect((HOST,PORT))
   option='d'
   filen,filen_ext=os.path.splitext(datax)
   print("client got connected")
   c.send(option.encode('ascii'))
   time.sleep(0.1)
   c.send(datax.encode('ascii'))
   
 
   with open(filen+'.bin','rb') as cf:
      data1=cf.read()
      #print(data)
      c.sendall(data1)
      cf.close()

   time.sleep(0.1)


   with open(filen+'.json','rb') as cf2:
      data3=cf2.read()
      #print(data3)
      c.sendall(data3)
      cf2.close()      

   with open(filen+'_decompressed.txt','wb') as cf1:
      data2=c.recv(8192)
      #print(data1)
      cf1.write(data2)
      cf1.close()
      
   c.close()
