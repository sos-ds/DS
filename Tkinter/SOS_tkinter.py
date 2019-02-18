import tkinter as tk
from tkinter import *

class Application(tk.Frame):
    def __init__(sos, master=None):
        super().__init__(master)

#        sos_1 = Label(sos, text="SOS dienests 112", fg="red", font="Verdana 25")
#        sos_1.pack()

        sos.master = master
        sos.pack()
        sos.create_widgets()


    def create_widgets(sos):
        sos.police = tk.Button(sos,font="Verdana 20")
        sos.police["text"] = "Valsts policija - 110"
        sos.police["command"] = sos.policija
        sos.police.pack(side="top")

        sos.fire = tk.Button(sos, font="Verdana 20")
        sos.fire["text"] = "Valsts ugunsdzēsības un glābšanas dienests  - 112"
        sos.fire["command"] = sos.glabsana
        sos.fire.pack(side="top")

        sos.ambulance = tk.Button(sos, font="Verdana 20")
        sos.ambulance["text"] = "Neatliekamās medicīniskās palīdzības dienests - 113"
        sos.ambulance["command"] = sos.medicina
        sos.ambulance.pack(side="top")
    

        

        sos.quit = tk.Button(sos, text="QUIT", fg="red", font="Verdana 20",
                              command=sos.master.destroy)
        sos.quit.pack(side="bottom")

    def policija(sos):
        print("Policijas dienesta izsaukums")

    def medicina(sos):
        print("Neatliekamās medicīniskās palīdzības dienesta izsaukums")

    def glabsana(sos):
        print("Valsts ugunsdzēsības un glābšanas dienesta izsaukums")    

root = tk.Tk()
root.title("SOS dienests 112")
app = Application(master=root)
app.mainloop()
