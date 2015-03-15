import matplotlib.pyplot as plt
import numpy as np

N = 10000
M = 1000
x = np.zeros([N, M])
y = np.zeros([N, M])
z = np.zeros(N)
for i in range(1, N):
    x[i, :] = x[i - 1, :] + np.random.normal(0.0, 1.0, M)
    y[i, :] = y[i - 1, :] + np.random.normal(0.0, 1.0, M)
    z[i] = np.mean(x[i, :] ** 2.0 + y[i, :] ** 2.0)

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(6,6))
axes[0,0].hist(x[0,:],bins=100)
axes[0,1].hist(x[int(N/6),:],bins=100)
axes[1,0].hist(x[int(N/2),:],bins=100)
axes[1,1].hist(x[N-1,:],bins=100)
plt.show()
