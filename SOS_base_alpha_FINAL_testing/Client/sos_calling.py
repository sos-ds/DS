import tkinter as tk
from tkinter import *
import socket
import sys
import sqlite3
import subprocess


s = socket.socket()
s.connect(("localhost",9999))
 
master = Tk()
master.minsize(300,100)
master.geometry("600x600")

master.title("SOS dienests 112")

 
def callback1():
     f = open ("file_sūtīt_110.txt", "rb")
     l = f.read(1024)
     while (l):
        s.send(l)
        l = f.read(1024)

def callback2():
     f = open ("file_sūtīt_112.txt", "rb")
     l = f.read(1024)
     while (l):
        s.send(l)
        l = f.read(1024)

def callback3():
     f = open ("file_sūtīt_113.txt", "rb")
     l = f.read(1024)
     while (l):
        s.send(l)
        l = f.read(1024)
 
 
photo1=PhotoImage(file="pol1.png")
sos = Button(master,image=photo1, text="Latvijas valsts policija - 110                                         ",
             command=callback1, height=150, width=450, compound=LEFT)
sos.pack()


photo2=PhotoImage(file="glab1.png")
sos1 = Button(master,image=photo2, text="Valsts ugunsdzēsības un glābšanas dienests  - 112   ",
              command=callback2, height=150, width=450, compound=LEFT)
sos1.pack()


photo3=PhotoImage(file="med1.png")
sos3 = Button(master,image=photo3, text="Neatliekamās medicīniskās palīdzības dienests - 113",
              command=callback3, height=150, width=450, compound=LEFT)
sos3.pack()


master.quit = tk.Button(master, text="AIZVĒRT", fg="red", font="Verdana 15",
                    command=sos.master.destroy)
master.quit.pack(side="top")


def support():
   subprocess.call("support.py", shell=True)

supp = Button(master, text="Atstāt atsauksmi", command=support,
               font="Verdana 15")
supp.pack()



 
mainloop()
 
s.close()
