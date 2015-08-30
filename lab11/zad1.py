__author__ = 'wemstar'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataFrame=pd.read_excel('dane_dunaj_tryt.xlsx',na_values='-9999').interpolate()
lenght=len(dataFrame)
l=0
m=0
suma=np.sum(dataFrame.Opady)
m=suma
l=np.sum(dataFrame.Opady*np.arange(lenght))
tt=l/m
Cin = dataFrame['Opady']
WymuszenieJedno=np.zeros(lenght-2)
WymuszenieJedno[0]=suma
Cout=np.convolve(Cin,WymuszenieJedno)/100000
plt.plot(Cout,label='Symulacja')
plt.plot(dataFrame.Dunaj,label='Pomiary')
plt.ylabel('Koncentracja znacznika[kg/m^3]')
plt.xlabel('Czas[Miesiace]')
plt.legend()
plt.savefig('zad1.png')
plt.clf()

WymuszenieJedno=np.exp(dataFrame.index/tt)/tt
Cout=np.convolve(Cin,WymuszenieJedno)/50
plt.plot(Cout,label='Symulacja')
plt.plot(dataFrame.Dunaj,label='Pomiary')
plt.ylabel('Koncentracja znacznika[kg/m^3]')
plt.xlabel('Czas[Miesiace]')
plt.legend()
plt.savefig('zad2.png')
plt.clf()

PE=0.1
t=np.array(dataFrame.index).astype(float)
WymuszenieJedno=np.sqrt(4.0*np.pi*PE*t/tt)*1./tt*np.exp(-1.0*(1.-t/tt)**2.0/(4.*PE*t/tt))
Cout=np.convolve(Cin,WymuszenieJedno)
plt.plot(Cout,label='Symulacja')
plt.plot(dataFrame.Dunaj,label='Pomiary')
plt.ylabel('Koncentracja znacznika[kg/m^3]')
plt.xlabel('Czas[Miesiace]')
plt.legend()
plt.savefig('zad3.png')
plt.clf()



