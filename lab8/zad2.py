# -*- coding: utf-8 -*-
__author__ = 'wemstar'
import lab8.utils as utils
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import scipy.integrate

from sympy.utilities.lambdify import lambdify

def func(x, expr):
    expr.subs(x, 0)

def computeDataForFile(j):
    dt = 5
    xl = 4.3
    files = ['1,04_2', '1,052_1', '1,56_4', '1,56_5', '1,092_3']
    data = utils.getData(files)[files[j]]
    x = data.index
    reg = np.polyfit(x, data, 8)
    xs=Symbol('x')
    eq=1
    for i,param in enumerate(reg[::-1]):
        eq+=param*xs**i
    m0=np.float64(integrate(eq,(xs,0,180)))
    tk=np.float64(integrate(xs*eq,(xs,0,180)))/m0
    sigmaExp=eq*(xs-tk)**2.0
    sigma=np.float64(scipy.integrate.quad(lambda x:sigmaExp.subs(xs,x),0.01,180)[0])/m0
    U = xl * (np.sqrt(4. * sigma + tk ** 2.0) + 3. * tk) / (2. * (2. * tk ** 2.0 - sigma))
    masa = [float(f[:-2].replace(',', '.')) for f in files][j]
    A = 2.0 * (2. * tk ** 2.0 - sigma) / (m0 * xl * (np.sqrt(4.0 * sigma + tk ** 2.0) + 3. * tk))
    A = A * masa
    Q = U * A
    data.plot()
    funca = lambdify(xs, eq,'numpy')
    plt.plot(np.array(x).astype(float),funca(np.array(x).astype(float)))
    print("Dla {0} pomiaru Q: {1}  U: {2}".format(j,Q,U))

computeDataForFile(0)
computeDataForFile(1)
computeDataForFile(2)
computeDataForFile(3)
computeDataForFile(4)
plt.ylabel('Stężenie')
plt.xlabel('Czas')
plt.savefig('zad2.png')