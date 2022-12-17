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

theta_m = 3
def test_chi_m_calc(sample: list, sample_index: int):
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


def accept_chi_m(sample, s, a):
    l = list(set(sample))
    chi = chi2.ppf(1 - a, df=len(l) - 1)
    if s <= chi:
        return "H0 принимается"
    else:
        return "H0 отвергается"


test_chi_m = [test_chi_m_calc(results[i], volumes[i]) for i in range(len(results))]

crits = [0.1, 0.05, 0.01]
hyp_chi_m = [[accept_chi_m(results[i], test_chi_m[i], a) for i in range(len(results))] for a in crits]

chi_m = {'Тестовая статистика': test_chi_m, 'alpha=0.1': hyp_chi_m[0], 'alpha=0.05': hyp_chi_m[1],
         'alpha=0.01': hyp_chi_m[2]}
chi_table_m = pd.DataFrame(data=chi_m)
chi_table_m.index = volumes
print(chi_table_m)