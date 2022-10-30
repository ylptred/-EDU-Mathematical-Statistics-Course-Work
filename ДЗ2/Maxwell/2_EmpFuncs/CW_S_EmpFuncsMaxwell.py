import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import maxwell

def CDF(select, t):
    sum = 0
    for element in select:
        sum += int(element <= t)
    return sum / len(select)

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

    x = np.arange(0, 100, 0.5)
    y_true = [maxwell.cdf(t, loc = 0, scale = 3) for t in x]
    y = [CDF(selection, t) for t in x]
    plt.title(f'Эмпирическая функция распределения Максвелла при n = {volume}')
    plt.xlim(0, 20)
    plt.plot(x, y, label = f'n = {volume}')
    plt.plot(x, y_true, label = 'real')
    plt.legend()

    plt.show()
