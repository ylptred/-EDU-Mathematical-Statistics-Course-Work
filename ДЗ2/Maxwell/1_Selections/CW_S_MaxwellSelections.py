import numpy as np
import random


theta = 3.0

def JohnksAlgorithm(xi1, xi2, xi3, xi4):
    r = -np.log(xi1)
    w1 = xi2 ** 2
    w2 = xi3 ** 2
    w = w1 + w2
    if w <= 1:
        r = r - (np.log(xi4) * w1/w)
        return theta * np.sqrt(2 * r)

tmp = []
while len(tmp) < 1000:
    xi1 = random.uniform(0, 1)
    xi4 = random.uniform(0, 1)
    xi2 = random.uniform(0, 1)
    xi3 = random.uniform(0, 1)
    number = JohnksAlgorithm(xi1, xi2, xi3, xi4)
    if number is not None:
        tmp.append(str(round(number, 6)))

for i in range(0, 1001, 10):
    print(' '.join(tmp[i:(i + 10)]))

