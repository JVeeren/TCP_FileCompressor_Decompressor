import socket
import os
import time
HOST = ""
PORT = 8080
def client_fn(file1,ip):
   HOST=ip
   c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   connected=c.connect((HOST,PORT))
   option="c"
   filen,filen_ext=os.path.splitext(file1)
   print(filen)
   print("client got connected")
   c.send(option.encode('ascii'))
   time.sleep(0.1)
   c.send(file1.encode('ascii'))
   #c.send(b'hi server')
  
   with open(filen+'.txt','rb') as cf:
      data1=cf.read()
      #print(data1)
      c.send(data1)
      cf.close()

   with open(filen+'.bin','wb') as cf1:
      data2=c.recv(8192)
      #print(data2)
      cf1.write(data2)
      cf1.close()

   with open(filen+'.json','wb') as cf2:
      data3=c.recv(8192)
      #print(data3)
      cf2.write(data3)
      cf2.close()      

    
   c.close()