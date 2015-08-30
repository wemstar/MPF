__author__ = 'wemstar'
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
import matplotlib
from scipy.stats import maxwell

matplotlib.rc('font', family='Arial')
catalogs=['daneA','daneB','daneC']
positions=['{0}/position.txt'.format(x) for x in catalogs]
velocities=['{0}/velocity.txt'.format(x) for x in catalogs]
posColX=["{0}_pos".format(x) for x in range(1,968,2)]
posColY=["{0}_pos".format(x) for x in range(2,969,2)]
velColX=["{0}_vel".format(x) for x in range(1,968,2)]
velColY=["{0}_vel".format(x) for x in range(2,969,2)]
tables=[]
for pos,vel in zip(positions,velocities):
    posA=pd.read_csv(pos,index_col=0,sep=';',header=None)
    posA=posA.drop([posA.columns[-1]], axis=1)
    velocityA=pd.read_csv(vel,index_col=0,sep=';',header=None)
    velocityA=velocityA.drop([velocityA.columns[-1]], axis=1)
    tables.append(posA.join(velocityA,lsuffix='_pos', rsuffix='_vel'))
def proces(dataFrame,filename,index):
    posX=np.array(dataFrame.loc[index][posColX])
    posY=np.array(dataFrame.loc[index][posColY])
    mask=np.all([posX>(0.1*22.) ,posX < (22.0-0.1*22.)],axis=0)
    vel=np.sqrt(np.array(dataFrame.loc[index][velColX]**2.0)+np.array(dataFrame.loc[index][velColY]**2.0))[mask]
    n,bin,path=plt.hist(vel,bins=18)
    bin=np.arange(bin[0],bin[-1])
    rv = maxwell(loc=0,scale=100)
    plt.plot(bin, rv.pdf(bin)*10000, 'k-', lw=2, )
    plt.xlabel('Prędkości')
    plt.ylabel('Ilość cząstek')
    plt.title('Histogram prędkości cząstek')
    plt.savefig("{0}_sppedHist.png".format(filename))
    plt.clf()
    plt.xlabel('Pozycja X')
    plt.ylabel('Pozycja Y')
    plt.title('Pozycja cząstek')
    plt.plot(posX[mask],posY[mask],'.')
    plt.savefig("{0}_partPos.png".format(filename))
    plt.clf()
    plt.xlabel('Pozycja Y')
    plt.ylabel('Ilość cząstek')
    plt.title('Histogram rozkłady horyzontalnego')
    plt.hist(posY[mask])
    plt.savefig("{0}_partoHos.png".format(filename))
    plt.clf()
proces(tables[0],"A",7000)
proces(tables[1],"B",7000)
proces(tables[2],"C",7000)


