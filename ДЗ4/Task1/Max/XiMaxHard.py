from scipy.stats import chi2
from scipy.stats import maxwell
import math
import numpy as np
import pandas as pd


def test_chi_m_calc_o(sample: list, sample_index: int, theta_m):
    s = 0

    l = list(sorted(sample))

    freq = []
    N = 50

    delta = (math.floor(l[-1]) + 1 - round(l[0])) / N

    lb, rb = math.floor(l[0]), math.floor(l[0]) + delta
    c = 0
    i = 0
    x = []

    while i <= len(l):
        if i == len(l):
            x.append(lb + delta / 2)
            freq.append(c)
            break
        elif lb <= l[i] < rb:
            c += 1
            i += 1
        else:
            x.append(lb + delta / 2)
            freq.append(c)
            c = 0
            lb, rb = rb, rb + delta

    for i in range(len(x) - 1):
        prob = maxwell.cdf(x[i + 1] - delta / 2, scale=theta_m) - maxwell.cdf(x[i] - delta / 2, scale=theta_m)
        s += (freq[i] - sample_index * prob) ** 2 / (sample_index * prob)

    prob = maxwell.cdf(x[-1] + delta / 2, scale=theta_m) - maxwell.cdf(x[-1] - delta / 2, scale=theta_m)

    s += (freq[-1] - sample_index * prob) ** 2 / (sample_index * prob)

    return s


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
            selection.append(float(i2[j]))
    results.append(selection)


def accept_chi_m_o(sample, s, a):
    l = list(set(sample))
    chi = chi2.ppf(1 - a, df=len(l) - 2)
    if s <= chi:
        return "H0 принимается"
    else:
        return "H0 отвергается"

variances_m = [np.var(s) for s in results]
means_m = [np.average(s) for s in results]
tml_estimates_m = [np.sqrt((variances_m[i]+means_m[i]**2)/3) for i in range(len(results))]
test_chi_m_o = [test_chi_m_calc_o(results[i], volumes[i], tml_estimates_m[i]) for i in range(len(results))]

crits = [0.1, 0.05, 0.01]
hyp_chi_m_o = [[accept_chi_m_o(results[i], test_chi_m_o[i], a) for i in range(len(results))] for a in crits]

chi_m_o = {'Тестовая статистика': test_chi_m_o, 'alpha=0.1': hyp_chi_m_o[0], 'alpha=0.05': hyp_chi_m_o[1],
           'alpha=0.01': hyp_chi_m_o[2]}
chi_table_m = pd.DataFrame(data=chi_m_o)
chi_table_m.index = volumes
print(chi_table_m)
