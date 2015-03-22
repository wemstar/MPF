import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from lab2 import utils
blaszka = np.zeros([200, 200])
blaszka[:, :] = 20.0
utils.warunekPoczatkowy(blaszka)

blaszka=utils.iteruj(blaszka,utils.warunekDwa)

X, Y = np.meshgrid(np.arange(200), np.arange(200))
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, blaszka, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)


plt.show()



