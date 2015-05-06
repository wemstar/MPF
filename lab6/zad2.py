__author__ = 'wemstar'

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
Eg = 280000
z = 3.0
d = 5.0
T = 170. + 273.
v = 3.
T0 = 237. + 15.
uw = np.array([20., 10., 5., 2.])
h = 120.

Q = (np.pi * d ** 2.) / 4. * (273. / T) * (1.3 * v) * (T - T0)
dh = (1.126 * Q ** 0.58) / (5.0 ** 0.7)
H = 306. + dh


matplotlib.rc('font', family='Arial')
a = np.array([0.555,0.865,0.845,0.818,0.784,0.756])
b = np.array([1.284,1.108,0.978,0.822,0.660,0.551])
m = np.array([0.080,0.143,0.196,0.270,0.363,0.440])
uw=np.array([
    np.arange(1,3,.1),
    np.arange(1,5,.1),
    np.arange(1,8,.1),
    np.arange(1,11,.1),
    np.arange(1,5,.1),
    np.arange(1,4,.1),
])
u = uw * h ** m / 14.
A = 0.088 * (6. * m ** (-0.3) + 1. - np.log(H / z))
B = 0.038 * m ** 1.3 * (8.7 - np.log(H / z))
x = 15000
sigmaY = A * x ** a
sigmaZ = B * x ** b
S = (Eg / (2. * np.pi *  sigmaY * sigmaZ)) * np.exp(-((H ** 2.0) / (2. * sigmaZ ** 2.0))) * 1000.0
S=S/uw
plt.plot(uw[0],S[0],label='Stan Równowagi 1')
plt.plot(uw[1],S[1],label='Stan Równowagi 2')
plt.plot(uw[2],S[2],label='Stan Równowagi 3')
plt.plot(uw[3],S[3],label='Stan Równowagi 7')
plt.plot(uw[4],S[4],label='Stan Równowagi 5')
plt.plot(uw[5],S[5],label='Stan Równowagi 6')
plt.xlabel('Prędkość wiatru [m/s]')
plt.ylabel('Stężenie w punkcie')
plt.legend()
plt.savefig('zad2.png')

plt.show()
