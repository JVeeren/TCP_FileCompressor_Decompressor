from tkinter import *
import testclient as cl
import testdclient as dl
import testexit as tl
import testcheckserver as ll
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import os 
import time as timer
import re
import threading
from datetime import datetime


window=Tk()
window.geometry("500x500")
window.title=("WINDOW")



txt=""
txtd=""
txt1=StringVar()
txt2=""
txtip=""
txtch=""
checkvar=999
y=0
z=0
w=0
v=0
jas=0

def file_size(fname):
   import os
   statinfo = os.stat(fname)
   return statinfo.st_size


def string_fn(): #Compression to get string of label
   global y
   y=1
   cl.client_fn(txt,txtip)
   messagebox.showinfo(title ='status',message ="file compressed")
def showinfo():
   if z == 0 :
      label10=ttk.Label(window, text ="file info")
      label10.place(x=10,y=380)
      label11 = ttk.Label(window, text ="no file selected")
      label11.place(x=10,y=400)
   elif z > 0 and y == 0 :
      label12=ttk.Label(window,text="file info")
      label12.place(x=10,y=380)
      size1=file_size(txt)
      msg1= "selected text filesize : {}            "
      label13=ttk.Label(window,text = msg1.format(size1))
      label13.place(x=10,y=400)
      msg4= "send the file for compression          "
      label17=ttk.Label(window,text = msg4)
      label17.place(x=10,y=420)        
   else : 	
      label15=ttk.Label(window,text="file info")
      label15.place(x=10,y=380)
      size1=file_size(txt)
      msg1= "selected text filesize : {}    "
      label16=ttk.Label(window,text = msg1.format(size1))
      label16.place(x=10,y=400)  
      txt5,txt5_ext=os.path.splitext(txt)
      txt6=txt5+".bin"
      size2=file_size(txt6)
      msg2= "compressed  text file size is  : {}    "
      label17=ttk.Label(window,text = msg2.format(size2))
      label17.place(x=10,y=420)

def showinfo1():
   if  v == 0 :
      label18=ttk.Label(window, text ="file info")
      label18.place(x=260,y=380)
      label19 = ttk.Label(window, text ="no file selected")
      label19.place(x=260,y=400)
   elif v > 0 and w == 0 :
      label20=ttk.Label(window,text="file info")
      label20.place(x=260,y=380)
      size3=file_size(txtd)
      msg3= "selected bin filesize : {}    "
      label21=ttk.Label(window,text = msg3.format(size3))
      label21.place(x=260,y=400)
      msg4= "send the file for decompression      "
      label17=ttk.Label(window,text = msg4)
      label17.place(x=260,y=420)   
   else : 	
      label22=ttk.Label(window,text="file info")
      label22.place(x=260,y=380)
      size4=file_size(txtd)
      msg3= "selected bin  filesize : {}"
      label23=ttk.Label(window,text = msg3.format(size4))
      label23.place(x=260,y=400)  
      txt7,txt7_ext=os.path.splitext(txtd)
      txt8=txt7+".txt"
      size5=file_size(txt8)
      msg4= "decompresed text file size is: {}    "
      label17=ttk.Label(window,text = msg4.format(size5))
      label17.place(x=260,y=420)      
   


def string_fn1():
   global w
   w=1
   dl.client_fn1(txtd,txtip)
   messagebox.showinfo(title ='status',message ="file decompressed")

def callback():
    if messagebox.askyesno('Verify', 'Really quit?'):
       if y > 0 or w > 0 :
          try:
             tl.exitdc(txtip)
             print("client disconnected")
             exit()
          except:
             exit()
       else :
          exit()
    else:
        messagebox.showinfo('No', 'Quit has been cancelled')


def browse():
    button = ttk.Button(window, text = "Browse A File",command = fileDialog)
    button.place(x=80,y=180)
    
def fileDialog():
    
    filename = filedialog.askopenfilename(initialdir="/home/jasho007/Desktop/SUBMISSION/client/", title="Select A File", filetypes=(("txt files", "*.txt"),("all files", "*.*")))

    if not filename:
       if messagebox.showerror('try again','no file selected'):
          browse()  
    else:
       if jas >0:
          global y
          y=0
          label = ttk.Label(window, text ="file is selected")
          label.place(x=100,y=300)
          global txt
          txt=filename
          print(txt)
          #label.configure(text = filename)
          btn6=Button(window,text="OK",command=string_fn).place(x=80,y=210)
          global z
          z+=1
       else:
          messagebox.showerror('ip-entry','please enter ip')
 
