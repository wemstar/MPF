import numpy as np
import matplotlib.pyplot as plt

def iteracja(tablica,k=2370.0,dt=1.0,cw=900.0,ro=2700.0):
	nowaTablica=np.zeros(tablica.shape)
	nowaTablica[1:-1,1:-1]= tablica[1:-1,1:-1]+(k*dt)/(cw*ro)*(tablica[2:,1:-1] - 4.0*tablica[1:-1,1:-1]+tablica[:-2,1:-1] +tablica[1:-1,2:]+tablica[1:-1,:-2])
	return nowaTablica
	
	

def warunekPoczatkowy(blaszka):
	blaszka[0,:]=10.0;
	blaszka[-1,:]=10.0;
	blaszka[:,0]=10.0;
	blaszka[:,-1]=10.0;
	blaszka[90:110,90:110]=80.0

def warunekDwa(blaszka,dt=1.0,cw=900.0,ro=2700.0):
	warunekPoczatkowy(blaszka)
	temp=(50.0*dt)/(cw*ro*0.05*2.0*2.0);
	blaszka[89,89:111]=blaszka[89,89:111]+temp
	blaszka[111,89:111]=blaszka[111,89:111]+temp
	blaszka[89:111,89]=blaszka[89:111,89]+temp
	blaszka[89:111,111]=blaszka[89:111,111]+temp


blaszka=np.zeros([200, 200])
blaszka[:,:]=20.0
warunekPoczatkowy(blaszka)
plt.imshow(blaszka)
cax=plt.clim()
cbar=plt.colorbar(cax)

for x in range(50000):
	blaszka1=iteracja(blaszka,dt=1.0)

	blaszka=blaszka1
	warunekDwa(blaszka)
plt.imshow(blaszka)
plt.show()



