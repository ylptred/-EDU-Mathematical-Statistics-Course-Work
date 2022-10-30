import matplotlib.pyplot as plt
import numpy
from scipy.stats import binom

def CDF(selection, t):
    sum = 0
    for element in selection:
        sum += int(element <= t)
    return sum / len(selection)

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
            selection.append(int(i2[j]))

    x = numpy.arange(0, 87, 0.5)
    y_true = [binom.cdf(t, 87, 0.6) for t in x]

    y = [CDF(selection, t) for t in x]
    fig, ax = plt.subplots()
    plt.title(f'Эмпирическая функция Биномиального распределения, n = {volume}')
    ax.plot(x, y, label = f'n = {volume}')
    ax.plot(x, y_true, label = 'real')
    ax.legend()

    fig.set_figheight(5)
    fig.set_figwidth(8)
    plt.show()
