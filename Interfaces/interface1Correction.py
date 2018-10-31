try:
    from tkinter import *
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

from tkcalendar import Calendar, DateEntry
import time
from datetime import datetime, date, time

def Calendrier():

    def print_sel():
        valeur = cal.selection_get()
        print("la date est",cal.selection_get())
       # label = Label(fenetre, text=cal.selection_get().strftime('%m/%d/%Y'), bg="grey")  # Label
       # label.pack(padx=30, pady=10)
        cal.destroy()

    def recupere_date():
        return cal.selection_get()


    cal = Calendar(fenetre, font="Arial 14", selectmode='day', locale='en_US',
                   cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    ttk.Button(fenetre, text="ok", command=print_sel).pack()
    Button.destroy()


#initialisation variables
global valeur
valeur=datetime.date

#initialisation de la fenêtre
fenetre=Tk()
Frame1 = Frame(fenetre, borderwidth=2)
Frame1.pack(side=RIGHT, padx=500, pady=200)

label = Label(fenetre, text="Choix compteurs", bg="grey")   #Label
label.pack(padx=30, pady=10)

#Liste déroulante compteurs
variable = StringVar(fenetre)
variable.set("Compteurs") # default value
liste = OptionMenu(fenetre, variable, "Compteurs_2004", "Compteurs_2005", "Compteurs_2006", "Compteurs_2007")
liste.pack(padx=30, pady=10)


#Création du calendrier pour choix des dates
ttk.Button(fenetre, text='Calendrier', command=Calendrier).pack(padx=40, pady=10)
ttk.Label(fenetre, textvariable=valeur).pack(padx=30, pady=10)


#######################
# Barre de menu
menubar = Menu(fenetre)

fenetre.config(menu=menubar)
menufichier = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Fichier", menu=menufichier)

compteur= menufichier.add_command(label="Compteurs")
menufichier.add_command(label="Historique")
menufichier.add_separator()
menufichier.add_command(label="Quitter")


fenetre.mainloop()

