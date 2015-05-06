__author__ = 'wemstar'
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rc('font', family='Arial')

for filename in ["cos", "cos2", "1"]:
    tablica = []
    with open(filename + '.txt') as fp:
        for x in fp:
            z = x.split(' ')
            z = [g for g in z if g]
            tablica.append(z)
    tablica = np.array(tablica).astype(float)
    print(tablica.shape)
    rezerwuaryWodne = tablica[:, 1:11]
    roznica = (rezerwuaryWodne[1::10, :] - rezerwuaryWodne[:-1:10, :]) ** 2.0
    roznica = np.sum(roznica, axis=1)
    for i, z in enumerate(roznica):
        if (z == 0.0):
            print(i * 10)
            break
    plt.ylim([-1.0, 5.0])
    for i, rez in enumerate(rezerwuaryWodne.T):
        plt.plot(rez, label='Rezerwuar {0}'.format(i + 1))
    plt.xlabel('Lata')
    plt.ylabel('Steżenie mMol/m^3')
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename + ".png")
    plt.cla()
    plt.clf()
