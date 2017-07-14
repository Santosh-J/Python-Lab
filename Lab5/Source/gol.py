import numpy as np

def life(X, steps):
    # X is the matrix size and steps are the generations
    def roll(x, y):
        # to roll  X in a given direction

        return np.roll(np.roll(X, y, axis=0), x, axis=1)

    for _ in range(steps):
        # counting the number of neighbours according to the rules

        Y = roll(1, 0) + roll(0, 1) + roll(-1, 0) \
            + roll(0, -1) + roll(1, 1) + roll(-1, -1) \
            + roll(1, -1) + roll(-1, 1)

        X = np.logical_or(np.logical_and(X, Y ==2), Y==3)
        X = X.astype(int)
        yield X

X = np.zeros((10, 10)) # 10 by 10

X[3, 2:4] = 1
X[4, 1:3] = 1
X[5, 2] = 1
print(X)