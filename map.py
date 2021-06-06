import sys

import numpy as np


# initialize dataset
dataset = np.genfromtxt(sys.stdin, delimiter=',')
dataset = np.insert(dataset, -1, np.ones(dataset.shape[0]), axis=1)
dataset[:, -1] = np.vectorize(lambda x: 1 if x == 1 else -1)(dataset[:, -1])
# initialize parameters
epochs = 1000
lr = 0.01
w = np.random.randn(dataset.shape[1] - 1)


# training
for epoch in range(1, epochs):
    for row in dataset:
        x, y = row[:-1], row[-1]
        yhat = np.sum(w * x)
        if y * yhat < 1:
            w += lr * (y * x - 2 * (1 / epoch) * w)
        else:
            w -= lr * (2 * (1 / epoch) * w)


# output
np.savetxt(sys.stdout.buffer, w, fmt='%.6f', newline=' ')
print()
