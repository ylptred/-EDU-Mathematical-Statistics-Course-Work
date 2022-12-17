import numpy as np
from scipy.stats import binom
import pandas as pd


def supremum_b_r(cdf_emp, cdf_true):
    x = np.arange(0, n, 1)
    s = 0
    for i in x:
        s = max(s, abs(cdf_emp[i] - cdf_true[i]))
    return s


def CDF(selection, t):
    sum = 0
    for element in selection:
        sum += int(element <= t)
    return sum / len(selection)


volumes = [5, 10, 100, 200, 400, 600, 800, 1000]
results = []
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
    results.append(selection)

n = 87
theta = 0.6
x = np.arange(0, n, 1)
cdf_true_b = [binom.cdf(i, n, theta) for i in x]

test_kolmogorov_b = [np.sqrt(volumes[i]) * supremum_b_r([CDF(results[i], j) for j in x], cdf_true_b) for i in range(len(results))]
crit_kolmogorov = [1.22, 1.36, 1.63]
hyp_kolmogorov_b = [["H0 принимается" if t < a else "H0 отвергается" for t in test_kolmogorov_b] for a in
                    crit_kolmogorov]
kolmogorov_b = {'Тестовая статистика': test_kolmogorov_b, 'alpha=0.1': hyp_kolmogorov_b[0],
                'alpha=0.05': hyp_kolmogorov_b[1], 'alpha=0.01': hyp_kolmogorov_b[2]}
kolmogorov_table_b = pd.DataFrame(data=kolmogorov_b)
kolmogorov_table_b.index = volumes
print(kolmogorov_table_b)