def browse1():
    button = ttk.Button(window, text = "Browse A File",command = fileDialog1)
    button.place(x=300,y=180)

def fileDialog1():
 
    filename = filedialog.askopenfilename(initialdir="/home/jasho007/Desktop/SUBMISSION/client/", title="Select A File", filetypes=(("bin files", "*.bin"),("all files", "*.*")))
    
    if not filename:
       if messagebox.showerror('try again','no file selected'):
          browse1()
    else:
       if jas > 0:
          global w
          w=0	
          label5=ttk.Label(window, text ="file is selected")
          label5.place(x=100,y=300)        
          global txtd
          txtd=filename
          print(txtd)
          label5.configure(text = filename)
          btn7=Button(window,text="OK",command=string_fn1).place(x=300,y=210)
          messagebox.showinfo(title ='file selection',message ="Table file selected automatically with same name")
          global v
          v+=1
       else:
          messagebox.showerror('ip-entry','please enter ip')

def exit1():
   global y
   global w
   if y > 0 or w > 0 :
      callback()
   else :
   	  callback()

def iptake():
   
   global txtip
   global txt1
   global jas
   txtip=txt1.get()
   print(txtip)
   jas+=1


def ipcheck():
   global txtch
   global txt1
   global checkvar
   txtch=txt1.get()   	
   print(txtch)
   if  len(txtch) >=9 and len(txtch) <= 15:
      x2=txtch.split(".")
      if len(x2) == 4:
         if len(x2[0]) > 0 and len(x2[1]) > 0 and len(x2[2]) > 0 and len(x2[3]) > 0 and len(x2[0]) < 4 and len(x2[1]) < 4  and len(x2[2]) < 4 and len(x2[3]) < 4 :
            if  x2[0].isdigit() and x2[1].isdigit() and x2[2].isdigit() and x2[3].isdigit():
               #progressbar =ttk.progressbar=ttk.Progressbar(window,orient = HORIZONTAL,length = 50)
               #progressbar.place(x=400,y=60)
               #progressbar.config(mode ='determinate',maximum = 10.0,value = 0.0)
               #progressbar.start()
               start_submit_thread(None)
               timer.sleep(0.1)
               if  checkvar == 1 :
                  iptake()
                  #progressbar.config(mode ='determinate',maximum = 10.0,value = 10.0)
                  messagebox.showinfo('connection status','server online')
               else:
                  #progressbar.stop()
                  if messagebox.showerror('connection status','server offline'):
                      print("server offline")
            else:
               if messagebox.showerror('try again','invalid ip'):
                  print("invalid ip ")                    
         else:
            if messagebox.showerror('try again','invalid ip'):
               print("invalid ip ")
      else:
         if messagebox.showerror('try again','invalid ip'):
            print("invalid ip ")
   else:
      if messagebox.showerror('try again','invalid ip'):
         print("invalid ip")

def submit():
   global checkvar
   checkvar=ll.check(txtch)
   # put your stuff here


def start_submit_thread(event):
   global submit_thread
   submit_thread = threading.Thread(target=submit)
   submit_thread.daemon = True
   progressbar.start()
   submit_thread.start()
   window.after(1, check_submit_thread)

def check_submit_thread():
    if submit_thread.is_alive():
        window.after(1, check_submit_thread)
    else:
        progressbar.stop()

C=Canvas(window,bg="sky blue",height=500,width=500)
C.pack()


label1=Label(window,text="Compression Service",width=20,bg="green",fg="yellow",font=("arial",20,"bold"))
label1.place(x=90,y=0)
progressbar =ttk.progressbar=ttk.Progressbar(window,orient = HORIZONTAL,length = 50)
progressbar.place(x=400,y=60)

label2=Label(window,text="Options",width=10,bg="green",fg="white")
label2.place(x=10,y=100)
btn1=Button(window,text="Compress",command=browse).place(x=80,y=150)
btn2=Button(window,text="Decompress",command=browse1).place(x=300,y=150)           #command=self_fn1
btn3=Button(window,text="Exit",command=exit1).place(x=440,y=10)
label3=Label(window,text="IP ADDRESS",width=10,bg="green",fg="white").place(x=20,y=60)
lb=Entry(window,textvariable=txt1).place(x=120,y=60)
btn8=Button(window,text="OK",command=ipcheck).place(x=300,y=55)
bth9=Button(window,text="show compressed",command=showinfo).place(x=80,y=240)
bth10=Button(window,text="show decompressed",command=showinfo1).place(x=300,y=240)
mainloop()
 
 
