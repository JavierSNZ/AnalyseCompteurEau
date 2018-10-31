#!/usr/bin/env python3

##################Recupère le fichier csv du site###########
####Dernière modification le 30/09/2019######

import csv
import urllib.request

url = 'http://www.mmi.iutmulhouse.uha.fr/water_data.csv'
urllib.request.urlretrieve(url, "Data.csv")
print ("successfully completed")