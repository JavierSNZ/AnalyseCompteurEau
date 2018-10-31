#!/usr/bin/env python3

############ Récupère les infos sur le CSV et les stocks dans une structure ##########
#################Deux méthodes sont utilisées############
####Dernière modification le 30/09/2018######

import csv
from collections import namedtuple

class RecupereDonnesDuCSV:		# Définition de notre classe

    def __init__(self):
        self.id_mesure = []
        self.instant_muc = []
        self.instant_serveur = []
        self.index_compteur = []
        self.status = []
        self.id_compteur = []
        self.instant_compteur = []

    def donnees(self, Fichier, compteur):
        # Nous initialisons la liste des noms de champs
        Headers = namedtuple('Headers', 'id_mesure, instant_muc, instant_serveur, index_compteur, status, id_compteur, instant_compteur, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, n20, n21, n22, n23, n24')
        with open(Fichier, newline='') as f:
            reader = csv.reader(f)
            for header in map(Headers._make, reader):
        # Nous pouvons afficher les valeurs à l'aide des attributs nommés
                if header.id_compteur == str(compteur):		#Tri des valeurs en fonction du compteur
  #                  print(header.instant_muc, header.id_compteur, header.id_mesure)
                    #On enregistre chaques données dans un tableau
                    self.id_mesure.append(header.id_mesure)
                    self.instant_muc.append(header.instant_muc)
                    self.instant_serveur.append(header.instant_serveur)
                    self.index_compteur.append(header.index_compteur)
                    self.status.append(header.status)
                    self.id_compteur.append(header.id_compteur)
                    self.instant_compteur.append(header.instant_compteur)

    def supprimeColonnes(Fichier):
        with open('filtre.csv', 'w', newline='') as g:
               #     print(row)
            writer = csv.writer(g)
            with open(Fichier, newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    i=26
                    while i>6:
                        del row[i]
                        i = i-1
                    writer.writerow(row)

        #donnees('Data/Data.csv', compteur)
    def get_mesure(self):
        print(self.id_mesure)


#A décocher pour tester la classe:
#mesdonnees = RecupereDonnesDuCSV()
#compteur = input("\n choix du compteur (2005 -> Ru) \n")
#compteur = 2005
#mesdonnees.donnees('Data/Data.csv',compteur)
#mesdonnees.get_mesure()