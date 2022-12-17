from scipy.stats import binom
import random
import pandas as pd

volumes = [5, 10, 100, 200, 400, 600, 800, 1000]


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


theta_0 = 0.6
theta_1 = theta_0 + 0.02

y = [binom.ppf(0.99, 87 * i, theta_0) for i in volumes]

binomial_nums = []
for i in volumes:
    selection = []
    for j in range(i):
        num = binomial(87, theta_0)
        selection.append(num)
    binomial_nums.append(selection)

sum_array = []
for i in binomial_nums:
    sum_array.append(sum(i))

data = {"sum(x_i)": sum_array,
        "c_alpha": y,
        "Итог": ["Принимаем theta = " + (f"{theta_0}" if sum_array[i] < y[i] else f"{theta_1}") for i in
                 range(len(volumes))]
        }

table = pd.DataFrame(data=data, index=volumes)
print(table)

beta = [binom.cdf(y[i], 87 * val, theta_1) for i, val in enumerate(volumes)]

data_beta = {'sum(x_i)': sum_array, 'c_alpha': y, 'beta': beta}

table_beta = pd.DataFrame(data=data_beta, index=volumes)
print(table_beta)