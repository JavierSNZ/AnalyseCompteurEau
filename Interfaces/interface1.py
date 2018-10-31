import sys
try:
    from tkinter import *
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

from tkcalendar import Calendar, DateEntry
import time
from datetime import datetime, date, time

import matplotlib.pyplot as plt
import numpy as np


fenetre=Tk()

Frame1 = Frame(fenetre, borderwidth=2)
Frame1.pack(side=RIGHT, padx=500, pady=200)

#Liste déroulante compteurs

label = Label(fenetre, text="Choix compteurs", bg="grey")
label.pack(padx=30, pady=10)

variable = StringVar(fenetre)
variable.set("Compteurs") # default value

liste = OptionMenu(fenetre, variable, "Compteurs_2004", "Compteurs_2005", "Compteurs_2006", "Compteurs_2007")
liste.pack(padx=30, pady=10)


#Création du calendrier pour choix des dates


global valeur
valeur=datetime.date
def Calendrier():


    def print_sel():
        valeur = cal.selection_get()
        print("la date est",cal.selection_get())
        cal.destroy()

    def recupere_date():
        return cal.selection_get()


    cal = Calendar(fenetre, font="Arial 14", selectmode='day', locale='en_US',
                   cursor="hand1", year=2018, month=2, day=5)

    cal.pack(fill="both", expand=True)
    ttk.Button(fenetre, text="ok", command=print_sel).pack()

ttk.Button(fenetre, text='Calendrier', command=Calendrier).pack(padx=40, pady=10)
ttk.Label(fenetre, textvariable=valeur).pack(padx=30, pady=10)

#declaration boutons VALIDER

Bouton=Button(fenetre, text="Valider",command=fenetre.command)
Bouton.pack(padx=30, pady=10)


#Tracer du graphique

#M = np.loadtxt('dataRU.txt')
#x= float
#plt.plot(M[:,0], 'x')

#plt.xlabel('Temps')
#plt.ylabel('Index compteurs')
#plt.axis([24, 24, 1, 10])
#plt.title('Données compteur RU')

#plt.show()



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

