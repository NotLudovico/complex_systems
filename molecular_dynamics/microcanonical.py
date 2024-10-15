import math
from fractions import Fraction

N_1 = 6
N_2 = 18
E = 16

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

print("\nProbabilities: ", probs)
for i in range(0, len(probs)):
    probs[i] = float(probs[i])

print("Probabilities: ", probs)

print("\nAverage Energies: ", weighted_energies)
for i in range(0, len(weighted_energies)):
    weighted_energies[i] = float(weighted_energies[i])
print("Average Energies: ", weighted_energies)

print("\nAverage Energy: ", sum(weighted_energies))

second_moment = 0
for i, el in enumerate(weighted_energies):
    second_moment += probs[i] * i * i

print("Standard Deviation: ", math.sqrt(
    abs(float(second_moment) - sum(weighted_energies)**2)))
print("Variance: ", abs(float(second_moment) - sum(weighted_energies)**2))
