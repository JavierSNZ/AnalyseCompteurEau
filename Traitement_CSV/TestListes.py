#!/usr/bin/env python3

##################Crée un CSV avec des données###########
###http://www.quennec.fr/trucs-astuces/langages/python/python-le-module-csv #####
####Dernière modification le 30/09/2019######

l = [
	['root', 'x', '0', '0', 'root', '/root', '/bin/bash'],
	['daemon', 'x', '1', '1', 'daemon', '/usr/sbin', '/usr/sbin/nologin'],
	['bin', 'x', '2', '2', 'bin', '/bin', '/usr/sbin/nologin'],
	['sys', 'x', '3', '3', 'sys', '/dev', '/usr/sbin/nologin'],
	['sync', 'x', '4', '65534', 'sync', '/bin', '/bin/sync'],
	['games', 'x', '5', '60', 'games', '/usr/games', '/usr/sbin/nologin'],
	['man', 'x', '6', '12', 'man', '/var/cache/man', '/usr/sbin/nologin'],
	['lp', 'x', '7', '7', 'lp', '/var/spool/lpd', '/usr/sbin/nologin'],
	['mail', 'x', '8', '8', 'mail', '/var/mail', '/usr/sbin/nologin'],
	['news', 'x', '9', '9', 'news', '/var/spool/news', '/usr/sbin/nologin'],
	['uucp', 'x', '10', '10', 'uucp', '/var/spool/uucp', '/usr/sbin/nologin'],
	['proxy', 'x', '13', '13', 'proxy', '/bin', '/usr/sbin/nologin'],
	['www-data', 'x', '33', '33', 'www-data', '/var/www', '/usr/sbin/nologin']]

import csv
with open('passwd.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	writer.writerows(l)

##suite : On récupère directement dans le CSV puis on affiche
from collections import namedtuple
# Nous initialisons la liste des noms de champs
Headers = namedtuple('Headers', 'LoginName, EncryptedPassword, UserId, GroupId, UserName, HomeDirectory, Interpreter')
with open('passwd.csv', newline='') as f:
	reader = csv.reader(f)
	for header in map(Headers._make, reader):
		# Nous pouvons afficher les valeurs à l'aide des attributs nommés
		print(header.LoginName, header.HomeDirectory)


###Complément
#>>> with open('fichier.csv', encoding='utf8', mode='r', newline='') as f1:
 #   reader = csv.reader(f1, delimiter=';')#
 #   for row in reader:
#        if row[0] == 'Yser':
  #          print(row)
