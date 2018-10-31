from datetime import timedelta, datetime
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from RecupereDonnesDuCSV2 import RecupereDonnesDuCSV

mesdonnees = RecupereDonnesDuCSV()
compteur = 2005
mesdonnees.donnees1('Data/SmallData.csv',compteur,1,1)
#mesdonnees.donnees('Data/SmallData.csv',compteur)
#print(mesdonnees.instant_muc)


x = [dt.datetime.strptime(d,' %Y-%m-%d %H:%M:%S') for d in mesdonnees.instant_muc]
print(type(x[1]))
print(x[1].day)
print(x[1])
#dateTime = x[1] + timedelta(days = 1)
#print (dateTime)

#x = mesdonnees.instant_muc
#x1 = x[1].date
#ajouter un jour à une date
y = range(len(x))

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter(' %Y-%m-%d %H:%M:%S'))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
plt.plot(x,y, marker="*")
plt.gcf().autofmt_xdate()
plt.ylabel('Date')
plt.show()