import numpy as np
import random
import pandas as pd
'''
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
            selection.append(float(i2[j]))
    results.append(selection)


for i in results:
    D_list_tmp = []
    for j in results:
        Dnm = round(D(i, j), 4)
        D_list_tmp.append(Dnm)
    D_list.append(D_list_tmp)


for i in D_list:
    print(i)
'''


# Сброс ограничений на количество выводимых рядов
pd.set_option('display.max_rows', None)

# Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)

# Сброс ограничений на количество символов в записи
pd.set_option('display.max_colwidth', None)

df = pd.DataFrame([[5, '0.0000', 0.3651, 0.6765, '0.5190', '0.6000', 0.5047, 0.5935, '0.6000'],
                   [10, 0.3651, '0.0000', 0.9347, 0.7252, 0.8433, 0.7109, 0.8367, 0.8464],
                   [100, 0.6765, 0.9347, '0.0000', 0.8981, 0.5143, 0.7715, 0.4125, 0.4577],
                   [200, '0.5190', 0.7252, 0.8981, '0.0000', 0.7217, 0.4491, 1.0436, 0.8004],
                   [400, '0.6000', 0.8433, 0.5143, 0.7217, '0.0000', '0.8650', 0.6124, 0.3803],
                   [600, 0.5047, 0.7109, 0.7715, 0.4491, '0.8650', '0.0000', '1.0030', 0.8198],
                   [800, 0.5935, 0.8367, 0.4125, 1.0436, 0.6124, '1.0030', '0.0000', 0.7748],
                   [1000, '0.6000', 0.8464, 0.4577, 0.8004, 0.3803, 0.8198, 0.7748, '0.0000']],
    columns=[' ', '5', '10', '100', '200', '400', '600', '800', '1000'])

print(df)
