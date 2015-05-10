import math
S=1366.1
sigma=5.670*10**-8
A=.3
T=math.pow(S/(sigma)/4.*(1-A),1./4.)-273.
print(T)
