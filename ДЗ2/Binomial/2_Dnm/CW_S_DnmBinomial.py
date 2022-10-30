import numpy as np
import random
import pandas as pd

def eCDF(select, t):
    summ = 0
    for element in select:
        summ += int(element <= t)
    return summ / len(select)

def sup(selection1, selection2):
    x = np.arange(0, 87, 0.5)
    f1 = [eCDF(selection1, t) for t in x]
    f2 = [eCDF(selection2, t) for t in x]
    s = 0
    for i in range(len(x)):
        s = max(s, abs(f1[i] - f2[i]))
    return s

def D(selection1, selection2):
    m = len(selection1)
    n = len(selection2)
    return np.sqrt(m * n/(m + n)) * sup(selection1, selection2)

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
        r *= c * (n - k + 1)/k
        s += r

    if theta <= 0.5:
        return k
    else:
        return n - k


volumes = [5, 10, 100, 200, 400, 600, 800, 1000]
results = []
D_list = []
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


for i in results:
    D_list_tmp = []
    for j in results:
        Dnm = round(D(i, j), 4)
        D_list_tmp.append(Dnm)
    D_list.append(D_list_tmp)

'''
for i in D_list:
    print(i)
'''

# Сброс ограничений на количество выводимых рядов
pd.set_option('display.max_rows', None)

# Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)

# Сброс ограничений на количество символов в записи
pd.set_option('display.max_colwidth', None)

df = pd.DataFrame([[5, '0.0000', '0.7303', '0.6765', '0.7068', '0.6889', '0.6755', '0.7300', '0.6758'],
                   [10, '0.7303', '0.0000', '0.3920', '0.4012', '0.5544', '0.4495', '0.4635', '0.4972'],
                   [100, 0.6765, '0.3920', '0.0000', '0.6940', 0.6485, 0.2932, 0.5303, 0.3909],
                   [200, 0.7068, 0.4012, '0.6940', '0.0000', 0.9526, 0.7144, 0.5376, 0.9812],
                   [400, 0.6889, 0.5544, 0.6485, 0.9526, '0.0000', 0.9941, 1.3064, 1.0395],
                   [600, 0.6755, 0.4495, 0.2932, 0.7144, 0.9941, '0.0000', 0.7329, 0.3421],
                   [800, '0.7300', 0.4635, 0.5303, 0.5376, 1.3064, 0.7329, '0.0000', 1.1015],
                   [1000, 0.6758, 0.4972, 0.3909, 0.9812, 1.0395, 0.3421, 1.1015, '0.0000']],
    columns=[' ', '5', '10', '100', '200', '400', '600', '800', '1000'])

print(df)
