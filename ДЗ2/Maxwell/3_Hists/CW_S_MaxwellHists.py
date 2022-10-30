import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import maxwell

volumes = [5, 10, 100, 200, 400, 600, 800, 1000]

for volume in volumes:
    selection = []
    tmp_1 = open(f'{volume}.txt', 'r').read()
    tmp_2 = tmp_1.split('\n')
    tmp_3 = []
    for i in tmp_2:
        tmp_3.append(i.split(' '))
    for i2 in tmp_3:
        for j in range(len(i2)):
            selection.append(float(i2[j]))
    x = np.arange(0, 20, 1)
    y_true = [maxwell.pdf(t, loc = 0, scale = 3) for t in x]
    plt.title(f'Гистограмма частот, n = {volume}')
    plt.hist(selection, density=True)
    plt.plot(x, y_true)
    plt.show()


