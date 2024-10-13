import random
import matplotlib.pyplot as plt


def prob(k, n, a):
    return (k + a) / (n + 2 * a)


results = []
random.seed(690)
n_list = []
k_n = []
for exp in range(0, 1):
    k = 0
    # random.seed(exp)
    for n in range(1, 5000):
        if random.random() < prob(k, n, 0.75):
            k += 1
        k_n.append(k / n)
        n_list.append(n)
    results.append(k / n)

fig, ax = plt.subplots()
ax.plot(n_list, k_n)

# ax.hist(results, 100)
plt.show()
