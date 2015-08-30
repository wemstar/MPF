__author__ = 'wemstar'
import pandas as pd
import numpy as np
def getData(files):
    data = pd.DataFrame()
    for fil in files:
        z = []
        with open(fil + '.txt') as fp:
            for line in fp:
                z.append([float(x) for x in line.split() if x])

        z = np.array(z)
        data[fil] = pd.Series(z[:, 1], index=z[:, 0])
    return data