import matplotlib.pyplot as plt
import numpy as np
import random

values = [0]
SIZE = 1000

for j in range(0, 100):
    values = [0]
    for i in range(1, SIZE):
        x = -1 if random.randint(0, 1) == 0 else 1
        new_position = values[-1] + x
        values.append(new_position)

    plt.plot(np.arange(0, SIZE), values)

plt.show()
