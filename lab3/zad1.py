import pylab as P
import numpy as np
import matplotlib

def iteruj(dane, Ca, Cd):
    dane[2:-1] = dane[2:-1] + (Cd * (1.0 - Ca) - Ca / 6.0 * (Ca ** 2.0 - 3.0 * Ca + 2.0)) * dane[3:] - (Cd * (
        2.0 - 3.0 * Ca) - Ca / 2.0 * (Ca ** 2.0 - 2.0 * Ca - 1.0)) * dane[2:-1] + (Cd * (1.0 - 3.0 * Ca) - Ca / 2.0 * (
        Ca ** 2.0 - Ca - 2.0)) * dane[1:-2] + (Cd * Ca + Ca / 6.0 * (Ca ** 2.0 - 1.0)) * dane[:-3]


dlugos = 100
szerokosc = 5
glebokosc = 1
matplotlib.rc('font', family='Arial')
dx = 0.1
dt = 0.1
c = P.zeros(int(dlugos / dx))
c[:] = 0.0
i = int(10 / dx)
d = int(90 / dx)
c[i] = 1.0 / (dx * szerokosc * glebokosc)
n = int(1000 / dt)
Ca = 0.1 * dt / dx
Cd = 0.01 * dt / (dx ** 2.0)
z = []
ro = []
f, axarr = P.subplots(3, 1)
subResults = []
for x in range(10000):
    iteruj(c, Ca, Cd)
    z.append(c[d])
    ro.append(P.sum(c[:] * (dx * szerokosc * glebokosc)))
    if x % 1000 == 0:
        subResults.append(np.copy(c))

for i,x in enumerate(subResults[1:]):
    axarr[0].plot(x,label="Po czasie {0}s".format(i*1000*dt))

axarr[0].set_title(u'gęstośc w czasie')
axarr[0].set_xlabel('polozenie')
axarr[0].set_ylabel('gestosc')
axarr[0].legend(loc='upper left', shadow=True,prop={'size':6})

axarr[1].plot(z)
axarr[1].set_title('Gestosc czytnik')
axarr[1].set_xlabel('czas')
axarr[1].set_ylabel('gestosc')

axarr[2].plot(ro)
axarr[2].set_title('Masa ogolna')
axarr[2].set_xlabel('czas')
axarr[2].set_ylabel('masa')
"""Graniczne dt
czyste U i czyste D
Metoda weryfikacji
"""
f.tight_layout(pad=0.4, h_pad=1.0)
P.savefig("zad1.png")
