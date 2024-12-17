import numpy as np


for i in range(2, 20):
    print("DIMENSION: ", i)
    num_of_evs_unstable = 0
    tries = 0
    DIMENSION = i
    for i in range(0, 100_000):
        r = np.random.rand()
        k = np.random.rand()
        d = np.random.rand()

        gamma = np.random.rand(DIMENSION) * 2
        beta = np.random.rand(DIMENSION) * 2

        # Solve for n^*
        matrix = []

        for i in range(0, DIMENSION):
            row = [0] * DIMENSION
            if i == 0:
                row[0] = -r / k
                row[1] = -gamma[1]
            else:
                row[i - 1] = beta[i] * gamma[i]
                if i + 1 < DIMENSION:
                    row[i + 1] = -gamma[i + 1]
            matrix.append(row)
        A = np.array(matrix)

        c = [0] * DIMENSION
        c[0] = -r
        c[-1] = d
        b = np.array(c)

        n = np.linalg.solve(A, b)

        skip = False
        for el in n:
            if el < 0:
                skip = True
                break

        if not skip:
            tries += 1
            # Calculate Jacobian
            matrix = []

            for i in range(0, DIMENSION):
                row = [0] * DIMENSION
                if i == 0:
                    row[0] = -r / k * n[0]
                    row[1] = -gamma[1] * n[0]
                else:
                    row[i - 1] = beta[i] * gamma[i] * n[i]
                    if i + 1 < DIMENSION:
                        row[i + 1] = -gamma[i + 1] * n[i]
                matrix.append(row)

            J = np.array(matrix)

            evs = np.linalg.eigvals(J)
            exception = False
            for ev in evs:
                if np.real(ev) > 0:
                    exception = True
            if exception:
                num_of_evs_unstable += 1
                print(evs)
                print(f"r: {r}, k: {k}, d:{d}")
                print(gamma[2:], beta[2:])

    print(num_of_evs_unstable, "/", tries)
