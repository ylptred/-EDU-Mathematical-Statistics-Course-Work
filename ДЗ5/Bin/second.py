from scipy.stats import binom
import random
import pandas as pd

volumes = [5, 10, 100, 200, 400, 600, 800, 1000]

theta_0 = 0.6
theta_1 = theta_0 + 0.02


def binomial(n, theta):
    if theta <= 0.5:
        t = theta
    else:
        t = 1 - theta
    c = t / (1 - t)
    r = (1 - t) ** n
    s = r
    k = 0
    alpha = random.uniform(0, 1)
    while alpha > s:
        k += 1
        r *= c * (n - k + 1) / k
        s += r
    if theta <= 0.5:
        return k
    else:
        return n - k


binomial_nums = []
for i in volumes:
    selection = []
    for j in range(i):
        num = binomial(87, theta_0)
        selection.append(num)
    binomial_nums.append(selection)

beta = [binom.cdf(y[i], 87 * val, theta_1) for i, val in enumerate(volumes)]

data_beta = {'sum(x_i)': sum_array, 'c_alpha': y, 'beta': beta}

table_beta = pd.DataFrame(data=data_beta, index=volumes)
print(table_beta)