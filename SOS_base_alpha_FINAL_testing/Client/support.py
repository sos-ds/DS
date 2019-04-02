from tkinter import *
import tkinter as tk
import smtplib
import tkinter.messagebox

f=Tk()
f.title("SOS atbalsts")


def layout():
    global msg_label0
    msg_label0 = Label(f,text='Lūdzu, rakstiet bez garumzīmēm un mīkstinājumiem',
                       fg="red", font="Verdana 15")
    
    global msg_body1
    msg_label1=Label(f,text='Vārds, Uzvārds*', font="Verdana 15")
    msg_body1=Text(f,height=0,width=35,bd=3,font="Verdana 15", wrap='word')
    
    global msg_body2
    msg_label2=Label(f,text='Telefona numurs*', font="Verdana 15")
    msg_body2=Text(f,height=0,width=35,bd=3,font="Verdana 15",wrap='word')


    global msg_body3
    msg_label3=Label(f,text='E-pasts*', font="Verdana 15")
    msg_body3=Text(f,height=0,width=35,bd=3,font="Verdana 15",wrap='word')

    global msg_body
    msg_label=Label(f,text='Ziņojums*', font="Verdana 15")
    msg_body=Text(f,height=5,width=35,bd=3,font="Verdana 15",wrap='word')

    send=Button(f,text='Sūtīt',width=15,command=lambda:[mail(),destroy()],bd=3, fg="red",
                font="Verdana 20")
    cancel=Button(f,text='Atcelt',width=15,command=destroy,bd=3,
                  font="Verdana 20")

    msg_label0.grid(row=2, column=1, padx=5,pady=3)
    
    msg_label1.grid(row=3,column=0,padx=5,pady=3)
    msg_body1.grid(row=3,column=1,padx=5,pady=3)

    msg_label2.grid(row=4,column=0,padx=5,pady=3)
    msg_body2.grid(row=4,column=1,padx=5,pady=3)

    msg_label3.grid(row=5,column=0,padx=5,pady=3)
    msg_body3.grid(row=5,column=1,padx=5,pady=3)

    msg_label.grid(row=6,column=0,padx=5,pady=3)
    msg_body.grid(row=6,column=1,padx=5,pady=3)

    cancel.grid(row=7,column=0,padx=5,pady=3)
    send.grid(row=7,column=1,padx=5,pady=3)
    

    f.mainloop()
    
def destroy():
    f.destroy()

def mail():
        try:
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            a='sos.atbalsts@gmail.com'
            b='dspavasaris'     
            c=msg_body1.get('1.0',END)+msg_body2.get('1.0',END)+msg_body3.get('1.0',END)+msg_body.get('1.0',END)
            d='sos.atbalsts@gmail.com'
            server.login(a,b)
            server.sendmail(a,d,c)
            server.close()
        except Exception as e:
            print(e)
        
layout()
