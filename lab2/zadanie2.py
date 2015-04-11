__author__ = 'wemstar'
import pylab as P
from lab2 import utils


blaszka = P.zeros([200, 200])
blaszka2 = P.zeros([200, 200])
blaszka[:, :] = 20.0
blaszka2[:, :] = 20.0
utils.warunekDwa(blaszka)

blaszka=utils.iteruj(blaszka,utils.warunekDwa,10000)

print(P.sum(blaszka-blaszka2)*280.0*1.784)
p = P.imshow(blaszka)


P.show()