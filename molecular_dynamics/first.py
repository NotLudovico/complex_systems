import matplotlib.pyplot as plt


def hooke(q, k=1):
    return -1 * k * q


def lj(q, epsilon=1, sigma=1):
    return 48 * epsilon * (sigma**12 / (q**13) - 0.5 * (sigma**6) / (q**7))


def verlet(*, q_curr, q_prev, mass, dt, n_steps, stride=1, force=hooke):
    q_list = []
    times = []

    for i in range(0, n_steps):
        q_next = 2 * q_curr - q_prev + force(q_curr) / mass * dt**2
        q_prev = q_curr
        q_curr = q_next

        if i % stride == 0:
            q_list.append(q_curr)
            times.append((i+1) * dt)

    return (times, q_list)


fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.set(xlabel="t", ylabel="q(t)", title="Motion in Hooke potential")
pq_list = verlet(q_curr=2, q_prev=2, mass=1,
                 dt=0.4, n_steps=1000, stride=1, force=hooke)
ax1.plot(pq_list[0], pq_list[1])

ax2.set(xlabel="t", ylabel="q(t)",
        title="Motion in Lennard-Jones potential")
pq_list = verlet(q_curr=2, q_prev=2, mass=1,
                 dt=0.05, n_steps=1000, stride=1, force=lj)
ax2.plot(pq_list[0], pq_list[1])

plt.show()
