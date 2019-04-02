import tkinter as tk
from tkinter import *
import socket
import sys
import sqlite3
import subprocess

root = Tk()
root.geometry('500x500')
root.title("SOS reģistrācija")

Fullname=StringVar()
Adrese=StringVar()
Telefon=StringVar()
var = IntVar()
c=StringVar()
var1= IntVar()

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
  file.write("Policijas dienesta izsaukums" + "\n")
  file.close()

  file = open("file_sūtīt_112.txt", "w", encoding="utf-8")
  file.write(Fullname_info)
  file.write("\n")
  file.write(Adrese_info)
  file.write("\n")
  file.write(Telefon_info)
  file.write("\n")
  file.write("Valsts ugunsdzesibas un glabsanas dienesta izsaukums" + "\n")
  file.close()

  file = open("file_sūtīt_113.txt", "w", encoding="utf-8")
  file.write(Fullname_info)
  file.write("\n")
  file.write(Adrese_info)
  file.write("\n")
  file.write(Telefon_info)
  file.write("\n")
  file.write("Neatliekamas mediciniskas palidzibas dienesta izsaukums" + "\n")
  file.close()
  print(" User ", Fullname_info, " has been registered successfully")

  
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
   


def registr_done():
   root.destroy()
   subprocess.call("sos_calling.py", shell=True)
   
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

label_4 = Label(root, text="Pilsēta", width=20, font=("bold", 10))
label_4.place(x=70,y=330)

list1 = ['Rīga','Liepāja','Daugavpils','Ventspils','Jūrmala','cita'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=18)
c.set('Izvēlies savu pilsētu') 
droplist.place(x=240,y=330)

button = Button(root, text='Registrēties',width=20,bg='brown',fg='white',
           command=lambda:[database(),save_info(),
                     registr_done()] ).place(x=180,y=400)

#root.quit = tk.Button(root, text="Ienākt", width=20,bg='brown',fg='white',
#                    command=root.destroy).place(x=180,y=430)
#root.quit.pack(side="bottom")

root.mainloop()
