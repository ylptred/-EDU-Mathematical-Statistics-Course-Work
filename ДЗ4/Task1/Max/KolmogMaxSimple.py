theta = 3


def CDF(selection, t):
  sum = 0
  for element in selection:
    sum += int(element <= t)
  return sum / len(selection)

def supremum_m_r(sample):
    x_m = np.arange(0, 5 * theta, 0.01)
    s = 0
    for x in x_m:
        s = max(s, abs(CDF(sample, x) - maxwell.cdf(x, scale=theta)))
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

x_m = np.arange(0, 5 * theta, 0.01)

test_kolmogorov_m = [np.sqrt(volumes[i]) * supremum_m_r(results[i]) for i in range(len(results))]
crit_kolmogorov = [1.22, 1.36, 1.63]
hyp_kolmogorov_m = [["H0 принимается" if t < a else "H0 отвергается" for t in test_kolmogorov_m] for a in
                    crit_kolmogorov]
kolmogorov_m = {'Тестовая статистика': test_kolmogorov_m, 'alpha=0.1': hyp_kolmogorov_m[0],
                'alpha=0.05': hyp_kolmogorov_m[1], 'alpha=0.01': hyp_kolmogorov_m[2]}
kolmogorov_table_m = pd.DataFrame(data=kolmogorov_m)
kolmogorov_table_m.index = volumes
print(kolmogorov_table_m)