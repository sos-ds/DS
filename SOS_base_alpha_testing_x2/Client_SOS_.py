import tkinter as tk
from tkinter import *
import socket
import sys
import sqlite3

starts = Tk()
starts.minsize(300,100)
starts.geometry("600x600")


starts.title("SOS dienests")
 
def callback():
     subprocess.call("dfd.py", shell=True)

logo = tk.PhotoImage(file="logo.png")
w1 = tk.Label(image=logo).pack(side="top")

label = Label(starts, text="Laipni lūdzam SOS dieniesta lietotnē!", font="Verdana 20", bd=0)
label.place(x=0,y=0)
label.pack()

sos_1 = Button(starts, text="Reģistrēties", fg="red", font="Verdana 20",
                    command=starts.destroy)
sos_1.pack()


starts.quit = tk.Button(starts, text="Ienākt", fg="red", font="Verdana 20",
                    command=starts.destroy)
starts.quit.pack(side="top")

 
mainloop()




def save_info():
  Fullname_info = Fullname.get()
  Adrese_info = Adrese.get()
  Telefon_info = Telefon.get()
  Telefon_info = str(Telefon_info)

 
  file = open("file_sūtīt_110.txt", "w", encoding="utf-8")
  file.write(Fullname_info)
  file.write("\n")
  file.write(Adrese_info)
  file.write("\n")
  file.write(Telefon_info)
  file.write("\n")
  file.write("Policijas dienesta izsaukums")
  file.close()

  file = open("file_sūtīt_112.txt", "w", encoding="utf-8")
  file.write(Fullname_info)
  file.write("\n")
  file.write(Adrese_info)
  file.write("\n")
  file.write(Telefon_info)
  file.write("\n")
  file.write("Valsts ugunsdzesibas un glabsanas dienesta izsaukums")
  file.close()

  file = open("file_sūtīt_113.txt", "w", encoding="utf-8")
  file.write(Fullname_info)
  file.write("\n")
  file.write(Adrese_info)
  file.write("\n")
  file.write(Telefon_info)
  file.write("\n")
  file.write("Neatliekamas mediciniskas palidzibas dienesta izsaukums")
  file.close()
  print(" User ", Fullname_info, " has been registered successfully")

root = Tk()
root.geometry('500x500')
root.title("SOS reģistrācija")

Fullname=StringVar()
Adrese=StringVar()
Telefon=StringVar()
var = IntVar()
c=StringVar()
var1= IntVar()

def database():
   name1=Fullname.get()
   email=Adrese.get()
   tel=Telefon.get()
   gender=var.get()
   country=c.get()
   prog=var1.get()
   conn = sqlite3.connect('SOS.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Klienti (Fullname TEXT,Adrese TEXT, Telefon TEXT, Gender TEXT, country TEXT)')
   cursor.execute('INSERT INTO Klienti (FullName,Adrese,Telefon,Gender,country) VALUES(?,?,?,?,?)',(name1,email,tel,gender,country,))
   conn.commit()
   

             
label_0 = Label(root, text="SOS reģistrācija",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="Vārds, Uzvārds",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Adrese",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,textvar=Adrese)
entry_2.place(x=240,y=180)

label_5 = Label(root, text="Telefona numurs",width=20,font=("bold", 10))
label_5.place(x=68,y=230)

entry_5 = Entry(root,textvar=Telefon)
entry_5.place(x=240,y=230)

label_3 = Label(root, text="Dzimums",width=20,font=("bold", 10))
label_3.place(x=70,y=280)

Radiobutton(root, text="Sieviešu",padx = 0, variable=var, value=1).place(x=235,y=280)
Radiobutton(root, text="Vīriešu",padx = 40, variable=var, value=2).place(x=290,y=280)

label_4 = Label(root, text="Pilsēta",width=20,font=("bold", 10))
label_4.place(x=70,y=330)

list1 = ['Rīga','Liepāja','Daugavpils','Ventspils','Jūrmala','cita'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=18)
c.set('Izvēlieties savu pilsētu') 
droplist.place(x=240,y=330)

Button(root, text='Registrēties',width=20,bg='brown',fg='white', command=lambda:[database(),save_info(),root.destroy()] ).place(x=180,y=400)

root.quit = tk.Button(root, text="Ienākt", width=20,bg='brown',fg='white',
                    command=root.destroy).place(x=180,y=430)
#root.quit.pack(side="bottom")




root.mainloop()



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
sos = Button(master,image=photo1, text="Latvijas valsts policija - 110                                         ", command=callback1, height=150, width=450, compound=LEFT)
sos.pack()


photo2=PhotoImage(file="glab1.png")
sos1 = Button(master,image=photo2, text="Valsts ugunsdzēsības un glābšanas dienests  - 112   ", command=callback2, height=150, width=450, compound=LEFT)
sos1.pack()


photo3=PhotoImage(file="med1.png")
sos3 = Button(master,image=photo3, text="Neatliekamās medicīniskās palīdzības dienests - 113", command=callback3, height=150, width=450, compound=LEFT)
sos3.pack()


master.quit = tk.Button(master, text="AIZVĒRT", fg="red", font="Verdana 15",
                    command=sos.master.destroy)
master.quit.pack(side="top")

 
mainloop()
 
s.close()

