import math
from fractions import Fraction

N_1 = 3
N_2 = 9
E = 8

sample_space = 0

success = []
for i in range(0, N_1 + 1):
    success.append(math.comb(N_1, i) * math.comb(N_2, E - i))

print(success)
probs = []
weighted_energies = []
ss_dim = sum(success)
for i, el in enumerate(success):
    probs.append(Fraction(el, ss_dim))
    weighted_energies.append(probs[-1] * i)

print("Sample Space Dimension: ", ss_dim)
print("Probabilities: ", probs)
print("Average Energies: ", weighted_energies)
print("Average Energy: ", sum(weighted_energies))
