import numpy as np
from scipy.stats import binom
import pandas as pd
from numpy import average, var
from scipy.stats import chi2

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)
pd.options.display.expand_frame_repr = False

kolm_l = 1.22
n = 87
theta = 0.6
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

def CDF(selection, t):
    sum = 0
    for element in selection:
        sum += int(element <= t)
    return sum / len(selection)


def supremum(s1, s2):
    x = np.arange(0, n, 0.5)
    f1 = [CDF(s1, t) for t in x]
    f2 = [CDF(s2, t) for t in x]
    s = 0
    for i in range(len(x)):
            s = max(s, abs(f1[i]-f2[i]))
    return s

def D(s1, s2):
    m = len(s1)
    n = len(s2)
    return np.sqrt(m*n/(m+n))*supremum(s1, s2)

Ds = [[D(s1, s2) for s2 in results] for s1 in results]

hyp_smirnov_b = [["H0 принимается" if t<=kolm_l else "H0 отвергается" for t in Dss] for Dss in Ds]
smirnov_b = {
    '5':hyp_smirnov_b[0],
    '10':hyp_smirnov_b[1],
    '100':hyp_smirnov_b[2],
    '200':hyp_smirnov_b[3],
    '400':hyp_smirnov_b[4],
    '600':hyp_smirnov_b[5],
    '800':hyp_smirnov_b[6],
    '1000':hyp_smirnov_b[7],
}
table_Ds_binom = pd.DataFrame(data=smirnov_b)
table_Ds_binom.index = volumes

print(table_Ds_binom)