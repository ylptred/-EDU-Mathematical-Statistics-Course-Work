import random
import matplotlib.pyplot as plt

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

binomial_nums = []
for i in range(10000):
    number = binomial(87, 0.6)
    binomial_nums.append(number)

array = dict((i, binomial_nums.count(i)
              /len(binomial_nums)) for i in binomial_nums)
dictionary = dict(sorted(array.items(), key=lambda x: x[0]))
print(dictionary, dictionary.values())
plt.plot(dictionary.keys(), dictionary.values())
plt.show()
