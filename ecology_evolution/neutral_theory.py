import random
import matplotlib.pyplot as plt

# Parameters
m = 10  # Number of groups
u = 1 / m**2  # Mutation probability
num_iterations = 1000_000  # Total iterations


# Initialize population
n_0 = 100
N = n_0 * m
n = [n_0] * m  # Initial population in each group

# Simulation
for _ in range(num_iterations):
    # One reproduces
    n[random.randint(0, m - 1)] += 1

    # One dies
    n[random.randint(0, m - 1)] -= 1

    # Ensure no group has a negative population
    for i in range(m):
        if n[i] < 0:
            n[i] = 0

    # One maybe mutates
    if random.random() < u:
        donor = random.randint(0, m - 1)
        recipient = random.randint(0, m - 1)
        if n[donor] > 0:  # Only mutate if the donor has at least one member
            n[donor] -= 1
            n[recipient] += 1

# Frequencies
total_population = sum(n)
x = [count / total_population for count in n]

# Heterozygosity
heterozygosity = 1 - sum(f**2 for f in x)
print(f"Heterozygosity: {heterozygosity:.4f}")

# Average x
print("Experimental Average x: ", sum(x) / m)
print("Theory:                 ", 1 / m)

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(range(m), x, color="skyblue", edgecolor="black")
plt.title("Population Frequencies After Simulation")
plt.xlabel("Group Index")
plt.ylabel("Frequency")
plt.xticks(range(m))
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
