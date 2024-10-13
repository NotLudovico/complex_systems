import matplotlib.pyplot as plt


def hooke(q, k):
    return -1 * k * q


def lj(q, epsilon, sigma):
    return 48 * epsilon * (sigma**12 / (q**13) - 0.5 * (sigma**6) / (q**7))


def verlet(q_curr, q_prev, mass, interaction, dt, n_steps, stride=1):
    q_list = []
    times = []

    for i in range(0, n_steps):
        force = 0
        match interaction:
            case "hooke":
                force = hooke(q_curr, 1)
            case "lj":
                force = lj(q_curr, 1, 1)

        q_next = 2 * q_curr - q_prev + force / mass * dt**2
        q_prev = q_curr
        q_curr = q_next

        if i % stride == 0:
            q_list.append(q_next)
            times.append(i * dt)

    return (times, q_list)


fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.set(xlabel="t", ylabel="q(t)", title="Motion in Hooke potential")
pq_list = verlet(2, 2, mass=1, interaction="hooke", dt=0.4, n_steps=1000)
ax1.plot(pq_list[0], pq_list[1])

ax2.set(xlabel="t", ylabel="q(t)", title="Motion in Lennard-Jones potential")
pq_list = verlet(2, 2, mass=1, interaction="lj", dt=0.05, n_steps=1000)
ax2.plot(pq_list[0], pq_list[1])

plt.show()
