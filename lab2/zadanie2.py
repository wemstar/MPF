__author__ = 'wemstar'
import pylab as P
from lab2 import utils


blaszka = P.zeros([200, 200])
blaszka[:, :] = 20.0
utils.warunekDwa(blaszka)

blaszka=utils.iteruj(blaszka,utils.warunekDwa,10000)


p = P.imshow(blaszka)


P.show()