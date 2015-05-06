import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.DataFrame()
files=['1,04_2','1,052_1','1,56_4','1,56_5','1,092_3']
dt=5
xl=4.3
for fil in files:
	z=[]
	with open(fil+'.txt') as fp:
		for line in fp:
			z.append([float(x) for x in line.split() if x])

	z=np.array(z)
	data[fil]=pd.Series(z[:,1],index=z[:,0])

m0=dt*0.5*np.sum(data+data.shift(1))
i=np.tile(np.arange(len(data)),(5,1)).T
tk=dt/(2*m0)*np.sum((i*dt)*data+(i+1)*dt*data.shift(1))
sigma=pd.DataFrame()
for fil in files:
	sigma[fil]=dt/(2*m0)*np.sum((i*dt-tk[fil])**2.0*data+((i+1)*dt-tk[fil])**2.0*data.shift(1))
sigma=np.diagonal(sigma)
D=(xl**2*(np.sqrt(4*sigma+tk**2.0)+3*tk)*(tk*np.sqrt(4.*sigma+tk**2.0)+2*sigma-tk**2.0))/(8.*(sigma-tk**2.0)**2.0)
U=xl*(np.sqrt(4.*sigma+tk**2.0)+3*tk)/(2.*(2*tk**2.0-sigma))
masa=[float(f[:-2].replace(',','.')) for f in files]
A=2.0*(2.*tk**2.0-sigma)/(m0*xl*(np.sqrt(4.0*sigma+tk**2.0)+3.*tk))
A=A*masa
Q=U*A

