import numpy as np
import pandas as pd


def MomentsMethod(vrs, mns, ress):
    return [1 - vrs[i]/mns[i] for i in range(len(ress))]


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

means = [np.average(element) for element in results]
variances = [np.var(element) for element in results]

res = MomentsMethod(variances, means, results)

rest = pd.DataFrame(data=res)
rest.index = volumes

print(rest)