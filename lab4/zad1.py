import pylab as P
import numpy as np
import matplotlib

def iteruj(dane, AB):
    dane = np.dot(AB, dane)
    return dane
matplotlib.rc('font', family='Arial')
np.set_printoptions(precision=3)
P.set_printoptions(precision=3)
dlugos = 4.3
szerokosc = 0.075
glebokosc = 0.035
dx = 0.01
dt = 0.1
x = int(dlugos / dx)
c = P.zeros(x)
c[:] = 0.0
i = int(0.1 / dx)
d = int(4 / dx)-1
c[i] = 1.04 / (dx * szerokosc * glebokosc)
n = int(4.3 / dt)
Ca = 0.085 * dt / dx
Cd = 0.01 * dt / (dx ** 2.0)
z = []
ro = []
AA = np.zeros([x, n])
BB = np.zeros([x, n])
for i in range(1, n - 1):
    AA[i, i] = 1.0 + Cd
    AA[i, i - 1] = -Cd * 0.5 - Ca * 0.25
    AA[i - 1, i] = -Cd * 0.5 + Ca * 0.25

    BB[i, i] = 1.0 - Cd
    BB[i, i - 1] = Cd * 0.5 + Ca * 0.25
    BB[i - 1, i] = Cd * 0.5 - Ca * 0.25

AA[0, 0], AA[-1, -1] = [1.0 + Cd, 1.0 + Cd]
AA[-1, -2] = -Cd * 0.5 - Ca * 0.25
AA[-2, -1] = -Cd * 0.5 + Ca * 0.25

BB[0, 0], BB[-1, -1] = [1.0 - Cd, 1.0 - Cd]
BB[-1, -2] = Cd * 0.5 + Ca * 0.25
BB[-2, -1] = Cd * 0.5 - Ca * 0.25
AA = np.linalg.inv(AA)
AB = np.dot(AA, BB)

f, axarr = P.subplots(3, 1)

subResults1=[]
for x in range(10000):
    c = iteruj(c, AB)
    z.append(c[d])
    ro.append(P.sum(c[:] * (dx * szerokosc * glebokosc)))
    subResults1.append(np.copy(c))
z=np.array(z)
ro=np.array(ro)
for i,x in enumerate(subResults1[1:]):
    axarr[0].plot(x,label="Po czasie {0}s".format(i*1000*dt))
axarr[0].text(.5,.9,u'gęstośc w czasie',horizontalalignment='center',transform=axarr[0].transAxes)
axarr[0].set_xlabel(u'połozenie')
axarr[0].set_ylabel(u'gęstosc')
axarr[0].legend(loc='upper left', shadow=True,prop={'size':7})

axarr[1].plot(z)

axarr[1].text(.5,.9,u'Gestosc czytnik',horizontalalignment='center',transform=axarr[1].transAxes)
axarr[1].set_xlabel('czas')
axarr[1].set_ylabel('gestosc')


axarr[2].plot(ro)
axarr[2].text(.5,.9,u'Masa ogolna',horizontalalignment='center',transform=axarr[2].transAxes)
axarr[2].set_xlabel('czas')
axarr[2].set_ylabel('masa')
f.tight_layout(pad=0.4, h_pad=1.0)

P.savefig("zad1.png")

