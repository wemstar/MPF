from sympy.solvers import nsolve
from sympy import Symbol
import numpy as np
import matplotlib.pyplot as plt

plt.close()
Ta = Symbol('Ta')
Ts = Symbol('Ts')
As = 0.19
ta = 0.53
aa = 0.30
c = 2.7
Sl = 1366.1
tap = 0.06
aap = 0.31
sigma = 5.670 * 10 ** -8
SL = np.arange(0.5 * Sl, 1.5 * Sl, 5.)
temps = np.zeros([len(SL), 2])
flag = True
for i, S in enumerate(SL):
    eq1 = (-ta) * (1. - As) * S / 4. + c * (Ts - Ta) + sigma * Ts ** 4. * (1. - aap) - sigma * Ta ** 4.
    eq2 = -(1. - aa - ta + As * ta) * S / 4. - c * (Ts - Ta) - sigma * Ts ** 4. * (
        1. - tap - aap) + 2. * sigma * Ta ** 4.0
    returns = nsolve((eq1, eq2), (Ta, Ts), (273., 273.))
    temps[i, 0] = float(returns[0])
    temps[i, 1] = float(returns[1])
    print(temps[i,1],S/Sl)
temps2 = np.zeros([len(SL), 2])

temps = temps - 273.15
plt.plot(SL / Sl, temps[:, 0], label='temperatura atmosfery')
plt.plot(SL / Sl, temps[:, 1], label='temperatura powierzchni')
plt.xlabel('Stosuunek so stalej slonecznej ziemi')
plt.ylabel('Temperatura [C]')
plt.legend()
plt.savefig('zad1.png')
"""
Zadanie
parametr A=212
parametr B=1.6
"""
	
