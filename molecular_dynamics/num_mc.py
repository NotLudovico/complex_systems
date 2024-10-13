from random import random, randint
import functools
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

n1 = 6
n2 = 18
tot_energy = 16

fig, ax = plt.subplots(1)
HIST_BINS = [0, 1, 2, 3, 4, 5, 6, 7]
ENERGIES = []


def generate_config(n1, n2):
    energies = [0] * (n1 + n2)
    while True:
        i = randint(0, (n1 + n2) - 1)
        if random() < 0.5 and energies[i] == 0:
            energies[i] = 1
            if sum(energies) == tot_energy:
                ENERGIES.append(sum(energies[:n1]))

                return ENERGIES


n, _ = np.histogram(generate_config(n1, n2), HIST_BINS, density=True)


def animate(frame_number, bar_container):
    n, _ = np.histogram(generate_config(n1, n2), HIST_BINS, density=True)
    for count, rect in zip(n, bar_container.patches):
        rect.set_height(count)

    return bar_container.patches


_, _, bar_container = ax.hist([0] * (n1+n2), HIST_BINS,  align='mid',
                              ec="yellow", fc="green", alpha=0.5)

MAX_PROB = 0.6
ax.set_ylim(top=MAX_PROB)  # set safe limit to ensure that all data is visible.
locs, labels = plt.xticks()  # Get the current locations and labels.
plt.xticks(np.arange(0.5, 8, step=1), HIST_BINS)

# draw grid
for loc in np.arange(0, MAX_PROB, step=0.02):
    ax.axhline(loc, alpha=0.2, color='#b0b0b0', linestyle='-', linewidth=0.8)

anim = functools.partial(animate, bar_container=bar_container)
ani = animation.FuncAnimation(fig, anim, 500, repeat=False, blit=True)

plt.grid()
plt.show()
