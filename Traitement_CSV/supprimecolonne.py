#!/usr/bin/env python3

############ Copie CSV original et le supprime les colonnes ##########
#################Supprime les colonnes 8 à 26############
####Dernière modification le 14/10/2018############

import csv


with open('filtre.csv', 'w', newline='') as g:
       #     print(row)
    writer = csv.writer(g)
    with open('Data.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            i=26
            while i>6:
                del row[i]
                i = i-1
            writer.writerow(row)