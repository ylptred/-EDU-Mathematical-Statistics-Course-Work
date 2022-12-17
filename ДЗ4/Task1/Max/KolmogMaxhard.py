from scipy.stats import chi2
from scipy.stats import maxwell
import pandas as pd
import math
import numpy as np

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

def CDF(selection, t):
  sum = 0
  for element in selection:
    sum += int(element <= t)
  return sum / len(selection)

theta_m = 3
def supremum_m_r_o(sample, theta):
  x_m = np.arange(0, 5*theta, 0.01)
  s = 0
  for x in x_m:
    s = max(s, abs(CDF(sample, x) - maxwell.cdf(x, scale=theta)))
  return s

x_m = np.arange(0, 5*theta_m, 0.01)
variances_m = [np.var(s) for s in results]
means_m = [np.average(s) for s in results]
tml_estimates_m = [np.sqrt((variances_m[i]+means_m[i]**2)/3) for i in range(len(results))]

test_kolmogorov_m = [np.sqrt(volumes[i])*supremum_m_r_o(results[i], tml_estimates_m[i]) for i in range(len(results))]
crit_kolmogorov = [1.22, 1.36, 1.63]
hyp_kolmogorov_b = [["H0 принимается" if t<a else "H0 отвергается" for t in test_kolmogorov_m] for a in crit_kolmogorov]
kolmogorov_m = {'Тестовая статистика':test_kolmogorov_m, 'alpha=0.1':hyp_kolmogorov_b[0],'alpha=0.05':hyp_kolmogorov_b[1],'alpha=0.01':hyp_kolmogorov_b[2]}
kolmogorov_table_m = pd.DataFrame(data=kolmogorov_m)
kolmogorov_table_m.index=volumes
print(kolmogorov_table_m)