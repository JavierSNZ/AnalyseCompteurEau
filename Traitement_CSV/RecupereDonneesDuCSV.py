#!/usr/bin/env python3

############ Récupère les infos sur le CSV et les stocks dans une structure ##########
#################Deux méthodes sont utilisés############
####Dernière modification le 30/09/2019######

import csv
from collections import namedtuple

def donnees():
	# Nous initialisons la liste des noms de champs
	#Headers = namedtuple('Headers', 'n1, n2, Date, n3, n4, NumCompteur, Valeur, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, n20, n21, n22, n23, n24')
	with open('Data.csv', newline='') as f:
		reader = csv.reader(f)
		#for header in map(Headers._make, reader):
	# Nous pouvons afficher les valeurs à l'aide des attributs nommés
		#print(header.Date, header.NumCompteur, header.Valeur)
		for row in reader:
			if row[1] == ' 2017-11-30 23:23:04':
				for column in row[1]:
					print (column[0],end = "")	#end empeche le retour à la ligne
				print("")

donnees()