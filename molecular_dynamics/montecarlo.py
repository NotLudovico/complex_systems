import matplotlib.pyplot as plt
import math
import numpy as np
from random import random

DELTA = 0.1


def energy(q):
    return q**2/2


def prob(q):
    return math.e ** (-q**2/2)


def trial(q):
    return q + random() * 2 * DELTA - DELTA


def run(q0=4, steps=1000):
    q = -2
    p = prob(q)
    positions = []

    for i in range(steps):
        qtry = trial(q)
        ptry = prob(qtry)
        alpha = ptry/p

        if alpha > 1:
            alpha = 1

        if alpha > random():
            q = qtry
            p = ptry

        positions.append(q)
    return positions


plt.hist(run(2, 2_000_000), bins=30, color='blue',
         edgecolor='black', alpha=0.7, density=True)
qs = np.linspace(-4, 4, 500)
plt.plot(qs, prob(qs) / math.sqrt(2 * math.pi), color='red')
plt.show()
