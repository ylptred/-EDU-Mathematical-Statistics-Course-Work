n = 87
theta = 0.6


def test_chi_b_calc(sample: list, sample_index: int):
    s = 0

    l = list(set(sorted(sample)))

    freq = [sample.count(i) for i in l]

    for i in range(len(l)):
        prob = binom.pmf(l[i], n, theta)
        s += (freq[i] - sample_index * prob) ** 2 / (sample_index * prob)

    return s


def accept_chi_b(sample, s, a):
    l = list(set(sorted(sample)))
    chi = chi2.ppf(1 - a, df=len(l) - 1)
    if s <= chi:
        return "H0 принимается"
    else:
        return "H0 отвергается"


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

test_chi_b = [test_chi_b_calc(results[i], volumes[i]) for i in range(len(results))]

crits = [0.1, 0.05, 0.01]
hyp_chi_b = [[accept_chi_b(results[i], test_chi_b[i], a) for i in range(len(results))] for a in crits]

chi_b = {'Тестовая статистика': test_chi_b, 'alpha=0.1': hyp_chi_b[0], 'alpha=0.05': hyp_chi_b[1],
         'alpha=0.01': hyp_chi_b[2]}
chi_table_b = pd.DataFrame(data=chi_b)
chi_table_b.index = volumes
print(chi_table_b)
