from scipy.stats import norm

alpha = [0.1, 0.05, 0.01]
beta = [0.1, 0.05, 0.01]
res = []

for a, b in [(0.1, 0.9), (0.05, 0.95), (0.01, 0.99)]:
  t_a = norm.ppf(a, loc=0, scale=1)
  t_b = norm.ppf(b, loc=0, scale=1)
  res.append(math.ceil(((t_b-t_a * (theta0 / theta1) ** 2 ) * (math.sqrt(6) * theta1 ** 2 / (3 * (theta1 ** 2 - theta0 ** 2)))) ** 2))

data = {'alpha': alpha, 'beta':beta, 'n':res}
table = pd.DataFrame(data=data)
print(table)