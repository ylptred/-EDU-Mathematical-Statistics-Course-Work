from scipy.stats import gamma
import pandas as pd
import numpy as np
from math import sin, log, pi, sqrt
import random
import math
from scipy.stats import norm

volumes = [5, 10, 100, 200, 400, 600, 800, 1000]


theta0 = 3.0
theta1 = theta0 + 0.5

def JohnksAlgorithm(xi1, xi2, xi3, xi4):
    r = -np.log(xi1)
    w1 = xi2 ** 2
    w2 = xi3 ** 2
    w = w1 + w2
    if w <= 1:
        r = r - (np.log(xi4) * w1/w)
        return theta0 * np.sqrt(2 * r)

selection = []
for i in volumes:
    tmp = []
    while len(tmp) < i:
        xi1 = random.uniform(0, 1)
        xi4 = random.uniform(0, 1)
        xi2 = random.uniform(0, 1)
        xi3 = random.uniform(0, 1)
        number = JohnksAlgorithm(xi1, xi2, xi3, xi4)
        if number is not None:
            tmp.append(number)
    selection.append(tmp)

y = [gamma.ppf(0.99, a=1.5 * i, scale=2 * theta0 ** 2) for i in volumes]

sum_array = []
for i in selection:
  sum_array.append(sum(i))

data = {
    "sum of x^2": sum_array,
    "c_alpha": y,
    "Итог": ["Принимаем theta = " + (f"{theta0}" if sum_array[i] < y[i] else f"{theta1}") for i in range(len(volumes))]}

table = pd.DataFrame(data=data)
table.index = volumes

print(table)


b = [gamma.cdf(y[i], a=1.5*volumes[i], scale=2 * theta1 ** 2) for i in range(len(volumes))]
data = {
    "c_alpha": y,
    "beta": b}

table2 = pd.DataFrame(data=data)
table2.index = volumes

print(table2)