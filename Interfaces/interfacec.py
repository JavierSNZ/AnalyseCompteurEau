try:
    from tkinter import *
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

from tkcalendar import Calendar, DateEntry
import time,datetime
from datetime import datetime, date, time, timedelta

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import xlrd #pour lecture des fichiers excel
from RecupereDonnesDuCSV2 import RecupereDonnesDuCSV


#initialisation de la fenêtre
fenetre=Tk()
Frame1 = Frame(fenetre, borderwidth=2)
Frame1.pack(side=RIGHT, padx=500, pady=200)

#Affichage label compteurs
label = Label(fenetre, text="Choix compteurs", bg="grey")   #Label
label.pack(padx=30, pady=10)


#Recupere la valeur du compteur (2005,2006, etc..)
def recup_valeur(self):
    valeur_cpt=var_compteur.get()
    #print("la valeur du compteur est", valeur_cpt)

#Affichage du graphique
    if valeur_cpt == 'Compteur_2005':
        print("la valeur du compteur est", valeur_cpt)
    bout_graph=ttk.Button(fenetre, text='Graphique_2005', command=graphique_2005).pack(padx=40, pady=10)



#Liste déroulante compteurs
var_compteur = StringVar(fenetre)
var_compteur.set("Compteurs") # default value
liste = OptionMenu(fenetre, var_compteur, "Compteur_2004", "Compteur_2005", "Compteur_2006", "Compteur_2007", command=recup_valeur)
liste.pack(padx=30, pady=10)


#initialisation variables
global valeur_cal
valeur_cal=datetime.date

#Création du calendrier
def Calendrier():

    def print_sel():
        #bouton_ok.pack_forget()
        valeur_cal = cal.selection_get()
        print("la date est",cal.selection_get())
        label = Label(fenetre, text=cal.selection_get().strftime('%d/%m/%Y'), bg="grey").pack(padx=30, pady=10) # Label

        cal.destroy()

    def recupere_date():
        return cal.selection_get()


    cal = Calendar(fenetre, font="Arial 14", selectmode='day', locale='en_US',
                   cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    bouton_ok=ttk.Button(fenetre, text="ok", command=print_sel).pack()
    bouton_ok.bind("<Button-1>", print_sel)  # clic gauche

#Affichage du calendrier pour choix des dates
ttk.Button(fenetre, text='Calendrier', command=Calendrier).pack(padx=40, pady=10)
#ttk.Label(fenetre, textvariable=valeur).pack(padx=30, pady=10)


#Création du graphique pour tracer les données data.csv

#rec_donnees= RecupereDonnesDuCSV()
#rec_donnees.donnees('Data.csv', 2005) # on récupere les donnees à partir de la methode données de RecupereDonnesCsv


#X1= rec_donnees.instant_compteu
#Y1= rec_donnees.id_mesure

#print("La donnees de X",X)


data = xlrd.open_workbook("water_data2005_test.xlsx")

feuille_1 = data.sheet_by_index(0)
feuille_1 = data.sheet_by_name("water_data2005")

#onrecupere colonnes et lignes
cols = feuille_1.ncols
rows =feuille_1.nrows

X= []
Y= []
for r in range(1,rows):
    X += [feuille_1.cell_value(rowx=r, colx=6)]
    Y += [feuille_1.cell_value(rowx=r, colx=0)]
#print("valeur X",X[1],"valeur X1",X1[1])
#print("valeur Y",Y[1],"valeur Y1",Y1[1])
#X1= [datetime.strftime(d, "%Y-%m-%d% H:%M:%S") for d in (X[feuille_1.cell_value(rowx=r, colx=1)])]




def graphique_2005():
    plt.plot(X, Y)
    #plt.gcf().autofmt_xdate() #affichage de la date en oblique
    plt.xlabel('instant compteur')
    plt.ylabel('Id mesure')
    plt.title('Water data2005')
    plt.grid()
    plt.show()




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
