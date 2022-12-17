from scipy.stats import norm
import math
import random
import pandas as pd

theta_0 = 0.6
theta_1 = theta_0 + 0.02
k = 87

alpha = [0.1, 0.05, 0.01]
beta = [0.1, 0.05, 0.01]
res = []

for a, b in [(0.1, 0.9), (0.05, 0.95), (0.01, 0.99)]:
    t_a = norm.ppf(a, loc=0, scale=1)
    t_b = norm.ppf(b, loc=0, scale=1)
    res.append(math.ceil(((t_b * math.sqrt(theta_1 * (1-theta_1)) - t_a * math.sqrt(theta_0 * (1-theta_0)))/(math.sqrt(k) * (theta_0 - theta_1)))**2))

data_ab = {'alpha': alpha, 'beta': beta, 'n': res}
table_ab = pd.DataFrame(data=data_ab)

print(table_ab)