__author__ = 'wemstar'
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

temperatura = 0.0


def iteracja(tablica, k=401.0, dt=1.0, cw=380.0, ro=8920.0, dx=0.005, dy=0.005):
    tablica[1:-1, 1:-1] = tablica[1:-1, 1:-1] + (k * dt) / (cw * ro * (dx )) * (
        tablica[2:, 1:-1] - 2.0 * tablica[1:-1, 1:-1] + tablica[:-2, 1:-1]) + (k * dt) / (cw * ro * (dy )) * (
        tablica[1:-1, 2:] - 2.0 * tablica[1:-1, 1:-1] + tablica[1:-1, :-2])


def warunekPoczatkowy(blaszka):
    blaszka[:, :] = 20.0
    blaszka[0, :] = 10.0;
    blaszka[-1, :] = 10.0;
    blaszka[:, 0] = 10.0;
    blaszka[:, -1] = 10.0;
    blaszka[18:23, 18:23] = 80.0


def plotData(data, name, dx):
    n, m = data.shape
    fig = plt.figure(figsize=plt.figaspect(.5))

    ax = fig.add_subplot(1, 2, 1)

    l = ax.imshow(data)
    l.set_clim(vmin=0.0, vmax=80.0)
    plt.colorbar(l)
    plt.yticks(np.arange(0, n, 10), np.arange(0, n * dx, 10.0 * dx))
    plt.xticks(np.arange(0, n, 10), np.arange(0, n * dx, 10.0 * dx))
    ax.set_xlabel(u'Współrzędna X')
    ax.set_ylabel(u'Współrzędna Y')
    ax.grid(True)

    ax = fig.add_subplot(1, 2, 2, projection='3d')
    X = np.arange(0, n * dx, dx)
    Y = np.arange(0, n * dx, dx)
    X, Y = np.meshgrid(X, Y)

    surf = ax.plot_surface(X, Y, data, rstride=1, cstride=1, cmap=cm.coolwarm, antialiased=False)

    ax.grid(True)
    ax.set_xlabel(u'Współrzędna X')
    ax.set_ylabel(u'Współrzędna Y')
    ax.set_zlabel(u'Temperatura')

    plt.savefig(name + ".png")
    plt.close('all')


