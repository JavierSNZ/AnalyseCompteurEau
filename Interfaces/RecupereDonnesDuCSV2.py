#!/usr/bin/env python3

############ Récupère les infos sur le CSV et les stocks dans une structure ##########
#################Deux méthodes sont utilisées############
####Dernière modification le 30/09/2018######

import csv
from collections import namedtuple
from datetime import timedelta, datetime

class RecupereDonnesDuCSV:		# Définition de notre classe

    def __init__(self):
        """Description de la Classe RecupereDonnesDuCSV:

        Cette classe permet d'effectuer des opérations sur un fichier CSV
        La fonction principale est donnees

        Fonctions:

        donnees(Fichier, compteur, date, jours)
        supprimeColonnes(Fichier)
        ajoutListeDate(Date, jours)
        ajoutDate(Date, jours)
        ConvertieListeDate(Dates)
        ConvertieDate(Dates)
        TriDates(UneDate, DateDepart, Jours)

        """

        self.id_mesure = []
        self.instant_muc = []
        self.instant_serveur = []
        self.index_compteur = []
        self.status = []
        self.id_compteur = []
        self.instant_compteur = []
        self.dateFin = []
        self.DateTrie = []


    def donnees(self, Fichier, compteur):
        """
        :param Fichier:
        :param compteur:
        :return: rien:

        On récupère un Fichier CSV et l'on effectue un tri
        """
        # Nous initialisons la liste des noms de champs
        Headers = namedtuple('Headers', 'id_mesure, instant_muc, instant_serveur, index_compteur, status, id_compteur, instant_compteur,'
                                        'n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, n20, n21, n22, n23, n24')
        with open(Fichier, newline='') as f:
            try:
                reader = csv.reader(f, delimiter=',')
            except TypeError:
                reader = csv.reader(f, delimiter=';')
            for header in map(Headers._make, reader):
        # Nous pouvons afficher les valeurs à l'aide des attributs nommés
                if header.id_compteur == str(compteur):		#Tri des valeurs en fonction du compteur
  #                  print(header.instant_muc, header.id_compteur, header.id_mesure)
                    #On enregistre chaques données dans un tableau
                    self.id_mesure.append(int(header.id_mesure))
                    self.instant_muc.append(header.instant_muc)
                    self.instant_serveur.append(header.instant_serveur)
                    self.index_compteur.append(int(header.index_compteur))
                    self.status.append(int(header.status))
                    self.id_compteur.append(int(header.id_compteur))
                    self.instant_compteur.append(int(header.instant_compteur))


    def donnees1(self, Fichier, compteur, date, jours):
        """
        On lit le fichier CSV. On fait un tri dans les données pour ne récupérer que les données du compteur
        sur la période "date" + "jours"
        :param Fichier:
        :param compteur:
        :param date:
        :param jours:
        :return:
        """
        #on récupère la date de fin
        self.dateUtile = self.ajoutDate(date, jours)
        print(self.dateUtile)
        # Nous initialisons la liste des noms de champs
        Headers = namedtuple('Headers', 'id_mesure, instant_muc, instant_serveur, index_compteur, status, id_compteur, instant_compteur,'
                                        'n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, n20, n21, n22, n23, n24')
        with open(Fichier, newline='') as f:
            try:
                reader = csv.reader(f, delimiter=',')
            except TypeError:
                reader = csv.reader(f, delimiter=';')
            for header in map(Headers._make, reader):
                # Nous pouvons afficher les valeurs à l'aide des attributs nommés
                if header.id_compteur == str(compteur):  # Tri des valeurs en fonction du compteur
                    # On enregistre chaques données dans un tableau
                    self.id_mesure.append(int(header.id_mesure))
                    self.instant_muc.append(header.instant_muc)
                    self.instant_serveur.append(header.instant_serveur)
                    self.index_compteur.append(int(header.index_compteur))
                    self.status.append(int(header.status))
                    self.id_compteur.append(int(header.id_compteur))
                    self.instant_compteur.append(int(header.instant_compteur))
                    #Triage des dates :
                    self.TriDates(header.instant_muc, date, jours)   #Appel à la fonction TriDate pour ne récupérer que les dates voulues

    def supprimeColonnes(self,Fichier):
        """
        Garde uniquement les 7 premières colonnes et supprime toutes les autres

        :param Fichier:
        :return:
        """
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

    def ajoutListeDate(self, Date, jours):
        """
        retourne une liste allant de la date de début qui est "Date"
        jusqu' à la date de fin correspondant à Date + jours.

        :Example:
         >>> print(ajoutListeDate(datetime(2017,11,30,20,8,23), 7))
        [datetime.datetime(2017, 12, 7, 20, 8, 23), datetime.datetime(2017, 12, 6, 20, 8, 23), datetime.datetime(2017, 12, 5, 20, 8, 23), datetime.datetime(2017, 12, 4, 20, 8, 23), datetime.datetime(2017, 12, 3, 20, 8, 23), datetime.datetime(2017, 12, 2, 20, 8, 23), datetime.datetime(2017, 12, 1, 20, 8, 23), datetime.datetime(2017, 11, 30, 20, 8, 23)]

        """
        while(jours>=0):
            DatePlusUn = Date + timedelta(hours=24*jours)
            self.dateFin.append(DatePlusUn) # On récupère tous les jours jusqu'a la Date+jours
            jours -= 1  #on incrémente jours à chaque tour de boucle
        return self.dateFin

    def ajoutDate(self, Date, jours):
        """
           Retourne une date incrémenté de x jours à partir de "Date"
           :Example:
             >>> print(ajoutDate(datetime(2017,11,30,20,8,23), 7))
             2017-12-07 20:08:23
        """
        if jours == 1:
            DateFin = Date + timedelta(hours=24*jours)
            return DateFin
        elif jours ==7:
            DateFin = Date + timedelta(hours=24*jours)
            return DateFin

    def ConvertieListeDate(self, Dates):
        """
        Convertie un tableau de dates au format int en datetime.datetime
        "Dates" = [' 2008-10-12 20:52:33','2008-10-12 21:58:43']
        :param Dates:
        :return:
        """
        DateTimeList = [datetime.strptime(d, ' %Y-%m-%d %H:%M:%S') for d in self.instant_muc]
        return DateTimeList

    def ConvertieDate(self, Dates):
        """
        Convertie une date au format int en datetime.datetime
        "Dates" = [' 2008-10-12 20:52:33','2008-10-12 21:58:43']
        :param Dates:
        :return:
        """
        UneDateTime = datetime.strptime(Dates, ' %Y-%m-%d %H:%M:%S')
        return UneDateTime

    def TriDates(self, UneDate, DateDepart, Jours):
        """
        Enregistre dans "DateTrie" uniquement les Dates comprises entre la "DateDepart" et "DateDepart" + "Jours"
        :param UneDate:
        :param DateDepart:
        :param Jours:
        :return:
        """
        UneDate = self.ConvertieDate(UneDate)
        DateFin = self.ajoutDate(DateDepart, Jours)
        if UneDate <= DateFin and UneDate >= DateDepart:
            self.DateTrie.append(UneDate)
            print("Ajouté !")


#A décocher pour tester la classe:
#mesdonnees = RecupereDonnesDuCSV()
#compteur = 2005
#date = datetime(2017,11,30,20,8,23)
#mesdonnees.donnees1('Data/SmallData.csv',compteur,date,7)
#print(mesdonnees.DateTrie)
#mesdonnees.TriDates(mesdonnees.instant_muc)