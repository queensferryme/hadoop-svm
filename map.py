import sys

from random import random


dataset = []
epochs = 10000
lr = 0.01
w1, w2 = random(), random()


for line in sys.stdin:
    x1, x2, y = line.split(',')
    dataset.append([float(x1), float(x2), 1 if float(y) > 0 else -1])


for epoch in range(1, epochs):
    for x1, x2, y in dataset:
        yhat = w1 * x1 + w2 * x2
        if y * yhat < 1:
            w1 += lr * (y * x1 - 2 * (1 / epoch) * w1)
            w2 += lr * (y * x2 - 2 * (1 / epoch) * w2)
        else:
            w1 -= lr * (2 * (1 / epoch) * w1)
            w2 -= lr * (2 * (1 / epoch) * w2)


print("{}\t{}".format(w1, w2))
