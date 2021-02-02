import socket
HOST = ""
PORT = 8080
def check(ip):
   HOST=ip
   c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

   try :
      connected=c.connect((HOST,PORT))
      print(connected)	  
      option='l'
      #print("client disconnected")
      c.send(option.encode('ascii'))
      return 1
      
   except:
      return 0
      print("server not live")

   c.close()