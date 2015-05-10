from sympy.solvers import nsolve
from sympy import Symbol
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rc('font', family='Arial')
def solveEquesion(As,S):
    eq1 = (-ta) * (1. - As) * S / 4. + c * (Ts - Ta) + sigma * Ts ** 4. * (1. - aap) - sigma * Ta ** 4.
    eq2 = -(1. - aa - ta + As * ta) * S / 4. - c * (Ts - Ta) - sigma * Ts ** 4. * (
        1. - tap - aap) + 2. * sigma * Ta ** 4.0
    return nsolve((eq1, eq2), (Ta, Ts), (273., 273.))
plt.close()
Ta = Symbol('Ta')
Ts = Symbol('Ts')
As1 = 0.19
As2 = 0.60
ta = 0.53
aa = 0.30
c = 2.7
Sl = 1366.1
tap = 0.06
aap = 0.31
sigma = 5.670 * 10 ** -8
SL = np.arange(0.2 * Sl, 1.8 * Sl, 5.)
temps = np.zeros([len(SL), 4])
flag1 = True
flag2 = True
SL1=SL
SL2=SL[::-1]
for i in range(len(SL1)):

    returns1 = solveEquesion(As1,SL1[i])
    returns2 = solveEquesion(As2,SL2[i])
    temps[i, 0] = float(returns1[0])
    temps[i, 1] = float(returns1[1])
    temps[i, 2] = float(returns2[0])
    temps[i, 3] = float(returns2[1])
    if (float(returns1[1]) < 263.):
        As1 = 0.6
    else:
        As1=0.19
    if (float(returns2[1]) > 263.):
        As2 = 0.19
        flag2 = False
    else:
        As2=0.6
    print("Ocieplanie Albedo: {0} stała słoneczna:{1} Ochładznie Albedo: {2} stała słoneczna: {3}".format(As1,SL1[i]/Sl,As2,SL2[i]/Sl))
temps2 = np.zeros([len(SL), 2])

temps = temps - 273.15
plt.plot(SL / Sl, temps[:, 0], label='temperatura atmosfery ocieplanie')
plt.plot(SL / Sl, temps[:, 1], label='temperatura powierzchni ocieplanie')

plt.plot(SL / Sl, temps[::-1, 2], label='temperatura atmosfery ochładzanie')
plt.plot(SL / Sl, temps[::-1, 3], label='temperatura powierzchni ochładzanie')
plt.xlabel('Stosuunek so stalej slonecznej ziemi')
plt.ylabel('Temperatura [C]')
plt.legend()
plt.savefig('zad3.png')