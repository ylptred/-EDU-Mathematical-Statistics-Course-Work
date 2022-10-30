from numpy import average, var
import pandas as pd
import random


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
    
means = [average(element) for element in results]
variances = [var(element) for element in results]
dict1 = {'Выборочное среднее':means, 'Выборочная дисперсия':variances}
table = pd.DataFrame(data=dict1)
table.index = volumes
print(table)

means_2 = [f'{round((((s - 52.2) / 52.2) * 100), 2)}%' for s in means]
variances_2 = [f'{round((((s - 20.88) / 20.88) * 100), 2)}%' for s in variances]
dict2 = {'Погрешность выборочного среднего':means_2, 'Погрешность выборочной дисперсии':variances_2}
table2 = pd.DataFrame(data=dict2)
table2.index = volumes
print(table2)
