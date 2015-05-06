__author__ = 'wemstar'
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from lab6.contraints import *
matplotlib.rc('font', family='Arial')
x = np.arange(100000, 200000000, 1000, float)
sigmaY = A * x ** a
sigmaZ = B * x ** b
S = (Eg / (2. * np.pi *  sigmaY * sigmaZ)) * np.exp(-((H ** 2.0) / (2. * sigmaZ ** 2.0))) * 1000.0
S1= S/uw[0]
S2= S/uw[1]
S3= S/uw[2]
S4= S/uw[3]

plt.plot(x/100000.,S1,label='v1=20')
plt.plot(x/100000.,S2,label='v2=10')
plt.plot(x/100000.,S3,label='v3=5')
plt.plot(x/100000.,S4,label='v4=2')
plt.xlabel('Odległość od emitera w km')
plt.ylabel(r'Steżenie PM10 [$\mu$g \m^3] ')
plt.legend()
plt.savefig('zad1.png')
plt.show()
