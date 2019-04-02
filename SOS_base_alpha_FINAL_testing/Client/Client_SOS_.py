import tkinter as tk
from tkinter import *
import socket
import sys
import subprocess

starts = Tk()
starts.minsize(300,100)
starts.geometry("600x600")


starts.title("SOS dienests")
 
def registr():
     starts.destroy()
     subprocess.call("registr.py", shell=True)

def ienakt():
     starts.destroy()
     subprocess.call("sos_calling.py", shell=True)

logo = tk.PhotoImage(file="logo.png")
w1 = tk.Label(image=logo).pack(side="top")

label = Label(starts, text="Laipni lūdzam SOS dieniesta lietotnē!",
              font="Verdana 20", bd=0)
label.place(x=0,y=0)
label.pack()

sos_1 = Button(starts, text="Jauns lietotājs", fg="red", font="Verdana 20",
                    command=registr)
sos_1.pack()


starts.quit = tk.Button(starts, text="Ienākt", fg="red", font="Verdana 20",
                    command=ienakt)
starts.quit.pack(side="top")

 
mainloop()
 

