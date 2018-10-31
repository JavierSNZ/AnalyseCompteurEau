try:
    from tkinter import *
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

from RecupereDonnesDuCSV2 import RecupereDonnesDuCSV

from tkcalendar import Calendar, DateEntry
from tkinter.filedialog import * # pour récupérer un fichier

import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import matplotlib.pyplot as plt
import xlrd #pour lecture des fichiers excel


from datetime import datetime, date, time


def BareDeMenu():
    menubar = Menu(fenetre)

    fenetre.config(menu=menubar)
    menufichier = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Fichier", menu=menufichier)

    menufichier.add_command(label="Ouvrir", command=ouvrir)
    menufichier.add_command(label="Compteurs")
    menufichier.add_command(label="Historique")
    menufichier.add_separator()
    menufichier.add_command(label="Quitter", command=sys.exit)

def ouvrir():
    filename = askopenfilename(title="Ouvrir votre document", filetypes=[('txt files', '.txt'), ('csv files', '.csv')])
    fichier = open(filename, "r")
    content = fichier.read()
    fichier.close()
    print(content)

def Calendrier():

    def print_sel(event):
        print("la date est",cal.selection_get())
        button.pack_forget()    #On cache le boutton
        label1["text"] = cal.selection_get().strftime('%d/%m/%Y')
        cal.destroy()
     #   cal.destroy()
    def get_date():
        return cal.selection_get().strftime('%m/%d/%Y')

    cal = Calendar(fenetre, font="Arial 14", selectmode='day', locale='en_US',
                   cursor="hand1")
    cal.pack(fill="both", expand=True)
    button = Button(fenetre, text="ok", command=print_sel)
    button.pack()
    button.bind("<Button-1>", print_sel)#clic gauche


#initialisation variables
global valeur
valeur=datetime.date

#initialisation de la fenêtre
fenetre=Tk()
fenetre.title('Analyse compteurs')
# Create a canvas
w, h = 300, 200
canvas = Canvas(fenetre, width=w, height=h)
canvas.pack(side=RIGHT, padx=5,pady=5)

label = Label(fenetre, text="Choix compteurs", bg="grey")   #Label
label.pack(side=TOP, padx=30, pady=10)

#Liste déroulante compteurs
def getvar(self):
    print(variable.get())
variable = StringVar(fenetre)
variable.set("Compteurs") # default value
liste = OptionMenu(fenetre, variable, "Compteurs_2004", "Compteurs_2005", "Compteurs_2006", "Compteurs_2007", command= getvar)
#OptionMenu(frame, var, *(options), command = OptionMenu_SelectionEvent).pack()
liste.pack(side=TOP, padx=30, pady=10)

#Création du calendrier pour choix des dates
ttk.Button(fenetre, text='Calendrier', command=Calendrier).pack(padx=40, pady=10)
label1 = Label(fenetre, text="", bg="grey")  # Affichage de la date
label1.pack(side=TOP, padx=30, pady=10)


#Création du graphique pour tracer les données data RU.txt

data = xlrd.open_workbook("Data/SmallData.xlsx")

feuille_1 = data.sheet_by_index(0)
feuille_1 = data.sheet_by_name("SmallData")

#nrecupere colonnes et lignes
cols = feuille_1.ncols
rows =feuille_1.nrows

X= []
Y= []
for r in range(1,rows):
    X += [feuille_1.cell_value(rowx=r, colx=3)]
    Y += [feuille_1.cell_value(rowx=r, colx=0)]


def graphique_2005():
    plt.plot(X, Y)
    plt.xlabel('instant compteur')
    plt.ylabel('Id mesure')
    plt.title('Water data2005')
    plt.grid()
    plt.show()

#création de la figure
f = Figure(figsize=(6, 4), dpi=100)
a = f.add_subplot(111)
t = np.arange(0.0, 3.0, 0.01)
s = np.sin(2*np.pi*t)

a.plot(t, s)
a.set_title('Tk embedding')
a.set_xlabel('X axis label')
a.set_ylabel('Y label')


# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=canvas)
canvas.show()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
canvas._tkcanvas.pack(side=LEFT, fill=BOTH, expand=1)

##test
mesdonnees = RecupereDonnesDuCSV()
compteur = 2005
mesdonnees.donnees('Data/SmallData.csv',str(compteur))

print(X)
print(mesdonnees.index_compteur)
#print(mesdonnees.id_mesure)
#######################
# Barre de menu
BareDeMenu()


fenetre.mainloop()

