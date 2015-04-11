import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import shutil
import os
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from lab2 import utils

# Stale poczatkowe
A = 0.2
B = 0.02
h = 0.005
dx = 0.005;
dt = 0.01;
Tk = 50.0

# wyliczenie stalych
n = A / dx + 1

# Parametry Miedzi
K = 237
cw = 900
ro = 2700
matplotlib.rc('font', family='Arial')

#wyczyszczenie i stworzenie nowych katalogow
shutil.rmtree('img1')
shutil.rmtree('img2')
os.makedirs('img1')
os.makedirs('img2')

for warunek1, directory in [[True, "img1"], [False, "img2"]]:
    #przygotowanie siatki
    data = np.zeros([n, n])
    utils.warunekPoczatkowy(data)
    utils.plotData(data, "{0}/poczatek".format(directory), dx)
    t = 0
    while True:
        copyData = np.copy(data)
        utils.iteracja(data, k=K, dt=dt, cw=cw, ro=ro, dx=dx, dy=dx)
        if warunek1:
            data[18:23, 18:23] = 80.0
        elif t * dt < 10.0:
            temp = (50.0 * dt) / (cw * B**2.0 * h * ro)
            data[18:23, 18:2] = data[18:23, 18:2] + temp

        dTemp = np.sum(np.abs(data[:, :] - copyData[:, :]))
        t += 1
        if t % 1000 == 0:
            utils.plotData(data, "{0}/poCzasie{1}".format(directory, int(t / 1000)), dx)
        if dTemp < 0.02:
            break
    utils.plotData(data, "{0}/koniec".format(directory), dx)


