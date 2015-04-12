__author__ = 'wemstar'
import pylab as P
f, axarr = P.subplots(1, 1)
axarr.plot(error)
axarr.set_title(u'Błąd średniokwadratowy')
axarr.set_xlabel(u'iteracja')
axarr.set_ylabel(u'błąd')
