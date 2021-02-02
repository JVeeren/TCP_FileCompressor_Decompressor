import socket
import sys
#from huffman import HuffmanCoding
import huffman as h
import os
import threading
import re
import time
class ClientThread(threading.Thread):
   def __init__(self,clientAddress,clientsocket):
      threading.Thread.__init__(self)
      self.csocket = clientsocket
      #print ("New connection added: ", addr)
   def run(self):
      print ("Connection from : ", addr)
      #while True:
      dol=conn.recv(1)
      option=dol.decode('ascii')
      print(option)
      if option == 'c':
         #cmd="mkdir "+name
         #os.system(cmd)
         fname=conn.recv(128)
         fname1=fname.decode('ascii')
         fname2=os.path.split(fname1)[1]
         fname3,fname3_ext=os.path.splitext(fname2)
         fname4,fname4_ext=os.path.splitext(fname1)
         print(fname3)
         print(fname4)
         x=re.split("/",fname4)
         print(x[2])
         name=x[2]
         cmd="mkdir "+name
         os.system(cmd)
         fname10=name+'/'+fname3
         with open(fname10+'_recieved.txt','wb') as f1:
            data1=conn.recv(8192)
            #print(data)
            f1.write(data1)           
            f1.close()
         #path=fname3+'_recieved.txt'
         time.sleep(0.1)
         path = "/home/veere/Desktop/SUBMISSION/server/"+fname10+'_recieved.txt'
         m = h.HuffmanCoding(path)
         m.compress()
    
         with open(fname10+'_recieved.bin','rb') as f2:
            data2=f2.read()
            #print(data2)
            conn.send(data2)
            f2.close()
         with open(fname10+'_recieved.json','rb') as f3:
            data3=f3.read()
            #print(data3)
            conn.send(data3)            
            f3.close() 
      if option == 'd':
         fname=conn.recv(128)
         fname6=fname.decode('ascii')
         fname7=os.path.split(fname6)[1]
         fname8,fname8_ext=os.path.splitext(fname7)
         fname9,fname9_ext=os.path.splitext(fname6)
         x1=re.split("/",fname9)
         print(x1[2])
         name1=x1[2]
         fname11=name1+'/'+fname8         

         with open(fname11+'_recieved.bin','wb') as f4:
            data4=conn.recv(8192)
            #print(data4)
            f4.write(data4)
            f4.close() 
         with open(fname11+'_recieved.json','wb') as f5:
            data5=conn.recv(8192)
            #print(data)
            f5.write(data5)
            f5.close()          
         time.sleep(0.1)
         path = "/home/veere/Desktop/SUBMISSION/server/"+fname11+'_recieved.bin'
         #out_path = "/home/veere/Downloads/project/recieved_sampled.bin"
         n = h.HuffmanCoding1(path)
         #output_path = h.compress()
         k=n.decompress() 
    
         with open(k,'rb') as f6:
            data6=f6.read()
            #print(data1)
            conn.send(data6)
            f6.close()
      if option == 'x':
         print("Client at ", addr , " disconnected...")
      if option == 'l':
         print("check from client")
            

HOST = ""
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
   server.listen(1)
   conn,addr = server.accept()
   newthread = ClientThread(addr, conn)
   newthread.start() 

else :
   conn.close()
   server.close()   
