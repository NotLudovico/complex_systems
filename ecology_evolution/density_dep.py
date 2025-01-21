import random
import matplotlib.pyplot as plt

# Parameters
N = 30  # Total population
b = 0.4  # Baseline transition rate
q = 0.2  # Control parameter
num_simulations = 1000  # Number of simulations per initial state
max_steps = 10000  # Safety cap for maximum simulation steps


# Transition rate: W_{n -> n+1} (moving up)
def w_up(n):
    return b * (N - n) / N * n / N * (1 - q * n / N)


# Transition rate: W_{n -> n-1} (moving down)
def w_down(n):
    return b * n / N * (N - n) / N * (1 - q * (N - n) / N)


# Fixation simulation
def simulate_fixation():
    fixation_probabilities = []

    for n_initial in range(N + 1):  # Iterate over all possible starting states
        fixations = 0

        for _ in range(num_simulations):
            n = n_initial
            for _ in range(max_steps):  # Run until fixation or time limit
                if n == 0 or n == N:  # Absorbing states
                    if n == N:
                        fixations += 1
                    break

                # Compute probabilities of moving up or down
                rate_up = w_up(n)
                rate_down = w_down(n)
                total_rate = rate_up + rate_down

                # Normalize transition rates to probabilities
                prob_up = rate_up / total_rate
                prob_down = rate_down / total_rate

                # Random step based on probabilities
                rand = random.random()
                if rand < prob_up:
                    n += 1
                elif rand < prob_up + prob_down:
                    n -= 1

        # Compute fixation probability for the current starting state
        fixation_probability = fixations / num_simulations
        fixation_probabilities.append(fixation_probability)
        print(
            f"Fixation probability starting from n = {n_initial}: {fixation_probability:.4f}"
        )

    return fixation_probabilities


# Run the simulation and plot the results
results = simulate_fixation()

# Plot fixation probabilities
plt.figure(figsize=(10, 6))
plt.plot(
    range(N + 1),
    results,
    marker="o",
    linestyle="-",
    color="b",
    label="Fixation Probability",
)
plt.xlabel("Initial Number of Individuals (n)")
plt.ylabel("Fixation Probability")
plt.title(f"Fixation Probability vs Initial State (q = {q}, N = {N}, b = {b})")
plt.grid()
plt.legend()
plt.show()
