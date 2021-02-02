import socket
HOST = ""
PORT = 8080
def exitdc(ip):
   HOST=ip
   c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   connected=c.connect((HOST,PORT))
   print(connected)
   option='x'
   #print("client disconnected")
   c.send(option.encode('ascii'))



   c.close()