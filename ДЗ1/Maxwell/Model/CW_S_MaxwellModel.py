import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns

theta = 3.0
def JohnksAlgorithm(xi1, xi2, xi3, xi4):
    r = -np.log(xi1)
    w1 = xi2 ** 2
    w2 = xi3 ** 2
    w = w1 + w2
    if w <= 1:
        r = r - (np.log(xi4) * w1/w)
        return theta * np.sqrt(2 * r)

maxwell_nums = []
while len(maxwell_nums) < 1000:
    xi1 = random.uniform(0, 1)
    xi4 = random.uniform(0, 1)
    xi2 = random.uniform(0, 1)
    xi3 = random.uniform(0, 1)
    number = JohnksAlgorithm(xi1, xi2, xi3, xi4)
    if number is not None:
        maxwell_nums.append(number)

sns.kdeplot(maxwell_nums)
plt.xlim(0, 20)
plt.show()
